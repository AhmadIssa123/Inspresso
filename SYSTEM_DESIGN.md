# Inspresso System Design

## Purpose

Inspresso is intended to help a user evaluate an espresso shot using measurable extraction variables rather than relying only on visual judgment. The prototype records shot mass and extraction time, can optionally record temperature, and produces a simple classification and adjustment recommendation.

## Functional Blocks

### 1. Sensing

The sensing subsystem obtains the physical measurements used by the analyzer.

- **Load cell:** measures espresso output mass.
- **Timer:** measures extraction duration in software.
- **Temperature sensor:** optional measurement for additional shot information.

### 2. Signal Interface / Conditioning

A load cell produces a small electrical signal and therefore requires an appropriate amplifier and analog-to-digital interface before the Raspberry Pi can use the measurement. The exact device is intentionally not specified in the software repository until the final hardware is selected.

### 3. Processing

The Raspberry Pi runs the Python application, receives measurements, stores shot records, and passes completed shot data to the decision logic.

### 4. Decision Logic

The first software prototype uses transparent threshold-based rules. The thresholds are stored in a configuration file so they can be changed as testing data is collected.

The final design should use experimentally justified thresholds rather than relying permanently on the example development values included in the repository.

### 5. User Interface

The planned user interface is a 3.5-inch display. It should eventually provide controls and screens for:

- tare
- start / stop shot
- live mass
- elapsed time
- optional temperature
- final classification
- recommended adjustment
- shot history

### 6. Data Storage

Each completed shot can be stored locally in CSV format with:

- date/time
- mass
- extraction time
- temperature
- classification
- recommendation

A CSV file is used initially because it is easy to inspect, export, and analyze. A database can be added later if the shot-history feature becomes more advanced.

## Data Flow

```text
Physical Shot
     |
     v
Sensors -> Raspberry Pi -> Measurement Object -> Analyzer -> Result
                                      |             |
                                      |             v
                                      +--------> CSV History
                                                    |
                                                    v
                                              User Interface
```

## Prototype vs. Final Design

The repository currently contains the software architecture and simulation path. Final GPIO connections, calibration constants, display drivers, temperature-sensor drivers, and enclosure dimensions depend on the components selected during hardware development.
