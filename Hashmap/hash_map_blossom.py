from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self,size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]


  def hash(self,key):
    encoded_key = key.encode()
    return sum(encoded_key)

  def compressor(self,hash_code):
    return hash_code % self.array_size

  def assign(self,key,value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
    list_at_array.insert(payload)


  def retrieve(self,key):
    array_index = self.compressor(self.hash(key))
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        return item[1]
    return None

blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assign(element[0],element[1])

print(blossom.retrieve('daisy'))