# Development Plan

## Phase 1 — Software Prototype

- Create shot data model
- Create configurable analysis rules
- Save shot history to CSV
- Validate behavior with simulated values
- Add unit tests

## Phase 2 — Load Cell Integration

- Select final load-cell amplifier / ADC interface
- Wire the load cell to the interface and Raspberry Pi
- Create a hardware driver
- Add tare support
- Calibrate using known masses
- Compare measured values with reference weights

## Phase 3 — Shot Timing

- Detect or manually trigger the start of extraction
- Track elapsed time with Python
- Determine a reliable end-of-shot method
- Validate timing against an external reference

## Phase 4 — Temperature

- Select and integrate the temperature sensor
- Record temperature with each shot
- Determine whether temperature should affect classification or remain informational

## Phase 5 — Touchscreen UI

- Build a simple 3.5-inch-display interface
- Add tare, start, stop, and history controls
- Show live mass and time
- Display the final recommendation clearly

## Phase 6 — Calibration and Decision Logic

- Collect repeated shot data
- Compare measurements with known grind adjustments
- Refine the configured thresholds
- Document accuracy and limitations

## Phase 7 — Enclosure

- Measure all final components
- Design the enclosure in CAD
- Include a stable load-cell mounting area
- Include a display opening and internal mounting points
- 3D print and revise the enclosure

## Phase 8 — Final Validation

- Test repeated measurements
- Check load-cell accuracy and repeatability
- Verify software classifications against test cases
- Verify data is saved correctly
- Document known limitations and future improvements
