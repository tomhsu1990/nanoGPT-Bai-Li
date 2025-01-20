import torch

# Load checkpoint
ckpt_path = 'out-baili-char/ckpt.pt'
checkpoint = torch.load(ckpt_path, map_location='cpu')

# Check model configuration
print(f"Model vocab_size in checkpoint: {checkpoint['model_args']['vocab_size']}")

