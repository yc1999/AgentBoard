# CUDA_VISIBLE_DEVICES=0,1,2,3 python agentboard/eval_main.py --cfg eval_configs/main_results_all_tasks.yaml \
#                     --tasks alfworld \
#                     --model  lemur-70b \
#                     --log_path results/lemur-70b \
#                     --wandb \
#                     --project_name evaluate-lemur-70b \
#                     --baseline_dir data/baseline_results \

python agentboard/eval_main.py --cfg eval_configs/main_results_all_tasks.yaml \
                    --tasks tool-query \
                    --model  gpt-3.5-turbo-0613 \
                    --log_path results/gpt-3.5-turbo \
                    --project_name evaluate-gpt-3.5-tubo \
                    --baseline_dir data/baseline_results \