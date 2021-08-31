# import libs
import os
import tweepy
from datetime import datetime
from tqdm import tqdm

# import configs
from config import *

def login():
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    print("Authentication complete!")
    return auth


def init_api(auth):
    api = tweepy.API(auth, wait_on_rate_limit=True)
    print("API Initiated!")
    return api


def tweet():
    print("Tweet:")
    tweet = input(" ")
    api.update_status(status =(tweet))
    print("you just tweeted: ", tweet) 


def reply():
    tweetid = "1366994552368758786"
    reply = "I'm Conscious of your shock, bcz i'm within your Consciousness!"

    api.update_status(reply, in_reply_to_status_id = tweetid, auto_populate_reply_metadata=True)
    print("you just replied: ", reply, "\n to ", tweetid) 


def get_followers(api):
    print("fetching followers...")
    followers = tweepy.Cursor(api.followers, screen_name)
    print("FETCHED")
    return followers


def update_database(dirname):
    print("Updating database...")
    basedir = os.path.join("data")
    latest = ""
    last = ""
    with open(os.path.join(basedir, "latest"), "r") as f:
        latest = f.read()
    print("Latest: ", latest)
    with open(os.path.join(basedir, "last"), "r") as f:
        last = f.read()
    print("Last: ", last)
    last = latest
    latest = os.path.join(basedir, dirname, "followers.txt")
    with open(os.path.join(basedir, "last"), "w+") as f:
        f.write(last)
    with open(os.path.join(basedir, "latest"), "w+") as f:
        f.write(latest)
    print("UPDATED LAST TO: ", last)
    print("UPDATED LATEST TO: ", latest)


def save_followers(followers, dirname):
    print("Saving list of followers...")
    basedir = os.path.join("data", dirname)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    text = ""
    for follower in tqdm(followers.items(max_followers_count)):
        # print(follower.screen_name)
        text = text+follower.screen_name+"\n"
    # print("FILE:", text)
    with open(os.path.join(basedir, "followers.txt"), "w+") as f:
        f.write(text)
    print("SAVED to ", os.path.join(basedir, "followers.txt"))   


def get_last_followers():
    print("Reading LAST...")
    basedir = os.path.join("data")
    last = ""
    with open(os.path.join(basedir, "last"), "r") as f:
        last = f.read()
    print("Last: ", last)
    datafile = last
    data = ""
    if os.path.exists(datafile):
        with open(datafile, "r") as f:
            data = f.read()
        print("READ!")
        return (1, data)
    else:
        data = ""
        print("FOUND Empty LAST!")
        return (0, data)


def get_latest_followers():
    print("Reading LATEST...")
    basedir = os.path.join("data")
    latest = ""
    with open(os.path.join(basedir, "latest"), "r") as f:
        latest = f.read()
    print("LATEST: ", latest)
    datafile = latest
    data = ""
    if os.path.exists(datafile):
        with open(datafile, "r") as f:
            data = f.read()
        print("READ!")
        return (1, data)
    else:
        data = ""
        print("FOUND Empty LATEST!")
        return (0, data)


def get_unfollowers(last_followers, latest_followers):
    unfollowers = set(last_followers.split()) - set(latest_followers.split())
    return unfollowers


def get_new_followers(last_followers, latest_followers):
    new_followers = set(latest_followers.split()) - set(last_followers.split())
    return new_followers


def sync():
    timestamp = datetime.now().strftime("%a_%d-%B-%Y_%H-%M-%S")
    print("TIMESTAMP:", timestamp)
    print("USERNAME:",screen_name)
    auth = login()
    api = init_api(auth)
    followers = get_followers(api)
    save_followers(followers, timestamp)
    update_database(timestamp)
    print("DONE!")


def status():
    last_flag, last_followers = get_last_followers()
    latest_flag, latest_followers = get_latest_followers()
    print("FLAGS:", last_flag, latest_flag)
    # print("TYPES:", type(last_followers.split()), type(latest_followers.split()))
    # print("LAST: \n", last_followers.split())
    # print("LATEST: \n", latest_followers.split())
    if last_flag and latest_flag:
        unfollowers = get_unfollowers(last_followers, latest_followers)
        print("UNFOLLOWERS: ", unfollowers)
        new_followers = get_new_followers(last_followers, latest_followers)
        print("NEW FOLLOWERS: ", new_followers)
    else:
        print("STOPPING: Nothing/Ambiguity to compare")

