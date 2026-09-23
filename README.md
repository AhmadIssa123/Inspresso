# ☕ Inspresso — Espresso Shot Analyzer

Inspresso is an embedded-system project that measures key espresso-shot variables and gives the user simple feedback about the extraction. The current design uses a **Raspberry Pi**, a **load cell** for mass measurement, optional **temperature sensing**, and a **3.5-inch display** for the user interface.

The goal is to record an espresso shot, analyze its measured values, classify the result, and recommend a simple grind adjustment such as **too coarse**, **too fine**, or **good**.

> **Project status:** Active development / prototype. Hardware drivers and classification thresholds must be calibrated against the final components and test data before the analyzer is treated as a finished measurement system.

## Features

- Measure espresso output mass using a load cell
- Track extraction time
- Support optional temperature measurement
- Analyze a completed shot using configurable thresholds
- Return a simple classification and adjustment recommendation
- Store shot history in CSV format
- Run in simulation mode while hardware is still being assembled
- Structured Python code for later Raspberry Pi integration

## System Overview

```text
Load Cell --------> Sensor Interface ----\
                                        \
Temperature Sensor -> Sensor Interface ---> Raspberry Pi ---> Decision Logic ---> 3.5" Display
                                        /
Timer ---------------------------------/
                                             |
                                             v
                                       Shot History
                                         CSV Data
```

## Repository Structure

```text
Inspresso/
├── README.md
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── requirements-hardware.txt
├── config.example.json
├── src/
│   └── inspresso/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       ├── config.py
│       ├── models.py
│       ├── sensors.py
│       ├── storage.py
│       └── app.py
├── tests/
│   └── test_analyzer.py
├── docs/
│   ├── SYSTEM_DESIGN.md
│   ├── SOFTWARE_SETUP.md
│   └── DEVELOPMENT_PLAN.md
├── hardware/
│   ├── COMPONENTS.md
│   └── WIRING_NOTES.md
├── data/
│   └── .gitkeep
└── images/
    └── .gitkeep
```

## How It Works

1. The user places a cup on the scale and tares the load cell.
2. Inspresso begins recording the shot.
3. The Raspberry Pi tracks mass and elapsed extraction time.
4. An optional temperature sensor records temperature.
5. When the shot ends, the software compares the measurements with configured target ranges.
6. The system returns feedback such as:
   - **Good** — measurements are within the configured target range.
   - **Too Coarse** — the shot appears to have extracted too quickly and/or produced too much output.
   - **Too Fine** — the shot appears to have extracted too slowly and/or produced too little output.
   - **Review Shot** — measurements give conflicting indications.
7. The result is saved to shot history for later review.

## Quick Start — Simulation Mode

This repository can run without Raspberry Pi hardware so the software can be developed first.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Inspresso.git
cd Inspresso
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux/Raspberry Pi:

```bash
source .venv/bin/activate
```

### 3. Install the project

```bash
pip install -e .
```

### 4. Create your local configuration

Copy `config.example.json` to `config.json` and edit the values as your testing improves.

### 5. Run a simulated shot

```bash
python -m inspresso --simulate --mass 36.2 --time 29.5 --temperature 67.0
```

Example output:

```text
Inspresso Shot Result
Mass: 36.2 g
Time: 29.5 s
Temperature: 67.0 C
Classification: GOOD
Recommendation: Shot is within the configured target range.
```

## Configuration

The initial values in `config.example.json` are **development defaults only**. They are intentionally configurable because the final target ranges should come from your project requirements and testing.

```json
{
  "target_mass_g": 36.0,
  "mass_tolerance_g": 4.0,
  "min_time_s": 25.0,
  "max_time_s": 35.0,
  "temperature_enabled": true,
  "history_file": "data/shot_history.csv"
}
```

## Hardware

Planned major components include:

- Raspberry Pi
- Load cell
- Load-cell amplifier / ADC interface
- Optional temperature sensor
- 3.5-inch display
- Power supply
- 3D-printed enclosure

See [`hardware/COMPONENTS.md`](hardware/COMPONENTS.md) and [`hardware/WIRING_NOTES.md`](hardware/WIRING_NOTES.md).

## Software

The prototype software is written in **Python** and separates the project into independent modules for:

- sensing
- configuration
- shot analysis
- data storage
- user interaction

This makes it easier to test the decision logic on a computer before connecting the final sensors to the Raspberry Pi.

## Future Development

- Connect and calibrate the final load-cell hardware
- Add the selected temperature sensor
- Create the touchscreen graphical interface
- Automatically detect the start and end of a shot
- Improve classification using collected shot data
- Add shot-history viewing on the display
- Add calibration tools
- Design and print the final enclosure

## Author

**Ahmad Issa**  
Electrical & Computer Engineering  
University of Memphis

## Academic Project Notice

This repository documents an engineering design project in active development. Values, hardware interfaces, and algorithms may change as the prototype is tested and validated.
