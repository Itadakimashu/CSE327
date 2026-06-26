import argparse
from ollama import chat

finish_project_prompt = """
You are a software engineer. You will be given a project description and requirements. Your task is to implement the project according to the specifications provided. Please ensure that your implementation is complete, functional, and adheres to best coding practices. If there are any ambiguities in the requirements, make reasonable assumptions and document them in your code comments.
please provide the complete code implementation, including any necessary files, classes, functions, and documentation. If the project requires multiple files, please structure your response accordingly and indicate the file names clearly. Your goal is to deliver a fully functional project that meets the specified requirements.
just provide the code implementation without any additional explanations or commentary. Ensure that the code is well-organized, properly formatted, and ready to be executed or compiled as needed.
"""

def run_model(file_path, model="gemma4:e4b", mode="fix-code"):
    # Read file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build prompt depending on mode
    if mode == "fix-code":
        prompt = f"Fix the following buggy code:\n\n{content}\n\nReturn corrected code."
    elif mode == "finish-project":
        prompt = f"Here are project requirements:\n\n{content}\n\n{finish_project_prompt}"
    else:
        prompt = f"Analyze the following file:\n\n{content}"

    # Call Ollama
    print(f"Sending prompt to model '{model}'...")
    response = chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in response:
        with open("output/response.txt", "a", encoding="utf-8") as f:
            f.write(chunk.message.content)
        print(chunk.message.content, end="", flush=True)



def main():
    parser = argparse.ArgumentParser(description="Local AI CLI with Ollama + Qwen")
    parser.add_argument("file", help="Path to the input file")
    parser.add_argument("--mode", choices=["fix-code", "finish-project"], default="fix-code",
                        help="Choose task mode: fix-code or finish-project")
    args = parser.parse_args()

    run_model(args.file, mode=args.mode)

if __name__ == "__main__":
    main()
