# StudyTextLab - Main Entry

from ui import (
    print_header,
    print_main_menu,
    print_current_text_preview,
    prompt_command,
    prompt_question,
    print_error,
    print_info,
    print_result_block,
    print_history_list,
)
from loaders import (
    load_text_from_user,
    load_text_from_txt_file,
    select_txt_file_interactive,
    select_pdf_file_interactive,
)
from history import (
    save_history,
    list_history_files,
    load_history_file,
)

# ---- 팀원들이 구현한 Task 모듈 ----
from tasks import qa
from tasks import summarization
from tasks import translation
from tasks import sentiment
from tasks import topic_classification
from tasks import keywords
from tasks import similarity
from tasks import grammar
from tasks import report_pdf_analysis


def pause():
    input("\n(스크린샷 촬영 후 Enter를 누르면 메뉴로 돌아갑니다...) ")


def init_pipelines():
    """
    프로그램 시작 시 한 번만 호출해서
    각 Task 모듈의 모델/파이프라인을 미리 로드.
    """
    print_info("Loading NLP pipelines... (this may take a while on first run)")

    pipelines = {}
    pipelines["qa"] = qa.load_qa_pipeline()
    pipelines["summarizer"] = summarization.load_summarizer()
    pipelines["translator"] = translation.load_translator()
    pipelines["sentiment"] = sentiment.load_sentiment_model()
    pipelines["topic_classifier"] = topic_classification.load_topic_classifier()
    pipelines["embedder"] = similarity.load_embedder()
    pipelines["grammar_model"] = grammar.load_grammar_model()

    print_info("All pipelines loaded successfully.\n")
    pause()
    return pipelines


def main():
    pipelines = init_pipelines()

    current_text: str = ""
    second_text: str = ""

    while True:
        print_header("StudyTextLab - AI Text Lab for Students")
        print_current_text_preview(current_text)
        print_main_menu()

        cmd = prompt_command()

        # ==========================
        # 텍스트 관련 메뉴
        # ==========================
        if cmd == "q":
            print_info("프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            pause()
            break

        elif cmd == "t":
            current_text = load_text_from_user()
            print_info("현재 텍스트가 업데이트되었습니다.")
            pause()

        elif cmd == "f":
            path = select_txt_file_interactive()
            if path is None:
                print_error("선택된 파일이 없습니다.")
                pause()
                continue
            current_text = load_text_from_txt_file(path)
            print_info(f"텍스트 파일을 로드했습니다: {path.name}")
            pause()

        elif cmd == "c":
            current_text = ""
            print_info("현재 텍스트를 초기화했습니다.")
            pause()

        # ==========================
        # 히스토리 관련 메뉴
        # ==========================
        elif cmd == "h":
            history_files = list_history_files()
            if not history_files:
                print_error("저장된 히스토리가 없습니다.")
                pause()
                continue
            print_history_list(history_files)
            choice = input("열어볼 히스토리 번호를 입력하세요 (엔터: 취소): ").strip()
            if not choice:
                continue
            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(history_files):
                    raise ValueError
            except ValueError:
                print_error("잘못된 번호입니다.")
                pause()
                continue

            data = load_history_file(history_files[idx])
            print_result_block("History Detail", data)
            pause()

        # ==========================
        # Q&A
        # ==========================
        elif cmd == "1":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요. (T 또는 F)")
                pause()
                continue
            question = prompt_question()
            result = qa.run_qa(pipelines["qa"], current_text, question)
            print_result_block("Q&A Result", result)
            save_history("qa", {"context": current_text, "question": question}, result)
            pause()

        # ==========================
        # Summarization
        # ==========================
        elif cmd == "2":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            summary = summarization.run_summarization(
                pipelines["summarizer"],
                current_text,
                max_len=60,
                min_len=20,
            )
            print_result_block("Summarization Result", {"summary": summary})
            save_history("summarization", {"text": current_text}, {"summary": summary})
            pause()

        # ==========================
        # Translation
        # ==========================
        elif cmd == "3":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            translated = translation.run_translation(pipelines["translator"], current_text)
            print_result_block("Translation Result", {"translated": translated})
            save_history("translation", {"text": current_text}, {"translated": translated})
            pause()

        # ==========================
        # Sentiment
        # ==========================
        elif cmd == "4":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            result = sentiment.run_sentiment(pipelines["sentiment"], current_text)
            print_result_block("Sentiment Result", {"sentiment": result})
            save_history("sentiment", {"text": current_text}, {"result": result})
            pause()

        # ==========================
        # Topic Classification
        # ==========================
        elif cmd == "5":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            result = topic_classification.run_topic_classification(
                pipelines["topic_classifier"],
                current_text,
            )
            print_result_block("Topic Classification Result", result)
            save_history("topic_classification", {"text": current_text}, result)
            pause()

        # ==========================
        # Keyword Extraction
        # ==========================
        elif cmd == "6":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            result = keywords.extract_keywords(current_text, top_k=10)
            print_result_block("Keyword Extraction Result", {"keywords": result})
            save_history("keywords", {"text": current_text}, {"keywords": result})
            pause()

        # ==========================
        # Similarity Check
        # ==========================
        elif cmd == "7":
            if not current_text.strip():
                print_error("먼저 기준 텍스트를 입력하거나 파일을 로드하세요. (T 또는 F)")
                pause()
                continue
            print_info("비교할 두 번째 텍스트를 입력합니다.")
            second_text = load_text_from_user()
            sim_result = similarity.compute_similarity(
                pipelines["embedder"],
                current_text,
                second_text,
            )
            print_result_block("Similarity Result", sim_result)
            save_history(
                "similarity",
                {"text_a": current_text, "text_b": second_text},
                sim_result,
            )
            pause()

        # ==========================
        # Grammar Correction
        # ==========================
        elif cmd == "8":
            if not current_text.strip():
                print_error("먼저 텍스트를 입력하거나 파일을 로드하세요.")
                pause()
                continue
            corrected = grammar.run_grammar_correction(
                pipelines["grammar_model"],
                current_text,
            )
            print_result_block("Grammar Correction Result", corrected)
            save_history(
                "grammar_correction",
                {"original": current_text},
                corrected,
            )
            pause()

        # ==========================
        # PDF Smart Analysis
        # ==========================
        elif cmd == "p":
            pdf_path = select_pdf_file_interactive()
            if pdf_path is None:
                print_error("선택된 PDF 파일이 없습니다.")
                pause()
                continue

            report = report_pdf_analysis.analyze_pdf(
                summarizer=pipelines["summarizer"],
                topic_classifier=pipelines["topic_classifier"],
                keyword_extractor=keywords.extract_keywords,
                pdf_path=str(pdf_path),
            )
            print_result_block("PDF Smart Analysis Report", report)
            save_history("pdf_analysis", {"pdf_path": str(pdf_path)}, report)
            pause()

        else:
            print_error("알 수 없는 명령입니다. 다시 입력해 주세요.")
            pause()


if __name__ == "__main__":
    main()
