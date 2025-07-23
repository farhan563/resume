def generate_summary(text, sentence_count=7):
    sentences = text.split('.')
    summary = '. '.join(sentences[:sentence_count])
    return summary.strip() + '.'
