import io
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

file1 = open('./assest/text.txt')
line = file1.readline()
words = line.split()

appendFile = open('./assest/filteredText.txt', 'a')
for r in words:
    if r not in stopWords:
        appendFile.write(" "+r)
appendFile.close()

# wordTokens = word_tokenize(text)
#
# filteredSentence = [w for w in wordTokens if w not in stopWords]
#
# print(word_tokenize(text))
# print(filteredSentence)
