


f = open("c:\\Users\\E\\Desktop\\the_republic_plato.txt")

file_contents = f.read()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just"]

# LEARNER CODE START HERE
frequencies = {}
# Remove puntuation marks from the text
for char in punctuations:
    file_contents = file_contents.replace(char, "")

# iterate through the file_contents
for word in file_contents.split():
    if word.lower().isalpha() and word.lower() not in uninteresting_words:
        frequencies[word.lower()] = frequencies.get(word.lower(), 0) + 1  # Add the word or increments the counter

#print(frequencies)
# print(max(frequencies, key=frequencies.get))
print(frequencies["other"])

