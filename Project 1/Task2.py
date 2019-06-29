"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)



with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    dic ={}
    for c in calls:
        if c[0] not in dic:
            dic[c[0]]= int(c[3])

        elif c[0] in dic:
            dic[c[0]]= dic[c[0]] + int(c[3])

        if c[1] not in dic:
            dic[c[1]]=int(c[3])

        elif c[1] in dic:
            dic[c[1]] = dic[c[1]] + int(c[3])

    t= list(max(zip(dic.values(),dic.keys())))

    print(t[1],"spent the longest time, ",t[0],"seconds,on the phone during september 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
