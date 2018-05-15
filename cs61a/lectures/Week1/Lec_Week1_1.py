## Numeric expressions
2018
2000 + 18
1 - 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)


## Call expressions
max(3, 4.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(pow(10, 2), pow(2, 10), 1010)

## Importing and arithmetic with call expressions
from operator import add, mul, sub
add(1, 2)
mul(4, 6)
mul(add(4, mul(4, 6)), add(3, 5))
add(2, mul(9, mul(add(4, mul(4, 6)), add(3, 5))))
sub(100, mul(7, add(8, 4)))

from math import sqrt
sqrt(256)

## Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
import urllib.request
url = "http://composingprograms.com/shakespeare.txt"
urllib.request.urlretrieve(url, "shakespeare.txt")

shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count("the")
text.count('thus')
text.count("thou")
text.count("you")
text.count("forsooth")
text.count(",")
text.count(",") / len(text)

## Sets
# A set contains an unordered collection of unique and immutable objects
words = set(text)
"forsooth" in words
"the" in words
len(words)  # Unique words
max(words)
max(words, key = len)

## Reversals
# reversal of "draw"
"draw"[::-1]
# evaluates to the set of all Shakespearian words that
# are simultaneously a word spelled in reverse and
# have a length of 6
{w for w in words if w[::-1] in words and len(w) == 6}

{w for w in words if w[::-1] in words and len(w) > 6}
# Nothing exists

# the reverse of w is the same as w and its length of 4
{w for w in words if w == w[::-1] and len(w) == 4}

{w for w in words if w == w[::-1] and len(w) > 4}


# Note: the file /usr/share/dict/words is specific to Mac
words = set(open("/usr/share/dict/words").read().split())
len(words)
"computer" in words=
{w for w in words if w[::-1] in words and len(w) == 6}
{w for w in words if w[::-1] in words and len(w) > 7}