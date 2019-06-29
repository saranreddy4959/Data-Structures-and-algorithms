In the class LRU cache I used a collections ordered dictionary which are like regular dictionaries but they remember the order that items were inserted.
orderedDict.popitem(last=False): In this method it removes a key,value pair in the FIFO order

In the get method I am first removing the key to get that value and again inserting the same key value into the dictionary so that it changes the insertion order as FIFO and finally returns the value if a particular key is not present it returns -1

In the set method we are inserting new key value pairs and if the capacity is equal to the length of the dictionary then it removes the recently used in FIFO order.


Time complexity:O(1)
Space Complexity:O(n) as we are creating the size of cache so n depends on the given size of cache 