'''
    交叉熵
'''

import torch

def cross_entropy(logits, targets):
    # 计算 LogSoftmax
    log_probs = torch.softmax(logits, dim=-1)  # 归一化，变成概率值

    # 取出正确类别的 log 概率，gather 可理解为按照指定索引，从张量中取出对应位置的元素
    correct_log_probs = log_probs.gather(dim=-1, index=targets.unsqueeze(-1)).squeeze(-1)

    # 计算交叉熵并求平均
    loss = -correct_log_probs.mean()
    return loss
