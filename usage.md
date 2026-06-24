# Usage Guide

This CLI lets you run **Qwen 3.5 4B** locally with [Ollama](https://ollama.ai) to analyze files.  
It supports two modes:

- **fix-code** → Correct buggy Python code files.
- **finish-project** → Generate project scaffolding or complete requirements from documentation.

---

## Prerequisites

1. Install [Ollama](https://ollama.ai).
2. Pull the model locally:
   ```bash
   ollama pull qwen3.5:4b
   ```
