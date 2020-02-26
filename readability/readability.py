# readability in python
from cs50 import get_string
import math

# getting text from user
text = get_string("Text: ")

# letters , words , sentences counter
letters = 0
words = 1
sentences = 0


for i in text:
    # check for letters
    if i.isalpha():
        letters += 1
    # check for words
    if i.isspace():
        words += 1
    # check for sentences
    if i in [".", "!", "?"]:
        sentences += 1


l = 100 * letters / words
s = 100 * sentences / words

grade = round(0.0588 * l - 0.296 * s - 15.8)

grade = int(grade)

# print grades for text
if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade ", grade)
