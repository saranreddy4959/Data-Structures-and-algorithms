In this problem we have to build a trie and if we give a prefix then we should get a all the remaining words in the suffix present in the trie. Basically what I  have done is taken a list and have created 26 elements which are by default none and also I have taken another child which is end of word.If the end of word is true or false so that it comes to know about the end of word.

While inserting first I am assigning an empty string as the root node and take the each character from the word and placing it at particular index.In the suffix function I will add all the word for  that into a list 

Time Complexity: O(n)
Space Complexity:O(n*m)