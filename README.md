*****************************************************************************
1. A python script bullying_tweet.py is provided to download the tweet to bullying_tweet.csv (including tweet texts) from Twitter API. You have to sign up for a Twitter account and apply for access tokens from Twitter.  Alternatively, a quick way to inspect a tweet is via the URL https://twitter.com/statuses/TweetID

*****************************************************************************
Original notes

This dataset contains data collected from Twitter stream API and labeled by 
experienced annotators for the study of bullying in social media.  We 
collected tweets using the public Twitter stream API, such that each tweet 
contains at least one of the following keywords: "bully, bullied, bullying". 
We further removed re-tweets by excluding tweets containing the acronym "RT." 
The tweets are cased-folded and tokenized, but without any stemming or stopword removal. 
Any user mentions preceded by a ``@'' were replaced by the anonymized user name ``@USERNAME''. 
Any URLs starting with ``http'' were replaced by the token ``HTTPLINK''. 
Hashtags (compound words following ``#'') were not split and were treated as 
a single token. Emoticons, such as ``:)'' or ``:D'', were also included as 
tokens. Our features include both unigrams and bigrams that appear at least 
twice in the tweets. 


----------------------------------Content----------------------------------

data.csv
	This contains the tweet ids, which is useful to retrieve tweets from 
	Twitter APIs. Each line corresponds to one tweet and has seven fields 
	separated by commas:
	Tweet ID, User ID, Bullying_Traces?, Type, Form, Teasing?, Author_Role, Emotion

	The possible values for Bullying_Traces?: 
		y (bullying trace) 
		n (not a bullying trace)
	The possible values for Type: 
		accusation
		cyberbullying
		denial
		report
		self-disclosure
		NA - The tweet is not a bullying trace and we didn't annotate its type
	The possible values for Form: 
		cyberbullying
		other
		physical
		property damage
		relational
		verbal
		NA - The tweet is not a bullying trace and we didn't annotate its form
	The possible values for Teasing?
		y - Teasing
		n - Not teasing
		NA - The tweet is not a bullying trace and we didn't annotate if it is teasing
	The possible values for Author_Role
		accuser
		assistant
		bully
		defender
		reinforcer
		reporter
		victim
		other
		NA - The tweet is not a bullying trace and we didn't annotate its author role
	The possible values for Emotion
		anger
		embarrassment
		empathy
		fear
		none
		other
		pride
		relief
		sadness
		NA - The tweet is not a bullying trace and we didn't annotate its emotion
		
-----------------------------Reference -----------------------------------------

[1] Learning from bullying traces in social media.
Jun-Ming Xu, Kwang-Sung Jun, Xiaojin Zhu, and Amy Bellmore.
In North American Chapter of the Association for Computational Linguistics - Human Language Technologies (NAACL-HLT).
Montreal, Canada, 2012.

[2] Understanding and Fighting Bullying with Machine Learning.
Jun-Ming Xu.
Phd Thesis, University of Wisconsin-Madison, June 2015.

Contact: Jun-Ming Xu (xujm@cs.wisc.edu), Xiaojin Zhu (jerryzhu@cs.wisc.edu)
