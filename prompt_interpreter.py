import json

with open("sound_dictionary.json") as f:
    SOUND_DICT = json.load(f)

def interpret_prompt(prompt: str) -> dict:
    """Mock interpretation of a text prompt into synth parameters."""
    parameters = {}
    words = prompt.lower().split()

    for word in words:
        if word in SOUND_DICT:
            parameters.update(SOUND_DICT[word])

    return parameters

if __name__ == "__main__":
    import sys
    prompt = " ".join(sys.argv[1:]) or "shimmering ambient pad"
    print(json.dumps(interpret_prompt(prompt), indent=2))
