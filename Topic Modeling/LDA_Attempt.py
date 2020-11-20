from RedditScrapeAttempt import get_posts
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import Phrases
from gensim.corpora import Dictionary

def ProcessDocuments(docsUnsafe, nobelow=10, noabove=0.1):

    docs = docsUnsafe.copy()
    # object that can split string into tokens (split on whitespace)
    tokenizer = RegexpTokenizer(r'\w+')
    # object that lemmatizes (congeals different forms of same word) tokens
    lemmatizer = WordNetLemmatizer()

    # Reduce each string into a list of tokens
    for i in range(len(docs)):
        docs[i] = docs[i].lower()
        docs[i] = tokenizer.tokenize(docs[i])

        # Remove single char tokens and numeric tokens.
        # Also Lemmatize all valid tokens
        docs[i] = [lemmatizer.lemmatize(token) for token in docs[i] if (len(token) > 1) and not token.isnumeric()]

    # Add bigrams (two consecutive words)
    bigram = Phrases(docs, min_count=20)
    for i in range(len(docs)):
        for token in bigram[docs[i]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[i].append(token)

    # Create a dictionary representation of the documents.
    dict = Dictionary(docs)

    # filter out the irrelevant tokens
    # dict.filter_n_most_frequent(50)
    dict.filter_extremes(no_below=nobelow, no_above=noabove)


    #Vectorize into list of document token lists (token_id, token_count)
    corpus = [dict.doc2bow(doc) for doc in docs]



    return dict, corpus 
