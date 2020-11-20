import praw
import openai
import json

writes = 0

def getresponses(num, temp, tokenlength, prompt):

    global writes

    openai.api_key = "sk-AO6NCUKkCZHSBQuv9SD3HjrJTWOLDzCIhVAr35Af"
    response = openai.Completion.create(engine="davinci", temperature=temp, frequency_penalty=0.5, prompt=prompt, max_tokens=tokenlength, n=num)
    completions = response.choices

    file = open("40responses.txt", "a")


    for choice in completions:
        file.write(prompt + choice["text"])
        file.write("\n\n\n____________________________________________________________________________________\n\n\n")
        print("Wrote to file " + str(writes) + " times. \n")
        writes += 1

    file.close()


reddit = praw.Reddit(
    client_id="5bqOH6aMlqJ_iQ",
    client_secret="r0XnL1a4O1obqO9rrrXIQggUbjU",
    user_agent="VaxScrape"
)


# returns a list of posts that contain one or more of the keywords
def getReleventPosts(posts, keywords):
    list = []
    for post in posts:
        if keywords[0] in post.title:
            list.append(post)
    return list

# Returns list of text bodies of top [numpost] hot posts in [subreddit]
def get_posts(subreddit, numposts):
    i = 0
    s = 0
    t = 0
    posts = reddit.subreddit(subreddit).hot(limit=numposts)
    posttext = []
    for post in posts:
        if len(post.selftext) > 100:
            posttext.append(post.selftext)
            print("SELFTEXT " + str(s))
            s += 1
        elif len(post.title) > 100:
            posttext.append(post.title)
            print("TITLE " + str(t))
            t += 1
        else:
            print("NOT LONG ENOUGH: " + str(i))
            i += 1
        print(str(i + s + t))
    return posttext
