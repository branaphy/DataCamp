# Import the needed packages
from nltk import word_tokenize

# Tokenize each item in the review column 
word_tokens = [word_tokenize(review) for review in reviews.review]

# Print out the first item of the word_tokens list
print(word_tokens[0])
