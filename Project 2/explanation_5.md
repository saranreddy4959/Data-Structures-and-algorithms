So, for the Blockchain we will use the hashing and implementation of linked lists.
In this black chain we have blocks of data where each block comprises of timestamp,data,previous hash, and its present hash value.

Now we will get the data and store it in some variable and calculate the hash value for that data

Using linked lists, when the head is None it will take the head as data which we send first and assign the previous hash value to 0.Now,if we add a new block to the list what we will do assign the perilously calculated values of hash to the previous hash in this block and hash value will be the presently calculated hash value.So,this process goes on while adding to every new block.


Time Complexity: O(n) n is the number of blocks present in the linked list
Space Complexity:O(n) as we are creating a list and appending all the details required in to the list.So, n is the numbers of elements of the list or size of the list. 
