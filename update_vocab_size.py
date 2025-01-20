import pickle

meta_path = 'data/baili_char/meta.pkl'
with open(meta_path, 'rb') as f:
    meta = pickle.load(f)

print(f"Current vocab_size in meta.pkl: {len(meta['itos'])}")
print(f"Example itos: {list(meta['itos'].items())[:10]}")

# Expand the vocabulary to match 2503
for i in range(len(meta['itos']), 2503):
    meta['itos'][i] = f"<unk_{i}>"  # Add placeholder tokens
    meta['stoi'][f"<unk_{i}>"] = i

meta['vocab_size'] = 2503

# Save the updated meta.pkl
with open(meta_path, 'wb') as f:
    pickle.dump(meta, f)

print("Updated meta.pkl to vocab_size 2503.")

