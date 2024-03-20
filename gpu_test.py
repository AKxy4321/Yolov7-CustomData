import torch

if torch.cuda.is_available():
    print("CUDA devices are available.")
    print(f"Number of CUDA devices: {torch.cuda.device_count()}")
    print(f"Current CUDA device: {torch.cuda.current_device()}")
else:
    print("CUDA is not available. PyTorch will use CPU.")
