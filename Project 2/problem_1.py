import collections

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.dict=collections.OrderedDict()

    def get(self,key):
        try:
            value=self.dict.pop(key)
            self.dict[key]=value
            return value
        except KeyError:
            return -1

    def set(self,key,value):
        try:
            self.dict.pop(key)
        except KeyError:
            if len(self.dict)>=self.capacity:
                self.dict.popitem(last=False)
        self.dict[key]=value

#Test case -1
our_cache = LRUCache(5)

print(our_cache.set(1, 1))
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(3))

print(our_cache.set(5, 5)) 
print(our_cache.set(6, 6))

print(our_cache.get(3))      # returns 3
    

#Test case-2

our_cache=LRUCache(4)
our_cache.set(1,"www.google.com")
our_cache.set(2,"wwww.facebook.com")
our_cache.set(3,"www.youtube.com")

print(our_cache.get(1))   #returns www.google.com
print(our_cache.get(2))   #wwww.facebook.com

our_cache.set(4,"www.twitter.com")
our_cache.set(5,"www.amazon.com")

print(our_cache.get(3)) #returns -1 because the cache reached its capacity and 3 was the recently used entry
print(our_cache.get(4))

#Test case-3

our_cache=LRUCache(3)
our_cache.set(1,9)
our_cache.set(2,10)

print(our_cache.get(1))  #return 9
print(our_cache.get(2))  #return 10

our_cache.set(3,30)
our_cache.set(4,40)

print(our_cache.get(1))  #returns -1 
print(our_cache.get(3))  #returns 30
