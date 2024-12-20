# Installation
Create a new virtual environment
```bash
uv venv
```

Activate the virtual environment
- On Windows:
```bash
.venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source .venv/bin/activate
```
Install the package in development mode
```bash
uv pip install -e .
```

Install development dependencies
```bash
uv pip install -e ".[dev]"

```
# Run
In order to run the code 
```bash
uv run main.py
```