STOP_WORDS = {
    "the", "a", "an", "and", "or", "but",
    "in", "on", "at", "to", "for", "of",
    "with", "by", "from", "is", "was", "are",
    "were", "be", "been", "being", "it", "this",
    "that", "as", "not", "he", "she", "they",
    "we", "you", "i", "his", "her", "their",
    "my", "your", "me", "him", "them", "us",
    "our", "its", "who", "which", "what", "when",
    "where", "how", "why", "all", "any", "some",
    "no", "nor", "so", "very", "too", "also",
    "have", "has", "had", "do", "does", "did",
    "can", "could", "will", "would", "shall",
    "should", "may", "might", "must"
}

import string

def clean_words(content):
    words = content.lower().split()

    cleaned_words = []

    for word in words:
        word = word.strip(string.punctuation)

        if word and word not in STOP_WORDS:
            cleaned_words.append(word)

    return cleaned_words

from collections import Counter

def get_word_frequency(content):
    words = clean_words(content)
    return Counter(words)

def get_most_common(content, n=10):
    frequency = get_word_frequency(content)
    return frequency.most_common(n)