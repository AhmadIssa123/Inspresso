from .config import InspressoConfig
from .models import ShotMeasurement, ShotResult


GOOD = "GOOD"
TOO_COARSE = "TOO COARSE"
TOO_FINE = "TOO FINE"
REVIEW = "REVIEW SHOT"


def analyze_shot(shot: ShotMeasurement, config: InspressoConfig) -> ShotResult:
    """Analyze a shot using simple, configurable prototype rules.

    These rules are deliberately transparent so they can be replaced or tuned
    after real testing data is collected.
    """

    mass_ok = config.min_mass_g <= shot.mass_g <= config.max_mass_g
    time_ok = config.min_time_s <= shot.extraction_time_s <= config.max_time_s

    if mass_ok and time_ok:
        return ShotResult(
            GOOD,
            "Shot is within the configured target range.",
        )

    fast = shot.extraction_time_s < config.min_time_s
    slow = shot.extraction_time_s > config.max_time_s
    high_mass = shot.mass_g > config.max_mass_g
    low_mass = shot.mass_g < config.min_mass_g

    if (fast and not low_mass) or (high_mass and not slow):
        return ShotResult(
            TOO_COARSE,
            "The shot appears fast/high-yield. Try a slightly finer grind and test again.",
        )

    if (slow and not high_mass) or (low_mass and not fast):
        return ShotResult(
            TOO_FINE,
            "The shot appears slow/low-yield. Try a slightly coarser grind and test again.",
        )

    return ShotResult(
        REVIEW,
        "The measurements give mixed indications. Review the shot and repeat the test.",
    )
