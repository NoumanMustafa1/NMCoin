import hashlib

class NMCoin:
    def __init__(self, previous_blockhash, transaction_list):
        self.previous_blockhash = previous_blockhash
        self.transaction_list = transaction_list
        self.block_data = f"{previous_blockhash}:" + "-".join(transaction_list)
        self.blockhash = self.calculate_blockhash()
    
    def calculate_blockhash(self):
        return hashlib.sha256(self.block_data.encode()).hexdigest()

    def __str__(self):
        return f"{self.blockhash}:{self.block_data}"
    
    def block_size(self):
        return len(self.block_data)

t1 = "Ali gav Ahmed 2 NMCoin"
t2 = "Arsl gav Shumeila 24 NMCoin"
t3 = "Nouman gav Ali 22 NMCoin"
t4 = "Amina gav Shumeila 12 NMCoin"
t5 = "Salman gav Ahmed 3 NMCoin"
t6 = "Hamid gav Afaan 6 NMCoin"

NMCoin1 = NMCoin("initial Transaction", [t1,t2,t3])

print(NMCoin1.block_size())
print(NMCoin1.blockhash)
print(NMCoin1.previous_blockhash)


NMCoin2 = NMCoin(NMCoin1.blockhash, [t4,t6,t5])

print(NMCoin2.block_size())
print(NMCoin2.blockhash)
print(NMCoin2.previous_blockhash)

NMCoin3 = NMCoin(NMCoin1.blockhash, [t5,t4,t6])

print(NMCoin3.block_size())
print(NMCoin3.blockhash)
print(NMCoin3.previous_blockhash)

