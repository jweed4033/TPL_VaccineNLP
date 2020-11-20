import random
from Train_LDA import trainModel
from RedditScrapeAttempt import get_posts
import numpy as np
from LDA_Attempt import ProcessDocuments
import matplotlib.pyplot as plt


docs1 = get_posts(subreddit='MachineLearning', numposts=1000)
docs2 = get_posts(subreddit='Psychedelics', numposts=1000)
docs3 = get_posts(subreddit='PoliticalDiscussion', numposts=1000)
"""docs4 = get_posts(subreddit='Stims', numposts=1000)
docs5 = get_posts(subreddit='Psychedelics', numposts=1000)
docs6 = get_posts(subreddit='DrugNerds', numposts=1000)
docs7 = get_posts(subreddit='shrooms', numposts=1000)
docs8 = get_posts(subreddit='Psychonaut', numposts=1000)
docs9 = get_posts(subreddit='addiction', numposts=1000)
docs10 = get_posts(subreddit='trees', numposts=1000)"""
docs = docs1 + docs2 + docs3 #+ docs4 + docs5 + docs6 + docs7 + docs8 + docs9 + docs10




random.shuffle(docs)


# Cross validation shit
"""belowList = [100, 50, 20]
aboveList = [.05, .1, .25]

matrix = np.zeros((len(belowList), len(aboveList)))

for a in range(len(aboveList)):
    for b in range(len(belowList)):
        print("__________________________________________________")
        print("no_below: ", aboveList[a])
        print("no_above: ", belowList[b])
        matrix[a, b] =  trainModel(docs = docs, nobelow=belowList[b], noabove=aboveList[a])

print(matrix)
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.show()"""

model, avg_topic_coherence, corpus = trainModel(docs=docs, nobelow=5, t=3)

for i in range(4):
    distribution = model.get_document_topics(bow=corpus[i + 100], minimum_probability=None, minimum_phi_value=None, per_word_topics=False)
    print("Disty:", distribution)
    print("Corpy: ", docs[i + 100])
    print("____________________________________________________________________________________")




# Up next: How to classify a new example based on the learned topics
