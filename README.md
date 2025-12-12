# StudyTextLab

StudyTextLab is a HuggingFace-based AI text analysis tool designed for students.
It provides multiple NLP functionalities such as summarization, question answering,
translation, sentiment analysis, and document analysis through a simple CLI interface.

---

## Project Overview

StudyTextLab was created to help students efficiently understand and analyze lecture notes,
assignments, and academic documents. Instead of using separate tools for different NLP tasks,
this project integrates multiple open-source NLP models from HuggingFace into a single,
unified text analysis laboratory.

The project focuses on:
- Practical use of open-source NLP libraries
- Modular design for collaborative development
- Clear command-line interaction for real users (students)

---

## Features

- Question Answering (QA)
- Text Summarization
- Translation (English ↔ Korean)
- Sentiment Analysis
- Topic Classification
- Keyword Extraction
- Text Similarity / Plagiarism Check
- Grammar Correction
- PDF Smart Analysis (Summary + Topic + Keywords)

---

## Demo / Screenshots

> Put demo images/videos inside the `docs/` folder and reference them here.

### Main Menu (CLI Interface)
> 📌 Insert a screenshot of the main menu here
- File: `docs/demo_main_menu.png`

Example (uncomment after adding the file):
<!-- ![Main Menu](docs/demo_main_menu.png) -->

---

### Summarization Example
> 📌 Insert a screenshot showing summarization results here
- File: `docs/demo_summarization.png`

Example (uncomment after adding the file):
<!-- ![Summarization](docs/demo_summarization.png) -->

---

### Question Answering Example
> 📌 Insert a screenshot showing QA results here
- File: `docs/demo_qa.png`

Example (uncomment after adding the file):
<!-- ![Q&A](docs/demo_qa.png) -->

---

### PDF Smart Analysis Example
> 📌 Insert a screenshot or short demo video (GIF/MP4) here
- File: `docs/demo_pdf_analysis.gif` (recommended)  
  or `docs/demo_pdf_analysis.mp4` (if allowed)

Example (uncomment after adding the file):
<!-- ![PDF Analysis](docs/demo_pdf_analysis.gif) -->

> Note: If demo files are too large, screenshots may be used instead of videos.

---

## Dependencies

- Python 3.10 or higher
- transformers
- torch
- sentence-transformers
- scikit-learn
- pypdf

All required packages are listed in `requirements.txt`.

---

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/your-team-name/StudyTextLab.git
cd StudyTextLab

# Create venv
python -m venv venv

# Activate venv
# macOS/Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate
# Windows (CMD):
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
