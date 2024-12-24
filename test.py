import torch

import example.cuda

in_t = torch.arange(10., dtype=torch.float32, device='cuda')
out_t = torch.empty_like(in_t)

example.cuda.double_arr(outarr=out_t, inarr=in_t)
print(out_t)
