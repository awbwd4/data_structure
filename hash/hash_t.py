class hashTable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [[] for _ in range(tableSize)]

    def getHashKey(self, key):
        hashkey = 0
        for c in key:
            hashkey += ord(c) - ord("a")
        hashkey %= self.tableSize
        return hashkey

    def add(self, key, value):
        hashkey = self.getHashKey(key)
        if not self.hashTable[hashkey]:
            self.hashTable[hashkey] = [key, value]
            print("hashkey ", hashkey, "위치에 key", key, "value ", value, "값이 저장되었습니다.")
        else:
            nextHash = (hashkey + 1) % self.tableSize
            while self.hashTable[nextHash]:
                nextHash = (nextHash + 1) % self.tableSize
                if nextHash == hashkey:  # 한바퀴 돌았으면 빈테이블이 없다는 뜻
                    print("빈 테이블을 찾는데 실패하였습니다.")
                    return
            self.hashTable[nextHash] = [key, value]
            print("hashkey ", nextHash, "위치에 key", key, "value ", value, "값이 저장되었습니다.")

    def find(self, key):
        hashkey = self.getHashKey(key)
        if self.hashTable[hashkey][0] == key:
            return self.hashTable[hashkey][1]
        else:
            nextHash = (hashkey + 1) % self.tableSize
            while self.hashTable[nextHash][0] != key:
                nextHash = (nextHash + 1) % self.tableSize
                if nextHash == hashkey:  # 한바퀴 돌았으면 빈테이블이 없다는 뜻
                    print("찾기 실패")
                    return
            return self.hashTable[nextHash][1]


myHashTable = hashTable(10)
myHashTable.add("abc", 10)
myHashTable.add("cba", 20)
print("key 값 abc의 value는 ", myHashTable.find("abc"))
print("key 값 cba의 value는 ", myHashTable.find("cba"))
