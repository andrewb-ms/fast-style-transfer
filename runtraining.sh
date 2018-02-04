#!/bin/bash
python style.py --style /msshared/inputpaintings/degas1.jpg \
  --checkpoint-dir /msshared/trainingtest_newmodels/ \
  --test /msshared/trainingtest_input/test3.jpg \
  --test-dir /msshared/trainingtest_output/ \
  --content-weight 1.5e1 \
  --checkpoint-iterations 1000 \
  --batch-size 20
