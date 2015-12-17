# Follow *[@RealTrumpTalk](https://twitter.com/RealTrumpTalk)* on Twitter!

# TrumpTalk
Using markov-chains to parse tweets by [@realDonaldTrump](https://twitter.com/realDonaldTrump) and create tweets new using what he says. It will post a new tweet every 30 minutes, which has a 40% chance of mentioning a user, and a 75% chance of including a hashtag. Every 12 hours, the database of tweets will be refreshed and re-parsed to stay up to date.

### Dependencies
- [Tweepy](https://github.com/tweepy/tweepy)
- [Markovify](https://github.com/jsvine/markovify)

### Setup
1. Clone the repository, or in some way get the code.
2. Create a Twitter account to use for the script.
3. Go to https://apps.twitter.com and create a new app. Fill in the information and find your consumer key and secret.
4. Generate your access key and access secret below.
5. Open up your favorite editor and make a new file called `credentials.py` and copy in the variables below.

```python
consumer_key = "Your_key"
consumer_secret = "Your_secret"
access_key = "Token_key"
access_secret = "Token_secret"
```
Replace the values within the quotes with the appropriate values you just got from your Twitter app.
6. *(Optional) If you want to use a different account than @realDonaldTrump, you just need to go into `main.py` and change all instances of `realDonaldTrump` to whatever username you would like to use.*

### Running
In terminal, run `python main.py`
Depending on how your system is configured, you may need to run it as root with `sudo python main.py`, which will prompt you for your password.

### Contributing
If you find a bug, know a better way of doing something, or want to add a feature, please feel free to open a pull request and I will take a look.
