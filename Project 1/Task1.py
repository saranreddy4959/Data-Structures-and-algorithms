"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    text1 = set()
    text2=set()
    for t in texts:
        text1.add(t[0])
        text2.add(t[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    call1 = set()
    call2=set()

    for c in calls:
        call1.add(c[0])
        call2.add(c[1])

    total_set = text1.union(text2).union(call1).union(call2)

    print("There are "+str(len(total_set))+" different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
