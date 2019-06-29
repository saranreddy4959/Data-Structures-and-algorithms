In this first we will make dictionary in make dictionary function we well pass a string to it in that for each character it checks the frequency for the letter and store it in a dictionary using key, value pair

In the build code method basically what I am doing first we send the dictionary and converting it a list of tuples where each tuple has char and its frequency (ch, freq). We are extracting the two minimum tuples using extract _min function to iterate it and get the minimum count  and we are combining it and again we are adding it to tuple and removing the previous used two minimum tuples. At the end we will be getting list representing the tree structure

In the generate code method we are assigning the empty string to root after that using recursion assigning 0 for left subtree and 1 for right subtree returns a dictionary with key being char and its binary value where it is placed in the tree

In the next we compress the string we go over the one character at a time and for each character we will get the value in dictionary

For the decompression we use starting at the root and read one bit at a time.For 0 we go to the left subtree and for 1 we go to the right subtree so when a leaf is reached we append the letter of the leaf and come back to the root.

Time Complexity: O(n) because we are doing encoding and decoding by iterating the elements in the dictionary 
Space Complexity: O(n) where n is the number of elements in the dictionary
