"""
Prepare a dataset for character-level language modeling using Traditional Chinese characters.
The script maps characters to integers for encoding.
It saves train.bin, val.bin containing the IDs, and meta.pkl containing the encoder, decoder, and other related info.
"""
import os
import pickle
import numpy as np

# Use the provided input file (Traditional Chinese text)
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"Input file not found: {input_file_path}")

# Read the dataset
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = f.read()
print(f"Length of dataset in characters: {len(data):,}")

# Extract all unique characters
chars = sorted(list(set(data)))
vocab_size = len(chars)
print("All the unique characters:", ''.join(chars))
print(f"Vocab size: {vocab_size:,}")

# Create mappings from characters to integers and vice versa
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# Encoding and decoding functions
def encode(s):
    return [stoi[c] for c in s]  # Convert string to list of integers

def decode(l):
    return ''.join([itos[i] for i in l])  # Convert list of integers to string

# Split the dataset into training and validation sets (90% train, 10% val)
n = len(data)
train_data = data[:int(n * 0.9)]
val_data = data[int(n * 0.9):]

# Encode both splits into integers
train_ids = encode(train_data)
val_ids = encode(val_data)
print(f"Train has {len(train_ids):,} tokens")
print(f"Val has {len(val_ids):,} tokens")

# Export to binary files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# Save metadata for encoding/decoding later
meta = {
    'vocab_size': vocab_size,
    'itos': itos,
    'stoi': stoi,
}
with open(os.path.join(os.path.dirname(__file__), 'meta.pkl'), 'wb') as f:
    pickle.dump(meta, f)

print("Dataset preparation complete!")
