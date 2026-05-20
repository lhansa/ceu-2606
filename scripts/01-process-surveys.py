from __future__ import annotations

from pathlib import Path

import pandas as pd


def process_surveys(input_path: Path, output_dir: Path) -> tuple[Path, Path]:
    """Convert the first two sheets of an Excel workbook into daily CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    sheets = pd.read_excel(input_path, sheet_name=[0, 1])
    frames = list(sheets.values())

    def to_snake_case(col):
        import re
        col = col.strip().replace("\n", " ")
        col = re.sub(r"[\s\-\/]+", "_", col)
        col = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", col)
        col = re.sub(r"[^a-zA-Z0-9_]", "", col)
        return col.lower()

    # Convert columns to snake_case
    frames = [df.rename(columns=lambda c: to_snake_case(str(c))) for df in frames]

    daily_score_path = output_dir / "daily-score.csv"
    daily_volume_path = output_dir / "daily-volume.csv"

    frames[0].to_csv(daily_score_path, index=False)
    frames[1].to_csv(daily_volume_path, index=False)

    return daily_score_path, daily_volume_path


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    input_path = project_root / "data" / "raw" / "YouGov Combined Jan 2015 - Mar 2020.xlsx"
    output_dir = project_root / "data" / "processed"

    daily_score_path, daily_volume_path = process_surveys(input_path, output_dir)
    print(f"Created: {daily_score_path}")
    print(f"Created: {daily_volume_path}")


if __name__ == "__main__":
    main()
