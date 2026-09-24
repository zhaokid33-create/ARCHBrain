---
title: (5 条消息) 如何使用 Grasshopper 生成若干点之间的最短路径 (Minimal Path)?
source: https://www.zhihu.com/question/28518480?sort=created
published:
created: 2026-04-15
description: 请问右边的这个图形是怎么生成的？在grasshopper里面又怎么操作呢？对这个问题的资料进行补充如下：1：（…
tags:
  - clippings
---
[Detour path networks](https://zhida.zhihu.com/search?content_id=12386029&content_type=Answer&match_order=1&q=Detour+path+networks&zhida_source=entity)中出现了Frei Otto另一个非常有名的模拟实验，是的，他又用道具了，这次用到的是羊毛线模型 Wool-thread model. 左图为连接各个目的点的干燥的羊毛，右图为湿润的羊毛。湿润的羊毛彼此之间因为水的张力作用吸附在了一起，形成了多个路径变为一个路径的转变。这个实验的意图在于减少各个目的点的Direct path的总长度，同时让绕圈因素维持在一个比较低的范围。个人感觉3. Detour path networks 和 2. Minimal path networks 有很多相似点，都是为了缩短路径，不同处在于，后者2更倾向于用一个完美的数学思路来模拟，得到的是唯一解。而前者3得到的模拟结果并不是唯一的，因为诸多影响因素的不同，而最终会得到不同的结果，但是这些结果的共同目标都是优化路径总长度。

![](https://picx.zhimg.com/80/8f33517f37c96901f7f146f6dade603c_720w.webp?source=1def8aca)

对于Detour path system的利用也是非常广泛，因为在建筑行业中，设计并不是唯一解，比如说做城市设计，绝对不会有要求说这片地最后的道路总长一定要满足Minimal path的理论最小值。相反，一个有多个可控参数，可调整又可优化路网总长度的模拟工具不是更好？Detour path system 横空出世，来看[Zaha hadid事务所](https://zhida.zhihu.com/search?content_id=12386029&content_type=Answer&match_order=1&q=Zaha+hadid%E4%BA%8B%E5%8A%A1%E6%89%80&zhida_source=entity)2006年在伊斯坦布尔做的这个城市设计，官网有一个视频，模拟了如何从Direct path到优化后的道路（下图的形状）的渐变过程，形象生动。我把链接贴出来

[Kartal Masterplan](https://link.zhihu.com/?target=http%3A//www.zaha-hadid.com/masterplans/kartal-pendik-masterplan/)

==Vimeo需翻墙。==

![](https://picx.zhimg.com/80/8bc3dacdda6586f7437c9d2f63e65cbc_720w.webp?source=1def8aca)

![](https://picx.zhimg.com/50/6425b9fb090f2fad94a8b5c29e6fde91_720w.jpg?source=1def8aca)

  
  

====\----------------------------------------------------------------------------------------------------------------------------------------====

==说了一大堆介绍问题背景的话，现在回到问题上面来，说到这里，相信大家应该已经熟悉这几个名词的概念了。题主贴出来的图属于2. Minimal path system，在图下面贴的那两个Vimeo的视频，模拟的是3.Detour path system，不过说实在的，目的类似，平时做做设计的时候也不用分那么清楚。==

==下面我来模拟一下视频中出现的那个线路优化的过程。首先我在rhino中创建了一个方形，任意选取了边长上的一些点，可以想象这个方形是一个城市范围，或者一个建筑，而那些选定的点是你想在其彼此之间创建连接的功能空间。先上最粗暴的方式 1. Direct path==

![](https://pic1.zhimg.com/50/f4a9463edf71d5858ab67078ef233c54_720w.jpg?source=1def8aca)

==图中的绿线代表了所有需要的功能之间的连接，如果最后他们都变成交通空间的话甲方一定会疯的。于是我们用Frei Otto的羊毛线模型来模拟优化以下这个粗暴的路网系统，在借助Grasshopper的优化之后（有使用Kangaroo），可以得到和真实羊毛模拟非常近似的结果。==

![](https://pica.zhimg.com/50/f42025b17616f1e8c9454791ab9fa0a4_720w.jpg?source=1def8aca)

==屏幕截图实在太糙，不能忍。上个Diagram表达一下。如下图，红点是上文中所提到的目的点，即需要连接的功能空间，彼此之间淡淡的虚线是Direct path，图中加粗了的粗线是优化后的结果，当然这个优化结果你可以通过调节Grasshopper中的一些参数值来控制吸附强度和影响范围，从而影响新路网的最终形态。可以发现，图中很多粗暴的直线连接都在一股吸附力的作用下黏在了一起，从而减少了总路径的长度。==

![](https://picx.zhimg.com/50/ac99c78ff9c6bd7245b54276b94bacbf_720w.jpg?source=1def8aca)

==附上Grasshopper definition图，简单说明下原理。==

![](https://pic1.zhimg.com/50/89e13e1bf1f1b06a03cd47d6a329ccba_720w.jpg?source=1def8aca)

  

==看到这个图是不是发现好短好简单，作为最短路径生成的GH，他自己好意思长？==

==这个definition运行的原理就是把原Direct path的线切分成若干段之后接入一个弹力(Spring from line)，切分的点接入一个引力(Powerlaw)，然后用Kangaroo运算器就能完成模拟过程，最终那些且分点和线段在引入力的作用下重新排布，最后一个电池（curve from control points）就是从运算后得出的点重新组建成新的Curve，也就是我们需要的优化路径。==

==至于你要做的事情就是接入你的基本路径curve，在第一个input接入那堆Direct path，这个你想GH做也行，直接手动连也很快，随意。然后根据模型中的线间距调节影响范围和吸附力大小，就是控制接入Powerlaw的那两个滑条的读数。至于setting可以直接用默认的参数，不会有什么太大影响，变化快慢和强度通过上述值和Timer（图中是1ms）的时间控制就能完成。==

==接下来轮到题主贴出来的那张图，也就是关于 2. Minimal path system 应该如何通过steiner tree的算法实现。==

==这个我不会。==

\----------------------------------------------------------------------------------------------------------------------------------------

==先写到这了，看情况再补充，正如我前面提到过的，Minimal path 是一个唯一解的完美模型，对于一个做设计的建筑师是否需要用到这个模型，有待讨论。个人觉得，这个系统可能更适合用在更加精确的结构研究上吧。上面有不少文字是自己的理解，可能会有理解偏差甚至出错的地方，欢迎指正。==

[编辑于 2015-03-22 00:12](//www.zhihu.com/question/28518480/answer/42482048)

 

[![知乎用户pKnkv4](https://pic1.zhimg.com/v2-abed1a8c04700ba7d72b45195223e0ff_l.jpg?source=1def8aca)](//www.zhihu.com/people/lzeaf)

[知乎用户pKnkv4](//www.zhihu.com/people/lzeaf)

43 人赞同了该回答

[羊毛吸引的算法](https://zhida.zhihu.com/search?content_id=12665285&content_type=Answer&match_order=1&q=%E7%BE%8A%E6%AF%9B%E5%90%B8%E5%BC%95%E7%9A%84%E7%AE%97%E6%B3%95&zhida_source=entity)看似很牛逼，但是应用到道路系统上是根本不成立的。如果一个城市的道路都是最短的，那他的效率只在车辆数非常小的情况下效率最高。比如拿北京而言，如果北京的车辆只有现在的5%-10%，那这个系统可能有效降低了交通成本。但是真正考虑到实际系统时，道路的饱和程度是非常高的。如果多条道路互相吸附重叠，随意软件模拟一下就会发现交通灯的等待时间会以排列组合的复杂度般地增高（比如6叉路口之类，想想交通灯怎么分配）。与此同时，因为道路的总长度缩短了，而且部分道路在两个节点之间非常近的时候，道路容纳车辆的效率降低了，很多车根本就开不到道路上，经过的一段道路的车无法进入下一段道路，就会造成交通节点的极端拥堵。如果真的研究过图论，在非拓扑的情况下（无立交桥）只有[方格路网](https://zhida.zhihu.com/search?content_id=12665285&content_type=Answer&match_order=1&q=%E6%96%B9%E6%A0%BC%E8%B7%AF%E7%BD%91&zhida_source=entity)的效率是最高的，而在一定条件下有更高效率的结构是[六边形路网](https://zhida.zhihu.com/search?content_id=12665285&content_type=Answer&match_order=1&q=%E5%85%AD%E8%BE%B9%E5%BD%A2%E8%B7%AF%E7%BD%91&zhida_source=entity)（如果你愿意生活在视线永远不能穿透任何空间的街区里的话）。所以这个理论只是沽名钓誉而已，玩玩就好，不必当真。