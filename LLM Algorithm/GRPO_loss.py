'''
    GRPO 损失函数
'''

import torch
import torch.nn.functional as F

def compute_grpo_loss(
    logits,          # [B*G, S, V]
    ref_logps,       # [B*G, S]
    old_logps,       # [B*G, S]
    actions,         # [B*G, S]
    rewards,         # [B*G]
    attention_mask,  # [B*G, S]
    group_size,
    beta=0.1,
    eps=0.2,
):

    # 1. 提取实际生成 Token 的 log probability
    logps = torch.gather(
        F.log_softmax(logits, dim=-1),
        dim=2,
        index=actions.long().unsqueeze(2)
    ).squeeze(2)

    # 2. 计算组内 Advantage
    bs = logits.shape[0] // group_size
    rewards = rewards.detach().reshape(bs, group_size)

    mean_r = rewards.mean(dim=-1, keepdim=True)
    var_r = rewards.var(dim=-1, keepdim=True, unbiased=False)

    adv = (rewards - mean_r) / torch.sqrt(var_r + 1e-8)
    adv = adv.reshape(-1).unsqueeze(1)

    # 3. 计算新旧策略概率比值
    ratio = torch.exp(logps - old_logps.detach())

    # 4. PPO Clip Loss
    coef_1 = adv * ratio
    coef_2 = adv * torch.clamp(ratio, 1 - eps, 1 + eps)

    per_token_loss = -torch.minimum(coef_1, coef_2)

    # 5. KL Loss
    kl_diff = ref_logps.detach() - logps
    kl_loss = torch.exp(kl_diff) - kl_diff - 1

    # 6. 合并
    total_loss = per_token_loss + beta * kl_loss

    # 7. Mask + 平均
    mask = attention_mask.to(total_loss.dtype)

    active_loss = total_loss * mask
    final_loss = active_loss.sum() / mask.sum().clamp_min(1)

    return final_loss
