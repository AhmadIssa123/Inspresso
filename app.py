from .analyzer import analyze_shot
from .config import InspressoConfig
from .models import ShotMeasurement, ShotResult
from .storage import save_shot


def process_shot(
    mass_g: float,
    extraction_time_s: float,
    temperature_c: float | None,
    config: InspressoConfig,
    save_history: bool = True,
) -> tuple[ShotMeasurement, ShotResult]:
    """Create, analyze, and optionally save one espresso-shot measurement."""

    shot = ShotMeasurement(
        mass_g=mass_g,
        extraction_time_s=extraction_time_s,
        temperature_c=temperature_c,
    )
    result = analyze_shot(shot, config)

    if save_history:
        save_shot(shot, result, config.history_file)

    return shot, result
