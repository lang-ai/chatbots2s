#!/bin/bash

python -m sockeye.evaluate --references y_text_test.txt --hypotheses output_file.txt --metrics bleu chrf rouge1 rouge2 rougel