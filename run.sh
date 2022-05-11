python3 convert_to_csv.py --jsonl_file "${1}" --output_file "./valid.csv"

mkdir output

CUDA_VISIBLE_DEVICES=3 python run_summarization.py \
--model_name_or_path "google/mt5-small" --do_predict --predict_with_generate \
--overwrite_output_dir --source_prefix "summarize: " --test_file "./valid.csv" \
--output_dir "./output" --text_column "article" --per_device_eval_batch_size 30 \
--summary_column "title" --num_beams 4

python3 output_jsonl.py --output_path "${2}"
