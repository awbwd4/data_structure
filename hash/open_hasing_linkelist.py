class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    size = 0
    key = ""
    hash_table = []

    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [Node(None, None) for _ in range(self.size)]
        # key, value, next

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

    def saveData(self, key, value):
        hash_address = self.getAddress(key)
        # 해당 해쉬 주소에 데이터가 있을 경우
        if self.hash_table[hash_address] is not None:
            cur = self.hash_table[hash_address]
            prev = self.hash_table[hash_address]
            while cur is not None:
                if cur.key == key:
                    cur.value = value
                    # 기존의 키에 대핟하는 데이터 업데이트
                    return True
                else:
                    prev = cur
                    cur = cur.next
            # 해당 해쉬 주소에 해당하는 링크드 리스트 내에 검색한 key값이 없는 경우
            # 새로 생성해줌.
            prev.next = Node(key, value)
        # 해당 해쉬 주소에 데이터가 없을 경우
        else:
            self.hash_table[hash_address] = Node(key, value)

    def searchData(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] is not None:
            cur = self.hash_table[hash_address]
            while cur is not None:
                if cur.key == key:
                    return cur
                else:
                    cur = cur.next
            return None
        else:
            print("No saved data!")
            return None

    def delete(self, key):
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] is not None:
            self.hash_table[hash_address] = None
            return True
        else:
            return False


h = HashTable(3)
print(h.hash_table)
h.saveData("hazel", "0102201")
result = h.searchData("hazel")
print(result.value)
