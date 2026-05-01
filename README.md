# Research AI Assistant

Most basic AI tools only perform single-step processing (search and then summarize).
I have build a system that behaves more like an AI agent, capable of:
1. refining queries
2. iteratively gathering information
3. handling incomplete or noisy data
4. managing token limits in real-world API usage
This project is  more of a realistic approach to AI system design.

## Overview
This is a CLI-based AI Research Assistant that performs intelligent web research using APIs and LLMs.
It takes a user query, refines it, searches the web, and generates structured insights including summary, key points, and sources.

## Features/what it does?
* Query refinement using LLM
* Multi-step reasoning (agent-like workflow)
* Web search integration (Tavily API)
* AI summarization (Groq LLM)
* Context trimming to handle token limits
* Retry mechanism for robustness
* Clean structured output
* 
## Tech Stack
* Python
* Tavily API (Search)
* Groq API (LLM)
* JSON processing

## How it works/workflow
1. User enters query
2. System refines query using LLM
3. Performs web search
4. Collects and trims results
5. Uses multi-step reasoning loop
6. Generates structured response

## How to Run
pip install -r requirements.txt
python main.py

## Example Output
SUMMARY:
AI in healthcare improves diagnosis, drug discovery, and patient care.
KEY POINTS:
* Improves diagnostic accuracy
* Enhances drug discovery
* Automates repetitive tasks
SOURCES:
* https://example.com

## Challenges & Solutions

1. LLM Output Inconsistency
LLMs sometimes return non-JSON responses even when instructed.
**Solution:**
* Strict prompt engineering
* JSON cleaning and parsing logic
  
2. Token Limit Errors
Large context caused API failures due to token limits.
**Solution:**
* Implemented context trimming
* Limited number of results and content size

3. API Reliability
Occasional failures or malformed responses.
**Solution:**
* Added retry mechanism for robustness
## outcomes
* Handling LLM output inconsistencies
* Managing token limits
* Building agent-like systems without frameworks
* Designing robust API-based workflows
