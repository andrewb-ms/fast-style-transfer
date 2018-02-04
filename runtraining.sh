#!/bin/bash
python style.py --style path/to/style/img.jpg \
  --checkpoint-dir checkpoint/path \
  --test path/to/test/img.jpg \
  --test-dir path/to/test/dir \
  --content-weight 1.5e1 \
  --checkpoint-iterations 1000 \
  --batch-size 20
