from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
import time
import random

logger = logging.getLogger()

USERNAME = "orangejuicefan101"
PASSWORD = "PizzaTankInstagram647!@#"
USER_ID = "61853572437"

myFile = open("followers.txt", "r") 
existing_names = set(myFile.read().splitlines())
myFile.seek(0)

cl = Client()
cl.load_settings("session.json")
cl.login (USERNAME, PASSWORD) # this doesn't actually login using username/password but uses the session
cl.get_timeline_feed()

myLink = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/DAWRqUHPu7h/'))

for line in myFile:
    currentName = line.strip()
    currentId = str(cl.user_id_from_username(currentName))
    currentFollowers = cl.user_followers(user_id=currentId, amount=0)

    print(currentId)

    for person in currentFollowers:
        victimName = cl.username_from_user_id(person)

        if victimName in existing_names:
            print(f"{person}: {victimName}, Already Finished")
        else:
            existing_names.add(victimName)
            try:
                cl.media_comment(media_id=myLink, text="@" + victimName)
                sleep_time = random.uniform(240,300)
                print(f"Processed {person}: {victimName}, Sent comment")
                print(f"Sleeping for {sleep_time:.2f} seconds to avoid spam detection.")
                time.sleep(sleep_time)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            

        
#followerDictionary = cl.user_followers(user_id=USER_ID, amount=0)

print("doneyaba")