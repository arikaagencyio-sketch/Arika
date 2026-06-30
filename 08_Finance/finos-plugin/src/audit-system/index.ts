import { createHash, randomUUID } from "node:crypto";

export interface AuditRecord {
  id: string;
  entityId: string;
  actorId: string;
  action: string;
  resourceType: string;
  resourceId: string;
  occurredAt: string;
  previousHash?: string;
  hash: string;
  metadata?: Record<string, unknown>;
}

export class AuditSystem {
  private readonly records: AuditRecord[] = [];

  record(input: Omit<AuditRecord, "id" | "occurredAt" | "hash" | "previousHash">): AuditRecord {
    const previousHash = this.records.at(-1)?.hash;
    const occurredAt = new Date().toISOString();
    const id = randomUUID();
    const payload = JSON.stringify({ ...input, id, occurredAt, previousHash });
    const hash = createHash("sha256").update(payload).digest("hex");
    const record = { ...input, id, occurredAt, previousHash, hash };
    this.records.push(record);
    return record;
  }

  verify(): boolean {
    for (let index = 0; index < this.records.length; index++) {
      const record = this.records[index];
      const previousHash = index === 0 ? undefined : this.records[index - 1]?.hash;
      if (record.previousHash !== previousHash) return false;
    }
    return true;
  }

  list(entityId: string): AuditRecord[] {
    return this.records.filter((record) => record.entityId === entityId);
  }
}
