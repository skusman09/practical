import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        """Initialize the block with given parameters."""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """Compute the hash of the block by hashing its contents."""
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

class Blockchain:
    def __init__(self, difficulty=2):
        """Initialize the blockchain with an empty chain and set the mining difficulty."""
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain (genesis block)."""
        genesis_block = Block(0, str(datetime.datetime.now()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        """Return the last block in the blockchain."""
        return self.chain[-1]

    def add_new_block(self, data):
        """Add a new block to the blockchain."""
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=str(datetime.datetime.now()),
            data=data,
            previous_hash=last_block.hash,
        )
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block):
        """Mine the block by finding a valid hash (meeting the difficulty requirement)."""
        print(f"Mining block {block.index}...")
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        print(f"Block {block.index} mined with nonce {block.nonce}: {block.hash}")

    def is_chain_valid(self):
        """Check if the blockchain is valid by verifying the hashes and links."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def display_chain(self):
        """Print the entire blockchain."""
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)
    blockchain.add_new_block("Block 1 Data")
    blockchain.add_new_block("Block 2 Data")
    blockchain.add_new_block("Block 3 Data")
    blockchain.display_chain()
    print("Is blockchain valid?", blockchain.is_chain_valid())
