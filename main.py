import concurrent.futures
from parsing import parse_and_store
from docUpdation import store_updated_data
from Keyword import extract_keywords_from_docs
from summarization import summarize_doc
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

def process_document(filename, text):
    summary = summarize_doc({filename: text}, api_key)[filename]
    keywords = extract_keywords_from_docs({filename: text})[filename]
    store_updated_data(filename, summary, keywords)
    print(f"Summary and keywords for {filename} updated successfully")
    return summary

def main(folder_path):
    pdf_texts = parse_and_store(folder_path)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_document, filename, text) for filename, text in pdf_texts.items()}
        for future in concurrent.futures.as_completed(futures):
            print(f"Processed document summary: {future.result()}")


if __name__ == "__main__":
    folder_path = "/home/ashupathak/wasserstoff_AIIntern_TASK/file"
    main(folder_path)