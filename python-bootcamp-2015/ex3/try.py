# Q1
import json
with open('speeches.json') as infile:
    y = json.load(infile)

# Q2
len(y)

# Q3
presidents = []
for i in range(len(y)):
    presidents = presidents + [y[i]['president']]
presidents
    
# Q4
dates = []
for i in range(len(y)):
    dates = dates + [y[i]['date']]
dates

# Q5
def speech_tuple(dic):
    x = dic['president']
    y = len(dic['text'].replace('\n', ' ').replace('  ', ' ').split(' '))
    z = dic['date']
    result = (x, y, z)
    return result

# Q6
objects = []
for i in range(len(y)):
    objects = objects + [speech_tuple(y[i])]
objects
