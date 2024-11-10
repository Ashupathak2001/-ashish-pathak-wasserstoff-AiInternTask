import yake

def extract_keywords(text, num_keywords = 10):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords[:num_keywords]]

def extract_keywords_from_docs(pdf_texts):
    keywords_dict = {}
    for filename, text in pdf_texts.items():
        keywords_dict[filename] = extract_keywords(text)
        print(f"Keywords extracted for {filename} successfully")
    return keywords_dict