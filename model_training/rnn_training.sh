#!/bin/bash

python -m sockeye.train -d train_data \
                       -vs x_text_validate.txt \
                       -vt y_text_validate.txt \
                       --encoder rnn \
                       --decoder rnn \
                       --num-embed 256 \
                       --rnn-num-hidden 512 \
                       --rnn-attention-type dot \
                       --max-seq-len 60 \
                       --decode-and-evaluate 500 \
                       -o model