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

All demo images or videos should be placed inside the docs/ folder.

Required demo files:
- docs/demo_main_menu.png : Main menu screen
- docs/demo_summarization.png : Summarization result
- docs/demo_qa.png : Question answering result
- docs/demo_pdf_analysis.gif (or .mp4) : PDF smart analysis demo

If video files are too large, screenshots may be used instead.

---

## Dependencies

This project uses the following libraries.  
All dependencies are installed via requirements.txt.

Required environment:
- Python 3.10 or higher

Core libraries:
- transformers
- torch
- numpy

Feature-related libraries:
- sentence-transformers (text embedding and similarity)
- scikit-learn (keyword extraction utilities)
- keybert (keyword extraction)
- pypdf (PDF text extraction)

---

## Installation

1. Clone the repository:
   git clone https://github.com/your-team-name/StudyTextLab.git
   cd StudyTextLab

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   macOS / Linux:
   source venv/bin/activate

   Windows (PowerShell):
   venv\Scripts\Activate

   Windows (CMD):
   venv\Scripts\activate.bat

4. Install dependencies:
   pip install -r requirements.txt

---

## How to Run

Run the program from the project root directory:
python -m src.main

Usage flow:
1. Start the program.
2. Input text manually or load a TXT/PDF file from the data/ folder.
3. Select an NLP task using the CLI menu.
4. Results are displayed in the terminal and saved as JSON files in the history/ folder.

---

## Project Structure

StudyTextLab is organized with a modular structure to support collaborative development
and clear separation of responsibilities.

```text
StudyTextLab/
 ├─ src/                       # Main source code
 │   ├─ main.py                # Program entry point
 │   ├─ ui.py                  # CLI user interface
 │   ├─ loaders.py             # Text and file loaders (TXT, PDF)
 │   ├─ history.py             # Result saving and loading logic
 │   └─ tasks/                 # NLP task modules
 │        ├─ __init__.py
 │        ├─ qa.py             # Question Answering
 │        ├─ summarization.py  # Text Summarization
 │        ├─ translation.py    # Translation (EN ↔ KO)
 │        ├─ sentiment.py      # Sentiment Analysis
 │        ├─ topic_classification.py  # Topic Classification
 │        ├─ keywords.py       # Keyword Extraction
 │        ├─ similarity.py     # Text Similarity
 │        ├─ grammar.py        # Grammar Correction
 │        └─ report_pdf_analysis.py   # PDF Smart Analysis
 ├─ data/                      # Sample input files (TXT, PDF)
 ├─ history/                   # Saved analysis results (JSON)
 ├─ docs/                      # Screenshots and demo media
 ├─ requirements.txt           # Python dependencies
 ├─ LICENSE                    # Project license
 └─ README.md                  # Project documentation
```

---

## Team Members & Contributions

- Member 1 (Leader): Main system, CLI UI, loaders, history, integration
- Member 2: Summarization and Translation
- Member 3: Question Answering and Sentiment Analysis
- Member 4: Topic Classification and Keyword Extraction
- Member 5: Similarity Check, Grammar Correction, PDF Smart Analysis

Each member implemented their features independently and integrated them through GitHub
pull requests.

---

## Collaboration Workflow

- Public GitHub repository
- Feature-based branch development
- Pull requests required before merging into main branch
- Commit history preserved for evaluation

---

## References

HuggingFace Transformers:
https://huggingface.co/docs/transformers

HuggingFace Model Hub:
https://huggingface.co/models

Sentence Transformers:
https://www.sbert.net/

pypdf Documentation:
https://pypdf.readthedocs.io/

---

## License

This project is released under the MIT License.
See the LICENSE file for details.
