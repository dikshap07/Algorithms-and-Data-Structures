"""Hahmap with collision handling"""


class Bucket():

    def __init__(self):

        self.bucket = []

    def get(self,key):

        for (k,v) in self.bucket:

            if k == key:
                return v

        return -1

    def update(self,key,value):

        key_found = False

        for i,kv in enumerate(self.bucket):
            if key == kv[0]:

                self.bucket[i] = (key,value)
                key_found = True

                break

        if not key_found:
            self.bucket.append((key,value))

    def remove(self,key):

        for i,kv in enumerate(self.bucket):

            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):

        self.key_space = 2069
        self.hashmap = [Bucket() for i in range(self.key_space)]
        
    def put(self, key: int, value: int) -> None:
        key_found = False
        # print(f" Updat key : {key} value to {value}")
        hash_key = key %self.key_space
        self.hashmap[hash_key].update(key,value)

    def get(self, key: int) -> int:

        hash_key = key % self.key_space
        return self.hashmap[hash_key].get(key)

    
    def remove(self, key: int) -> None:

        hash_key = key % self.key_space
        self.hashmap[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



"""hashmap implementatin without taking care of collisions"""
class MyHashMap:

    def __init__(self):
        self.hashmap = []
        
    def put(self, key: int, value: int) -> None:
        key_found = False
        # print(f" Updat key : {key} value to {value}")
        for index,(curr_key,curr_value) in enumerate(self.hashmap):

            if key == curr_key:

                key_found = True
                self.hashmap[index][1] = value
                # print(f"New hashmap : {self.hashmap}")
                
                break

        if not key_found:

            self.hashmap.append([key,value])
        

    def get(self, key: int) -> int:
        key_found = False
        for curr_key,curr_value in self.hashmap:
            # print(f"curr_key = {curr_key},curr_value : {curr_value}")
            # print(f"hash = {self.hashmap}")
            # print(f"Key to find : {key}")

            if key == curr_key:

                key_found = True
                # print(f"in get: get({key}: {curr_value})")
                return curr_value


        if not key_found:

            return -1


    
    def remove(self, key: int) -> None:

        key_found = False
        for index,(curr_key,curr_value) in enumerate(self.hashmap):


            if key == curr_key:

                key_found = True
                index_to_remove = index
                break

        if key_found:

            self.hashmap.pop(index_to_remove)

        else:
            return