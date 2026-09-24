---
title: Grasshopper模拟羊毛及建筑学应用
source: https://zhuanlan.zhihu.com/p/72094932
author:
published:
created: 2026-04-15
description: 弗雷奥托在1988年进行了“羊毛实验”：将松弛交错的羊毛浸入水中并缓慢取出，可以得到给定点的最短路径。 2006年，扎哈使用Maya的毛发动力学模拟，建立了最短路径网，并应用在位于伊斯坦布尔的Kartal-Pendik总平面…
tags:
  - clippings
---
[弗雷奥托](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=%E5%BC%97%E9%9B%B7%E5%A5%A5%E6%89%98&zhida_source=entity) 在1988年进行了“ [羊毛实验](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=%E7%BE%8A%E6%AF%9B%E5%AE%9E%E9%AA%8C&zhida_source=entity) ”：将松弛交错的羊毛浸入水中并缓慢取出，可以得到给定点的最短路径。

![](https://pica.zhimg.com/v2-23940002a89a58902114646c97eef0fe_1440w.jpg)

图源：http://www.patrikschumacher.com/Texts/Parametricism%20-%20A%20New%20Global%20Style%20for%20Architecture%20and%20Urban%20Design.html

2006年，扎哈使用 [Maya](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=Maya&zhida_source=entity) 的 [毛发动力学模拟](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=%E6%AF%9B%E5%8F%91%E5%8A%A8%E5%8A%9B%E5%AD%A6%E6%A8%A1%E6%8B%9F&zhida_source=entity) ，建立了最短路径网，并应用在位于伊斯坦布尔的 [Kartal-Pendik总平面](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=Kartal-Pendik%E6%80%BB%E5%B9%B3%E9%9D%A2&zhida_source=entity) 中。

![](https://picx.zhimg.com/v2-9724101e0b0d7febef3abfa678b7d753_1440w.jpg)

![](https://pic2.zhimg.com/v2-5263ac5c2f9443df258df1ec8d5f3b53_1440w.jpg)

借助插件 [kangaroo](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=kangaroo&zhida_source=entity) ，我们也可以用 [grasshopper](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=grasshopper&zhida_source=entity) 模拟这个过程。其电池图如下

![](https://pic1.zhimg.com/v2-8af96c05fd9a1bb78eee0a2ad2c962ca_1440w.jpg)

要完成这个实验，需要满足几个要求：

1.曲线的端点是确定且不可移动的——否则所有曲线会聚集到一点。

2.需要人为建立初始曲线——模拟羊毛本质上是迭代，可以看作是优化，当然需要初始条件

3.初始曲线必须互相靠近或相交——只有这样，仅在微小尺度下生效的吸引力 才能对物件发挥作用。

4.曲线可以弯曲，移动，但 **很难** 伸缩和折叠——充分模拟羊毛特性，使得实验结果尽量不失真。

**正式开始**

1.在grasshopper里画圆，取等分点，打乱这些点的顺序，两两一组建立树形数据：

![](https://pic2.zhimg.com/v2-c1fde750ecf795fbc7c61b6e0e400529_1440w.jpg)

2.在圆内随机生成点，使用内插点曲线依次连接圆上点1、随机点、圆上点2

![](https://pic2.zhimg.com/v2-d83a06520ea62c9f8c87e8a2ec804129_1440w.jpg)

![](https://pica.zhimg.com/v2-b05496f67a7fdb164e82da0b0f218844_1440w.jpg)

3.使用kangaroo，建立一个模拟系统：

为了对接kangaroo的运算器，需要将曲线转化为1阶多段线

![](https://pic3.zhimg.com/v2-22cc54efe80533ea3db453a093ec01e8_1440w.jpg)

从上到下，群组的作用分别是：

显示迭代后的多段线；

施加锚固的力，以固定多段线的起点和终点；

在每条多段线的端点处施加一个相互吸引的力。利用数学关系，使它的作用范围稍大于多段线子线段的平均长度——如果该范围过大，同一根多段线的各顶点间也会相互吸引，导致线条扭曲、抖动和坍缩；过小，则不会显现相互吸引的效果。

给每条线施加一个很大的弹力，使其很难伸缩

给每根多段线的 两两相邻的子线段 一个阻止弯曲的力（维持夹角为0）

---

调节参数并开始迭代，就可以看到最终结果：

![](https://pica.zhimg.com/v2-23fe6ebd6b0be6f2828be10423ce511a_1440w.jpg)

那么，对于建筑学学生来说，此模型有没有可能提供一些设计思路呢？是有的。

上文中，作者建立了三维空间中的羊毛模型，并重点描述了一天当中，不同时间段的功能活跃度对人流的影响。同时也考虑到不同路径的重要程度，并调整不同权重加以区分。

受到上文的启发和影响，我们也在商业综合体设计中运用了“羊毛算法”。

**注意！以下内容均为设计构思，只能在想法层面达到逻辑自洽，并未有任何实例和统计结果证明此种方法在实际情况下为最优解！**

![](https://pica.zhimg.com/v2-c1625659bc7b2513e72589649a24cf18_1440w.jpg)

绘制：lzx zzh

根据前期调研、文化背景和方案探讨，我们确定了“集市”的概念。体现在方案上，就是集中排布的小面积商业。

![](https://picx.zhimg.com/v2-2737c68b2a581e89ec6f4c7df4e758a5_1440w.jpg)

绘制：lzx zzh

我们将此模型应用于确定零散商业的平面布置。

![](https://picx.zhimg.com/v2-7e30731de98e93a2f2ecd4fa105c5cff_1440w.jpg)

绘制：lzx zzh

并根据 不同参数对最终结果的影响 进行了分析。

![](https://pic2.zhimg.com/v2-64b14f9b544321bbc0d314e6621d6237_1440w.jpg)

绘制：lzx zzh

据此，得一层平面图如下

![](https://pic3.zhimg.com/v2-a7d44ff64e6afb5d42102e29a4c34820_1440w.jpg)

绘制：lzx zzh

---

需要grasshopper1.0

kangaroo2.0（ [rhino6](https://zhida.zhihu.com/search?content_id=104150410&content_type=Article&match_order=1&q=rhino6&zhida_source=entity) 中已内置）

文件下载： [pan.baidu.com/s/1ln-E23](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1ln-E23-TxobzC8Frlg-sng)

提取码：o1tz

发布于 2019-07-04 00:32[建筑学](https://www.zhihu.com/topic/19568972)[Rhino](https://www.zhihu.com/topic/19655248)[Grasshopper](https://www.zhihu.com/topic/19839895)[Kamvas 22(Gen 3)数位屏新品上市，90Hz高刷加持](https://store.huion.cn/product/shuweiping/Kamvas-22-Gen-3?spu=biz%3D0%26ci%3D3692314%26si%3D04598773-e61e-47aa-88e2-084ea6e79fce%26ts%3D1776191141%26zid%3D1629)

[

21.5英寸屏幕，兼具大尺寸显示与高分辨率，拥有90Hz刷新率，画面通透沉浸的同时绘画更流畅；五种色彩模式辅以△...

](https://store.huion.cn/product/shuweiping/Kamvas-22-Gen-3?spu=biz%3D0%26ci%3D3692314%26si%3D04598773-e61e-47aa-88e2-084ea6e79fce%26ts%3D1776191141%26zid%3D1629)