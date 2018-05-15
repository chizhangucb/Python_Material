#!/usr/bin/ env pythons

import sys
from mr import emit, values_by_key

def count_vowels(line):
    for vowel in 'aeiou':
        count = line.cout(vowel)
        if count > 0:
            emit(vowel, count)
            
for key, value_iterator in values_by_key(sys.stdin):
    emit(key, sum(value_iterator))
