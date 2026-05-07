# TenderAI — AI-Powered Intelligent Tender Evaluation System

TenderAI is an explainable AI-based prototype designed for automated government tender evaluation and eligibility analysis.

The system assists procurement teams by extracting information from tender and bidder documents, evaluating eligibility criteria, generating confidence-based assessments, and maintaining transparent audit trails.

Developed for the **AI for Bharat Hackathon** under the theme:

> AI-Based Tender Evaluation and Eligibility Analysis for Government Procurement by CRPF

---

# Features

- OCR-based document text extraction
- NLP preprocessing using SpaCy
- AI-powered eligibility evaluation
- Confidence scoring and explainability
- Human-in-the-loop review workflow
- Audit trail and evaluation logs
- Government-ready dashboard interface
- Self-hosted LLM support using Ollama

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## AI Components
- Tesseract OCR
- SpaCy NLP
- Llama 3 / Mistral (self-hosted via Ollama)

## Database
- MongoDB

---

# Project Workflow

1. Upload tender and bidder documents
2. OCR extracts machine-readable text
3. NLP identifies eligibility clauses and entities
4. AI engine evaluates bidder compliance
5. Confidence scoring determines:
   - Eligible
   - Ineligible
   - Needs Manual Review
6. Results are displayed with evidence references and audit logs

---

# Prototype Modules

- Upload & Evaluation Dashboard
- AI Pipeline Visualization
- Results Dashboard
- Audit Trail System
- Tender Criteria Viewer

---

# Running the Project

## Frontend

Open:

```bash
hackathon.html
