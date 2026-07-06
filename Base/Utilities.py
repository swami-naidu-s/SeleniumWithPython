import json

def get_config_data(key: str) -> str | dict | int:
    with open("config.json", "r") as f:
        data = json.load(f)
    return data[key]