
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import string
import markovify
import shelve
import random
import time
import HTMLParser
from datetime import datetime

# READ THE README.MD!
import credentials as creds

h = HTMLParser.HTMLParser()

#Twitter API credentials
consumer_key = creds.consumer_key
consumer_secret = creds.consumer_secret
access_key = creds.access_key
access_secret = creds.access_secret

done_ids = shelve.open('parsed_ids')

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def stripTweets():
    with open('realDonaldTrump_tweets.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if row['id'] not in done_ids.keys():
                text = row['text']
                words = [text]
                for word in words:
                    if word[0] == '#':
                        with open('hashtags.csv', 'ab') as f:
                    		writer = csv.writer(f)
                    		writer.writerow([word])

                    if word[0] == '@' and len(word) > 1:
                        with open('@mentions.csv', 'ab') as f:
                            writer = csv.writer(f)
                            writer.writerow([word])
                line = " ".join(words)
                count += 1
                with open('parsed.csv', 'ab') as parsed:
                    writer = csv.writer(parsed)
                    writer.writerow([line])

                done_ids[row['id']] = True
        print "[LOG:] Parsed "+str(count)+" new tweets."

def markov():
    with open('parsed.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        text = ''
        for row in reader:
            escapes = ''.join([chr(char) for char in range(1, 32)])
            t = str(row).translate(None, escapes)
            t = t.decode('string_escape')
            text += t

    text_model = markovify.Text(text)

    return decorate(h.unescape(text_model.make_short_sentence(140)))

def decorate(s):
    l_m = []
    l_h = []

    with open('@mentions.csv', 'rb') as mentions:
        m_reader = csv.reader(mentions)
        for row in m_reader:
            l_m.append(row)

    with open('hashtags.csv', 'rb') as hashtags:
        h_reader = csv.reader(hashtags)
        for row in h_reader:
            l_h.append(row)

    r_1 = random.random()
    r_2 = random.random()

    if r_1 <= .4:
        user = random.sample(l_m, 1)
        if str(user[0][0]) == '@realDonaldTrump':
            s = "\""+str(user[0][0]) + " " + s+"\""
        else:
            s = str(user[0][0]) + " " + s

    if r_2 >= .35:
        hashtag = random.sample(l_h, 1)
        s = s + " " + str(hashtag[0][0])
    print "[OUT:] " + s
    return s


ctime = datetime.now().strftime('%H:%M')
print "["+ctime+"] Posting new status."
status = markov()
api.update_status(status)

print "["+ctime+"] Parsing tweets."
stripTweets()

print "["+ctime+"] Batch completed. Going back to sleep."
