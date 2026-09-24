---
title: 【深度学习】扩散模型（Diffusion Models）基础理论
source: https://zhuanlan.zhihu.com/p/1977785927842682007
author:
published:
created: 2026-04-15
description: 学习计划本篇为【AIGC深入与应用】系列文章（1） —— 扩散模型（Diffusion Models）篇背景图像生成领域最常见生成模型有GAN和VAE，2020年， DDPM（Denoising Diffusion Probabilistic Model）被提出，被称为扩散…
tags:
  - clippings
---
目录

收起

学习计划

背景

原理介绍

前向过程

逆向过程

训练一个扩散模型

架构

级联扩散模型 Cascaded Diffusion Models

潜在扩散模型 Latent Diffusion Models

对比

GAN（Generative adversarial network）

VAE （Variational Auto Encoder）

Diffusion Models

其他任务领域用途

预测

附录

## 学习计划

> **本篇为【AIGC深入与应用】系列文章（1） —— 扩散模型（Diffusion Models）篇**

## 背景

图像生成领域最常见生成模型有GAN和VAE，2020年， **[DDPM](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=DDPM&zhida_source=entity) （Denoising Diffusion Probabilistic Model）** 被提出，被称为 **扩散模型（Diffusion Model）** ，同样可用于图像生成。近年扩散模型大热，在 OpenAI, Nvidia 和 Google 成功地训练了大规模的模型后，扩散模型已经吸引了很多人的注意。基于扩散模型的架构有 GLIDE, [DALLE-2](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=DALLE-2&zhida_source=entity), Imagen 和 完全开源的 [Stable Diffusion](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=Stable+Diffusion&zhida_source=entity) 。

## 原理介绍

**扩散模型的原理** 是基于数学中的 **马尔可夫** 性质，即当一个随机过程在给定现在状态和过去状态时，其未来状态的数据分布仅依赖于当前状态。 扩散模型中，通过将高斯噪声添加到初始图像中，在不断加噪的过程中将图片转换为纯噪音图像（类似雪花屏）。 **由于图像的参数是已知的，所以扩散模型前向加噪的过程是可控的** 。

> **扩散模型：** 和其他生成模型一样，实现从噪声（采样自简单的分布）生成目标数据样本。

扩散模型包括两个过程： **前向过程（forward process）** 和 **反向过程（reverse process）**

正向过程的基本思想是相当简单的。把输入图像 x0 并通过一系列的T步骤，逐渐向其添加高斯噪声。值得注意的是，正向过程与神经网络的正向传播无关，但是正向传播对于为我们的神经网络生成目标（应用 t<T 噪声步骤后的图像）是有必要的。

之后， **神经网络被训练** 为 **通过逆转噪声过程以恢复原始数据** 。通过对 **反向过程** 进行 **建模** ，我们可以生成新的数据。这就是所谓的反向扩散过程，或者说是生成式模型的采样过程。

无论是前向过程还是反向过程都是一个参数化的马尔可夫链（Markov chain），其中反向过程可用于生成数据样本（它的作用类似GAN中的生成器，只不过GAN生成器会有维度变化，而DDPM的反向过程没有维度变化）。

