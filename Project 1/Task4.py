"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    telephone_marketing= set()

    for c in calls:
        telephone_marketing.add(c[0])


    for c in calls:
        if c[1] in telephone_marketing:
            telephone_marketing.remove(c[1])


    for t in texts:
        if t[0] in telephone_marketing:
            telephone_marketing.remove(t[0])

        elif t[1] in telephone_marketing:
            telephone_marketing.remove(t[1])


    print("These numbers could be telemarketers: \n" + "\n".join(sorted(list(telephone_marketing))))



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
