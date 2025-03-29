# AI Research & Development Project

This repository contains experimental work focused on exploring and implementing various AI concepts through research
and development initiatives.

## Overview

This project serves as a dynamic sandbox for testing and implementing innovative AI-related concepts, with a focus on:

- Seamless integration of AI agents and tools
- Prototyping experimental AI architectures
- Advancing machine learning models and frameworks

## Project Structure

The project includes:

- `server`: A FastAPI-based server for interacting with an agent and performing various analysis operations on resumes.
- `langchain-mcp-adapter`: A module to integrating LangChain and MCP to enable advanced AI experiments and workflows.
- `langchain-mcp-adapter-with-rag`: A module to integrating LangChain and MCP to enable advanced AI experiments and workflows with Retrieval-Augmented Generation.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mathieuka/AI-research-and-development-py.git
   ```
2. **Install dependencies**:
   ```bash
   make install
   ```

## Requirements

- **Python:** Version 3.13.1
- **direnv:** Install via `brew install direnv` for managing environment variables effectively.


## Environment Variables

Create a `.env` file in the root directory and define the following:

- `OPENAI_API_KEY`: Your OpenAI API key for enabling GPT-based features.