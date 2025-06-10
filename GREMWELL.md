# GREMWELL Implementation Roadmap

This document outlines the planned work for integrating a new **Gremwell** testing mode into `promptmap2`. The goal is to provide repeatable tests against a simple FastAPI application to evaluate prompt injection defenses.

## Proposed Command Line Options

The following options will be added to `promptmap2.py`:

| Option | Default | Purpose |
|-------|---------|---------|
| `--target-url` | `http://localhost:8000` | Base URL of the FastAPI demo to test. |
| `--gremwell-config` | `gremwell.yaml` | Path to additional configuration specific to the Gremwell mode. |
| `--gremwell` | off | Enable Gremwell testing mode. When active, prompts are sent to the FastAPI target instead of a local system prompt file. |

Existing parameters such as `--model`, `--model-type`, `--rules`, and `--iterations` will still apply.

## Files to Modify

- `promptmap2.py` – extend the argument parser to accept the new options and implement logic for issuing requests to the target URL when `--gremwell` is specified.
- `requirements.txt` – include `fastapi` and `uvicorn` for the demo server.
- `README.md` – document how to launch the FastAPI test server and how to use the new CLI arguments.
- `tests/` (new directory) – host automated tests for the Gremwell mode.
  - `tests/fastapi_app.py` – minimal FastAPI application that exposes a vulnerable `/chat` endpoint.
  - `tests/test_gremwell.py` – integration tests invoking the CLI against the local FastAPI server.

## Test Cases

1. **Prompt Stealing** – send crafted prompts through the FastAPI endpoint and verify the system prompt is leaked.
2. **Distraction** – ensure the LLM answers out-of-scope questions when distracted via the API.
3. **Firewall Mode** – confirm that when the endpoint acts as a firewall, responses include the expected pass condition.

The demo FastAPI application will intentionally echo received prompts to make testing straightforward. Tests will run the server using `uvicorn` in a background process and then call `promptmap2.py` with the new options.

