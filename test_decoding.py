import pickle
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm

with open("/mnt/nas3/weiwei/transformers/examples/pytorch/summarization/input_ids.pkl", 'rb') as f:
    input_ids = pickle.load(f)

tokenizer = AutoTokenizer.from_pretrained("/mnt/nas4/weiwei/ADL/proj3/ckpt/mt5_small_cosine/checkpoint-10500/", cache_dir="/mnt/nas4/weiwei/ADL/proj3/cache/")
model = AutoModelForSeq2SeqLM.from_pretrained("/mnt/nas4/weiwei/ADL/proj3/ckpt/mt5_small_cosine/checkpoint-10500/", cache_dir="/mnt/nas4/weiwei/ADL/proj3/cache/").to(torch.device('cuda:3'))

predictions = []
for ids in tqdm(input_ids):
    x = torch.tensor(ids).unsqueeze(0).to(torch.device('cuda:3'))
    
    out=model.generate(x, do_sample=True, max_length=64, top_k=0, temperature=0.4)
    predictions.append(tokenizer.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))

predictions = [pred.strip() for pred in predictions]
output_prediction_file = "./tem4_generated_predictions.txt"
with open(output_prediction_file, "w") as writer:
    writer.write("\n".join(predictions))
