# Software Setup

## Development Computer

1. Install Python 3.10 or newer.
2. Open a terminal in the Inspresso folder.
3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the environment.
5. Install the package:

```bash
pip install -e .
```

6. Copy `config.example.json` to `config.json`.
7. Run a simulation:

```bash
python -m inspresso --simulate --mass 36 --time 30 --temperature 67
```

## Raspberry Pi

The same application structure can run on Raspberry Pi OS. After the final load-cell interface, display, and temperature sensor are selected, their Python libraries should be added to `requirements-hardware.txt` and the corresponding drivers should be implemented behind the interfaces in `sensors.py`.

Keeping the hardware layer separate from the analysis layer allows the classification and storage logic to be tested without needing the physical prototype connected.
