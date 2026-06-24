import argparse
from ollama import chat

def run_model(file_path, model="qwen3.5:4b", mode="fix-code"):
    # Read file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build prompt depending on mode
    if mode == "fix-code":
        prompt = f"Fix the following buggy code:\n\n{content}\n\nReturn corrected code."
    elif mode == "finish-project":
        prompt = f"Here are project requirements:\n\n{content}\n\nFinish the project implementation."
    else:
        prompt = f"Analyze the following file:\n\n{content}"

    # Call Ollama
    response = chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.message.content

def main():
    parser = argparse.ArgumentParser(description="Local AI CLI with Ollama + Qwen")
    parser.add_argument("file", help="Path to the input file")
    parser.add_argument("--mode", choices=["fix-code", "finish-project"], default="fix-code",
                        help="Choose task mode: fix-code or finish-project")
    args = parser.parse_args()

    output = run_model(args.file, mode=args.mode)
    print("\n=== AI Output ===\n")
    print(output)

if __name__ == "__main__":
    main()
