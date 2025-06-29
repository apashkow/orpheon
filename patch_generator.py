import json
import os

EXPORT_PATH = "export"

def generate_patch(parameters: dict, name="generated_patch") -> dict:
    """Stub that returns a .vital patch-style dictionary."""
    patch = {
        "osc1": parameters.get("osc1", "sine"),
        "filter": parameters.get("filter", "lowpass"),
        "env1": parameters.get("env1", {"attack": 0.1, "decay": 0.5}),
        "name": name
    }

    os.makedirs(EXPORT_PATH, exist_ok=True)
    with open(f"{EXPORT_PATH}/{name}.vital.json", "w") as f:
        json.dump(patch, f, indent=2)

    return patch

if __name__ == "__main__":
    # Demo with mocked parameters
    sample = {
        "osc1": "saw",
        "filter": "bandpass",
        "env1": {"attack": 0.4, "decay": 1.2}
    }
    print(json.dumps(generate_patch(sample, "shimmering_pad"), indent=2))
