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

    s=set()
    for c in calls:
        if c[0].startswith("(080)"):

            if c[1][0]=="(":
                s.add(c[1][:c[1].find(")")+1])

            elif c[1][0]=="7" or c[1][0]=="8" or c[1][0]=="9":
                s.add(c[1][:4])

            elif c[1].startswith("140"):
                s.add("140")

    print("The numbers called by people in Bangalore have codes:" + "\n" + "\n".join(sorted(list(s))))

    counter_for_allcalls=0
    counter_for_banglore=0
    for i in calls:
        if i[0].startswith("(080)"):
            counter_for_allcalls+=1
            if i[1].startswith("(080)"):
                counter_for_banglore+=1
    percentage = (counter_for_banglore/counter_for_allcalls)*100

    print(str("%.2f" % (percentage)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
