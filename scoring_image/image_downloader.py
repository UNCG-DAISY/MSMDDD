import pandas as pd
import sys, os
import threading
from time import sleep
import matplotlib.image as mpimg
import urllib2


def getimage(url, full_name):
    if os.path.isfile(full_name):
        return mpimg.imread(full_name)
    try:
        f = urllib2.urlopen(url)
    except Exception as exc:
        return None

    data = f.read()
    with open(full_name, "wb") as code:
        code.write(data)
    return mpimg.imread(full_name)


data = pd.read_csv("tweetClasses.csv") # reads a 3-column dataframe with IDs, Image URLs, and Classes.

SpamFolder = "Images/SpamReal/Spam/"
RealFolder = "Images/SpamReal/Real/"

done = 0
total = len(data)

for _, row in data.iterrows():
    folder = SpamFolder if row["class"] == 0 else RealFolder
    fullname = "{}{}.jpg".format(folder, row["tid"])
    t = threading.Thread(target=getimage, args=(row["url"], fullname))
    t.start()
    sleep(0.01)
    done += 1
    sys.stdout.write("{} / {}\r".format(done, total))
    sys.stdout.flush()