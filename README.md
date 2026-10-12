# Signal Hanami

A simple pipeline for collecting candidate technology and business signals, passing them through an LLM-based filter, and writing the best items into an Obsidian-ready brief.

## Overview

This project is designed to scan a small set of public sources, rank them, and keep only items that have strong signal quality. The workflow is:

1. ingest source items
2. filter them through an LLM analyst
3. write the selected items into markdown notes for an Obsidian vault

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a `.env` file from `.env.example` and set the required environment variables.

## Required environment variables

```bash
GROQ_API_KEY=your_api_key_here
GITHUB_TOKEN=optional_token_for_rate_limit_reduction
```

## Usage

```bash
python main.py
```

## Project structure

```text
signal_hanami/
  alpha_filter.py
  ingestion.py
  obsidian_sink.py
  app.py
  main.py
```

## Limitations

- This is a local tool, not a production service.
- Output quality depends on source availability and the LLM model used.
- The filter is intentionally conservative; some low-signal items will be rejected.

## Contributing

Please keep changes focused, document new configuration options, and add tests when modifying the ingestion or filtering logic.
