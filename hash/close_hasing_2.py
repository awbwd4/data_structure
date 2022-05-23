class HashTable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [[] for _ in range(tableSize)]
        if not self.hashTable[0]:
            print(self.hashTable[0])

    def getHashKey(self, key):
        hashkey = 0
        for c in key:
            hashkey += ord(c) - ord("a")
        hashkey %= self.tableSize
        return hashkey

    def add(self, key, value):
        hashkey = self.getHashKey(key)
        if not self.hashTable[hashkey]:  # 이 위치에 아무것도 없으면?!
            self.hashTable[hashkey] = [key, value]
            # 키와 데이터를 여기에 저장함.
            print(
                "add - hashkey ",
                hashkey,
                "위치에 key",
                key,
                "value ",
                value,
                "값이 저장되었습니다.",
            )
        else:
            if self.hashTable[hashkey][0] == key:
                # 첫번째 위치의 키 값이 동일하면 데이터 업데이트
                self.hashTable[hashkey][0] = value
            else:
                nextHash = (hashkey + 1) % self.tableSize
                while self.hashTable[nextHash]:
                    nextHash = (nextHash + 1) % self.tableSize
                    if nextHash == hashkey:
                        # 한바퀴 다 돌았으면 빈테이블이 없다는 뜻
                        print("빈테이블 없음")
                        return
                self.hashTable[nextHash] = [key, value]
            print("hashkey ", nextHash, "위치에 key", key, "value ", value, "값이 저장되었습니다.")

    def find(self, key):
        hashkey = self.getHashKey(key)
        if self.hashTable[hashkey][0] == key:
            return self.hashTable[hashkey][1]
        else:
            nexthash = (hashkey + 1) % self.tableSize
            while self.hashTable[nexthash][0] != key:
                nexthash = (nexthash + 1) % self.tableSize
                if nexthash == hashkey:
                    print("찾기 실패")
                    return
            return self.hashTable[nexthash][1]


h = HashTable(3)
myHashTable = HashTable(10)
myHashTable.add("abc", 10)
myHashTable.add("cba", 20)
myHashTable.add("abc", 30)

print("key 값 abc의 value는 ", myHashTable.find("abc"))
print("key 값 cba의 value는 ", myHashTable.find("cba"))
