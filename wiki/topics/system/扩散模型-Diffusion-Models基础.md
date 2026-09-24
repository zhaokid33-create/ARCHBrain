# 扩散模型（Diffusion Models）基础理论

tags: [深度学习, AIGC, 扩散模型, DDPM, Stable Diffusion, LDM, GAN, VAE, U-Net]
updated: 2026-04-17
sources: [raw/links/【深度学习】扩散模型（Diffusion Models）基础理论.md]

## Summary
扩散模型（Diffusion Model）是2020年后图像生成领域的主流范式，基于马尔可夫链的前向加噪+反向去噪过程，Stable Diffusion 是其最广为人知的实现。

## 核心原理
- 基于马尔可夫性质：未来状态仅依赖当前状态
- 前向过程（Forward）：逐步向图像添加高斯噪声，直至变为纯噪声（可控，参数已知）
- 反向过程（Reverse）：训练神经网络逐步去噪，从纯噪声还原图像（生成过程）
- 训练目标：最大化数据的证据下界（ELBO），等价于学习去噪步骤

## 架构：U-Net
- 编码器（下采样）：卷积+池化，降低分辨率，提取语义信息
- 解码器（上采样）：转置卷积/插值，恢复分辨率
- 跳跃连接（Skip-connections）：保留空间细节，缓解梯度消失
- 时间步 t 通过正弦位置嵌入注入每个残差块

## 两种高分辨率扩展方案
- 级联扩散模型（Cascaded）：多个扩散模型串联，逐步提升分辨率；需强数据增强（高斯模糊）
- 潜在扩散模型（LDM）：先用 VAE 编码到低维潜在空间，在潜在空间做扩散，再解码回像素空间

## Stable Diffusion
- 基于 LDM 架构，Stability AI + CompVis 开发，2022年8月开源
- 关键设计：CLIP 文本编码器（text-to-image）、LAION 数据集训练、高效推理
- 组件：VAE编码器 → 潜在空间扩散（U-Net）→ VAE解码器

## 三大生成模型对比
| 模型 | 机制 | 特点 |
|------|------|------|
| GAN | 生成器vs判别器对抗 | 生成快，训练不稳定，模式崩塌风险 |
| VAE | 编码为分布，采样解码 | 训练稳定，生成略模糊 |
| Diffusion | 迭代去噪 | 质量高，推理慢，可控性强 |

## Links
- 
- 
