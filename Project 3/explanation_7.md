In this we have to take the path and split the using '/' as separator and keep each word as a key. So, after the insertion into the trie we will lookup for the path if its found we have to display about handler and if it is not found we have to display not found handler as the path doesnt exit over here.

Time complexity:O(n) for the insertion into the trie and also the lookup
Space complexity: O(n*m) where is 'n' number of path components and 'm' is size of the words(which points to other tries)