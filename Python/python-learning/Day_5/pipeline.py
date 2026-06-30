import json
import csv
import os

def load_and_validate_config(config_path):
    """
    A realistic AI pipeline function combining everything from today:
    - file I/O (reading JSON)
    - error handling (missing file, bad format)
    - clean structure (could be its own module: config_loader.py)
    """
    try:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(config_path, "r") as f:
            config = json.load(f)
        
        # Validate required keys exist
        required_keys = ["model_name", "learning_rate", "epochs"]
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required config key: '{key}'")
        
        print(f"Config loaded successfully: {config['model_name']}")
        return config

    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        return None
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format in {config_path}")
        return None
    except KeyError as e:
        print(f"[ERROR] {e}")
        return None
    finally:
        print("[LOG] Config loading attempt finished\n")


# Test it
sample_config = {
    "model_name": "PlacementPredictor", 
    "learning_rate": 0.01,
    "epochs": 100
}
with open("test_config.json", "w") as f:
    json.dump(sample_config, f)

result = load_and_validate_config("test_config.json")
result2 = load_and_validate_config("missing_file.json")