#!/bin/bash

python -m sockeye.train -d train_data \
                      -vs x_text_validate.txt \
                      -vt y_text_validate.txt \
                      --encoder cnn \
                      --decoder cnn \
                      --num-embed 128 \
                      --cnn-num-hidden 128 \
               		  --cnn-positional-embedding-type fixed \
               		  --cnn-activation-type glu \
                      --rnn-attention-type dot \
                      --max-seq-len 100 \
               		  --batch-size 1024 \
                      --decode-and-evaluate 500 \
					  --device-ids -1 \
                      -o cnn_model