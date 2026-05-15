from pathlib import Path
import csv

log_dir = "."
log_files = [
    "concepts",
    "instances",
    "subclasses",
    "used_instances",
    "used_subclasses",
    "properties",
    "software_languages",
    "programming_languages"
    ]

with open("summary.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["Metric", "Count"])

    for stem in log_files:
        path = Path(log_dir + "/" + stem + ".log")

        with path.open("r", encoding="utf-8", errors="replace") as f:
            line_count = sum(1 for _ in f)

        writer.writerow([stem, line_count])
