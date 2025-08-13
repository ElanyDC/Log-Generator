# Shark Meter Log Generator

A Python-based tool to generate and store logs from Shark energy meters using Modbus/TCP.

## Features
- Connects to multiple Shark meters via Modbus/TCP
- Reads register data periodically
- Stores logs in CSV format
- Configurable via `config.json`

## Requirements
- Python 3.8+
- `pymodbus`
- `pandas`

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/shark-meter-log-generator.git
cd shark-meter-log-generator
pip install -r requirements.txt
```

## Usage
1. Edit `config.json` to match your meter IP, port, and unit IDs.
2. Run:
```bash
python log_generator.py
```
3. Logs will be stored in the `sample_logs/` folder.

## Notes
- Default registers in this script are for demonstration. Replace with actual Shark meter register addresses.
- Make sure your meters are accessible from your network.

## License
MIT License
