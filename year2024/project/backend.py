from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading
from multiprocessing import Manager
from blockchain import Blockchain

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Move the Manager and Blockchain creation inside the main block
if __name__ == '__main__':
    manager = Manager()
    blockchain = Blockchain(manager)

    def mine_blocks():
        while True:
            new_block = blockchain.mine_block()  # Mine a block
            # Emit the new block to the frontend
            socketio.emit('new_block', {
                'index': new_block.index,
                'transactions': new_block.transactions,
                'hash': new_block.hash,
                'previous_hash': new_block.previous_hash,
                'miner': new_block.miner,
                'timestamp': new_block.timestamp
            })
            time.sleep(5)  # Delay to simulate mining time

    # Start mining in a separate thread
    threading.Thread(target=mine_blocks, daemon=True).start()

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('connect')
    def handle_connect():
        print("Client connected")
        # Emit the entire chain, starting with the Genesis block
        for block in blockchain.chain:
            socketio.emit('new_block', {
                'index': block.index,
                'transactions': block.transactions,
                'hash': block.hash,
                'previous_hash': block.previous_hash,
                'miner': block.miner,
                'timestamp': block.timestamp
            })

    # Run the Flask-SocketIO app
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
