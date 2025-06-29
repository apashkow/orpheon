import sys
from prompt_interpreter import interpret_prompt
from patch_generator import generate_patch

def main():
    prompt = " ".join(sys.argv[1:]) or "shimmering ambient pad with metallic tail"
    print(f"\n🎙 Interpreting prompt: \"{prompt}\"")
    parameters = interpret_prompt(prompt)
    patch = generate_patch(parameters, name=prompt.replace(" ", "_"))
    print("\n✅ Patch generated and saved:")
    print(patch)

if __name__ == "__main__":
    main()
