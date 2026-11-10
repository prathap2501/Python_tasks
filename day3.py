
sentence = input("Enter a sentence: ")

# Count vowels
vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Total vowels:", count)

# Count words
words = sentence.split()
print("Total words:", len(words))

# Reverse the sentence
print("Reverse:", sentence[::-1])