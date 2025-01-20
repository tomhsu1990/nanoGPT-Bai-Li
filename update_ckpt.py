import torch

# Load checkpoint
ckpt_path = 'out-baili-char/ckpt.pt'
checkpoint = torch.load(ckpt_path, map_location='cpu')

# Resize weights
old_vocab_size = 2503
new_vocab_size = 2331

# Truncate or pad embedding weights
checkpoint['model']['transformer.wte.weight'] = checkpoint['model']['transformer.wte.weight'][:new_vocab_size, :]
checkpoint['model']['lm_head.weight'] = checkpoint['model']['lm_head.weight'][:new_vocab_size, :]

# Update vocab_size in model_args
checkpoint['model_args']['vocab_size'] = new_vocab_size

# Save the modified checkpoint
torch.save(checkpoint, ckpt_path)
print(f"Checkpoint updated to vocab_size {new_vocab_size}.")

