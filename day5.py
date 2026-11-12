paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Unique Words:", set(frequency.keys()))
print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)

top_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 3 Most Used Words:")

for word, count in top_words[:3]:
    print(word, ":", count)
