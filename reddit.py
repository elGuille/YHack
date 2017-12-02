import praw
reddit = praw.Reddit(username="shryans", password="Shryans@27", client_id="clbYCsRuqIqVwA", client_secret="cSIK9IunrBE_4PPMRJmK1-qrp1k", user_agent="usragent")
key_words = ['Bitcoin growth', 'Bitcoin stock price', 'ICO price', 'bitcoin bubble', 'bitcoin stock price' , 'bitcoin growth', 'ico price']
subreddit = []
for i in key_words:
	subreddit.append(reddit.subreddit(i))
top = []
for i in subreddit:
	top.append(i.top(limit=100))