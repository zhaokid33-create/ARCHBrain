---
title: Grasshopper黏菌生长模拟
source: https://zhuanlan.zhihu.com/p/259784204
author:
published:
created: 2026-04-15
description: 今天介绍一个自然界的规划大师，智能的就像外来物种，这种生物的名字叫黏菌。其外表像真菌、行为像动物的有机体。没有嘴、没有眼睛但是却找到食物，没有大脑但是“学习”走迷宫却不费劲。更神奇的是，即使把它切成…
tags:
  - clippings
---
![动图封面](https://pic2.zhimg.com/v2-c531a29928e0be1440f3153d47551625_b.jpg)

电影（异星觉醒）中异形的幼年形态

今天介绍一个自然界的规划大师，智能的就像外来物种，这种生物的名字叫 [黏菌](https://zhida.zhihu.com/search?content_id=145860525&content_type=Article&match_order=1&q=%E9%BB%8F%E8%8F%8C&zhida_source=entity) 。其外表像真菌、行为像动物的有机体。没有嘴、没有眼睛但是却找到食物，没有大脑但是“学习”走迷宫却不费劲。更神奇的是，即使把它切成两半，短时间之内还能“自愈”，简直就是现实版的“毒液”既视感。

![](https://pic4.zhimg.com/v2-7858d05aae01d0423a92cd9ba7bc6591_1440w.jpg)

因为黏菌在整个生命周期里既表现出了原生动物的特征，也表现出了真菌的繁殖特性，生物学家最后也不得以把它归为 [原生生物界](https://zhida.zhihu.com/search?content_id=145860525&content_type=Article&match_order=1&q=%E5%8E%9F%E7%94%9F%E7%94%9F%E7%89%A9%E7%95%8C&zhida_source=entity) ，属于黏菌门。但是最神奇的地方还不在这里，因为作为一种单细胞生物，它们表现出来的智慧才是让人无法理解的。

![动图封面](https://pic3.zhimg.com/v2-18af9c559b91e85cb2526eb688f46ee0_b.jpg)

将黏菌放在迷宫中，在起点和终点处均放置黏菌最爱的食物，并且在迷宫中，连接两个食物源的道路包含四种不同长度的路线。研究人员发现，黏菌在找寻食物的同时会对路径进行优化，直到确定一条最短路径。

尽管这些生物没有大脑，但它们能够在黏菌留下的痕迹中储存对过去事件的"记忆"。黏液路径中储存的化学信息可以帮助黏菌更快地找到食物来源，因为黏菌不会浪费时间向已经探索过的地方发出触角。黏菌甚至可以学习，然后通过与其他黏菌融合，将学到的信息传递下去。

![动图封面](https://pica.zhimg.com/v2-4f4bcc11afbc66e69c259aa27b402ec0_b.jpg)

黏菌在觅食过程中，表现出了惊人的线路规划能力。它伸展形成复杂的管道网，并通过一些简单规则管理网络，那些与食物没有连接的管道逐渐衰退，而找到食物的管道不断强化，并将营养物质送回中心。黏菌虽然没有大脑，却设计出了高效复杂的食物运输网络，将资源准确输送到需要的地方。

![动图封面](https://picx.zhimg.com/v2-6c48dc016edfa5c37162621ef1d280e5_b.jpg)

现在人类投入巨资建造运输网络，试图实现资源的有效流动，那我们能否借鉴黏菌的一些经验呢？科学家曾做过试验，用燕麦片在地图上标记出东京及其周边城市，测试黏菌的觅食路线是否足以媲美这个超级铁路系统。经过反复测试，科学家发现单细胞的黏菌能够创造出与东京铁路线非常相似的网络。

![](https://pica.zhimg.com/v2-759743836f35453ac9c1d370e63ff202_1440w.jpg)

Grasshopper中的 [Physarealm](https://zhida.zhihu.com/search?content_id=145860525&content_type=Article&match_order=1&q=Physarealm&zhida_source=entity) 插件可模拟黏菌规划最优路线的方式，这种设计手法既可应用于大尺度的城市规划上，也可应用于小尺度空间流线优化。

![](https://pica.zhimg.com/v2-cbedc88ad33a4aa1f3b60e48f4a798d0_1440w.jpeg)

Physarealm插件的使用方法与黏菌的行为方式类似，需要指定点作为粒子发射器，模拟黏菌出生的位置；然后指定点作为食物终点，经过主模拟器的运算，可自动生成高效率的空间网络。

![](https://pic3.zhimg.com/v2-0dfbddb771f8d2e5c34f43cc37f0b720_1440w.jpg)

Physarealm插件的使用方法与 [kangaroo](https://zhida.zhihu.com/search?content_id=145860525&content_type=Article&match_order=1&q=kangaroo&zhida_source=entity) 类似，都需要timer运算器进行驱动，并且用布尔开关来控制程序运行与否。主模拟器Physarealm可生成模拟细菌的粒子，将粒子的运动轨迹连成曲线，最后可将曲线的长度值作为渐变色的依据。

![](https://pic1.zhimg.com/v2-601df386d090cd52638a8e7a1845dfd8_1440w.jpg)

![动图封面](https://pic4.zhimg.com/v2-720c12e20f8c5d4a9d2c73c6d75d34bb_b.jpg)

Physarealm插件的使用方法与kangaroo类似，都需要timer运算器进行驱动，并且用布尔开关来控制程序运行与否。主模拟器Physarealm可生成模拟细菌的粒子，将粒子的运动轨迹连成曲线，最后可将曲线的长度值作为渐变色的依据。

![](https://pic2.zhimg.com/v2-746b8c846145759ccc74fe17c4dce929_1440w.jpg)

![动图封面](https://picx.zhimg.com/v2-156e8d2e992dd40175480dc05230fd97_b.jpg)

公众号 [犀牛参数化云平台](https://zhida.zhihu.com/search?content_id=145860525&content_type=Article&match_order=1&q=%E7%8A%80%E7%89%9B%E5%8F%82%E6%95%B0%E5%8C%96%E4%BA%91%E5%B9%B3%E5%8F%B0&zhida_source=entity)

犀牛参数化云平台简介：为犀牛和参数化爱好者提供交流的平台，同时也为了推广参数化更多更新的技术应用，欢迎爱好犀牛和GH的朋友一起来交流~

还没有人送礼物，鼓励一下作者吧

编辑于 2020-09-27 13:52[Grasshopper](https://www.zhihu.com/topic/19839895)[参数化设计](https://www.zhihu.com/topic/19900144)[参数化建模](https://www.zhihu.com/topic/19922611)