from file_reader import read_file, get_lines # type: ignore
from stats import count_lines, count_words, count_sentences, average_word_length, average_words_per_sentence # type: ignore
from word_frequency import get_most_common # type: ignore

content = read_file("test.txt")
lines = get_lines("test.txt")

""" print(f"Lines: {count_lines(lines)}")
print(f"Words: {count_words(content)}")
print(f"Sentences (approx): {count_sentences(content)}")
print(f"Average word length: {average_word_length(content):.2f}")
print(f"Average words per sentence: {average_words_per_sentence(content):.2f}")  """

print("Most common words:")
for word, freq in get_most_common(content, n=10):
    print(f"  {word}: {freq}")

