GUIDES:
+ [Sentiment Analysis Using NLTK](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)
+ []()

NLTK: Natural Language Toolkit

__Questions:__
- Metrics on training models: are these really classified by searching for those emoticons? How would be classify? (see twitter-corpus README)

__Random Thoughts:__
Using tagger, getting only the nouns present in the lyrics of a song, sorting by frequency, and searching for those using reddit's search to do heavy lifting.. -- *MVP driver*

Overall steps: (next guide)
- clean dataset for processing
- train model with pre-classified data
- use model to classify rest of data

!!Step back-- How to use NLTK
===

What we did:
- download corpus -- body of data, here tweets from twitter's REST API
- download POS tagger -- part of speach (nouns, verbs, etc), here one called `perceptron` that uses an algorithm of that name to tag the words
