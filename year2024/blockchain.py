import time


class User:
    def __init__(self, username, birthdate, password, balance=0):
        self.username = username
        self.birthdate = birthdate  # Stored as a string "YYYY-MM-DD"
        self.password = password
        self.balance = balance

    def login(self, birthdate, password):
        if self.birthdate == birthdate and self.password == password:
            print("Login successful!")
            return True
        else:
            print("Login failed! Incorrect credentials.")
            return False

    def update_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


class Block:
    def __init__(self, index, transactions, previous_hash, miner, difficulty=1):
        self.index = index
        self.transactions = transactions  # Store user transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.miner = miner
        self.hash = self.calculate_hash()

    def simple_hash(self, data, mod=256):
        hash_value = 0
        for char in data:
            hash_value = (hash_value ^ ord(char)) * (hash_value << 5)
            hash_value = hash_value % mod
        return hash_value

    def calculate_hash(self):
        return format(self.simple_hash(str(self.index) + str(self.transactions) +
                                       str(self.previous_hash) + str(self.timestamp) +
                                       str(self.nonce) + self.miner), 'x')

    # Proof of work method
    def mine_block(self):
        target = "0" * self.difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Block mined by {self.miner}: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.users = {}
        self.miner_reward = 10  # Set a reward for mining a block

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", "Genesis", difficulty=1)

    def add_user(self, username, birthdate, password, balance=0):
        if username not in self.users:
            self.users[username] = User(username, birthdate, password, balance)
            print(f"User {username} created with balance {balance}")
        else:
            print("Username already exists.")

    def create_transaction(self, sender_username, receiver_username, amount, miner_username):
        sender = self.users.get(sender_username)
        receiver = self.users.get(receiver_username)
        miner = self.users.get(miner_username)

        if sender and receiver and miner:
            if sender.balance >= amount:
                sender.update_balance(-amount)
                receiver.update_balance(amount)
                miner.update_balance(self.miner_reward)
                transaction = {
                    'from': sender_username,
                    'to': receiver_username,
                    'amount': amount
                }
                self.add_block(transaction, miner_username)
            else:
                print(f"Transaction failed: {sender_username} has insufficient funds.")
        else:
            print("Transaction failed: One or more users do not exist.")

    def add_block(self, transaction, miner):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transaction, previous_block.hash, miner)
        new_block.mine_block()
        self.chain.append(new_block)
        print(f"Block added with transaction: {transaction}")

    def view_ledger(self):
        for block in self.chain:
            print(f"\nBlock {block.index}:")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Miner: {block.miner}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")

    # def mining(self):


# Example usage of login
blockchain = Blockchain()
blockchain.add_user("A", "1990-01-01", "apassword", 100)
blockchain.add_user("B", "1992-02-02", "bpassword", 50)
blockchain.add_user("C", "1985-05-05", "cpassword", 0)  # Miner

if blockchain.users["A"].login("1990-01-01", "apassword"):
    blockchain.create_transaction("A", "B", 20, "C")

blockchain.create_transaction("B", "B", 80, "B")

blockchain.view_ledger()

