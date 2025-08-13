import json
import time
import pandas as pd
from datetime import datetime
from pymodbus.client import ModbusTcpClient
import os

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def connect_meter(ip, port):
    return ModbusTcpClient(ip, port=port)

def read_meter_data(client, unit_id):
    # Example: read voltage register (assuming 40001)
    # Replace with Shark meter register addresses
    result = client.read_holding_registers(0, 10, unit=unit_id)
    if result.isError():
        return None
    return result.registers

def save_log(meter_name, data, folder):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([{"timestamp": timestamp, "data": data}])
    file_path = os.path.join(folder, f"{meter_name}_log.csv")
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

def main():
    config = load_config()
    while True:
        for meter in config["meters"]:
            client = connect_meter(meter["ip"], meter["port"])
            if client.connect():
                data = read_meter_data(client, meter["unit_id"])
                if data:
                    save_log(meter["name"], data, config["output_folder"])
                    print(f"Logged data for {meter['name']}: {data}")
                else:
                    print(f"Failed to read data from {meter['name']}")
                client.close()
            else:
                print(f"Cannot connect to {meter['name']}")
        time.sleep(config["log_interval_seconds"])

if __name__ == "__main__":
    main()
