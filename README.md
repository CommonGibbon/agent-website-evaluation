# BluePill Web Eval

A framework for simulating and evaluating the realism of AI agents interacting with websites. This tool spawns persona-based agents to explore web applications, logs their interactions, and evaluates how "human-like" their behavior is.

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1.  **Install Dependencies:**
    ```bash
    poetry install
    ```

2.  **Install Playwright Browsers:**
    ```bash
    poetry run playwright install
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```bash
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

### 1. Run Simulation
Spawn AI agents to perform tasks on a target website.
*Edit `scripts/run_simulation.py` to configure the target URL and objective.*

```bash
poetry run python scripts/run_simulation.py
```
*Logs will be saved to `logs/YYYY-MM-DD_HH-MM-SS/`.*

### 2. Run Evaluation
Evaluate the realism of the recorded agent sessions.

```bash
poetry run python scripts/run_evaluation.py logs/<timestamp_directory>
```
*Results are exported to `report_data/realism_eval.csv`.*

### 3. Generate Reports
Convert simulation logs into readable Markdown reports.

```bash
poetry run python scripts/logs_to_markdown.py logs/<timestamp_directory>
```
*Markdown reports are saved to `report_data/`.*

## Project Structure

- `src/web_eval`: Core logic for agents, personas, and evaluation metrics.
- `scripts/`: Executable scripts for running simulations and evaluations.
- `logs/`: JSON logs of agent sessions.
- `report_data/`: Generated evaluation reports and CSVs.
- `notebooks/`: Jupyter notebooks for analysis.
