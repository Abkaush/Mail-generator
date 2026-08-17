import re


def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Remove URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    # Retain common punctuation useful for job post semantics
    text = re.sub(r'[^a-zA-Z0-9\s.,\-\/\(\)]', '', text)
    # Replace multiple whitespaces/newlines with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()