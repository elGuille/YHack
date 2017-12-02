import pandas as pd
import requests
import json

import pprint
pp = pprint.PrettyPrinter(indent=2)

def read_file(filename):
    file = open(filename)
    raw_data = file.read()
    lines = raw_data.split('\n')

    keep = ['id', 'created_utc', 'title', 'selftext', 'num_comments', 'score', 'subreddit']

    data = []
    for line in lines:
        if len(line) == 0:
            continue
        parsed = json.loads(line)
        #pp.pprint(parsed)
        data.append({x: y for x, y in parsed.items() if x in keep})
    return data

sample = read_file('sample.json')

def filter_for(data, slist):
    for s in slist:
        if s in data:
            return True
    return False



data = pd.DataFrame(columns=keep)


# data = []
# for line in lines:
#     print(line)
#     line_data = json.loads(line)
#     #data.append({x: y for x, y in line_data.items() if x in keep})
# 
# pp.pprint(data)
