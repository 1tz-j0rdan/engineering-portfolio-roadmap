"""Generate certification roadmap and dashboard from data/*.csv."""
from pathlib import Path
from collections import Counter
import csv
ROOT = Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT / 'data' / name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

certs = read('certifications.csv')
phases = read('certification_phases.csv')
counts = Counter(c['status'] for c in certs)
statuses = ['Not Started','Planned','Studying','Exam Scheduled','Passed - Pending Credential','Earned','On Hold','Expired','Retired']
summary = f"{len(certs)} certifications tracked · {counts['Earned']} earned · {counts['Studying']} studying · {counts['Exam Scheduled']} scheduled"
road = ['# Certification Roadmap','','Generated from `data/certifications.csv`. Edit the CSV, then run `python scripts/update_certifications.py`.','','> Certification names and availability reflect the supplied planning list, not independently verified current provider offerings. Check official provider requirements before registering.','']
for ph in phases:
    road += [f"## Phase {ph['phase']} — {ph['title']}", '', f"**Goal:** {ph['goal']}", '']
    for c in certs:
        if c['phase'] != ph['phase']: continue
        mark = 'x' if c['status'] == 'Earned' else ' '
        evidence = f" — [credential]({c['credential_url']})" if c['credential_url'] else ''
        road.append(f"- [{mark}] **{c['order']}. {c['provider']}: {c['certification']}** — {c['status']}{evidence}")
    road.append('')
(ROOT/'docs'/'CERTIFICATIONS.md').write_text('\n'.join(road),encoding='utf-8')
progress=['# Certification Progress Dashboard','',f'**{summary}**','','## Status breakdown','','| Status | Count |','|---|---:|']
progress += [f'| {s} | {counts[s]} |' for s in statuses]
progress += ['','## Phase completion','','| Phase | Domain | Earned | Total |','|---:|---|---:|---:|']
for ph in phases:
    subset=[c for c in certs if c['phase']==ph['phase']]
    progress.append(f"| {ph['phase']} | {ph['title']} | {sum(c['status']=='Earned' for c in subset)} | {len(subset)} |")
progress += ['','## Currently studying or scheduled','','| ID | Certification | Status | Exam date |','|---|---|---|---|']
active=[c for c in certs if c['status'] in ('Studying','Exam Scheduled','Passed - Pending Credential')]
for c in active: progress.append(f"| {c['id']} | {c['provider']}: {c['certification']} | {c['status']} | {c['exam_scheduled_on'] or '—'} |")
if not active:progress.append('| — | None yet | — | — |')
progress += ['','## Earned credentials','','| ID | Certification | Earned | Expires | Evidence |','|---|---|---|---|---|']
earned=[c for c in certs if c['status']=='Earned']
for c in earned:
    link=f"[Credential]({c['credential_url']})" if c['credential_url'] else '—'
    progress.append(f"| {c['id']} | {c['provider']}: {c['certification']} | {c['earned_on']} | {c['expires_on'] or '—'} | {link} |")
if not earned: progress.append('| — | None yet | — | — | — |')
(ROOT/'docs'/'CERTIFICATION-PROGRESS.md').write_text('\n'.join(progress)+'\n',encoding='utf-8')
readme=ROOT/'README.md'
content=readme.read_text(encoding='utf-8')
a='<!-- CERT_PROGRESS_START -->';b='<!-- CERT_PROGRESS_END -->'
if a in content and b in content:
    start=content.index(a)+len(a);end=content.index(b)
    content=content[:start]+'\n'+summary+'\n'+content[end:]
    readme.write_text(content,encoding='utf-8')
print(summary)
