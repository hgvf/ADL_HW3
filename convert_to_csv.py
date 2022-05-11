import json
import csv
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--jsonl_file', type=str, default='/mnt/nas4/weiwei/ADL/proj3/data/public.jsonl')
parser.add_argument('--output_file', type=str, default="valid.csv")
opt = parser.parse_args()

ids = []
maintext = []
title = []

with open(opt.jsonl_file, 'r') as ff:
    json_list = list(ff)

for json_str in json_list:
    data = json.loads(json_str)

    if 'title' not in data.keys():
        title.append('Hello, world\n')
    else:
        title.append(data['title'])

    ids.append(data['id'])
    maintext.append(data['maintext'])

data = {}
data['id'] = ids
data['article'] = maintext
data['title'] = title

df = pd.DataFrame(data)

df.to_csv(opt.output_file, encoding='utf-8')