from email.utils import getaddresses


class HashTable:
    size = 0
    key = 0
    hash_table = []

    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [None for _ in range(self.size)]

    def getKey(self, data):
        self.key = ord(data[0])
        # ord() 받은 문자의 유니코드 정수를 반환한다.
        return self.key

    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value

    def read(self, key):
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] is not None:
            return self.hash_table[hash_address]
        else:
            print("No saved data!")

    def delete(self, key):
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] is not None:
            self.hash_table[hash_address] = None
            return True
        else:
            return False


hTable = HashTable(3)

print(hTable.hash_table)
print(hTable.getAddress("Dave"))
hTable.save("Dave", "00112233")
hTable.save("David", "00112234")
hTable.save("Daniel", "00112235")
hTable.save("Dan", "00112236")
hTable.save("Dial", "00112237")


print(hTable.read("Dave"))
