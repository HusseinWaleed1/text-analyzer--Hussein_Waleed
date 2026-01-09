import re
from collections import Counter


def analyze_text(text: str):
    text = text.lower()
    text_clean = re.sub(r"[^\w\s]", "", text)

    words = text_clean.split()
    word_count = len(words)

    sentence_count = len(re.findall(r"[.!?]+", text))

    word_frequencies = Counter(words)
    top_10_words = word_frequencies.most_common(10)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10_words
    }


if __name__ == "__main__":
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    result = analyze_text(text)

    print("Text Analysis Results")
    print("---------------------")
    print(f"Word Count: {result['word_count']}")
    print(f"Sentence Count: {result['sentence_count']}")
    print("Top 10 Most Frequent Words:")
    for word, count in result["top_10_words"]:
        print(f"{word}: {count}")