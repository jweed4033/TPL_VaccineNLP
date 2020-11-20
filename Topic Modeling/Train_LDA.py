from gensim.models import LdaModel
from LDA_Attempt import ProcessDocuments
from RedditScrapeAttempt import get_posts




def trainModel(docs, t=5, c=2000, p=20, i=400, nobelow=10, noabove=0.1):

    dict, corpus = ProcessDocuments(docs, nobelow, noabove)
    print('Number of unique tokens: %d' % len(dict))
    print('Number of documents: %d' % len(corpus))

    num_topics = t
    chunksize = c
    passes = p
    iterations = i
    eval_every = None  # Don't evaluate model perplexity, takes too much time.

    # Make a index to word dictionary.
    if len(dict) == 0:
        return -20

    temp = dict[0]  # This is only to "load" the dictionary.
    id2word = dict.id2token

    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        chunksize=chunksize,
        alpha='auto',
        eta='auto',
        iterations=iterations,
        num_topics=num_topics,
        passes=passes,
        eval_every=eval_every
    )

    top_topics = model.top_topics(corpus) #, num_words=20)

    # Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    from pprint import pprint
    pprint(top_topics)

    return model, avg_topic_coherence, corpus
