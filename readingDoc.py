filename = "RC_2017-03"

#https://github.com/alumbreras/reddit_parser <-- good tutorial on  parsing in a stream


import json
import ijson
import pandas as pd
import time

start = time.time()

#df = pd.read_json(filename, lines = True)

#print (df.columns)

#print(df.shape)

#df1 = list(df['subreddit'])

#print(set(df1))

#f = open(filename, "r")
#json.load(f)
#f.close()

list = []

with open(filename, 'r') as f:
    for i , line in enumerate(f):
        d = json.loads(line)
        if d['subreddit'] == 'rugbyunion':
            list.append(d)


df = pd.DataFrame(list)

print(df.keys())

df.to_pickle("test_pickle.pkl")

df1 = pd.read_pickle("test_pickle.pkl")
print(df1.head())
print((time.time() - start)/60)
