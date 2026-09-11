def count_lines(lines):
    return len(lines)

def count_words(content):
    words = content.split()
    return len(words)

def count_sentences(content):
    # naive but effective: count sentence-ending punctuation
    sentence_endings = content.count(".") + content.count("!") + content.count("?")
    return sentence_endings

def average_word_length(content):
    words = content.split()
    if not words:
        return 0
    total_length = sum(len(word.strip(".,!?;:\"'")) for word in words)
    return total_length / len(words)

def average_words_per_sentence(content):
    word_count = count_words(content)
    sentence_count = count_sentences(content)
    if sentence_count == 0:
        return 0
    return word_count / sentence_count