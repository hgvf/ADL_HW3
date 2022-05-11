import json
import argparse
import pandas as pd
import jsonlines

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='./output.jsonl')
opt = parser.parse_args()

with open('./output/generated_predictions.txt', 'r') as f:
    pred = f.readlines()

df = pd.read_csv('./valid.csv')

output = []
for i in range(len(pred)):
    tmp = {}
    tmp['id'] = str(df.iloc[i]['id'])
    tmp['title'] = pred[i]
    output.append(tmp)

with jsonlines.open(opt.output_path, 'w') as f:
    f.write_all(output)
