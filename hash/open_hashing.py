# opne hasing, 이중 리스트로 해결


class OpenHash:
    size = 0
    key = 0
    hash_table = []

    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [None for _ in range(self.size)]
        print(type(self.hash_table[0]))

    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)
        print(key)
        print(value)
        print(hash_address)
        print(type(self.hash_table[hash_address]))
        print(self.hash_table[hash_address])

        # 해당 주소에 데이터가 존재하는 경우
        if self.hash_table[hash_address] is not None:
            print("==", type(self.hash_table[hash_address]))
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    # 덮어씌우기. 해당 key가 이미 존재할 경우에는 여기로 들어간다.
                    self.hash_table[hash_address][a][1] = value
                    return
            # 이중 리스트 구현
            self.hash_table[hash_address].append([key, value])
        # 해당 주소에 데이터가 존재하지 않는 경우
        else:
            # 여기에서 이중리스트를 최초에 구현해줌. 값을 넣을때는 반드시 이중리스트로 넣는다.
            self.hash_table[hash_address] = [[key, value]]
            print(self.hash_table[hash_address])

    def delete(self, key):
        hash_address = self.getAddress(key)

        # 해당 주소에 데이터가 존재할 경우
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    # 해당 주소값에 위치한 이중 리스트의 길이가 1 즉, 데이터가 하나만 있을 경우
                    if len(self.hash_table[hash_address] == 1):
                        self.hash_table[hash_address] = 0
                    # 데이터가 여러개일 경우
                    else:
                        del self.hash_table[hash_address][a]
                        # 해당 주소의 이중 리스트를 통째로 날린다.
                    return
            return False
        # 해당 주소에 데이터가 존재하지 않을 경우
        else:
            return False

    def read(self, key):
        hash_address = self.getAddress(key)

        # 해당 주소에 데이터가 존재할 경우
        if self.hash_table[hash_address] is not None:
            for i in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][i][0] == key:
                    return self.hash_table[hash_address][i][1]
        # 해당 주소에 데이터가 존재하지 않을 경우
        else:
            print("no data")
            return


h_table = OpenHash(10)

print(h_table.hash_table)

print("key : ", h_table.getKey("Hazel"))
print("address : ", h_table.getAddress("Hazel"))
print("key : ", h_table.getKey("Hidden"))
print("address : ", h_table.getAddress("Hidden"))
print("key : ", h_table.getKey("Hineken"))
print("address : ", h_table.getAddress("Hineken"))
h_table.save("Hazel", "010201")
h_table.save("Hidden", "010202")
h_table.save("Hineken", "010203")


print(h_table.hash_table)

print(h_table.read("Hazel"))
