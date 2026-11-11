'''
    多头注意力 MHA
'''

import torch
import torch.nn as nn
import math

class MHA(nn.Module):
    def __init__(self, d_model, heads, d_k):
        super().__init__()  # 调用父类的构造函数（初始化方法）
        
        # assert d_model == heads * d_k

        # 定义参数
        self.d_model = d_model
        self.heads = heads
        self.d_k = d_k

        # 定义 QKV 映射矩阵
        self.q_linear = nn.Linear(d_model, d_model, bias=False)
        self.k_linear = nn.Linear(d_model, d_model, bias=False)
        self.v_linear = nn.Linear(d_model, d_model, bias=False)
        
        # 聚合头
        self.linear = nn.Linear(d_model, d_model, bias=False)

    def forward(self, q, k, v, mask=None):
        batch = q.shape[0]
        q_len = q.shape[1]
        k_len = k.shape[1]  # 标准 MHA 中 k_len == v_len

        # 定义 QKV (batch, len, d_model) -> (batch, len, heads, d_k)
        # -> (batch, heads, len, d_k)
        q = self.q_linear(q).reshape(batch, q_len, self.heads, self.d_k).transpose(1, 2)
        k = self.k_linear(k).reshape(batch, k_len, self.heads, self.d_k).transpose(1, 2)
        v = self.v_linear(v).reshape(batch, k_len, self.heads, self.d_k).transpose(1, 2)

        # 计算注意力
        att = torch.matmul(q, k.transpose(-1, -2)) / math.sqrt(self.d_k)
        if mask is not None:
            att = att.masked_fill(mask==0, -1e9)
        att = att.softmax(dim=-1)  # 注意力矩阵最后一维是 Key 序列维度，每个 Query 对所有 Key 的权重需要归一化
        out = torch.matmul(att, v)

        # 整合
        out = out.transpose(1, 2).reshape(batch, q_len, self.d_model)
        out = self.linear(out)
        
        return out
