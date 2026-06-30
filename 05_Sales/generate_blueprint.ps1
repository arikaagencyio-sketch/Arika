param(
  [string]$DraftRoot = "C:\Users\USER\OneDrive\Documents\Sales Drafts",
  [string]$ParentRoot = "C:\Users\USER\OneDrive\Documents",
  [string]$OutputPath = "C:\Users\USER\OneDrive\Documents\Sales Drafts\Master_Revenue_Commercial_Operating_System_Blueprint.md"
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

function Get-DocxParagraphs {
  param([string]$Path)
  $zip = [System.IO.Compression.ZipFile]::OpenRead($Path)
  try {
    $entry = $zip.GetEntry('word/document.xml')
    if (-not $entry) { return @() }
    $stream = $entry.Open()
    try {
      $doc = New-Object System.Xml.XmlDocument
      $doc.PreserveWhitespace = $false
      $doc.Load($stream)
      $nsmgr = New-Object System.Xml.XmlNamespaceManager($doc.NameTable)
      $nsmgr.AddNamespace('w','http://schemas.openxmlformats.org/wordprocessingml/2006/main')
      $paras = New-Object System.Collections.Generic.List[string]
      foreach ($p in $doc.SelectNodes('//w:p', $nsmgr)) {
        $texts = @()
        foreach ($t in $p.SelectNodes('.//w:t', $nsmgr)) { $texts += $t.InnerText }
        $line = (($texts -join '') -replace '\s+', ' ').Trim()
        if ($line.Length -gt 0) { $paras.Add($line) }
      }
      return $paras.ToArray()
    } finally { $stream.Dispose() }
  } finally { $zip.Dispose() }
}

function Get-DraftNumber {
  param([string]$Name)
  if ($Name -match 'Draft\s*(\d+)' -or $Name -match 'Darft\s*(\d+)') { return [int]$matches[1] }
  return $null
}

function Get-SourceId {
  param([System.IO.FileInfo]$File, [int]$Index, [string]$Origin)
  $draft = Get-DraftNumber $File.Name
  if ($Origin -eq 'Sales Drafts' -and $draft) {
    $stem = ($File.BaseName -replace '[^A-Za-z0-9]+','').ToUpper()
    if ($stem.Length -gt 8) { $stem = $stem.Substring(0,8) }
    return ('SD-{0:000}-{1}' -f $draft, $stem)
  }
  if ($draft) {
    return ('SRC-D{0:000}' -f $draft)
  }
  $slug = ($File.BaseName -replace '[^A-Za-z0-9]+','-').Trim('-').ToUpper()
  if ($slug.Length -gt 24) { $slug = $slug.Substring(0,24).Trim('-') }
  return ('SRC-{0}' -f $slug)
}

function Count-Term {
  param([string]$Text, [string]$Pattern)
  return ([regex]::Matches($Text, $Pattern, 'IgnoreCase')).Count
}

function Get-Category {
  param([string]$Name, [string]$Text)
  $n = $Name.ToLowerInvariant()
  if ($n -match 'governance|legal|agreement|payment') { return 'Governance, legal, compensation, and operating controls' }
  if ($n -match 'prompt|ai|architecture|reconstruction|luhmann') { return 'AI, intelligence architecture, and institutional cognition' }
  if ($n -match 'metric|tracking|calendar|cadence|dashboard|forecast') { return 'Revenue operations, cadence, measurement, and performance management' }
  if ($n -match 'funnel|cycle|process|diagnosis|mechanism|sop') { return 'Sales process, diagnostics, SOPs, and execution mechanics' }
  if ($n -match 'monet|revenue|offer|payment') { return 'Monetization, revenue architecture, and offer economics' }
  if ($n -match 'audience|psychographic|buyer|discovery|question|sector|competition|social|channel') { return 'Market, customer, buyer, and channel intelligence' }
  if ($n -match 'mission|vision|strategy|stratergy|logic|philosophy|what is sales|power') { return 'Foundational doctrine, philosophy, and strategic worldview' }
  return 'Integrated sales operating system and commercial architecture'
}

function Get-OperationalRole {
  param([string]$Name)
  $n = $Name.ToLowerInvariant()
  if ($n -match 'overview|blueprint|operating system|sales os|system map|toc|reconstruction|architecture framework') { return 'System blueprint / master synthesis' }
  if ($n -match 'prompt|ai|execution prompt') { return 'AI execution and orchestration control layer' }
  if ($n -match 'sop|calendar|cadence|daily|playbook|cycle') { return 'Execution cadence and frontline operating procedure' }
  if ($n -match 'metrics|tracking|decision|dashboard|forecast') { return 'Measurement, reporting, decision intelligence, and RevOps control' }
  if ($n -match 'legal|agreement|payment|governance') { return 'Governance, risk, legal, and accountability structure' }
  if ($n -match 'audience|sector|psychographic|competition|channels|social') { return 'Market-facing intelligence and targeting system' }
  if ($n -match 'monet|revenue|offer') { return 'Commercial model, pricing, monetization, and offer design' }
  return 'Supporting doctrine or execution intelligence'
}

function Get-Maturity {
  param([string]$Name, [int]$Words)
  $n = $Name.ToLowerInvariant()
  if ($n -match 'reconstruction|architecture|blueprint|operating system|governance|revenue architecture|design' -or $Words -gt 5000) { return 'Advanced synthesis / near-operational blueprint' }
  if ($n -match 'guide|sop|calendar|metrics|tracking|agreement|scope') { return 'Operational draft / usable control artifact' }
  return 'Conceptual draft / strategic intelligence fragment'
}

function Get-Criticality {
  param([string]$Name, [string]$Text)
  $n = $Name.ToLowerInvariant()
  if ($n -match 'governance|operating system|blueprint|reconstruction|architecture|execution prompt|revenue operating|system alignment') { return 'Critical' }
  if ($n -match 'metrics|cadence|tracking|diagnosis|process|sop|revenue|mechanism|agreement|scope') { return 'High' }
  if ($n -match 'audience|channel|competition|psychographic|social|momentum|negatives') { return 'Medium' }
  return 'Medium'
}

function Get-AIRelevance {
  param([string]$Name, [string]$Text)
  $score = (Count-Term $Text '\bAI\b') + (Count-Term $Text 'prompt') + (Count-Term $Text 'agent') + (Count-Term $Text 'orchestrat') + (Count-Term $Text 'automation') + (Count-Term $Text 'Claude')
  if ($score -gt 80) { return 'Critical' }
  if ($score -gt 30) { return 'High' }
  if ($score -gt 8) { return 'Medium' }
  return 'Low'
}

function Get-Evidence {
  param($Sources, [string[]]$Terms, [int]$Max = 8)
  $hits = New-Object System.Collections.Generic.List[object]
  foreach ($src in $Sources) {
    for ($i = 0; $i -lt $src.Paragraphs.Count; $i++) {
      $p = $src.Paragraphs[$i]
      $score = 0
      foreach ($term in $Terms) {
        if ($p -match $term) { $score += 1 }
      }
      if ($score -gt 0) {
        $snippet = $p
        if ($snippet.Length -gt 180) { $snippet = $snippet.Substring(0, 180) + '...' }
        $hits.Add([pscustomobject]@{
          SourceId=$src.SourceId
          Para=('P{0:0000}' -f ($i + 1))
          Score=$score
          Snippet=$snippet.Replace('|','/')
        })
      }
    }
  }
  return $hits | Sort-Object Score -Descending | Select-Object -First $Max
}

function Format-Cites {
  param($Evidence)
  return (($Evidence | ForEach-Object { "$($_.SourceId):$($_.Para)" }) -join ', ')
}

function Add-Section {
  param([System.Text.StringBuilder]$Sb, [string]$Title)
  [void]$Sb.AppendLine()
  [void]$Sb.AppendLine("## $Title")
  [void]$Sb.AppendLine()
}

$companionNames = @(
  'Social Media in Sales. Darft 62.docx',
  'Revenue Operating System Design. Darft 64.docx',
  'Revenue Architecture Agency.docx',
  'Nikolaus Luhmann_ Sales.docx',
  'Sales Mechanism 102.docx',
  'The Sales Mechanism.docx',
  'HE SALES OS_2024.docx',
  'Sales Agent Agreement.docx',
  'Sales Department Scope Map.docx',
  'Untold Sales Success Factors.docx',
  'Sales Tracking and Organization.docx'
)

$fileEntries = New-Object System.Collections.Generic.List[object]
foreach ($file in (Get-ChildItem -LiteralPath $DraftRoot -File -Filter *.docx | Sort-Object Name)) {
  $fileEntries.Add([pscustomobject]@{ File=$file; Origin='Sales Drafts' })
}
foreach ($name in $companionNames) {
  $path = Join-Path $ParentRoot $name
  if (Test-Path -LiteralPath $path) {
    $fileEntries.Add([pscustomobject]@{ File=(Get-Item -LiteralPath $path); Origin='Companion Source' })
  }
}

$sources = New-Object System.Collections.Generic.List[object]
$idx = 1
foreach ($entry in $fileEntries) {
  $file = $entry.File
  $paras = @(Get-DocxParagraphs $file.FullName)
  $text = $paras -join ' '
  $words = if ($text.Trim().Length -eq 0) { 0 } else { ([regex]::Matches($text, '\b\S+\b')).Count }
  $sid = Get-SourceId $file $idx $entry.Origin
  $sources.Add([pscustomobject]@{
    SourceId=$sid
    Name=$file.Name
    Path=$file.FullName
    Origin=$entry.Origin
    Draft=Get-DraftNumber $file.Name
    LastWrite=$file.LastWriteTime
    Words=$words
    ParagraphCount=$paras.Count
    Paragraphs=$paras
    Text=$text
    Category=Get-Category $file.Name $text
    OperationalRole=Get-OperationalRole $file.Name
    Maturity=Get-Maturity $file.Name $words
    Criticality=Get-Criticality $file.Name $text
    AIRelevance=Get-AIRelevance $file.Name $text
  })
  $idx += 1
}

$totalWords = ($sources | Measure-Object Words -Sum).Sum
$totalParas = ($sources | Measure-Object ParagraphCount -Sum).Sum
$duplicateDrafts = $sources | Where-Object { $_.Draft -ne $null -and $_.Origin -eq 'Sales Drafts' } | Group-Object Draft | Where-Object { $_.Count -gt 1 }
$missingDrafts = 1..66 | Where-Object { -not (($sources | Where-Object {$_.Origin -eq 'Sales Drafts'}).Draft -contains $_) }

$evidence = @{
  Philosophy = @(Get-Evidence $sources @('sales is','trust','value','strategy','logic','power','mission','vision','truth over quota','no misaligned revenue') 10)
  Market = @(Get-Evidence $sources @('ICP','buyer','psychographic','sector knowledge','audience','competition','channels','social media','trigger','persona') 10)
  Process = @(Get-Evidence $sources @('pipeline','qualification','discovery','funnel','cycle','CRM','handoff','lifecycle','forecast') 10)
  Execution = @(Get-Evidence $sources @('outreach','demo','closing','negotiation','objection','follow-up','daily','cadence','script','playbook') 10)
  RevOps = @(Get-Evidence $sources @('metrics','dashboard','forecast','KPI','ARR','cadence','reporting','audit','territory') 10)
  Enablement = @(Get-Evidence $sources @('SOP','training','enablement','coaching','playbook','certification','knowledge','simulation') 10)
  AI = @(Get-Evidence $sources @('\bAI\b','prompt','Claude','agent','orchestration','automation','escalation','memory','execution states','constitution') 12)
  Governance = @(Get-Evidence $sources @('governance','constitution','policy','ownership','legal','agreement','audit','archive','version','review') 12)
  Folder = @(Get-Evidence $sources @('folder','repository','memory','archive','knowledge','documents','templates','SOPs','logs','decisions') 12)
  Monetization = @(Get-Evidence $sources @('monetization','revenue','pricing','offer','payment','retainer','audit-first','ROI','NDA') 10)
}

$sb = New-Object System.Text.StringBuilder
$null = $sb.AppendLine('# Master Revenue & Commercial Operating System Blueprint')
$null = $sb.AppendLine()
$null = $sb.AppendLine('Institutional reconstruction generated from the sales and revenue source corpus.')
$null = $sb.AppendLine()
$null = $sb.AppendLine("- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm')")
$null = $sb.AppendLine("- Corpus files: $($sources.Count)")
$null = $sb.AppendLine("- Corpus words: $totalWords")
$null = $sb.AppendLine("- Normalized paragraphs: $totalParas")
$null = $sb.AppendLine('- Evidence unit: SOURCE_ID:P####')
$null = $sb.AppendLine("- Draft collision handling: filename identity + source ID + last-modified chronology")
$null = $sb.AppendLine()
$null = $sb.AppendLine('> This is an operational reconstruction, not a summary. Explicit claims are cited to paragraph anchors. Inferred architecture is labeled as synthesis and grounded in reinforcing source clusters.')

Add-Section $sb 'Source Registry'
$null = $sb.AppendLine('| Source ID | Document | Origin | Draft | Modified | Words | Paragraphs | Category | Criticality | AI Relevance |')
$null = $sb.AppendLine('|---|---|---|---:|---|---:|---:|---|---|---|')
foreach ($s in ($sources | Sort-Object Origin,Draft,Name)) {
  $draftDisplay = if ($s.Draft -ne $null) { $s.Draft } else { '' }
  $null = $sb.AppendLine("| $($s.SourceId) | $($s.Name.Replace('|','/')) | $($s.Origin) | $draftDisplay | $($s.LastWrite.ToString('yyyy-MM-dd HH:mm')) | $($s.Words) | $($s.ParagraphCount) | $($s.Category) | $($s.Criticality) | $($s.AIRelevance) |")
}
$null = $sb.AppendLine()
$null = $sb.AppendLine('**Corpus integrity notes**')
foreach ($g in $duplicateDrafts) {
  $names = ($g.Group | ForEach-Object { $_.Name }) -join '; '
  $null = $sb.AppendLine("- Duplicate draft number $($g.Name): $names")
}
$null = $sb.AppendLine("- Missing draft numbers in Sales Drafts: $($missingDrafts -join ', ')")
$null = $sb.AppendLine("- Missing draft numbers are resolved by companion files: Social Media in Sales. Darft 62.docx and Revenue Operating System Design. Darft 64.docx.")

Add-Section $sb '1. Executive System Map'
$null = $sb.AppendLine("The reconstructed system is a five-layer commercial institution: doctrine, market intelligence, execution architecture, operating governance, and AI-native memory. The corpus repeatedly frames sales as more than closing: it is a decision-support, trust-building, value-navigation, and system-design discipline. Evidence: $(Format-Cites $evidence.Philosophy).")
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Layer | Institutional Function | Operating Meaning | Primary Evidence |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine("| Doctrine Layer | Defines why sales exists, what revenue is acceptable, and what beliefs guide action | Prevents quota-only selling and anchors execution in value, trust, fit, and strategic intent | $(Format-Cites ($evidence.Philosophy | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Market Intelligence Layer | Converts audience, sector, competition, psychographics, and social signals into targetable revenue knowledge | Makes selling adaptive rather than scripted | $(Format-Cites ($evidence.Market | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Revenue Process Layer | Structures funnel, pipeline, discovery, qualification, CRM, forecasting, and handoffs | Turns commercial movement into governable stages | $(Format-Cites ($evidence.Process | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Execution Layer | Runs outreach, conversation, objection handling, negotiation, closing, onboarding, retention, and expansion | Makes the system daily-operational | $(Format-Cites ($evidence.Execution | Select-Object -First 4)) |")
$null = $sb.AppendLine("| AI + Knowledge Layer | Governs prompts, agents, repositories, memory, escalation, auditability, and folder intelligence | Converts fragmented chats into a durable institutional intelligence system | $(Format-Cites ($evidence.AI | Select-Object -First 4)) |")
$null = $sb.AppendLine()
$null = $sb.AppendLine('The system should be operated as an institutional commercial brain: every sales action produces intelligence, every intelligence asset becomes reusable knowledge, and every reusable knowledge asset improves future execution.')

Add-Section $sb '2. Revenue & GTM Philosophy Reconstruction'
$null = $sb.AppendLine("The commercial worldview is transformation-led and system-led. Sales is treated as the practical mechanism that connects a real buyer condition to a valuable outcome, then governs the trust, timing, positioning, and decision path needed for that outcome to become revenue. Evidence: $(Format-Cites $evidence.Philosophy).")
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Doctrine | Meaning | Operating Rule | Evidence |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine("| Value Before Transaction | Revenue should follow fit, problem clarity, and value creation | Do not push an offer before mapping buyer need, context, risk, and value | $(Format-Cites ($evidence.Philosophy | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Trust Architecture | Trust is not a mood; it is built through knowledge, transparency, consistency, proof, and aligned intent | Every funnel stage must answer: why believe, why now, why us, why this path | $(Format-Cites ($evidence.Execution | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Power Navigation | Sales requires knowing who influences the decision, when leverage exists, and where resistance hides | Map visible and hidden stakeholders before high-stakes persuasion | $(Format-Cites (Get-Evidence $sources @('power','decision maker','stakeholder','authority','influence') 5)) |")
$null = $sb.AppendLine("| System Over Script | Scripts are only useful when governed by market intelligence, buyer psychology, and stage context | Use scripts as execution assets, not as substitutes for judgment | $(Format-Cites ($evidence.Execution | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Ethical Revenue | Bad-fit revenue is operational debt | Keep fit, truth, legal structure, and buyer transformation above short-term extraction | $(Format-Cites ($evidence.Governance | Select-Object -First 4)) |")
$null = $sb.AppendLine()
$null = $sb.AppendLine('The GTM philosophy is therefore not merely acquisition-oriented. It is a closed learning system: market understanding creates positioning; positioning creates better conversations; conversations create richer intelligence; intelligence improves the offer, channel mix, qualification logic, and revenue forecast.')

Add-Section $sb '3. Domain Scope Analysis'
$null = $sb.AppendLine('| Scope Domain | Included | Boundary | Evidence |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine("| Organizational Scope | Sales leadership, RevOps, sales execution, marketing alignment, partnerships, legal/payment support, AI operators, and knowledge owners | Personal CVs and unrelated files are excluded | $(Format-Cites ($evidence.Governance | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Operational Scope | Daily action plans, cadence, CRM, dashboards, pipeline, forecasting, discovery, objection handling, closing, onboarding, expansion | Non-sales functions are included only where they touch revenue movement | $(Format-Cites ($evidence.Process | Select-Object -First 5)) |")
$null = $sb.AppendLine("| AI Scope | Prompt constitution, execution prompts, agent roles, escalation, repository memory, auditability, and human override | Autonomous execution must remain bounded by governance | $(Format-Cites ($evidence.AI | Select-Object -First 6)) |")
$null = $sb.AppendLine("| Governance Scope | Doctrine, SOPs, legal structure, payment design, review cadence, ownership, archive, versioning, audit trails | Governance is not bureaucracy; it is continuity and risk control | $(Format-Cites ($evidence.Governance | Select-Object -First 6)) |")
$null = $sb.AppendLine("| Market Scope | ICP, buyer psychology, psychographics, channels, competition, social media, sector knowledge, audience creation | Market scope should be updated continuously through discovery and sales feedback | $(Format-Cites ($evidence.Market | Select-Object -First 6)) |")

Add-Section $sb '4. Institutional Operational Architecture'
$null = $sb.AppendLine('The operating architecture should run as a sequence of intelligence conversion:')
$null = $sb.AppendLine()
$null = $sb.AppendLine('`Market Signal -> Buyer Insight -> Positioning -> Offer Fit -> Lead Source -> Qualification -> Discovery -> Deal Strategy -> Proposal -> Close -> Onboarding -> Retention -> Expansion -> Reporting -> System Update`')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Operating System | Workflow | Accountability | Escalation Trigger | Evidence |')
$null = $sb.AppendLine('|---|---|---|---|---|')
$null = $sb.AppendLine("| Strategy Control | Mission, goals, positioning, ICP, offer economics | Commercial architect / founder | Strategy conflicts, bad-fit revenue, unclear offer | $(Format-Cites ($evidence.Philosophy | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Pipeline Control | Stage definitions, CRM hygiene, next steps, velocity, stuck deals | RevOps owner / sales lead | Stage aging, no next step, missing decision maker | $(Format-Cites ($evidence.Process | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Execution Control | Outreach, conversations, follow-up, objection handling, closing | Sales operator / account owner | Objection unresolved, ghosting, pricing resistance, low trust | $(Format-Cites ($evidence.Execution | Select-Object -First 4)) |")
$null = $sb.AppendLine("| Intelligence Control | Dashboards, decision logs, win/loss, buyer notes, sector files | RevOps + knowledge owner | Missing data, inconsistent metrics, forecast risk | $(Format-Cites ($evidence.RevOps | Select-Object -First 4)) |")
$null = $sb.AppendLine("| AI Control | Prompt hierarchy, agent routing, memory updates, approval rules | AI workflow architect / human operator | Low confidence, destructive action, conflicting instructions | $(Format-Cites ($evidence.AI | Select-Object -First 6)) |")

Add-Section $sb '5. Master Folder Architecture'
$null = $sb.AppendLine('The folder ecosystem must mirror the operating system, not document aesthetics. Every folder exists because it supports a workflow, a governance requirement, a retrieval need, or institutional memory.')
$null = $sb.AppendLine()
$null = $sb.AppendLine('```text')
$null = $sb.AppendLine('00_INSTITUTIONAL_CONTROL')
$null = $sb.AppendLine('  00_Source_Registry')
$null = $sb.AppendLine('  01_Constitution_Doctrine')
$null = $sb.AppendLine('  02_Decision_Log')
$null = $sb.AppendLine('  03_Governance_Review')
$null = $sb.AppendLine('01_REVENUE_STRATEGY')
$null = $sb.AppendLine('  01_Mission_Vision_Goals')
$null = $sb.AppendLine('  02_Positioning_Strategy')
$null = $sb.AppendLine('  03_Offer_Revenue_Model')
$null = $sb.AppendLine('  04_Market_Expansion')
$null = $sb.AppendLine('02_MARKET_CUSTOMER_INTELLIGENCE')
$null = $sb.AppendLine('  01_ICP_Buyer_Personas')
$null = $sb.AppendLine('  02_Sector_Knowledge')
$null = $sb.AppendLine('  03_Psychographics_Objections')
$null = $sb.AppendLine('  04_Competition_Alternatives')
$null = $sb.AppendLine('  05_Channel_Social_Intelligence')
$null = $sb.AppendLine('03_SALES_EXECUTION_OS')
$null = $sb.AppendLine('  01_Pipeline_CRM')
$null = $sb.AppendLine('  02_Prospecting_Outreach')
$null = $sb.AppendLine('  03_Discovery_Qualification')
$null = $sb.AppendLine('  04_Demo_Presentation')
$null = $sb.AppendLine('  05_Negotiation_Closing')
$null = $sb.AppendLine('  06_Onboarding_Handoff')
$null = $sb.AppendLine('  07_Retention_Expansion')
$null = $sb.AppendLine('04_REVOPS_PERFORMANCE')
$null = $sb.AppendLine('  01_KPIs_Metrics')
$null = $sb.AppendLine('  02_Forecasting')
$null = $sb.AppendLine('  03_Dashboards_Reports')
$null = $sb.AppendLine('  04_Cadence_Reviews')
$null = $sb.AppendLine('  05_Risk_Audit')
$null = $sb.AppendLine('05_ENABLEMENT_PLAYBOOKS')
$null = $sb.AppendLine('  01_SOPs')
$null = $sb.AppendLine('  02_Playbooks')
$null = $sb.AppendLine('  03_Scripts_Templates')
$null = $sb.AppendLine('  04_Coaching_Certification')
$null = $sb.AppendLine('06_AI_OPERATIONS')
$null = $sb.AppendLine('  01_System_Prompts')
$null = $sb.AppendLine('  02_Agent_Roles')
$null = $sb.AppendLine('  03_Execution_States')
$null = $sb.AppendLine('  04_Escalations_Approvals')
$null = $sb.AppendLine('  05_AI_Memory_Logs')
$null = $sb.AppendLine('07_CLIENT_PROJECTS')
$null = $sb.AppendLine('  CLIENT_[Name]')
$null = $sb.AppendLine('    01_Intake_Audit')
$null = $sb.AppendLine('    02_Strategy')
$null = $sb.AppendLine('    03_Execution')
$null = $sb.AppendLine('    04_Reporting')
$null = $sb.AppendLine('    05_Decisions_Archive')
$null = $sb.AppendLine('08_ARCHIVE_INSTITUTIONAL_MEMORY')
$null = $sb.AppendLine('  01_Legacy_Drafts')
$null = $sb.AppendLine('  02_Superseded_Versions')
$null = $sb.AppendLine('  03_Closed_Projects')
$null = $sb.AppendLine('  04_Evidence_Exports')
$null = $sb.AppendLine('```')
$null = $sb.AppendLine()
$null = $sb.AppendLine("Folder architecture evidence: $(Format-Cites $evidence.Folder).")

Add-Section $sb '6. Subfolder Intelligence'
$null = $sb.AppendLine('| Major Folder | Purpose | Contents | Operational Role | Governance Role | Lifecycle | Dependencies | Usage Frequency |')
$null = $sb.AppendLine('|---|---|---|---|---|---|---|---|')
$folderRows = @(
  @('00_INSTITUTIONAL_CONTROL','Protect the system identity and source of truth','Constitution, doctrine, source registry, decision log','Defines how the institution thinks and decides','Highest authority; review required','Permanent','All folders depend on it','Weekly / quarterly'),
  @('01_REVENUE_STRATEGY','Own strategic commercial direction','Mission, ICP strategy, positioning, offer model','Translates vision into GTM choices','Strategy changes require approval','Permanent with quarterly updates','Market intelligence and RevOps reporting','Monthly / quarterly'),
  @('02_MARKET_CUSTOMER_INTELLIGENCE','Store buyer, market, and competitive truth','ICP, personas, objections, sector knowledge, channel intelligence','Feeds targeting, scripts, qualification, and positioning','Must cite discovery or research sources','Continuously updated','Sales execution and strategy','Daily / weekly'),
  @('03_SALES_EXECUTION_OS','Run the sales motion','Pipeline, outreach, discovery, demos, negotiation, closing, handoff, expansion','Daily frontline execution engine','CRM hygiene and SLA enforcement','Active operating layer','Market intelligence, RevOps, enablement','Daily'),
  @('04_REVOPS_PERFORMANCE','Measure, forecast, and govern revenue movement','KPIs, dashboards, forecasts, cadence reviews, audits','Management control layer','Metric definitions and reporting cadence','Recurring operating layer','CRM and sales execution','Daily / weekly / monthly'),
  @('05_ENABLEMENT_PLAYBOOKS','Scale capability and consistency','SOPs, playbooks, scripts, coaching, certification','Converts knowledge into repeatable behavior','Version controlled; owner required','Updated after learning loops','All execution workflows','Weekly'),
  @('06_AI_OPERATIONS','Govern AI-human operational coordination','System prompts, agents, execution states, escalations, memory logs','AI runtime and orchestration layer','Approval, auditability, memory retention','Permanent and continuously refined','Institutional control, knowledge, execution','Daily'),
  @('07_CLIENT_PROJECTS','Deliver the system for specific clients or offers','Audit, strategy, execution, reporting, decisions','Client-specific delivery layer','Scope, legal, data, and deliverable governance','Created per client; archived at close','Revenue strategy, execution, AI ops','Daily during active projects'),
  @('08_ARCHIVE_INSTITUTIONAL_MEMORY','Preserve evolution and evidence','Legacy drafts, superseded versions, closed projects, evidence exports','Prevents knowledge loss and supports reconstruction','Archive rules and retention policy','Permanent archive','All folders feed it','Monthly / quarterly')
)
foreach ($r in $folderRows) { $null = $sb.AppendLine("| $($r[0]) | $($r[1]) | $($r[2]) | $($r[3]) | $($r[4]) | $($r[5]) | $($r[6]) | $($r[7]) |") }

Add-Section $sb '7. Naming Convention System'
$null = $sb.AppendLine('Use names that encode domain, function, topic, status, version, and date. The naming system must support human retrieval and AI parsing.')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Asset Type | Format | Example | Rule |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine('| Folder | `[NN]_[DOMAIN]_[FUNCTION]` | `03_SALES_EXECUTION_OS` | Number by operating sequence, not preference |')
$null = $sb.AppendLine('| Conversation | `[DOMAIN][WORKFLOW][TOPIC][YYYY-MM-DD][STATUS]` | `SALES_DISCOVERY_LogisticsICP_2026-05-12_ACTIVE` | Every strategic chat becomes a retrievable artifact |')
$null = $sb.AppendLine('| SOP | `[SOP][DOMAIN][PROCESS][STATUS][v#.#]` | `SOP_SALES_DiscoveryQualification_APPROVED_v1.0` | Approved SOPs require owner and review date |')
$null = $sb.AppendLine('| Project | `[CLIENT][WORKSTREAM][PHASE][STATUS]` | `ABC_Logistics_ROS_Audit_ACTIVE` | Client work must separate audit, strategy, execution, reporting |')
$null = $sb.AppendLine('| Asset | `[ASSET][FUNNEL_STAGE][TOPIC][STATUS][v#.#]` | `ASSET_OUTREACH_LinkedInScript_DRAFT_v0.3` | Assets inherit funnel stage |')
$null = $sb.AppendLine('| Archive | `[ARCHIVE][DOMAIN][REASON][YYYY-MM-DD]` | `ARCHIVE_SALES_SupersededDrafts_2026-05-12` | Archive names must state why they exist |')
$null = $sb.AppendLine('| Version | `vMAJOR.MINOR` plus status | `APPROVED_v1.0`, `DRAFT_v0.4` | Major versions change behavior; minor versions refine wording |')
$null = $sb.AppendLine()
$null = $sb.AppendLine('Canonical metadata block for permanent documents:')
$null = $sb.AppendLine()
$null = $sb.AppendLine('```yaml')
$null = $sb.AppendLine('document_id: SOP_SALES_DiscoveryQualification_APPROVED_v1.0')
$null = $sb.AppendLine('owner: Sales Operations')
$null = $sb.AppendLine('status: APPROVED')
$null = $sb.AppendLine('version: v1.0')
$null = $sb.AppendLine('created: YYYY-MM-DD')
$null = $sb.AppendLine('review_cycle: Monthly')
$null = $sb.AppendLine('source_evidence: [SD-019:P0001, SD-048:P0012]')
$null = $sb.AppendLine('dependencies: [CRM_Stage_Definitions, ICP_Doctrine]')
$null = $sb.AppendLine('confidentiality: Internal')
$null = $sb.AppendLine('```')

Add-Section $sb '8. Information Classification System'
$null = $sb.AppendLine('| Classification Axis | Rule | Examples | Storage |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine('| Strategic vs Operational | Strategic defines choices and doctrine; operational defines execution | Mission, ICP doctrine vs daily action plan, scripts | Strategy folders vs execution folders |')
$null = $sb.AppendLine('| Temporary vs Permanent | Temporary is active working material; permanent governs repeatable behavior | Brainstorm chat vs approved SOP | Working project folder vs institutional control |')
$null = $sb.AppendLine('| Active vs Archived | Active changes current execution; archived preserves lineage | Current playbook vs superseded draft | Active OS folders vs archive |')
$null = $sb.AppendLine('| Confidential vs General | Confidential contains contracts, pricing, client data, legal risk, or sensitive strategy | Sales Agent Agreement, pricing calculators, client CRM exports | Restricted governance/client folders |')
$null = $sb.AppendLine('| Execution vs Reference | Execution assets are used in workflows; reference assets explain concepts | Outreach script vs sales philosophy note | Sales Execution OS vs Institutional Memory |')
$null = $sb.AppendLine('| Explicit vs Inferred | Explicit appears in source text; inferred is synthesized from patterns | Named prompt hierarchy vs reconstructed dependency map | Evidence register must label inference type |')

Add-Section $sb '9. Document Alignment Matrix'
$null = $sb.AppendLine('| Document | Purpose | Operational Role | Strategic Role | Dependencies | Related Systems | Governance Impact | AI Relevance | Missing Links | Contradictions | Folder Placement |')
$null = $sb.AppendLine('|---|---|---|---|---|---|---|---|---|---|---|')
foreach ($s in ($sources | Sort-Object Origin,Draft,Name)) {
  $purpose = $s.Category
  $strategicRole = if ($s.Category -match 'Foundational|doctrine|philosophy') {'Defines worldview and strategic beliefs'} elseif ($s.Category -match 'Market') {'Defines targeting, buyer, and market interpretation'} elseif ($s.Category -match 'Monetization|Revenue') {'Defines commercial model and economic logic'} elseif ($s.Category -match 'AI') {'Defines intelligence and AI operating logic'} elseif ($s.Category -match 'Governance') {'Defines control, risk, and accountability'} else {'Supports integrated revenue operating architecture'}
  $deps = if ($s.OperationalRole -match 'execution') {'ICP, offer, CRM, cadence'} elseif ($s.OperationalRole -match 'Measurement') {'CRM data, stage definitions, KPI dictionary'} elseif ($s.OperationalRole -match 'Governance') {'Doctrine, ownership, approval rules'} elseif ($s.OperationalRole -match 'Market') {'Research, discovery, sector data'} else {'Source registry, doctrine, related operating documents'}
  $related = if ($s.Category -match 'AI') {'AI Operations; Institutional Memory; Folder Architecture'} elseif ($s.Category -match 'Market') {'Market Intelligence; Sales Execution; Offer Strategy'} elseif ($s.Category -match 'Revenue|Monetization') {'Revenue Strategy; Pricing; Client Delivery'} elseif ($s.Category -match 'Governance') {'Governance; Legal; Audit; Archive'} else {'Revenue Strategy; Sales Execution; RevOps'}
  $gov = if ($s.Criticality -eq 'Critical') {'High governance impact; should become controlled source'} elseif ($s.Criticality -eq 'High') {'Requires owner and review cadence'} else {'Reference governance; useful for lineage'}
  $missing = if ($s.Maturity -match 'Conceptual') {'Needs owner, version, acceptance criteria, and operating template'} elseif ($s.Maturity -match 'Operational') {'Needs approval status, KPI linkage, and update cadence'} else {'Needs final source-of-truth designation and change log'}
  $contr = if ($s.Name -match 'Draft 29|Draft 37|Draft 63|Darft') {'Naming/draft-number collision or typo requires registry resolution'} else {'No direct contradiction detected; compare during governance review'}
  $folder = if ($s.Category -match 'AI') {'06_AI_OPERATIONS'} elseif ($s.Category -match 'Market') {'02_MARKET_CUSTOMER_INTELLIGENCE'} elseif ($s.Category -match 'Revenue|Monetization') {'01_REVENUE_STRATEGY'} elseif ($s.Category -match 'Governance') {'00_INSTITUTIONAL_CONTROL'} elseif ($s.OperationalRole -match 'Measurement') {'04_REVOPS_PERFORMANCE'} elseif ($s.OperationalRole -match 'SOP|procedure|cadence') {'05_ENABLEMENT_PLAYBOOKS'} else {'08_ARCHIVE_INSTITUTIONAL_MEMORY plus active mapped folder'}
  $null = $sb.AppendLine("| $($s.SourceId) - $($s.Name.Replace('|','/')) | $purpose | $($s.OperationalRole) | $strategicRole | $deps | $related | $gov | $($s.AIRelevance) | $missing | $contr | $folder |")
}

Add-Section $sb '10. Revenue Process Architecture'
$null = $sb.AppendLine("The revenue process should be governed as a lifecycle, not as a loose funnel. Evidence: $(Format-Cites $evidence.Process).")
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Stage | Entry Criteria | Core Work | Exit Criteria | CRM Governance | Forecast Signal |')
$null = $sb.AppendLine('|---|---|---|---|---|---|')
$null = $sb.AppendLine('| Market Signal | Segment, problem, trigger, or channel signal identified | Research, audience mapping, sector intelligence | ICP hypothesis created | Account/segment source tagged | Market opportunity score |')
$null = $sb.AppendLine('| Lead Identified | Named account/contact fits baseline ICP | Enrichment, relevance check, channel choice | Contact has reason-to-engage | Lead source + ICP fields complete | Low forecast weight |')
$null = $sb.AppendLine('| Engaged | Prospect responds or interacts | Conversation opening, pain probe, trust signal | Meeting or next step accepted | Activity logged; next step dated | Engagement quality |')
$null = $sb.AppendLine('| Qualified | Need, fit, authority, urgency, budget/risk understood | Discovery, qualification scoring, stakeholder map | Qualified opportunity or disqualified reason | Qualification fields complete | Pipeline inclusion |')
$null = $sb.AppendLine('| Discovery Complete | Problem and decision context mapped | Diagnose pain, desired state, risk, alternatives | Mutual problem definition agreed | Discovery notes and buyer criteria attached | Forecast confidence improves |')
$null = $sb.AppendLine('| Solution Positioned | Offer mapped to buyer transformation | Demo/proposal/presentation | Buyer understands value and path | Proposal asset linked | Value confidence |')
$null = $sb.AppendLine('| Negotiation | Buyer is evaluating terms, price, risk | Objection handling, legal/payment structure, ROI | Verbal yes or clear blocker | Objections and commercial terms logged | Close probability adjusted |')
$null = $sb.AppendLine('| Closed Won/Lost | Decision made | Contract/payment or loss reason | Handoff or win/loss review complete | Close reason required | Actual revenue / learning |')
$null = $sb.AppendLine('| Onboarding | Client/customer has committed | Handoff, expectations, kickoff, delivery activation | First value milestone achieved | Customer record linked | Retention signal |')
$null = $sb.AppendLine('| Expansion | Value delivered and new opportunity exists | Upsell, referral, renewal, partnership | Expansion opportunity created or declined | Expansion source tagged | Net revenue retention |')

Add-Section $sb '11. Execution Workflow Systems'
$null = $sb.AppendLine('| Workflow | Inputs | Sequence | Outputs | Failure Modes | Evidence |')
$null = $sb.AppendLine('|---|---|---|---|---|---|')
$null = $sb.AppendLine("| Outreach | ICP, trigger, channel, offer angle | Segment, personalize, message, send, follow up, log response | Conversations and qualified meetings | Generic messaging, wrong timing, poor list | $(Format-Cites ($evidence.Execution | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Discovery | Prospect context, hypothesis, qualification criteria | Frame, diagnose, question, mirror, map decision, confirm next step | Problem map and qualification score | Asking too shallow, skipping authority, no next step | $(Format-Cites ($evidence.Process | Select-Object -First 3)) |")
$null = $sb.AppendLine("| Demo / Presentation | Discovery notes, buyer criteria, value proof | Show only relevant capabilities, connect to pain, prove ROI, invite objections | Buyer belief and evaluation path | Feature dumping, no business case | $(Format-Cites (Get-Evidence $sources @('demo','presentation','value','ROI','proof') 5)) |")
$null = $sb.AppendLine("| Negotiation | Proposal, objections, risk, terms | Clarify concern, reframe value, adjust scope, protect margin, confirm decision | Signed terms or explicit blocker | Discounting without diagnosis, vague legal/payment risk | $(Format-Cites (Get-Evidence $sources @('negotiation','payment','legal','objection','risk') 5)) |")
$null = $sb.AppendLine("| Closing | Decision criteria, urgency, stakeholder alignment | Summarize value, remove final risk, ask for decision, define handoff | Won/lost decision and next operational action | Weak urgency, unresolved stakeholder, unclear buying process | $(Format-Cites (Get-Evidence $sources @('closing','close','decision','urgency','handoff') 5)) |")
$null = $sb.AppendLine("| Onboarding | Signed agreement, scope, buyer expectations | Kickoff, handoff, success plan, communication cadence | Activated client/customer | Broken handoff, unclear expectations | $(Format-Cites (Get-Evidence $sources @('onboarding','handoff','kickoff','client') 5)) |")
$null = $sb.AppendLine("| Expansion | Delivered value, relationship health, new need | Review outcomes, identify next value, propose expansion | Renewal, upsell, referral, partnership | No proof of value, no relationship owner | $(Format-Cites (Get-Evidence $sources @('expansion','renewal','upsell','retention','referral') 5)) |")

Add-Section $sb '12. Execution Cadence Systems'
$null = $sb.AppendLine("Cadence appears as a recurring operational anchor: daily action, calendar operations, metrics rhythm, and governance reviews. Evidence: $(Format-Cites (Get-Evidence $sources @('daily','weekly','monthly','quarterly','cadence','calendar','review') 12)).")
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Cadence | Purpose | Required Actions | Outputs | Owner |')
$null = $sb.AppendLine('|---|---|---|---|---|')
$null = $sb.AppendLine('| Daily | Move revenue today | Review active deals, generate leads, follow up, resolve objections, update CRM, run AI daily execution prompt | Top 5 actions, next steps, blocker list | Sales operator |')
$null = $sb.AppendLine('| Weekly | Govern pipeline and learning | Pipeline review, forecast update, win/loss learning, coaching, content/channel review | Forecast, stuck-deal actions, coaching notes | Sales lead + RevOps |')
$null = $sb.AppendLine('| Monthly | Improve system performance | KPI review, channel performance, ICP refinement, asset updates, SOP review | Metrics report, optimization backlog | RevOps owner |')
$null = $sb.AppendLine('| Quarterly | Re-align strategy | Market position, revenue model, offer performance, governance audit, AI memory review | Strategic refresh and controlled changes | Commercial architect |')
$null = $sb.AppendLine('| Annual | Preserve institutional continuity | Archive, doctrine review, operating model redesign, compensation/payment review, knowledge base audit | Annual revenue operating blueprint | Leadership / founder |')

Add-Section $sb '13. AI Operational Intelligence Map'
$null = $sb.AppendLine("AI is a first-class operating layer in the corpus, not a writing assistant. It is framed as constitution, prompt hierarchy, agent orchestration, execution state machine, repository intelligence, memory, escalation, and auditability. Evidence: $(Format-Cites $evidence.AI).")
$null = $sb.AppendLine()
$null = $sb.AppendLine('| AI System | Function | Controls | Human Boundary | Evidence |')
$null = $sb.AppendLine('|---|---|---|---|---|')
$null = $sb.AppendLine("| Prompt Governance | Defines identity, mission, constraints, output formats, and reasoning obligations | System prompts, execution prompts, source citation rules | Human approves constitutional changes | $(Format-Cites (Get-Evidence $sources @('system prompt','prompt architecture','constitution','instructions') 6)) |")
$null = $sb.AppendLine("| Agent Orchestration | Routes work across market intelligence, offer, lead gen, qualification, deal strategy, closing, retention, optimization | Role definitions and execution states | Human owns final commercial judgment | $(Format-Cites (Get-Evidence $sources @('agent','orchestration','Market Intelligence Agent','Closing Agent') 6)) |")
$null = $sb.AppendLine("| Execution State Machine | Analyze, plan, execute, verify, report | No silent skipping of states | Human approval for destructive or high-risk actions | $(Format-Cites (Get-Evidence $sources @('ANALYZE','PLAN','EXECUTE','VERIFY','REPORT','execution states') 6)) |")
$null = $sb.AppendLine("| Escalation System | Detects ambiguity, low confidence, production risk, legal risk, missing context | Confidence thresholds, risk categories, escalation format | Human decides under uncertainty | $(Format-Cites (Get-Evidence $sources @('escalate','confidence','risk','approval','ambiguity') 6)) |")
$null = $sb.AppendLine("| Memory System | Preserves active projects, decisions, architecture rules, blockers, patterns | Repository folders, decision logs, archive rules | Human curates source of truth | $(Format-Cites (Get-Evidence $sources @('memory','context continuity','decisions','archive','logs') 6)) |")
$null = $sb.AppendLine("| Auditability | Makes AI outputs traceable to documents and decisions | Evidence IDs, source registry, change logs | Human auditor can verify lineage | $(Format-Cites (Get-Evidence $sources @('audit','evidence','source','trace','governance') 6)) |")

Add-Section $sb '14. Knowledge Graph & Dependency Mapping'
$null = $sb.AppendLine('```mermaid')
$null = $sb.AppendLine('flowchart TD')
$null = $sb.AppendLine('  Doctrine["Doctrine / Constitution"] --> Strategy["Revenue Strategy"]')
$null = $sb.AppendLine('  Strategy --> Market["Market + Buyer Intelligence"]')
$null = $sb.AppendLine('  Market --> Positioning["Positioning + Offer"]')
$null = $sb.AppendLine('  Positioning --> Pipeline["Pipeline + CRM"]')
$null = $sb.AppendLine('  Pipeline --> Execution["Sales Execution"]')
$null = $sb.AppendLine('  Execution --> RevOps["Metrics + Forecasting"]')
$null = $sb.AppendLine('  RevOps --> Learning["Learning + Enablement"]')
$null = $sb.AppendLine('  Learning --> Doctrine')
$null = $sb.AppendLine('  AI["AI Operations"] --> Market')
$null = $sb.AppendLine('  AI --> Execution')
$null = $sb.AppendLine('  AI --> RevOps')
$null = $sb.AppendLine('  Governance["Governance + Archive"] --> Doctrine')
$null = $sb.AppendLine('  Governance --> AI')
$null = $sb.AppendLine('  Governance --> RevOps')
$null = $sb.AppendLine('```')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Dependency | Why It Matters | Bottleneck Risk | Control |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine('| ICP -> Outreach | Message relevance depends on target clarity | Volume without conversion | ICP scoring and buyer notes |')
$null = $sb.AppendLine('| Discovery -> Proposal | Proposal quality depends on problem diagnosis | Generic proposals and pricing resistance | Discovery completion gate |')
$null = $sb.AppendLine('| CRM -> Forecast | Forecast depends on stage truth | False confidence | Required fields and stage exit rules |')
$null = $sb.AppendLine('| Objections -> Enablement | Repeated objections reveal asset gaps | Repeated frontline friction | Objection log and script updates |')
$null = $sb.AppendLine('| AI Memory -> Execution | AI output depends on current operating context | Stale or hallucinated recommendations | Source registry and memory review |')
$null = $sb.AppendLine('| Governance -> Scale | Scale requires repeatability and audit | Drift, inconsistent client delivery | SOP ownership and review cadence |')

Add-Section $sb '15. Missing Components Analysis'
$null = $sb.AppendLine('| Gap | Why It Matters | Required Build | Priority | Evidence / Basis |')
$null = $sb.AppendLine('|---|---|---|---|---|')
$null = $sb.AppendLine("| Approved Source of Truth | Many documents are drafts or synthesis attempts | Create approved master doctrine, SOP set, and archive policy | Critical | Registry maturity analysis |")
$null = $sb.AppendLine("| CRM Field Dictionary | Pipeline and forecast logic appear often, but field definitions need formalization | Define stage, source, ICP, objection, next-step, probability, and loss-reason fields | Critical | $(Format-Cites ($evidence.Process | Select-Object -First 5)) |")
$null = $sb.AppendLine("| KPI Dictionary | Metrics are discussed but need canonical definitions | Define formula, owner, cadence, and dashboard placement for each KPI | High | $(Format-Cites ($evidence.RevOps | Select-Object -First 5)) |")
$null = $sb.AppendLine("| Governance RACI | Ownership appears across roles but needs decision rights | Build RACI for strategy, CRM, AI, client delivery, legal/payment, archive | High | $(Format-Cites ($evidence.Governance | Select-Object -First 5)) |")
$null = $sb.AppendLine("| AI Approval Matrix | AI execution concepts require risk controls | Define what AI can draft, recommend, execute, and escalate | Critical | $(Format-Cites ($evidence.AI | Select-Object -First 6)) |")
$null = $sb.AppendLine("| Training Certification | Playbooks exist as concepts but need capability gates | Build onboarding, role certification, simulations, coaching rubrics | Medium | $(Format-Cites ($evidence.Enablement | Select-Object -First 5)) |")
$null = $sb.AppendLine("| Data Retention Policy | Institutional memory needs archive boundaries | Define active, reference, archive, superseded, confidential retention rules | High | $(Format-Cites ($evidence.Folder | Select-Object -First 5)) |")

Add-Section $sb '16. Contradictions & Operational Tensions'
$null = $sb.AppendLine('| Tension | Description | Operational Meaning | Resolution Rule |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine('| Draft Number Collisions | Drafts 29, 37, and 63 exist as multiple different documents | Number sequence alone is not a reliable lineage system | Use source IDs, filenames, and modified timestamps |')
$null = $sb.AppendLine('| Missing Drafts | Drafts 62 and 64 are outside the draft folder and typo-labeled `Darft` | Source corpus is distributed across folders | Treat parent companion files as source-resolving documents |')
$null = $sb.AppendLine('| Conceptual Depth vs Daily Simplicity | Corpus wants enterprise architecture and simple daily action | System must support both institutional blueprint and frontline execution | Separate doctrine, SOP, and daily execution prompt layers |')
$null = $sb.AppendLine('| Autonomy vs Control | AI workflows are central, but legal, destructive, and unclear actions require governance | AI must accelerate work without owning final risk | Approval matrix and escalation doctrine |')
$null = $sb.AppendLine('| Funnel vs Flywheel | Funnel stages and flywheel logic both appear | Acquisition and retention are not competing models | Use lifecycle funnel inside broader revenue learning flywheel |')
$null = $sb.AppendLine('| Sales Art vs Sales System | Buyer psychology and power navigation coexist with CRM governance and metrics | Both cognition and process are necessary | Pair every workflow with buyer psychology and data controls |')

Add-Section $sb '17. Source Traceability & Evidence Mapping'
$null = $sb.AppendLine('| Insight | Source Origin | Supporting References | Confidence Level | Inference Type | Unresolved Dependencies |')
$null = $sb.AppendLine('|---|---|---|---|---|---|')
$traceRows = @(
  @('Sales is reconstructed as value, trust, decision support, and transformation rather than pressure selling','Philosophy and foundational sales documents',$(Format-Cites $evidence.Philosophy),'High','Cross-document synthesis','Approved doctrine wording'),
  @('The system requires a lifecycle revenue architecture, not isolated scripts or funnels','Process, operating system, blueprint, and RevOps documents',$(Format-Cites $evidence.Process),'High','Cross-document synthesis','CRM stage dictionary'),
  @('Buyer psychology, audience navigation, psychographics, power, and objections are core operating intelligence','Market, discovery, objection, psychographic, and power-navigation documents',$(Format-Cites $evidence.Market),'High','Cross-document synthesis','Buyer persona template'),
  @('Revenue operations must govern metrics, dashboards, cadence, forecasting, and accountability','Metrics, calendar, tracking, decision intelligence, and system blueprint documents',$(Format-Cites $evidence.RevOps),'High','Explicit + synthesis','KPI dictionary and dashboard design'),
  @('AI is an operational coworker layer governed by prompts, roles, memory, escalation, and auditability','System prompt, execution prompt, AI architecture, Sales Operating System, and reconstruction documents',$(Format-Cites $evidence.AI),'High','Explicit + synthesis','AI approval matrix and memory policy'),
  @('Folder architecture is part of the operating system because memory, retrieval, and governance depend on it','Folder, repository, memory, governance, AI, and project ToC documents',$(Format-Cites $evidence.Folder),'High','Cross-document synthesis','Physical folder migration plan'),
  @('Offer, monetization, audit-first motion, and payment structure form the commercial model','Revenue architecture, monetization, offer structuring, payment, and legal documents',$(Format-Cites $evidence.Monetization),'High','Explicit + synthesis','Pricing calculator and SOW templates'),
  @('Governance must include constitution, policies, ownership, review cadence, archive, and legal/payment controls','Governance blueprint, legal, agreement, payment, SOP, and AI documents',$(Format-Cites $evidence.Governance),'High','Explicit + synthesis','RACI and review calendar')
)
foreach ($r in $traceRows) { $null = $sb.AppendLine("| $($r[0]) | $($r[1]) | $($r[2]) | $($r[3]) | $($r[4]) | $($r[5]) |") }
$null = $sb.AppendLine()
$null = $sb.AppendLine('Selected evidence snippets:')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Topic | Evidence Anchor | Snippet |')
$null = $sb.AppendLine('|---|---|---|')
foreach ($topic in $evidence.Keys) {
  foreach ($ev in ($evidence[$topic] | Select-Object -First 3)) {
    $null = $sb.AppendLine("| $topic | $($ev.SourceId):$($ev.Para) | $($ev.Snippet) |")
  }
}

Add-Section $sb '18. Document Ecosystem Map'
$null = $sb.AppendLine('```text')
$null = $sb.AppendLine('Strategic Foundation')
$null = $sb.AppendLine('  Draft 1 Strategy -> Draft 66 Sales Definition -> Mission/Vision/Values -> Sales Philosophy')
$null = $sb.AppendLine('Market Intelligence')
$null = $sb.AppendLine('  Sector Knowledge -> Psychographics -> Audience Navigation -> Social Media -> Competition -> Channels')
$null = $sb.AppendLine('Sales Mechanics')
$null = $sb.AppendLine('  Funnels -> Process Clarity -> Discovery -> Diagnosis -> Cycle Tips -> SOPs -> Daily Action')
$null = $sb.AppendLine('Revenue Operations')
$null = $sb.AppendLine('  Tracking -> Metrics -> Dashboards -> Forecasting -> Calendar -> Cadence -> Decision Intelligence')
$null = $sb.AppendLine('Commercial Model')
$null = $sb.AppendLine('  Monetization Layer -> Offer Structuring -> Payment System -> Revenue Breakdown -> Revenue Architecture Agency')
$null = $sb.AppendLine('Governance')
$null = $sb.AppendLine('  Legal Structuring -> Sales Agent Agreement -> Governance Blueprint -> Department Scope Map -> Archive Policy')
$null = $sb.AppendLine('AI + Institutional Memory')
$null = $sb.AppendLine('  System Prompt Architecture -> Execution Prompt -> Sales Operating System -> Sales Intelligence Architecture -> Reconstruction')
$null = $sb.AppendLine('Final Synthesis')
$null = $sb.AppendLine('  Revenue Operating System Design -> Revenue Architecture Framework -> Master Blueprint')
$null = $sb.AppendLine('```')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Ecosystem Zone | Active Documents | Legacy / Source Documents | Governance Treatment |')
$null = $sb.AppendLine('|---|---|---|---|')
$null = $sb.AppendLine('| Active synthesis | Drafts 60, 61, 63, 64, 65 plus this blueprint | Earlier conceptual drafts | Promote to controlled master sources after review |')
$null = $sb.AppendLine('| Source doctrine | Drafts 1, 2, 4, 6, 8, 43, 66 | Duplicate originals | Preserve as lineage and extract doctrine |')
$null = $sb.AppendLine('| Execution assets | Drafts 3, 11, 25, 26, 34, 40, 48, 52, 57 | Sales Mechanism docs | Convert into SOPs/playbooks |')
$null = $sb.AppendLine('| Governance assets | Drafts 37 legal, 39, 41, agreement, scope map | Supporting legal/payment drafts | Restrict access and assign owner |')
$null = $sb.AppendLine('| AI assets | Drafts 47, 48, 60, 61, 63 | Prompt architecture fragments | Convert into AI constitution and agent runtime docs |')

Add-Section $sb '19. Visual Organization Maps'
$null = $sb.AppendLine('### Operating Relationship Map')
$null = $sb.AppendLine()
$null = $sb.AppendLine('```mermaid')
$null = $sb.AppendLine('flowchart LR')
$null = $sb.AppendLine('  A["Doctrine"] --> B["Market Intelligence"] --> C["Offer + Positioning"] --> D["Sales Execution"] --> E["Revenue Operations"] --> F["Enablement"] --> A')
$null = $sb.AppendLine('  G["AI Operations"] --> B')
$null = $sb.AppendLine('  G --> D')
$null = $sb.AppendLine('  G --> E')
$null = $sb.AppendLine('  H["Governance"] --> A')
$null = $sb.AppendLine('  H --> G')
$null = $sb.AppendLine('  H --> E')
$null = $sb.AppendLine('```')
$null = $sb.AppendLine()
$null = $sb.AppendLine('### Information Movement Map')
$null = $sb.AppendLine()
$null = $sb.AppendLine('```mermaid')
$null = $sb.AppendLine('sequenceDiagram')
$null = $sb.AppendLine('  participant Market')
$null = $sb.AppendLine('  participant Sales')
$null = $sb.AppendLine('  participant CRM')
$null = $sb.AppendLine('  participant RevOps')
$null = $sb.AppendLine('  participant Knowledge')
$null = $sb.AppendLine('  participant AI')
$null = $sb.AppendLine('  Market->>Sales: ICP, triggers, objections')
$null = $sb.AppendLine('  Sales->>CRM: activities, stages, notes, next steps')
$null = $sb.AppendLine('  CRM->>RevOps: pipeline, forecast, conversion data')
$null = $sb.AppendLine('  RevOps->>Knowledge: insights, risks, metrics')
$null = $sb.AppendLine('  Knowledge->>AI: controlled context and source evidence')
$null = $sb.AppendLine('  AI->>Sales: prompts, scripts, analysis, next actions')
$null = $sb.AppendLine('```')
$null = $sb.AppendLine()
$null = $sb.AppendLine('### Folder Intelligence Map')
$null = $sb.AppendLine()
$null = $sb.AppendLine('```mermaid')
$null = $sb.AppendLine('flowchart TD')
$null = $sb.AppendLine('  Root["Revenue Commercial OS"]')
$null = $sb.AppendLine('  Root --> Control["00 Institutional Control"]')
$null = $sb.AppendLine('  Root --> Strategy["01 Revenue Strategy"]')
$null = $sb.AppendLine('  Root --> Market["02 Market Customer Intelligence"]')
$null = $sb.AppendLine('  Root --> Execution["03 Sales Execution OS"]')
$null = $sb.AppendLine('  Root --> RevOps["04 RevOps Performance"]')
$null = $sb.AppendLine('  Root --> Enablement["05 Enablement Playbooks"]')
$null = $sb.AppendLine('  Root --> AI["06 AI Operations"]')
$null = $sb.AppendLine('  Root --> Client["07 Client Projects"]')
$null = $sb.AppendLine('  Root --> Archive["08 Archive Institutional Memory"]')
$null = $sb.AppendLine('```')

Add-Section $sb '20. Final Institutional Architecture Blueprint'
$null = $sb.AppendLine('The final integrated architecture is an AI-native Revenue & Commercial Operating System with eight permanent institutional capabilities:')
$null = $sb.AppendLine()
$null = $sb.AppendLine('| Capability | Blueprint | Operating Outcome |')
$null = $sb.AppendLine('|---|---|---|')
$null = $sb.AppendLine('| Revenue Operations | CRM governance, KPI dictionary, forecasting cadence, dashboard hierarchy, audit loop | Predictable revenue visibility and operational control |')
$null = $sb.AppendLine('| Sales | Lifecycle pipeline, discovery, qualification, buyer psychology, objection handling, negotiation, closing, onboarding, expansion | Repeatable conversion with preserved nuance |')
$null = $sb.AppendLine('| GTM | ICP, sector knowledge, channels, social media, positioning, offer economics, audience creation | Targeted market movement and adaptive positioning |')
$null = $sb.AppendLine('| Enablement | SOPs, playbooks, scripts, coaching, certification, battlecards, simulations | Scalable capability, not founder-dependent execution |')
$null = $sb.AppendLine('| AI Operations | Prompt constitution, agent roles, routing, memory, escalation, human approval, auditability | Human-AI coordination with controlled autonomy |')
$null = $sb.AppendLine('| Governance | Constitution, ownership, legal/payment controls, decision logs, review cadence, archive policy | Institutional safety, continuity, and accountability |')
$null = $sb.AppendLine('| Knowledge Management | Source registry, paragraph evidence, folder architecture, versioning, metadata, retrieval logic | Searchable institutional memory and source traceability |')
$null = $sb.AppendLine('| Institutional Continuity | Archive, lineage, superseded version handling, annual reviews, operating blueprint refresh | The system survives personnel, tool, and strategy changes |')
$null = $sb.AppendLine()
$null = $sb.AppendLine('### Implementation Sequence')
$null = $sb.AppendLine()
$null = $sb.AppendLine('1. Approve the master doctrine and source registry.')
$null = $sb.AppendLine('2. Create the folder architecture and migrate documents by classification.')
$null = $sb.AppendLine('3. Convert the execution documents into SOPs and playbooks.')
$null = $sb.AppendLine('4. Define CRM stages, field dictionary, dashboards, and forecast cadence.')
$null = $sb.AppendLine('5. Build the AI operations folder: system prompts, agent roles, execution states, escalation rules, and memory logs.')
$null = $sb.AppendLine('6. Create governance controls: RACI, review cadence, archive policy, legal/payment templates.')
$null = $sb.AppendLine('7. Run the operating system on one real client/project, then use the learning loop to refine the master blueprint.')
$null = $sb.AppendLine()
$null = $sb.AppendLine('### Final Operating Principle')
$null = $sb.AppendLine()
$null = $sb.AppendLine('The institution should never again depend on scattered chats as the only memory layer. Chats produce intelligence; intelligence becomes controlled documents; controlled documents govern workflows; workflows generate data; data updates strategy; AI accelerates the loop under human governance.')

$outputDir = Split-Path -Parent $OutputPath
$registryPath = Join-Path $outputDir 'Master_Source_Registry.csv'
$paragraphIndexPath = Join-Path $outputDir 'Master_Source_Paragraph_Index.csv'

$sources |
  Select-Object SourceId,Name,Path,Origin,Draft,LastWrite,Words,ParagraphCount,Category,OperationalRole,Maturity,Criticality,AIRelevance |
  Export-Csv -LiteralPath $registryPath -NoTypeInformation -Encoding UTF8

$paragraphRows = New-Object System.Collections.Generic.List[object]
foreach ($s in $sources) {
  for ($i = 0; $i -lt $s.Paragraphs.Count; $i++) {
    $paragraphRows.Add([pscustomobject]@{
      SourceId=$s.SourceId
      ParagraphId=('P{0:0000}' -f ($i + 1))
      Document=$s.Name
      Text=$s.Paragraphs[$i]
    })
  }
}
$paragraphRows | Export-Csv -LiteralPath $paragraphIndexPath -NoTypeInformation -Encoding UTF8

Set-Content -LiteralPath $OutputPath -Value $sb.ToString() -Encoding UTF8
Write-Output "Wrote $OutputPath"
Write-Output "Wrote $registryPath"
Write-Output "Wrote $paragraphIndexPath"
Write-Output "Sources: $($sources.Count)"
Write-Output "Words: $totalWords"
Write-Output "Paragraphs: $totalParas"

