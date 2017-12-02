import pandas as pd
import requests
import json

import pprint

from parse_crypto import get_top

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

def search_data(data, slist):
    matches = []
    for s in slist:
        if s.lower() in data['title'].lower() or s.lower() in data['selftext'].lower():
            matches.append(s)
    return matches

def filter_data(data, slist):
    filtered = []
    for item in data:
        matches = search_data(item, slist)
        if len(matches) != 0:
            item['matches'] = matches
            filtered.append(item)
    return filtered

def filter_by_crypto(filename):
    sample = read_file('sample.json')
    cryptos = get_top()
    all_crypto = filter_data(sample, cryptos)
    return al_crypto

sample = filter_by_crypto('sample.json')
data = pd.DataFrame(sample)


# data = []
# for line in lines:
#     print(line)
#     line_data = json.loads(line)
#     #data.append({x: y for x, y in line_data.items() if x in keep})
# 
# pp.pprint(data)
