import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with (root/'data/projects.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
active=[p for p in rows if p['status']=='In Progress']
if active:
    print('In progress:')
    for p in active:print(f"  {p['id']}: {p['project']}")
else:
    next_items=[p for p in rows if p['status'] in ('Planned','Not Started')]
    if next_items:print(f"Next suggested: {next_items[0]['id']}: {next_items[0]['project']}")
    else:print('No unstarted projects remain.')
