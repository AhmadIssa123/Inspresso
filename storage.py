import csv
from pathlib import Path

from .models import ShotMeasurement, ShotResult


HEADER = [
    "recorded_at",
    "mass_g",
    "extraction_time_s",
    "temperature_c",
    "classification",
    "recommendation",
]


def save_shot(
    shot: ShotMeasurement,
    result: ShotResult,
    history_file: str | Path,
) -> None:
    """Append a shot and its analysis result to a CSV history file."""

    path = Path(history_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists()

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(HEADER)
        writer.writerow(
            [
                shot.recorded_at,
                f"{shot.mass_g:.2f}",
                f"{shot.extraction_time_s:.2f}",
                "" if shot.temperature_c is None else f"{shot.temperature_c:.2f}",
                result.classification,
                result.recommendation,
            ]
        )
