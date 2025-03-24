# CV Analysis Agent with ReAct

An intelligent agent that combines CV analysis capabilities with mathematical operations using the ReAct Reasoning and Acting strategy.

## Overview

This project implements a ReAct agent that can:
- Search and analyze CV content using Retrieval-Augmented Generation
- Perform mathematical calculations
- Combine both capabilities to answer complex queries about professional experience

## Architecture

The system consists of three main components:

1. **Main Client** (`client.py`)
   - Orchestrates the interaction between components
   - Creates and manages the ReAct agent
   - Handles user queries and displays responses

2. **RAG Service** (`doc_rag.py`)
   - Manages CV document processing
   - Provides semantic search capabilities
   - Uses OpenAI embeddings for document retrieval

3. **Math Service** (`math_server.py`)
   - Provides basic mathematical operations
   - Supports addition and multiplication

## Prerequisites

- Python 3.8+
- OpenAI API key
- Required Python packages (install via `make install` at the root of the project):
  - langchain
  - langgraph
  - python-dotenv
  - openai
  - pypdf

## Setup

1. **Environment Variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. **CV Document**
   - Create a `private` directory in the project root
   - Place your CV in PDF format inside the `private` directory
   - Name the file `cv.pdf`
   ```bash
   mkdir private
   cp your_cv.pdf private/cv.pdf
   ```

## Usage

1. Start service:
   ```bash
   python langchain-mcp-adapter-with-rag/client.py
   ```

## Example Queries

The agent can handle complex queries that combine CV analysis and calculations, such as:

```text
Based on my CV:
1. Find all periods where I worked with JavaScript
2. Calculate the total JavaScript experience
3. Calculate equivalent experience for parallel projects
```

## How It Works

1. The ReAct agent processes the query and determines which tools to use
2. For CV-related information, it uses the `search_cv` tool to retrieve relevant content
3. For calculations, it uses the math tools (`add` and `multiply`)
4. The agent follows a reasoning process to combine these tools effectively

## Limitations

- CV must be named exactly as `cv.pdf`
- Requires manual startup of services
- No error handling or fallbacks
