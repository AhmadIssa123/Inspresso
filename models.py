from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class ShotMeasurement:
    """Measured values for one espresso shot."""

    mass_g: float
    extraction_time_s: float
    temperature_c: float | None = None
    recorded_at: str = ""

    def __post_init__(self) -> None:
        if self.mass_g < 0:
            raise ValueError("mass_g cannot be negative")
        if self.extraction_time_s < 0:
            raise ValueError("extraction_time_s cannot be negative")
        if not self.recorded_at:
            object.__setattr__(
                self,
                "recorded_at",
                datetime.now(timezone.utc).isoformat(),
            )


@dataclass(frozen=True)
class ShotResult:
    """Analysis result for one espresso shot."""

    classification: str
    recommendation: str
