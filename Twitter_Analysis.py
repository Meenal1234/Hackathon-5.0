#!/usr/bin/python3.4

import textblob
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt 

def percentage(part,whole):
	return 100* float(part)/float(whole)

consumerKey= "TpE2mLdtis51FQW09hupmeqVu"
consumerSecret= "vqMiWm9YInh8s7CEX00EmJVi4wltg6c7aYo76kZTHOojKMU4PZ"
accessToken= "1010562175499407360-S6WR7S7RSkl4OYKcCgpj3xXTZ1UVG3"
accessTokenSecret= "zf5hBPcBugoKpOaGFLLsLBV4ML3UVhlC7gXQeAIzFFVTl"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api=tweepy.API(auth)

searchTerm=raw_input("Enter keyword/hashtag to search about: ")
noOfSearchTerms= int(input("Enter How many tweets to analyse: "))

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)

positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
	#print(tweet.text)
	analysis= TextBlob(tweet.text)
	polarity += analysis.sentiment.polarity

	if(analysis.sentiment.polarity==0):
		neutral +=1

	elif (analysis.sentiment.polarity<0.00):
		negative +=1

	elif (analysis.sentiment.polarity>0.00):
		positive +=1

positive=percentage(positive, noOfSearchTerms)
negative=percentage(negative, noOfSearchTerms)
neutral=percentage(neutral, noOfSearchTerms)


positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negative=format(negative,'.2f')

print("How people are reacting on " + searchTerm + "by analyzing" + str(noOfSearchTerms) + "Tweets.")

if (polarity==0):
	print("Neutral")
elif (polarity<0):
	print("Negative")
elif (polarity>0):
	print("positive")

labels=['Positive [' +str (positive)+'%]', 'Negative [' +str (negative)+'%]', 'Neutral [' +str (neutral)+'%]']

sizes= [positive, negative, neutral]

colors=['green', 'red', 'gold']

patches, texts= plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc="best")

plt.title('How people are reacting on ' + searchTerm +' by analyzing '+ str(noOfSearchTerms) +' Tweets.')

plt.axis('equal')

plt.tight_layout()

plt.show()
