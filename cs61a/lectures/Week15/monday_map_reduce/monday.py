#!/usr/bin/env python3

import sys

for line in sys.stdin:
    sys.stdout.write(' '.join(line))

# chmod a+x monday.py
# ./monday.py
# Then python3 will be run automatically

# ./mr.py run count_vowels_mapper.py sum_reducer.py shakespeare vowel_counts
