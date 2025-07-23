import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    return list(set(keywords))
