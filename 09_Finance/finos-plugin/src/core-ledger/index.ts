import { randomUUID } from "node:crypto";
import type { FinancialEvent, JournalEntry, LedgerAccount, LedgerLine } from "../shared/types.js";

export interface LedgerStore {
  accounts(entityId: string): Promise<LedgerAccount[]>;
  journalEntries(entityId: string): Promise<JournalEntry[]>;
  saveJournalEntry(entry: JournalEntry): Promise<JournalEntry>;
}

export class InMemoryLedgerStore implements LedgerStore {
  private readonly accountRows: LedgerAccount[] = [];
  private readonly journalRows: JournalEntry[] = [];

  seedAccounts(accounts: LedgerAccount[]): void {
    this.accountRows.push(...accounts);
  }

  async accounts(entityId: string): Promise<LedgerAccount[]> {
    return this.accountRows.filter((account) => account.entityId === entityId && account.isActive);
  }

  async journalEntries(entityId: string): Promise<JournalEntry[]> {
    return this.journalRows.filter((entry) => entry.entityId === entityId);
  }

  async saveJournalEntry(entry: JournalEntry): Promise<JournalEntry> {
    this.journalRows.push(entry);
    return entry;
  }
}

export class CoreLedgerService {
  constructor(private readonly store: LedgerStore) {}

  async postFromEvent(
    event: FinancialEvent,
    description: string,
    lines: Array<Omit<LedgerLine, "id" | "entityId">>
  ): Promise<JournalEntry> {
    const entry: JournalEntry = {
      id: randomUUID(),
      entityId: event.entityId,
      eventId: event.id,
      description,
      postedAt: new Date().toISOString(),
      status: "posted",
      lines: lines.map((line) => ({
        ...line,
        id: randomUUID(),
        entityId: event.entityId
      }))
    };

    this.assertBalanced(entry);
    await this.assertAccountsExist(entry);
    return this.store.saveJournalEntry(entry);
  }

  assertBalanced(entry: JournalEntry): void {
    const totals = entry.lines.reduce(
      (memo, line) => {
        if (line.debitMinor < 0 || line.creditMinor < 0) {
          throw new Error("Ledger debits and credits cannot be negative.");
        }
        if (line.debitMinor > 0 && line.creditMinor > 0) {
          throw new Error("Ledger line cannot contain both debit and credit.");
        }
        memo.debit += line.debitMinor;
        memo.credit += line.creditMinor;
        return memo;
      },
      { debit: 0, credit: 0 }
    );

    if (totals.debit !== totals.credit) {
      throw new Error(`Unbalanced journal entry: debit=${totals.debit}, credit=${totals.credit}.`);
    }
  }

  async trialBalance(entityId: string): Promise<Array<{ accountId: string; debitMinor: number; creditMinor: number }>> {
    const entries = await this.store.journalEntries(entityId);
    const rows = new Map<string, { accountId: string; debitMinor: number; creditMinor: number }>();

    for (const entry of entries.filter((candidate) => candidate.status === "posted")) {
      for (const line of entry.lines) {
        const current = rows.get(line.accountId) ?? {
          accountId: line.accountId,
          debitMinor: 0,
          creditMinor: 0
        };
        current.debitMinor += line.debitMinor;
        current.creditMinor += line.creditMinor;
        rows.set(line.accountId, current);
      }
    }

    return [...rows.values()];
  }

  private async assertAccountsExist(entry: JournalEntry): Promise<void> {
    const accounts = await this.store.accounts(entry.entityId);
    const accountIds = new Set(accounts.map((account) => account.id));
    for (const line of entry.lines) {
      if (!accountIds.has(line.accountId)) {
        throw new Error(`Unknown ledger account: ${line.accountId}.`);
      }
    }
  }
}
