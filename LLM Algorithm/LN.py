'''
    层归一化
'''

import torch
import torch.nn as nn

class LayerNorm(nn.Module):
    def __init__(self, d_model, eps=1e-6):
        super().__init__()

        # 定义参数
        self.d_model = d_model
        self.eps = eps

        # 定义可学习参数 gamma(缩放) 和 beta(平移)
        self.gamma = nn.Parameter(torch.ones(d_model))  # 初始化为 1（不缩放）
        self.beta = nn.Parameter(torch.zeros(d_model))  # 初始化为 0（不平移）

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)  # 对 Tensor 最后一个维度求平均值，并保留这个维度
        var = x.var(dim=-1, keepdim=True, unbiased=False)  # unbiased 意为保持无偏估计
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        out = self.gamma * norm_x + self.beta
        return out
    