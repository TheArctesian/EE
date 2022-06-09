# https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
import nltk
nltk.download()
sen = "I hate this world and I want to die"
tokens = nltk.word_tokenize(sen)
print(tokens)