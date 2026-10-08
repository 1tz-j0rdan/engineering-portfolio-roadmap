# Engineering Portfolio Roadmap

A living, GitHub-native roadmap and completion tracker covering **68 phases**, **812 catalog entries**, and **12 multidisciplinary capstones**. All entries start as **Not Started**; no completion is assumed.

## Start here

1. Read [the full roadmap](docs/ROADMAP.md).
2. Review [the nine-stage project workflow](docs/WORKFLOW.md) and [repository standards](docs/PROJECT-STANDARDS.md).
3. Run `python scripts/next_project.py` to see the next planned item.
4. Edit `data/projects.csv` when a project changes status. Allowed statuses: `Not Started`, `Planned`, `In Progress`, `Blocked`, `Completed`, `Archived`.
5. Run `python scripts/update_progress.py` to regenerate [progress](docs/PROGRESS.md).
6. Run `python scripts/validate.py` before committing.

## Current progress

<!-- PROGRESS_START -->
812 projects tracked · 0 completed · 0 in progress
<!-- PROGRESS_END -->

## Source of truth

- `data/projects.csv`: project status, priority, GitHub link, dates and notes.
- `data/phases.csv`: phase labels and optional high-level status.
- `data/capstones.csv`: capstone descriptions (the corresponding IDs also appear in projects.csv).
- `docs/SOURCE-ROADMAP.txt`: untouched source text for preservation and comparison.
- `docs/ROADMAP.md` and `docs/PROGRESS.md`: generated views; **do not manually edit**.

## Using VS Code

Open this folder with **File → Open Folder**. Install Python and GitHub Pull Requests extensions if helpful. Use the integrated terminal for the Python scripts and Git commands. No third-party Python dependencies are required.

## Workflow

Track one project as a separate repository when it merits one, and link it in `repository_url`; small exercises can live together in a learning repo. This central repo holds planning and evidence, not every project's implementation.

## Safety

Keep credentials and private data out of Git. Offensive-security projects should be performed only in authorized environments.

## Certification roadmap & tracker

- [Complete 22-phase certification roadmap](docs/CERTIFICATIONS.md)
- [Certification progress dashboard](docs/CERTIFICATION-PROGRESS.md)
- `data/certifications.csv` — editable tracker (statuses, dates, fees, credential links, study resources, related projects).
- `data/certification_phases.csv` — phase goals.
- `docs/SOURCE-CERTIFICATIONS.md` — original uploaded certification list, preserved for reference.

<!-- CERT_PROGRESS_START -->
125 certifications tracked · 0 earned · 0 studying · 0 scheduled
<!-- CERT_PROGRESS_END -->

To update certification progress:

```powershell
python scripts/next_certification.py
python scripts/update_certifications.py
python scripts/validate_certifications.py
```

**Status choices:** `Not Started`, `Planned`, `Studying`, `Exam Scheduled`, `Passed - Pending Credential`, `Earned`, `On Hold`, `Expired`, `Retired`. Dates use `YYYY-MM-DD`; monetary amounts are numbers in your chosen currency (use USD consistently). Mark `Earned` only when the credential is actually awarded, not merely when the exam is passed.

> The certification list is reproduced from your supplied roadmap. Exam availability, names, prerequisites, credential expiry, and certification requirements may change. Verify details with each issuer before booking.
