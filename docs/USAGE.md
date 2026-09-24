# Brain 使用指南

## 快速开始

### 1. 日常使用

#### 唤醒系统（重建索引）
```bash
python brain-wakeup.py wake-up
```

#### 搜索知识
```bash
# 语义搜索（通过 MemPalace）
python brain-wakeup.py search "黏菌算法"

# 或者直接在 Obsidian 中搜索
```

---

## 录入新内容

### 方式 1：通过 Obsidian Clipper（推荐）

1. 浏览网页时点击 Clipper 插件
2. 自动保存到 `raw/links/`
3. 等待每周五自动编译到 wiki

### 方式 2：手动录入笔记

```bash
# 创建临时文件
echo "你的笔记内容" > temp_note.txt

# 录入到 raw/notes/
python brain-wakeup.py add-raw notes "笔记标题" @temp_note.txt
```

### 方式 3：直接编辑 wiki（结构化内容）

对于中文内容，**不要使用** `brain-wakeup.py update-wiki`，直接用编辑器写入：

```bash
# 方式 A：在 Obsidian 中创建新文件
# 路径：wiki/topics/architecture/新文件.md

# 方式 B：用脚本写入
# 见下方"新增风格条目"示例
```

---

## 核心工作流

### 工作流 1：建筑案例录入

```bash
# 1. 准备案例文件（raw/articles/ 或 raw/links/）
# 文件格式示例：
# ---
# 项目名称: 瑞士蒙特卡罗索小镇改造
# 位置: 瑞士
# 年份: 1980-2020
# 设计师: Luigi Snozzi
# 风格: 现代主义
# 手法: 城市更新/织补
# ---

# 2. 等待自动编译（每周五 18:00）或手动触发
python compile_architecture.py

# 3. 查看倒排索引
cat outputs/architecture/building_types.md
cat outputs/architecture/regions.md
```

### 工作流 2：风格提示词库管理

#### 查看现有风格
```bash
# 渲染图风格
ls wiki/topics/architecture/风格细则-style_arch_*.md

# 线稿图风格
ls wiki/topics/architecture/风格细则-lineart_arch_*.md
```

#### 新增风格条目

**示例：新增 style_arch_005 - 混凝土粗野**

```python
# 1. 检查最大编号（当前是 004）
# 2. 创建新文件（编号 005）

content = """# 风格细则：style_arch_005 / 混凝土粗野

tags: [style, brutalism, concrete]
updated: 2026-09-24
parent: [[风格库工作流与参考模板]]

## 风格 ID
style_arch_005

## 中文名
混凝土粗野

## 英文名
Brutalist Concrete

## 核心特征
- 裸露混凝土表面
- 粗糙模板纹理
- 硬朗几何体块
- 强烈明暗对比

## 提示词（中文）
粗野主义风格，裸露浇筑混凝土，清晰木模板纹理，硬朗几何，深阴影，强明暗对比，低饱和度，建筑摄影。

## 提示词（英文）
Brutalist architecture style, exposed cast concrete, visible wood formwork texture, bold geometry, deep shadows, strong chiaroscuro, desaturated tones, architectural photography.

## 负向词
过度美化，光滑表面，塑料感，过饱和，装饰主义。

## 参数建议
- steps: 35
- guidance: 6.5
- denoise: 0.45
- style_weight: 0.70

## 参考项目
- [[波士顿市政厅]]
- [[巴比肯中心]]

## 更新记录
- 2026-09-24：初次创建
"""

# 3. 写入文件
from pathlib import Path
target = Path("E:/codex/brain/wiki/topics/architecture/风格细则-style_arch_005-混凝土粗野.md")
target.write_text(content, encoding='utf-8')

# 4. 更新总入口索引（编辑 提示词风格库.md）
# 5. 同步 MemPalace
# python brain-wakeup.py compile
```

### 工作流 3：MemPalace 语义检索

```bash
# 1. 索引新内容
python brain-wakeup.py compile

# 2. 语义搜索
python brain-wakeup.py search "建筑叙事学"

# 3. 在 Hermes 中调用（已配置快捷命令）
mp-search "扩散模型"
```

---

## 维护任务

### 每周维护清单

- [ ] 检查 raw/links/queue.txt（待处理的剪藏队列）
- [ ] 运行 `compile_architecture.py`（或等待自动执行）
- [ ] 清理 raw/ 中的重复/无效文件
- [ ] 检查 wiki/ 悬空双链
- [ ] 更新 INDEX.md（自动，但可手动触发 `brain-wakeup.py wake-up`）
- [ ] 同步 MemPalace 索引（`brain-wakeup.py compile`）

### 清理悬空双链

```bash
# 在 Obsidian 中：
# 1. 打开命令面板（Ctrl+P）
# 2. 搜索 "Show graph view"
# 3. 找到灰色节点（悬空链接）
# 4. 手动修复或删除
```

---

## 故障排查

### 问题 1：MemPalace 搜索无结果

```bash
# 重新索引
cd E:/codex/mempalace
python mempalace-wakeup.py mine E:/codex/brain/wiki/
```

### 问题 2：中文内容乱码

```bash
# 确保文件编码是 UTF-8
# Windows 用户注意：不要用记事本编辑，用 VSCode 或 Obsidian
```

### 问题 3：brain-wakeup.py 报错

```bash
# 检查 Python 版本（需要 3.8+）
python --version

# 检查路径配置
# 编辑 brain-wakeup.py，确认：
# BRAIN_ROOT = Path(r"E:\codex\brain")
# MEMPALACE_SCRIPT = Path(r"E:\codex\mempalace\mempalace-wakeup.py")
```

---

## 快捷技巧

### Obsidian 快捷键

- `Ctrl+O` — 快速打开文件
- `Ctrl+P` — 命令面板
- `Ctrl+G` — 打开关系图谱
- `Ctrl+E` — 切换编辑/预览模式
- `[[` — 创建内部链接

### Brain CLI 别名（可选配置）

在 `.bashrc` 或 `.hermesrc` 中添加：

```bash
alias brain-wake='python E:/codex/brain/brain-wakeup.py wake-up'
alias brain-search='python E:/codex/brain/brain-wakeup.py search'
alias brain-compile='python E:/codex/brain/brain-wakeup.py compile'
```

---

## 进阶使用

### 自定义编译规则

编辑 `compile_architecture.py`，修改分类维度：

```python
# 当前支持的维度：
# - building_types（建筑类型）
# - regions（地区）
# - design_methods（设计手法）
# - styles（风格）

# 可新增维度，例如：
# - scales（尺度：建筑/城市/景观）
# - periods（时期：现代/当代/历史）
```

### 集成到 Hermes Agent

在 Hermes 中调用 Brain：

```python
# 1. 在 .hermesrc 中已配置快捷命令：
# brain-wake, brain-search, brain-compile

# 2. 在对话中调用：
# "帮我搜索 Brain 中关于黏菌算法的内容"
# 百香果会自动调用 brain-search
```

---

## 参考资源

- [Obsidian 官方文档](https://help.obsidian.md/)
- [MemPalace GitHub](https://github.com/zhaokid33-create/MemPalace)
- [Hermes Agent 文档](https://hermes-agent.nousresearch.com/docs)

---

最后更新：2026-09-24
