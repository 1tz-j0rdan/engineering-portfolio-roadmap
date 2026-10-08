"""Print the earliest not-yet-earned certification and any active studies."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with (root/'data/certifications.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
active=[r for r in rows if r['status'] in ('Studying','Exam Scheduled','Passed - Pending Credential')]
for r in active:
    print(f"ACTIVE: {r['id']} — {r['provider']}: {r['certification']} ({r['status']})")
next_up=next((r for r in rows if r['status'] in ('Not Started','Planned')),None)
if next_up:print(f"NEXT: {next_up['id']} — {next_up['provider']}: {next_up['certification']}")
else:print('No remaining Not Started or Planned certifications.')
