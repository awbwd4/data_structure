class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


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
        if self.hash_table[hash_address].key is not None:
            if self.hash_table[hash_address].key == key:
                self.hash_table[hash_address] = value
                print("saveData[%d - %d]" % (key, value))
                return True
            # 해당 해쉬 주소에 데이터가 없을 경우
            else:
                curAddr = hash_address + 1  # 주소를 다음칸으로 하나 이동
                while self.hash_table[curAddr].key is not None:
                    # 다음주소의 키값이 동일한 경우
                    if self.hash_table[curAddr].key == key:
                        self.hash_table[curAddr].value = value
                        print("saveData[%d - %d]" % (key, value))
                        return True
                    else:
                        # 다음 주소에 데이터는 있으나 키 값이 다른 경우
                        curAddr += 1  # 반복문 내에서 이동
                        if curAddr >= self.size:  # 주소값이 테이블의 크기보다 더 커지면
                            print("saveData_No Data")
                            return False
                self.hash_table[curAddr] = Node(key, value)
                return True
        else:
            # 다음 주소의 값이 테이블의 크기보다는 작으나
            # 데이터가 존재하지 않은 경우(빈 슬롯인 경우)
            # 이 곳에 데이터를 저장한다.
            # print("saveData[%d - %d]" % (key, value))
            self.hash_table[hash_address] = Node(key, value)
            return True

    def searchData(self, key):
        hash_address = self.getAddress(key)

        # 해당 주소에 데이터가 있을 경우
        # 이 슬롯에 위치한 데이터가 내가 찾던 데이터가 맞는지 확인해야함.
        # 다른 경우 다른 주소로 가서 찾아야함.
        if self.hash_table[hash_address] is not None:
            if self.hash_table[hash_address].key == key:
                return self.hash_table[hash_address]
            else:
                curAddr = hash_address + 1
                # 해당 주소에 값은 존재하나 다른 key인 데이터인 경우
                # 주소를 옮겨가며 검색
                while self.hash_table[curAddr] is not None:
                    if self.hash_table[curAddr].key == key:
                        print("searchData_[%d]" % (key))
                        return self.hash_table[curAddr]
                    else:
                        curAddr += 1
                        if curAddr >= self.size:
                            print("searchData_No saved data!")
                            return None
                print("searchData_No saved data!")
                return None
                # 더 찾을 데이터가 없을 경우, 테이블 내에 테이터가 없는 것으로

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
h.saveData("hazel1", "0102202")
h.saveData("hazel2", "0102203")
h.saveData("hazel3", "0102204")
# result = h.searchData("hazel")
# print(result.value)
