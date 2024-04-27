import configparser
import json

def read_config_file(file_path):
    try:
        config = configparser.ConfigParser()
        config.read(file_path)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return None

def extract_config_data(config):
    data = {}
    for section in config.sections():
        data[section] = dict(config[section])
    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Saved configuration data to {output_file}")

if __name__ == "__main__":
    config_file_path = "sample_config.ini"
    output_json_file = "config_data.json"

    config = read_config_file(config_file_path)
    if config:
        config_data = extract_config_data(config)
        save_to_json(config_data, output_json_file)
