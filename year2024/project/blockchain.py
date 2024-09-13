import time
import hashlib
import random
from multiprocessing import Process, Manager, Queue, Lock


class User:
    def __init__(self, username, birthdate, password, balance=0):
        self.username = username
        self.birthdate = birthdate  # Stored as a string "YYYY-MM-DD"
        self.password = password
        self.balance = balance

    def login(self, birthdate, password):
        if self.birthdate == birthdate and self.password == password:
            print(f"{self.username}: Login successful!")
            return True
        else:
            print(f"{self.username}: Login failed! Incorrect credentials.")
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

    def calculate_hash(self):
        block_data = (str(self.index) + str(self.transactions) +
                      str(self.previous_hash) + str(self.timestamp) +
                      str(self.nonce) + self.miner)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self):
        # Proof of Work
        target = "0" * self.difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined successfully by {self.miner}: {self.hash}")


class Blockchain:
    def __init__(self, manager):
        self.chain = manager.list([self.create_genesis_block()])
        self.users = manager.dict()
        self.miner_reward = 10  # Reward for mining a block
        self.lock = Lock()  # Lock for synchronizing block additions

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", "Genesis", difficulty=1)

    def add_user(self, username, birthdate, password, balance=0):
        with self.lock:
            if username not in self.users:
                self.users[username] = User(username, birthdate, password, balance)
                print(f"User {username} created with balance {balance}")
            else:
                print(f"Username {username} already exists.")

    def create_transaction(self, sender_username, receiver_username, amount, miner_username):
        with self.lock:
            sender = self.users.get(sender_username)
            receiver = self.users.get(receiver_username)
            miner = self.users.get(miner_username)

            if sender and receiver and miner:
                if sender.get_balance() >= amount:
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
        with self.lock:  # Ensure only one miner can add a block at a time
            previous_block = self.chain[-1]
            new_block = Block(len(self.chain), transaction, previous_block.hash, miner, difficulty=1)
            new_block.mine_block()  # Call mine_block from Block class to mine the block
            self.chain.append(new_block)
            print(f"Block added with transaction: {transaction}, mined by {miner}")

    def mine_block(self, miner_username="Miner"):
        # This method can also be used for mining without transactions
        with self.lock:
            previous_block = self.chain[-1]
            new_block = Block(len(self.chain), "No Transactions", previous_block.hash, miner_username, difficulty=1)
            new_block.mine_block()  # Mine the new block
            self.chain.append(new_block)
            print(f"Block mined and added by {miner_username} with hash: {new_block.hash}")
            return new_block  # Return the mined block for any further processing


def mining_simulation(blockchain, miner_username, stop_queue):
    try:
        while stop_queue.empty():  # Run until stop signal is sent
            sender = random.choice(list(blockchain.users.values()))
            receiver = random.choice([user for user in blockchain.users.values() if user != sender])

            if sender.get_balance() > 1:
                amount = random.randint(1, sender.get_balance())
                blockchain.create_transaction(sender.username, receiver.username, amount, miner_username)
            else:
                print(f"{sender.username} has insufficient balance for a transaction.")
            time.sleep(2)  # Simulate time taken between transactions
    except KeyboardInterrupt:
        print(f"Miner {miner_username} stopping mining due to KeyboardInterrupt.")


def main():
    manager = Manager()
    blockchain = Blockchain(manager)
    stop_queue = Queue()  # Queue to signal all processes to stop

    # Add users to the blockchain
    blockchain.add_user("A", "1990-01-01", "apassword", 100)
    blockchain.add_user("B", "1992-02-02", "bpassword", 50)
    blockchain.add_user("C", "1985-05-05", "cpassword", 0)  # Miner

    # Start miner processes
    miners = [
        Process(target=mining_simulation, args=(blockchain, "C", stop_queue)),
        Process(target=mining_simulation, args=(blockchain, "B", stop_queue)),
        Process(target=mining_simulation, args=(blockchain, "A", stop_queue))
    ]

    for miner in miners:
        miner.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping mining simulation...")
        stop_queue.put("STOP")  # Signal all miners to stop

        # Ensure all miners stop gracefully
        for miner in miners:
            miner.join(timeout=1)
            if miner.is_alive():
                miner.terminate()

    # Display the blockchain ledger after stopping
    blockchain.view_ledger()


if __name__ == "__main__":
    main()

# website showing simulation
# - visualization - table
# flask

# add more ledgers? -> ledger with multiple children
# pandas, numpy, flask

# presentation of code, splitting files
# porkbun.com domain
