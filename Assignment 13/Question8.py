text = input("Enter a string:")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("word frequency:", freq)