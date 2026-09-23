from abc import ABC, abstractmethod


class MassSensor(ABC):
    """Interface for the final load-cell implementation."""

    @abstractmethod
    def tare(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_mass_g(self) -> float:
        raise NotImplementedError


class TemperatureSensor(ABC):
    """Interface for the optional temperature sensor."""

    @abstractmethod
    def read_temperature_c(self) -> float:
        raise NotImplementedError


class SimulatedMassSensor(MassSensor):
    def __init__(self, mass_g: float = 0.0) -> None:
        self.mass_g = mass_g

    def tare(self) -> None:
        pass

    def read_mass_g(self) -> float:
        return self.mass_g


class SimulatedTemperatureSensor(TemperatureSensor):
    def __init__(self, temperature_c: float = 0.0) -> None:
        self.temperature_c = temperature_c

    def read_temperature_c(self) -> float:
        return self.temperature_c


# TODO: Add the Raspberry Pi load-cell driver after the final ADC/amplifier is
# selected and calibrated. Keep GPIO-specific imports inside that driver so
# simulation mode continues to work on non-Raspberry Pi computers.
