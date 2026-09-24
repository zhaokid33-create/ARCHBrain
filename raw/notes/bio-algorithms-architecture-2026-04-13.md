# 仿生算法与生成设计研究

date: 2026-04-13
keywords: Slime mold architecture, Physarum polycephalum routing, Diffusion Limited Aggregation (DLA), Porous architecture design, Generative bio-design architecture, Biomimicry structures, Cellular automata architecture

---

## 1. 黏菌建筑 Slime Mold Architecture

### 核心生物学背景
Physarum polycephalum（多头绒泡菌）：
- 单细胞生物，通过管状网络输送营养与信号
- 栖息于阴暗、潮湿、凉爽环境（腐叶、朽木）
- 无神经系统，却能解决复杂网络优化问题

### 关键研究：东京铁路网络实验
Toshiyuki Nakagaki 等人（2010，发表于 Science）：
- 将黏菌放置于模拟东京地理的食物节点上
- 黏菌自发形成的管网与东京铁路系统高度吻合
- 证明简单生物体能找到复杂问题的高效解
- 论文：Rules for Biologically Inspired Adaptive Network Design（Science, 2010）

### 在建筑与城市设计中的应用
- 城市网络优化：以黏菌行为为模型设计高效城市网络、交通系统与空间连接
- 空间修复算法：黏菌网络优化原理用于城市基础设施修复与再生
- 计算设计工具：基于 Agent 的模拟，在 Grasshopper/Processing 中实现

### 与毕设的直接关联
黏菌算法作为垂直城市更新的空间修复机制：
- 识别巨构中的空置/老化空间节点
- 以黏菌扩散逻辑生成连接这些节点的网络
- 网络即新的城市修复路径，寄生/填充于既有结构空隙

---

## 2. 扩散限制聚集 Diffusion Limited Aggregation (DLA)

### 原理
DLA：粒子在布朗运动（随机游走）驱动下聚集，形成分形聚合体。
- 生成具有分形特征的树枝状/珊瑚状形态
- 自然界中的闪电、雪花、珊瑚、矿物结晶均遵循类似逻辑

### 在建筑中的应用
- 形态生成：生成有机的、分形的建筑形态
- 城市形态学：Michael Batty（UCL CASA）研究 DLA 与城市增长模型的关系
- 参数化设计：Grasshopper/Rhino 中有成熟的 DLA 实现插件

### 理论家
- Michael Batty：《分形城市》（Fractal Cities），DLA 城市增长模型，UCL 高级空间分析中心

### 与毕设的关联
DLA 作为空间填充机制：
- 模拟新建筑单元在巨构空隙中的扩散聚集过程
- 生成具有有机分形特征的填充形态
- 与黏菌算法互补：黏菌生成网络路径，DLA 生成填充形态

---

## 3. 多孔建筑 Porous Architecture

### 核心概念
多孔性（Porosity）在建筑中的意义：
- 渗透性：允许人流、空气、光线自由穿越
- 模糊边界：消解室内外、公共私密的明确界限
- 仿生逻辑：骨小梁结构、泡沫结构的建筑转译

### 代表建筑师
- 隈研吾（Kengo Kuma）：多孔、渗透性建筑哲学，模糊建筑与环境边界
- 参数化设计：Voronoi 图与多孔结构在参数化建筑中的应用

### 与毕设的关联
多孔性是垂直城市更新的空间结果：
- 黏菌/DLA 算法在巨构中生成的填充体天然具有多孔特征
- 多孔性保证新旧结构之间的空气、光线、人流渗透

---

## 4. 生成仿生设计 Generative Bio-design Architecture

### 核心研究机构与人物
- Neri Oxman / Mediated Matter（MIT Media Lab）：物质生态学，探索生物学、计算与制造的交叉
- Achim Menges / ICD Stuttgart：仿生计算设计与建造研究
- Zaha Hadid Architects：形态发生学原理在计算设计中的应用

### 核心概念
- 物质生态学（Material Ecology）：材料、结构、环境与生物过程的整合设计
- 形态发生（Morphogenesis）：以生物生长过程为模型的建筑形态生成
- 活性建筑材料：使用真菌、细菌等活性生物材料的建筑实验

---

## 5. 仿生结构 Biomimicry Structures

### 经典案例
- 高迪圣家堂：悬链线拱、分枝柱、有机几何
- Eastgate Centre（津巴布韦，Mick Pearce）：仿白蚁丘通风系统的被动冷却
- HOK：将仿生原理系统化应用于可持续建筑设计

### 结构仿生逻辑
- 骨骼结构：骨小梁的拓扑优化逻辑
- 树形结构：分枝柱的荷载传递效率
- 壳体结构：贝壳、蛋壳的曲面受力原理

---

## 6. 元胞自动机 Cellular Automata Architecture

### 原理
元胞自动机（CA）：基于简单局部规则，产生复杂全局行为的离散计算模型。
- Conway 生命游戏：最著名的 CA 模型
- Stephen Wolfram：《一种新科学》，CA 与复杂性理论

### 在建筑与城市设计中的应用
- 城市增长模拟：Michael Batty（UCL）用 CA 模拟城市扩张
- 建筑形态生成：Grasshopper 中的 CA 插件用于空间生成
- 自组织建筑系统：基于 CA 原理的自适应空间设计

### 与毕设的关联
CA 可作为黏菌/DLA 算法的补充工具：
- 模拟垂直城市中各空间单元的状态演化
- 生成具有涌现特征的城市更新方案
