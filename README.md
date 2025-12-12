# StudyTextLab

StudyTextLab is a HuggingFace-based AI text analysis tool designed for students.
It provides multiple NLP functionalities such as summarization, question answering,
translation, sentiment analysis, and document analysis through a simple CLI interface.

## Project Overview

StudyTextLab was created to help students efficiently understand and analyze lecture notes,
assignments, and academic documents. Instead of using separate tools for different NLP tasks,
this project integrates multiple open-source NLP models from HuggingFace into a single,
unified text analysis laboratory.

The project focuses on:
- Practical use of open-source NLP libraries
- Modular design for collaborative development
- Clear command-line interaction for real users (students)

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

## Demo / Screenshots

All demo images or videos should be placed inside the docs/ folder.

Required demo files:
- docs/demo_main_menu.png
- docs/demo_summarization.png
- docs/demo_qa.png
- docs/demo_pdf_analysis.gif (or .mp4)

If video files are too large, screenshots may be used instead.

## Dependencies

Required environment:
- Python 3.10 or higher (Python 3.11 recommended)

Libraries:
- transformers
- torch
- numpy
- sentence-transformers
- scikit-learn
- keybert
- pypdf
- sentencepiece
- protobuf

All dependencies are installed via requirements.txt.

## Installation

git clone https://github.com/your-team-name/StudyTextLab.git  
cd StudyTextLab  
python -m venv .venv  

Windows (PowerShell):  
.venv\Scripts\Activate  

macOS / Linux:  
source .venv/bin/activate  

pip install --upgrade pip setuptools wheel  
pip install -r requirements.txt  

## Windows HuggingFace Cache Path

$env:HF_HOME="F:\hf_cache"  
$env:TRANSFORMERS_CACHE="F:\hf_cache\transformers"  

## How to Run

python main.py

## Usage Flow

1. Start the program.
2. Input text manually or load a TXT/PDF file from the data/ folder.
3. Select an NLP task using the CLI menu.
4. Results are displayed in the terminal and saved as JSON files in the history/ folder.

## Project Structure

```text
StudyTextLab/  
 ├─ tasks/  
 │   ├─ __init__.py  
 │   ├─ qa.py  
 │   ├─ summarization.py  
 │   ├─ translation.py  
 │   ├─ sentiment.py  
 │   ├─ topic_classification.py  
 │   ├─ keywords.py  
 │   ├─ similarity.py  
 │   ├─ grammar.py  
 │   └─ report_pdf_analysis.py  
 ├─ data/  
 ├─ history/  
 ├─ docs/  
 ├─ main.py  
 ├─ ui.py  
 ├─ loaders.py  
 ├─ history.py  
 ├─ requirements.txt  
 ├─ LICENSE  
 └─ README.md  
```

## Team Members & Contributions

- Member 1 (Leader): Main system, CLI UI, loaders, history, integration
- Member 2: Summarization and Translation
- Member 3: Question Answering and Sentiment Analysis
- Member 4: Topic Classification and Keyword Extraction
- Member 5: Similarity Check, Grammar Correction, PDF Smart Analysis

## Collaboration Workflow

- Public GitHub repository
- Feature-based branch development
- Pull requests required before merging into main branch
- Commit history preserved for evaluation

## References

HuggingFace Transformers: https://huggingface.co/docs/transformers  
HuggingFace Model Hub: https://huggingface.co/models  
Sentence Transformers: https://www.sbert.net/  
pypdf Documentation: https://pypdf.readthedocs.io/  

## License

This project is released under the MIT License.
See the LICENSE file for details.
