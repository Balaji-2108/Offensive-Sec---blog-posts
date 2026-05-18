# Introduction

This document, demontrate how to buiild a basic vulnerable AI application to test prompt injection vulnerability

Using Python Flask, this application simulates a vulnerable AI chatbot to demonstrate prompt injection and data leakage risks.

The chatbot receives user input via a /chat endpoint and forwards it to a local LLM running on Ollama (port 11434).

A system prompt is defined that it is a secure assitance and can reveal internal data only if the admin request, which includes sensitive data such as admin passwords and API keys.
[](/writeups/Screenshots/VulnAI/systemprompt.jpg)

The application injects additional simulated internal data (simulating a RAG setup) like certain keywords like vpn or internal.
[](/writeups/Screenshots/VulnAI/Rag.jpg)

The chatbot processes the request and returns a response to the user.
[](/writeups/Screenshots/VulnAI/visualrep.png)

The design intentionally includes weaknesses such as:
Sensitive data embedded in system prompts
Improper context injection
No output filtering
These flaws make the application vulnerable to prompt injection attacks.

Full demonstration can be found in this blog post - 🔗[AI-pentesting-building-and-exploiting](https://open.substack.com/pub/balaji217/p/ai-pentesting-building-and-exploiting?r=89tm7m&utm_campaign=post&utm_medium=web)
