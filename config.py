from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class InspressoConfig:
    target_mass_g: float = 36.0
    mass_tolerance_g: float = 4.0
    min_time_s: float = 25.0
    max_time_s: float = 35.0
    temperature_enabled: bool = True
    history_file: str = "data/shot_history.csv"

    @property
    def min_mass_g(self) -> float:
        return self.target_mass_g - self.mass_tolerance_g

    @property
    def max_mass_g(self) -> float:
        return self.target_mass_g + self.mass_tolerance_g


def load_config(path: str | Path = "config.json") -> InspressoConfig:
    """Load config.json, falling back to safe prototype defaults."""

    config_path = Path(path)
    if not config_path.exists():
        return InspressoConfig()

    with config_path.open("r", encoding="utf-8") as file:
        raw = json.load(file)

    return InspressoConfig(**raw)
