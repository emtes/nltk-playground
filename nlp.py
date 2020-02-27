from typing import List, Dict # type hinting is important
from nltk.corpus import twitter_samples # me JSONs with tweets
from nltk.tag import pos_tag_sents # part of speach tagger

# Each tweet is an item
pos_tweets: list = twitter_samples.strings('positive_tweets.json')

# Goal: count adjective: descriptor and nouns: thing
'''
1. Tokenization: breaking up sequence of strings into /words(?)/phrases
Regardless, each piece is a token.
* In this case the strings are being split at each space
'''
pos_tweets_tokens: list = twitter_samples.tokenized('positive_tweets.json')

# tuples with token and tag
pos_tweets_tagged: list = pos_tag_sents(pos_tweets_tokens)

'''
JJ: adjective
NN: singular noun
NNS: plural noun
'''

# Let us count how many times these appear!
