with open("sample.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

with open("summary.txt", "w") as file:
    file.write("Lines: " + str(len(lines)) + "\n")
    file.write("Words: " + str(len(words)) + "\n")
    file.write("Characters: " + str(characters))

print("Summary generated successfully")