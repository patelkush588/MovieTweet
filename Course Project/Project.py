import twitter
import sys
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
reload(sys)
sys.setdefaultencoding("utf-8")


api=twitter.Api(consumer_key='fWgdytSVKGu4jaB3hyAoFN45w',
                  consumer_secret='UMwQ4IPO8H1DMXFmGo8hDq8obmwvKNdhiVZGHSr62z1to7SInO',
                  access_token_key='1339518248-WA5LD7c1EYej6qUIJLecM0LBRQP9nTVcshzmWqo',
                  access_token_secret='oO7AwxNR3kKiZCYigpiaIUHafsjiPe9I0QJSk5PB7IyF6')

movie=raw_input("Movie name: ")


def query_ex1():
    query = movie+' AND movie AND review'
    MAX_ID = None
    tweets = api.GetSearch(query,count=100, max_id=MAX_ID, result_type='mixed')
    for raw_tweet in tweets:
        tweet = json.loads(str(raw_tweet))
        #info = {"created_at": tweet['created_at'],"screen_name": tweet['user'], "text": tweet['text']}
        info={"text":tweet['text']}
        f=open(""+movie+".txt", 'a+')
        f.write(json.dumps(str(info)))
        f.write("\n")
        f.close()

print query_ex1()

def wordc():
    tweets=open(""+movie+".txt").read()
    word_cloud = WordCloud(stopwords='https',max_font_size=50).generate(tweets)
    plt.figure()
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

print wordc()