import json
import pandas as pd
import argparse
from tw_rouge import get_rouge

parser = argparse.ArgumentParser()
parser.add_argument('--test_file', type=str, default="/mnt/nas4/weiwei/ADL/proj3/valid.csv")
parser.add_argument('-ref_file', type=str, default="/mnt/nas4/weiwei/ADL/proj3/tem4_generated_predictions.txt")
opt = parser.parse_args()

df = pd.read_csv(opt.test_file)
df.head()

with open(opt.ref_file, 'r') as f:
    pred = f.readlines()

refs, preds = {}, {}
for idx, row in enumerate(df.iterrows()):
    refs[str(row[1][1])] = row[1][3]
    preds[str(row[1][1])] = pred[idx].strip()

keys =  refs.keys()
refs = [refs[key] for key in keys]
preds = [preds[key] for key in keys]

print(json.dumps(get_rouge(preds, refs), indent=2))
