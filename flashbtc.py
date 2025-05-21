import hashlib
from ecdsa import SigningKey, SECP256k1
from bit import PrivateKeyTestnet

# Set your wallet address and private key
wallet_address = 'bc1qdxcvngmm64qnhl3veu0su95p9xxvf7e2kez38e'
private_key = '19ffde1531f0849063e1fb4155ab95a3d57f128414c78c9d5897b99c135226cf'

# Convert private key to a usable format
private_key_hex = bytes.fromhex(private_key)
key = SigningKey.from_string(private_key_hex, curve=SECP256k1)

# Create a testnet transaction
txid = hashlib.sha256(b'bc1qdxcvngmm64qnhl3veu0su95p9xxvf7e2kez38e').hexdigest()
tx = PrivateKeyTestnet(txid)
tx.get_unspent()

# Set the amount and output address
amount = 100
output_address = 'bc1qw508d6qejxtdg4y5r3zarvaryyn94xw4ks4ez6'

# Create a transaction
tx.send(output_address, amount)

# Sign the transaction
tx_signatures = []
for x in tx.unspent:
    tx_signatures.append(key.sign(x.script_sig))

    # Broadcast the transaction
    tx.broadcast()
    