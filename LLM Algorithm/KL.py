'''
    KL 散度
'''

import torch.nn.functional as F

def kl(p_logits, q_logits):
    log_p = F.log_softmax(p_logits, dim=-1)
    log_q = F.log_softmax(q_logits, dim=-1)

    p = log_p.exp()

    kl = p * (log_p - log_q)
    return kl.sum(dim=-1).mean()