![](https://pica.zhimg.com/v2-fd0d57633a60eaeb46c9ba2beb2af2fa_1440w.jpg)

Forward diffusion process

从 x0 到 xT 为逐步加噪过的前向过程，噪声是已知的，该过程从原始图片逐步加噪至一组纯噪声。

![](https://pic1.zhimg.com/v2-457719e08a48d56934be4c4dc802312a_1440w.jpg)

Reverse diffusion process

从 xT 到 x0 为将一组随机噪声还原为输入的过程，是一个去噪过程，直到还原一张图片。

### 前向过程

![](https://picx.zhimg.com/v2-cb27955acdb30fb2291a4d232fbe6d89_1440w.jpg)

### 逆向过程

![](https://pica.zhimg.com/v2-01ef416e7de0715635dca305a28b74fc_1440w.jpg)

**用神经网络逼近反向过程**

![](https://picx.zhimg.com/v2-25eabcb5268ae8fb2dd0b88d30077147_1440w.jpg)

## 训练一个扩散模型

如果我们退一步讲，我们可以注意到， q 和 p 的组合与变分自编码器 (VAE) 非常相似。因此，我们可以通过优化训练数据的负对数似然来训练它。经过一系列的计算（我们在此不做分析），我们可以把证据下界 (ELBO) 写成如下：

![](https://pica.zhimg.com/v2-d8415fbec9c4e2d9619bf24fab39ef14_1440w.jpg)

很明显，通过 ELBO ，最大化的可能性可以归结为学习去噪步骤Lt 。具体细节不展开了，详见 [《扩散模型是如何工作的：从零开始的数学原理》](https://link.zhihu.com/?target=https%3A//shao.fun/blog/w/how-diffusion-models-work.html)

## 架构

到目前为止，我们还没有提到的一件事是模型的架构是什么样子的。请注意，模型的输入和输出应该是相同大小的。为此， Ho et al. 采用了一个 U-Net 。

![](https://pic1.zhimg.com/v2-f12717ad4aac7dfc848d9fedaee18b22_1440w.jpg)

U-Net网络结构

U-Net 是一种经典的编码器-解码器（Encoder-Decoder）结构：

- **编码器** （下采样路径）：通过卷积 + 池化逐步降低特征图的空间分辨率（宽高变小），但通道数增加，提取高层语义信息。
- **解码器** （上采样路径）：通过上采样（如转置卷积或插值）逐步恢复空间分辨率，同时减少通道数，重建精细的空间结构。

简而言之，U-Net 这是一种对称的架构，其输入和输出的空间大小相同，在相应特征维度的编码器和解码器块之间使用跳过连接（skip-connections） 。通常情况下，输入图像首先被降频，然后被升频，直到达到其初始尺寸。

**跳过连接** 就是在编码器的每一层（或某些层）将其输出的特征图 **直接“跳过”中间的网络层** ，与解码器中对应分辨率层级的特征图 **拼接** （concatenate）或相加。

![](https://picx.zhimg.com/v2-55d16caaca090a796579e8f3743759dd_1440w.jpg)

Skip-Connections图示

其作用，通常是为了更好保留空间细节信息，如避免编码器在下采样过程中会丢失精细的空间位置信息，或者缓解梯度消失问题（提供了从浅层到深层的“短路”路径，使梯度在反向传播时更容易流回浅层），有助于训练更深或更复杂的网络。

在 DDPMs 的原始实现中， U-Net 由宽 [ResNet](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=ResNet&zhida_source=entity) 块、 分组归一化（Group-Normalization）以及 自我注意（Self-Attention） 块组成。扩散时间段 t 是通过在每个残差块中加入一个正弦的位置嵌入（Positional-Embeddings）来指定的。

然而，将这些 U-Net 扩展到高分辨率的图像中，在计算上是非常昂贵的。为此研究人员研究了两种将扩散模型扩展到高分辨率的方法： **级联扩散模型** 和 **潜伏扩散模型** 。

### 级联扩散模型 Cascaded Diffusion Models

[Ho et al. 2021](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2106.15282) 引入了级联扩散模型，以努力产生高保真的图像。级联扩散模型包括一个由许多连续扩散模型组成的管道，生成分辨率越来越高的图像。每个模型通过连续地对图像进行上采样并增加更高分辨率的细节，生成一个比前一个质量更好的样本。为了生成一个图像，我们从每个扩散模型中依次取样。

![](https://pic3.zhimg.com/v2-bf6db50cbb0836f6a7b3c25976c96338_1440w.jpg)

Cascaded Diffusion Models

为了获得级联架构的良好效果，对每个超级分辨率模型的输入进行强有力的数据增强是至关重要的。为什么呢？因为它可以减轻之前级联模型的复合误差，以及由于训练-测试不匹配造成的误差。

研究发现，高斯模糊是实现高保真度的一个关键转变，他们把这种技术称为调节增强。

### 潜在扩散模型 Latent Diffusion Models

Latent Diffusion Model（LDM）是基于一个相当简单的想法：我们不是直接在高维输入上应用扩散过程，而是将输入投射到一个 **较小的潜在空间** （Latent Space），并在那里应用扩散。

更详细地说， [Rombach et al.](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2112.10752) 建议使用编码器网络将输入编码为潜在表示，即

![](https://pic1.zhimg.com/v2-5a684c11fd6c14d52b1d126b774559fe_1440w.jpg)

。这一决定背后的直觉是通过在低维空间处理输入来降低训练扩散模型的计算需求。之后，一个标准的扩散模型 (U-Net) 应用于生成新的数据，这些数据被一个解码器网络放大。

![](https://picx.zhimg.com/v2-b57eb8e1be4c22de78ecf3844d059b3d_1440w.jpg)

Latent Diffusion Models架构图示（直接以SD为例）

后来的广为人知的 **Stable Diffusion** （SD）就是由 Stability AI 联合 CompVis 等团队基于 LDM 架构开发的开源文生图模型（最初版本于 2022 年 8 月发布）。它使用了 LDM 的核心思想，并在大规模数据上训练得到。（LDM是架构/方法，而SD1.0、SDXL等是基于这个方法造出来的模型）

Stable Diffusion 在 LDM 基础上做了以下关键设计：

- **文本条件引导** ：引入 [CLIP](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=CLIP&zhida_source=entity) 文本编码器，实现 text-to-image 生成；
- **大规模训练** ：在 [LAION 数据集](https://zhida.zhihu.com/search?content_id=266973326&content_type=Article&match_order=1&q=LAION+%E6%95%B0%E6%8D%AE%E9%9B%86&zhida_source=entity) 上训练，支持开放域图像生成；
- **开源与优化** ：提供高效推理代码、支持多种分辨率、社区生态丰富。

## 对比

那么读到这里，想必你已经对扩散模型的整体框架有了一个大致的理解。我们再来对比一下GAN（生成对抗网络）、VAE（变分自编码器）和 Diffusion Models（扩散模型）是三种主流的 **生成式深度学习模型** ，在 **架构设计、训练方式、生成机制** 等方面的差异：

### GAN（Generative adversarial network）

通过 **生成器** （Generator）和 **判别器** （Discriminator）的对抗博弈，让生成器学会生成趋近训练数据集的逼真数据。GAN通常无编码器（除非是 BiGAN、ALI 等变体），而其中生成器的本质其实近似于解码器，用于将 **潜在空间** 的数据解码成图像数据。然后交给判别器（如最简单放一个二分类器）进行对抗训练。

![](https://pic4.zhimg.com/v2-79d3731406c0f7677dea074b08994a2b_1440w.jpg)

GAN的架构

```
# GAN代码示例
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
import matplotlib.pyplot as plt

# ----------------------------
# 超参数设置
# ----------------------------
batch_size = 128
image_size = 28 * 28  # MNIST 图像展平为 784 维向量
latent_dim = 100      # 噪声向量维度
hidden_dim = 256
lr = 0.0002
epochs = 50
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------------------
# 数据加载（MNIST）
# ----------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # 归一化到 [-1, 1]
])

dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# ----------------------------
# 生成器（Generator）
# ----------------------------
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(True),
            nn.Linear(hidden_dim, hidden_dim * 2),
            nn.ReLU(True),
            nn.Linear(hidden_dim * 2, image_size),
            nn.Tanh()  # 输出范围 [-1, 1]，与归一化图像匹配
        )

    def forward(self, z):
        return self.model(z)

# ----------------------------
# 判别器（Discriminator）
# ----------------------------
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(image_size, hidden_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x).view(-1)  # 输出标量概率

# ----------------------------
# 初始化模型、优化器、损失函数
# ----------------------------
G = Generator().to(device)
D = Discriminator().to(device)

criterion = nn.BCELoss()
optimizer_G = optim.Adam(G.parameters(), lr=lr, betas=(0.5, 0.999))
optimizer_D = optim.Adam(D.parameters(), lr=lr, betas=(0.5, 0.999))

# ----------------------------
# 训练循环
# ----------------------------
for epoch in range(epochs):
    progress_bar = tqdm(dataloader, desc=f"Epoch {epoch+1}/{epochs}")
    for i, (real_imgs, _) in enumerate(progress_bar):
        batch_size_now = real_imgs.size(0)
        real_imgs = real_imgs.view(batch_size_now, -1).to(device)

        # 真实标签和虚假标签
        real_labels = torch.ones(batch_size_now, device=device)
        fake_labels = torch.zeros(batch_size_now, device=device)

        # ---------------------
        # 训练判别器
        # ---------------------
        optimizer_D.zero_grad()

        # 真实图像损失
        real_loss = criterion(D(real_imgs), real_labels)

        # 生成假图像
        z = torch.randn(batch_size_now, latent_dim, device=device)
        fake_imgs = G(z)
        fake_loss = criterion(D(fake_imgs.detach()), fake_labels)

        d_loss = real_loss + fake_loss
        d_loss.backward()
        optimizer_D.step()

        # ---------------------
        # 训练生成器
        # ---------------------
        optimizer_G.zero_grad()
        g_loss = criterion(D(fake_imgs), real_labels)  # 欺骗判别器
        g_loss.backward()
        optimizer_G.step()

        progress_bar.set_postfix({"D Loss": d_loss.item(), "G Loss": g_loss.item()})

    # 每几个 epoch 保存一张生成图像示例
    if (epoch + 1) % 10 == 0:
        with torch.no_grad():
            z = torch.randn(16, latent_dim, device=device)
            fake_imgs = G(z).cpu().view(-1, 1, 28, 28)
            grid_img = torchvision.utils.make_grid(fake_imgs, nrow=4, normalize=True)
            plt.figure(figsize=(6, 6))
            plt.imshow(grid_img.permute(1, 2, 0))
            plt.axis('off')
            plt.title(f'Epoch {epoch+1}')
            plt.savefig(f'gan_epoch_{epoch+1}.png')
            plt.close()

print("训练完成！")
```

### VAE （Variational Auto Encoder）

基于 **概率图模型** ，将输入编码为潜在空间中的分布（通常是高斯分布），由编码器输出均值 μ 和方差 σ，再从中采样进行解码（解码器基于潜在变量 z 重建数据），目标是最大化数据的变分下界（ELBO）。

![](https://pic3.zhimg.com/v2-14e90430004165238234ed092b296da0_1440w.jpg)

VAE vs AE 结构对比

```
# VAE代码示例
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# 超参数设置
# ----------------------------
batch_size = 128
image_size = 28 * 28  # MNIST 图像展平为 784 维向量
hidden_dim = 400  # 隐层维度
latent_dim = 20  # 潜变量空间维度
lr = 0.001
epochs = 20
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------------------
# 数据加载（MNIST）
# ----------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # 归一化到 [-1, 1]
])

dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# ----------------------------
# 编码器（Encoder）
# ----------------------------
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc21 = nn.Linear(hidden_dim, latent_dim)  # mu
        self.fc22 = nn.Linear(hidden_dim, latent_dim)  # logvar

    def encode(self, x):
        h1 = F.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)  # 返回 mu 和 logvar

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        mu, logvar = self.encode(x.view(-1, image_size))
        z = self.reparameterize(mu, logvar)
        return z, mu, logvar

# ----------------------------
# 解码器（Decoder）
# ----------------------------
class Decoder(nn.Module):
    def __init__(self, latent_dim, hidden_dim, output_dim):
        super(Decoder, self).__init__()
        self.fc3 = nn.Linear(latent_dim, hidden_dim)
        self.fc4 = nn.Linear(hidden_dim, output_dim)

    def decode(self, z):
        h3 = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))  # 输出范围 [0, 1]

    def forward(self, z):
        return self.decode(z)

# 初始化模型、优化器
encoder = Encoder(image_size, hidden_dim, latent_dim).to(device)
decoder = Decoder(latent_dim, hidden_dim, image_size).to(device)
optimizer = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=lr)

# ----------------------------
# 损失函数：重构损失 + KL散度
# ----------------------------
def loss_function(recon_x, x, mu, logvar):
    BCE = F.binary_cross_entropy(recon_x, x.view(-1, image_size), reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + KLD

# ----------------------------
# 训练循环
# ----------------------------
for epoch in range(epochs):
    encoder.train()
    decoder.train()
    total_loss = 0
    for batch_idx, (data, _) in enumerate(tqdm(dataloader)):
        data = data.to(device)
        optimizer.zero_grad()

        z, mu, logvar = encoder(data)
        recon_batch = decoder(z)

        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        total_loss += loss.item()
        optimizer.step()

    print(f'Epoch {epoch + 1}, Loss: {total_loss / len(dataloader.dataset):.4f}')

    # 每个epoch结束后可视化生成结果
    with torch.no_grad():
        sample = torch.randn(16, latent_dim).to(device)
        sample = decoder(sample).cpu()
        grid_img = torchvision.utils.make_grid(sample.view(16, 1, 28, 28), nrow=4, normalize=True)
        plt.figure(figsize=(6, 6))
        plt.imshow(grid_img.permute(1, 2, 0))
        plt.axis('off')
        plt.show()

print("训练完成！")
```

### Diffusion Models

而本篇描述的扩散模型，则是模拟物理中的扩散过程：先逐步向数据加噪（前向过程），再训练神经网络逐步去噪（反向过程），最终从纯噪声生成数据。

![](https://pica.zhimg.com/v2-c6a0d37f6d906ceb0997191f6099e944_1440w.jpg)

本质上无传统编码器（但衍生的 LDM 中用 VAE 编码到潜在空间），而 Stable Diffusion 属于 **Latent Diffusion Model (LDM)** 模型的一种，它结合了 VAE 和 Diffusion，用 VAE的编码器将图像编码到潜在空间，再在潜在空间做扩散（去噪网络采取了U-Net），然后通过VAE的解码器将最终去噪完成的干净潜在表示 *z* 还原为像素空间的图像 。

```
# LDM简化版实现代码示例，主要有以下核心组成部分：
# 1. VAE的编码器：将像素图像 x 压缩到潜在空间 z
# 2. DDPM + U-Net：用于训练潜在空间中的扩散与反向去噪过程
# 3. VAE的解码器：从潜在表示 z 重建像素图像，最终输出生成图像

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from diffusers import AutoencoderKL, DDPMScheduler, UNet2DModel
from tqdm import tqdm

# ----------------------------
# 超参数设置
# ----------------------------
batch_size = 8
image_size = 32
latent_size = 4  # 32/8 = 4
num_epochs = 10
learning_rate = 1e-4
device = "cuda" if torch.cuda.is_available() else "cpu"

# ----------------------------
# 数据加载（CIFAR-10）
# ----------------------------
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # [-1, 1]
])

dataset = datasets.CIFAR10(root="./data", train=True, download=True, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# ----------------------------
# 加载组件（来自 Hugging Face）
# 我们将使用 Hugging Face 的 diffusers 库来加载官方 VAE 编码器
# ----------------------------

# Stable Diffusion 还加入了 CLIP 文本编码器 以支持文本和图像之间的编码转化 
vae = AutoencoderKL.from_pretrained("stability-ai/sd-vae-ft-ema").to(device)
vae.requires_grad_(False)  # 冻结 VAE（VAE 和 CLIP 通常不训练，仅训练 U-Net。）
vae.eval()

unet = UNet2DModel.from_pretrained("google/ddpm-cifar10-32").to(device)
optimizer = optim.AdamW(unet.parameters(), lr=learning_rate)

scheduler = DDPMScheduler(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="scaled_linear")

# ----------------------------
# 训练循环
# ----------------------------
for epoch in range(num_epochs):
    unet.train()
    total_loss = 0
    for i, (images, _) in enumerate(tqdm(dataloader)):
        images = images.to(device)

        # Step 1: VAE 编码图像到潜在空间
        with torch.no_grad():
            latents = vae.encode(images).latent_dist.sample()
            latents = latents * vae.config.scaling_factor  # 缩放

        # Step 2: 添加噪声（正向扩散）
        noise = torch.randn_like(latents).to(device)
        timesteps = torch.randint(0, scheduler.num_train_timesteps, (latents.shape[0],), device=device).long()
        noisy_latents = scheduler.add_noise(latents, noise, timesteps)

        # Step 3: U-Net 预测噪声（无条件）
        noise_pred = unet(noisy_latents, timesteps).sample

        # Step 4: 计算损失
        loss = nn.functional.mse_loss(noise_pred, noise)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.6f}")

print("✅ LDM 训练完成！")
```
![](https://picx.zhimg.com/v2-da986a2732021229a538a1cf297fc72b_1440w.jpg)

一张表AI总结一下

- **GAN** ：仍在特定领域（如实时生成、3D 生成）有优势，但通用图像生成已被 Diffusion 超越。
- **VAE** ：很少单独用于高质量生成，但作为 **表示学习工具** 或 **Diffusion 的前置模块** （如 LDM）仍非常重要。
- **Diffusion Models** ：当前生成 AI 的 **主流架构** ，需要较高的算力，目前正配合加速技术（如 DDIM、蒸馏、LCM）以解决速度问题。

## 其他任务领域用途

### 预测

[《Diffusion Models for Time Series Forecasting: A Survey》](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2507.14507)

本文是一篇综述性论文，系统地回顾了扩散模型（Diffusion Models）在时间序列预测（TSF）任务中的应用。论文首先介绍了标准扩散模型及其变体，如Denoising Diffusion Probabilistic Model（DDPM）和Denoising Diffusion Implicit Model（DDIM），并解释了它们如何被适配到TSF任务中。接着，作者提出了一个系统分类法，将现有方法按照条件来源（如历史时间序列或多模态数据）和条件整合机制（如特征中心整合和扩散中心整合）进行分类。

![](https://pic4.zhimg.com/v2-840679f38964be7ba95017941f53ec07_1440w.jpg)

与传统的预测方法相比，基于扩散模型的时间序列预测具有以下优点：

1. 能够捕捉到长期依赖关系，适用于需要考虑较长时间范围内的趋势或周期性的预测任务；
2. 具有较强的泛化能力，能够适应多种不同类型的时间序列数据；
3. 可以根据具体应用场景自定义条件，提高预测精度。

## 附录

- 《Denoising Diffusion Probabilistic Models 推导解读 》 [Denoising Diffusion Probabilistic Models 推导解读](https://zhuanlan.zhihu.com/p/1964643605391061692)
- 《Diffusion Models for Time Series Forecasting: A Survey》 [Diffusion Models for Time Series Forecasting: A Survey](https://link.zhihu.com/?target=https%3A//www.modelscope.cn/papers/2507.14507)
- 《扩散模型是如何工作的：从零开始的数学原理》 [shao.fun/blog/w/how-dif](https://link.zhihu.com/?target=https%3A//shao.fun/blog/w/how-diffusion-models-work.html)
- 《HuggingFace Learn - Annotated Diffusion》 [huggingface.co/blog/ann](https://link.zhihu.com/?target=https%3A//huggingface.co/blog/annotated-diffusion)

**声明：**

- 所有文章都为本人的学习笔记，非商用，
- 目的只求在工作学习过程中通过记录，梳理清楚自己的知识体系。
- 文章或涉及多方引用，如有纰漏忘记列举，请多指正与包涵。

还没有人送礼物，鼓励一下作者吧

编辑于 2025-12-16 10:23・浙江[深度学习（Deep Learning）](https://www.zhihu.com/topic/19813032)[AIGC](https://www.zhihu.com/topic/26215901)[扩散模型](https://www.zhihu.com/topic/25763577)[程序员0基础入门大模型的学习路线！](https://zhuanlan.zhihu.com/p/31864213680)

[

0基础入门大模型，transformer、bert这些是要学的，但是 你的第一口不一定从这里咬下去。真的没有必要一上来就把时间精力全部投入到复杂的理论、各种晦涩的数学公式还有编程语言上，这...

](https://zhuanlan.zhihu.com/p/31864213680)