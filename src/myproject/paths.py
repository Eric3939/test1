from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data"
RESULTS = ROOT / "results"
RUNS = ROOT / "runs"
SCRATCH = ROOT / "scratch"
SCRIPTS = ROOT / "scripts"


RAW_DATA = DATA / "raw"
PROCESSED_DATA = DATA / "processed"
FIGURES_RESULTS = RESULTS / "figures"
TABLES_RESULTS = RESULTS / "tables"

# ensure directories exist
for path in [
    DATA, RESULTS, RUNS, SCRATCH, SCRIPTS,
    RAW_DATA, PROCESSED_DATA, FIGURES_RESULTS, TABLES_RESULTS
]:
    path.mkdir(parents=True, exist_ok=True)
