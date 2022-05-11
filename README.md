# ADL_HW3

### Preprocess
jsonl to csv
```
python convert_to_csv.py --jsonl_file <jsonl_file> --output_file <output_csvfile>
```

### Fine-tuned T5-small model
```
CUDA_VISIBLE_DEVICES=<gpu_id> python run_summarization.py \
--model_name_or_path "google/mt5-small" --do_train --predict_with_generate \
--overwrite_output_dir --source_prefix "summarize: " --train_file <path_to_train_csv>  \
--output_dir <output_dir> \
--adafactor True --text_column "article" --summary_column "title" \
--per_device_train_batch_size 4 --gradient_accumulation_steps 10 \
--dataloader_num_workers 6 --save_steps 500 --num_train_epochs 20 \
--learning_rate 4e-5 --lr_scheduler_type cosine --warmup_steps 1000
```

### Inference
```
CUDA_VISIBLE_DEVICES=<gpu_id> python run_summarization.py \
--model_name_or_path "google/mt5-small" --do_predict --predict_with_generate \
--overwrite_output_dir --source_prefix "summarize: " --test_file <path_to_test_csv> \
--output_dir <output_dir> --text_column "article" --per_device_eval_batch_size 30 \
--summary_column "title" --num_beams 4

```
