import hashlib
import datetime as dt

class Block:
    def __init__(self,timestamp,data,previous_hash=0):
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.calc_hash(data)

    def calc_hash(self,data):
        sha=hashlib.sha256()
        hash_str = data.encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.previous_hash=0

    def append(self,timestamp,data):
        if self.head is None:
            block=Block(timestamp,data,self.previous_hash)
            self.head=Node(block)
            self.previous_hash=block.hash
            return

        node = self.head
        while node.next:
            node= node.next
        block=Block(timestamp,data,self.previous_hash)
        self.previous_hash=block.hash
        node.next=Node(block)

    def covert_list(self):
        lst=[]
        node=self.head
        while node:
            lst.append(node.value)
            node=node.next
        return lst

    def printing_block(self,lst):
        for i in lst:
            print("",i.timestamp,"\n",i.data,"\n",i.previous_hash,"\n",i.hash)
            print("-"*50)


lst=LinkedList()
lst.append(dt.datetime.now(),"1st Block")
lst.append(dt.datetime.now(),"2nd Block")
lst.append(dt.datetime.now(),"3rd Block")

lst.printing_block(lst.covert_list())

#output
"""
 2019-06-12 12:27:22.346207 
 1st Block 
 0 
 f1d11be4d08f4466280025d27f59e645750437ee2d3f75c43a0fe3ee283fdcc9
--------------------------------------------------
 2019-06-12 12:27:22.346241 
 2nd Block 
 f1d11be4d08f4466280025d27f59e645750437ee2d3f75c43a0fe3ee283fdcc9 
 89fb93d3c5ff3dc8d52513638ccd1cd4dc86c10da7b21f16dd52a9c0153a673a
--------------------------------------------------
 2019-06-12 12:27:22.346249 
 3rd Block 
 89fb93d3c5ff3dc8d52513638ccd1cd4dc86c10da7b21f16dd52a9c0153a673a 
 c35216c8e1abb431c8e9698005bc02236b952b35eec2f0eb314793000fe862e6
--------------------------------------------------
"""

        