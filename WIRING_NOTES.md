# Wiring Notes

The final wiring diagram should be added after the exact load-cell interface, temperature sensor, and 3.5-inch display are selected.

## Planned Connections

```text
Load Cell
   |
   v
Amplifier / ADC
   |
   v
Raspberry Pi ---- 3.5-inch Display
   |
   +---- Optional Temperature Sensor
```

## Before Final Wiring

Document the following for each selected component:

- supply voltage
- ground connection
- Raspberry Pi interface type
- required GPIO pins
- communication protocol, if applicable
- required Python library
- calibration procedure

Do not assume pin assignments from a different sensor board or display model. Use the datasheet for the exact component purchased.
