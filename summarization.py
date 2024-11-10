# from transformers import pipeline

# # initialize the summarization pipeline
# summarizer = pipeline("summarization", model = "facebook/bart-large-cnn")

# def generate_summary(text, chunk_size=512):
#     # Tokenize the text into chunks
#     inputs = summarizer.tokenizer(text, return_tensors="pt", truncation=True, padding="longest", max_length=chunk_size)
    
#     summaries = []
#     num_chunks = len(inputs['input_ids'])

#     # Summarize each chunk
#     for i in range(num_chunks):
#         # Decode each chunk separately and summarize it
#         chunk_text = summarizer.tokenizer.decode(inputs['input_ids'][i], skip_special_tokens=True)
#         summary = summarizer(chunk_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
#         summaries.append(summary)
    
#     # Combine all summaries
#     combined_summary = " ".join(summaries)
#     return combined_summary 

# def summarize_doc(pdf_texts):
#     summaries = {}
#     for filename, text in pdf_texts.items():
#         summaries[filename] = generate_summary(text)
#         print(f"Summary for {filename} generated successfully")
#     return summaries

import os
import cohere
from typing import Dict, Optional
from dotenv import load_dotenv
load_dotenv()

# set api_key
api_key = os.getenv("COHERE_API_KEY")

def generate_summary(text: str, api_key: str, chunk_size: int = 2048) -> str:
    
    # Initialize Cohere client
    co = cohere.Client(api_key)
    
    # Split text into chunks if it's too long
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []
    
    for chunk in chunks:
        try:
            # Generate summary using Cohere's summarize endpoint
            response = co.summarize(
                text=chunk,
                length='medium',  # Options: 'short', 'medium', 'long'
                format='paragraph',  # Options: 'paragraph', 'bullets'
                model='command',  # Options: 'command', 'command-light', 'command-nightly'
                additional_command='Make it concise and informative',
                temperature=0.3
            )
            summaries.append(response.summary)
        except Exception as e:
            print(f"Error summarizing chunk: {str(e)}")
            continue
    
    # Combine all summaries
    combined_summary = " ".join(summaries)
    return combined_summary

def summarize_doc(pdf_texts: Dict[str, str], api_key: str) -> Dict[str, str]:
    
    summaries = {}
    
    for filename, text in pdf_texts.items():
        try:
            summaries[filename] = generate_summary(text, api_key)
            print(f"Summary for {filename} generated successfully")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            summaries[filename] = f"Error generating summary: {str(e)}"
    
    return summaries


