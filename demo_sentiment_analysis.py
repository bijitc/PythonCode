"""
emoji unicode reference:
\U0001F642 - happy face
\U0001F641 - sad face
\U0001F610 - neutral face
"""

"""
Algorithm

1. Invite Blob (import TextBlob package)
2. Print question
3. Take a sentence as input
4. get polarity value from TextBlob
5. check value and print sentiment(Yay!/Oh no!/Ok!)

"""

from textblob import TextBlob

print("How are you feeling today?")
s = input("You: ")
p = TextBlob(s).sentiment.polarity

if p > 0:
    print("Blob: Yay! Your p value is", p)
elif p < 0:
    print("Blob: Oh no! Your p value is", p)
else:
    print("Blob: Ok! Your p value is", p)

