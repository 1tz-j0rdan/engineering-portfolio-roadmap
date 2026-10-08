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
