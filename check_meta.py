import pickle

# Load the meta.pkl file
meta_path = 'data/baili_char/meta.pkl'
with open(meta_path, 'rb') as f:
    meta = pickle.load(f)

itos = meta['itos']
stoi = meta['stoi']
print(f"Vocab size: {meta['vocab_size']}")
print(f"Example mapping (itos): {list(itos.items())[:10]}")

