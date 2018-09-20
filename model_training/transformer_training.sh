#!/bin/bash

python -m sockeye.train -d train_data \
                       -vs x_text_validate.txt \
                       -vt y_text_validate.txt \
                       --encoder transformer \
                       --decoder transformer \
                       --num-embed 128 \
                       --rnn-num-hidden 128 \
					   --transformer-model-size 128 \
                       --rnn-attention-type dot \
					   --rnn-scale-dot-attention \
                       --max-seq-len 100 \
                       --decode-and-evaluate 500 \
					   --batch-size 1024 \
					   --device-ids -1 \
                       -o model