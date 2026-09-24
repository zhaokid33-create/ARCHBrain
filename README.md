# Brain - External Knowledge Base System

**个人外置知识库系统**，用于建筑设计研究、AI 辅助工作流、知识积累与检索。

由 [kid](https://github.com/zhaokid33-create) 开发，服务于建筑设计工作流程

---

## 📦 项目概览

Brain 是一个三层结构的知识管理系统：
- **raw/** — 原始素材存储（只进不出）
- **wiki/** — AI 编译的结构化知识
- **outputs/** — 可复用成果（QA、总结、倒排索引）

配合 **Obsidian** 进行可视化管理，通过 **MemPalace** 实现语义检索。

---

## 🏗️ 目录结构

```
E:/codex/brain/
├── raw/                     # 原始素材（只进不出）
│   ├── articles/           # 文章剪藏
│   ├── links/              # 网页链接（Obsidian Clipper）
│   ├── notes/              # 手写笔记
│   └── media/              # 图片、截图等
│
├── wiki/                    # AI 编译的结构化知识
│   └── topics/
│       ├── architecture/   # 建筑类（当前重点）
│       │   ├── 提示词风格库.md              # 风格库总入口
│       │   ├── 风格库工作流与参考模板.md      # 渲染图风格工作流
│       │   ├── 线稿风格库工作流与参考模板.md  # 线稿图风格工作流
│       │   ├── 风格细则-style_arch_*.md     # 渲染图风格细则
│       │   ├── 风格细则-lineart_arch_*.md   # 线稿图风格细则
│       │   ├── 建筑案例库.md
│       │   ├── 仿生算法与生成设计.md
│       │   ├── 建筑叙事学.md
│       │   └── ...
│       └── system/         # 系统类
│           ├── Brain外置知识库系统架构.md
│           ├── 扩散模型-Diffusion-Models基础.md
│           └── ...
│
├── outputs/                 # 可复用成果
│   ├── architecture/       # 建筑案例倒排索引
│   │   ├── building_types.md
│   │   ├── regions.md
│   │   ├── design_methods.md
│   │   └── styles.md
│   ├── projects/           # 项目记录
│   ├── qa/                 # 问答对
│   └── summaries/          # 编译日志
│
├── .obsidian/              # Obsidian 配置
│   ├── plugins/            # 社区插件
│   │   ├── obsidian-clipper/
│   │   ├── open-in-terminal/
│   │   └── terminal/
│   └── workspace.json      # 工作区布局
│
├── brain-wakeup.py         # Brain CLI 工具
├── compile_architecture.py  # 建筑案例自动编译
├── create_task.ps1         # Windows 定时任务创建脚本
├── INDEX.md                # 自动维护的索引（由 brain-wakeup.py 生成）
├── mempalace.yaml          # MemPalace 配置
└── README.md               # 本文件
```

---

## 🚀 核心功能

### 1. **三层知识流转**
```
raw（原始素材） → wiki（结构化知识） → outputs（可复用成果）
```

### 2. **建筑风格提示词库**
- **三级结构**：总入口 → 工作流层 → 风格细则层
- **双轨并行**：
  - **渲染图风格**（`style_arch_###`）
  - **线稿图风格**（`lineart_arch_###`）
- **已收录风格**：
  - 渲染：金属模型、模型投影、水粉草地、胶片草地
  - 线稿：素描平面、素描轴测

### 3. **建筑案例库**
- **自动编译**：每周五 18:00 自动扫描 raw/ 中的案例
- **四维度倒排索引**：
  - 建筑类型（building_types）
  - 地区（regions）
  - 设计手法（design_methods）
  - 风格（styles）

### 4. **语义检索（MemPalace 集成）**
- ChromaDB 向量存储
- 自动索引 wiki/ 内容
- 支持自然语言查询

---

## 🛠️ 使用方法

### Brain CLI 工具

```bash
# 唤醒（重建索引）
python E:/codex/brain/brain-wakeup.py wake-up

# 搜索（语义/grep）
python E:/codex/brain/brain-wakeup.py search <query>

# 录入 raw
python E:/codex/brain/brain-wakeup.py add-raw notes "标题" @文件路径

# 更新 wiki（追加更新）
python E:/codex/brain/brain-wakeup.py update-wiki "主题" @文件路径

# 删除条目
python E:/codex/brain/brain-wakeup.py delete-wiki <topic>

# 编译并同步 MemPalace
python E:/codex/brain/brain-wakeup.py compile
```

**注意**：Windows 命令行传中文必须使用 `@文件路径`，不能直接传字符串。

---

## 📝 Obsidian 管理

### 插件配置

- **obsidian-clipper** (v0.2.9) — 网页剪藏，自动保存到 `raw/links/`
- **open-in-terminal** (v0.9.1) — 在终端打开当前目录
- **terminal** — 内置终端面板

### 工作区布局

- **左侧**：文件列表（按创建时间排序）+ 搜索 + 书签
- **中央**：关系图谱视图（默认打开）
- **右侧**：反向链接 + 出链 + 标签 + 大纲

### 自动忽略

配置了 `userIgnoreFilters: ["raw/"]`，raw/ 目录不参与图谱关系。

---

## 🔄 工作流示例

### 场景 1：收录建筑案例

```bash
# 1. 剪藏网页到 raw/links/（Obsidian Clipper）
# 2. 等待每周五自动编译，或手动触发：
python compile_architecture.py

# 3. 查看倒排索引
# outputs/architecture/building_types.md
# outputs/architecture/regions.md
```

### 场景 2：录入风格提示词

```bash
# 1. 检查当前最大编号
ls wiki/topics/architecture/风格细则-style_arch_*.md

# 2. 创建新风格细则（假设下一个编号是 005）
# 使用 write_file 直写目标路径（中文内容不走 brain_add）

# 3. 更新总入口索引
# 编辑 wiki/topics/architecture/提示词风格库.md

# 4. 同步 MemPalace
python brain-wakeup.py compile
```

### 场景 3：语义检索

```bash
# 搜索建筑叙事学相关内容
python brain-wakeup.py search "architectural narratology"

# 搜索黏菌算法
python brain-wakeup.py search "黏菌 扩散"
```

---

## ⚠️ 硬约束和已知坑点

### ✅ 必须遵守

1. **中文内容用 `write_file` 直写目标路径**，不走 `brain_add(wiki)`
2. **新增风格条目前先检查编号**，避免冲突（渲染/线稿独立递增）
3. **编译后必做**：
   - 清理悬空双链
   - 更新 INDEX.md
   - 同步 MemPalace
4. **Obsidian Clipper** 会自动转换 author 为 `[[双链]]`，需预处理

### ❌ 已知踩坑

1. `brain_add(wiki, category=...)` 会生成随机 hash 文件名到根目录
2. Windows 命令行传中文必须用 `@文件路径`，不能直接传字符串
3. MemPalace 没有 `add` 命令，只有 `mine`（扫描目录建索引）
4. 大文件必须分块写入（>200 行时先写基础结构，再追加详细内容）

---

## 📊 当前统计

- **Wiki 建筑类**：16 个结构化文档
- **Raw 笔记**：7 个原始笔记
- **Raw 链接**：7 个网页剪藏
- **Outputs**：20 个可复用成果
- **风格库条目**：
  - 渲染图风格：4 个（style_arch_001-004）
  - 线稿图风格：2 个（lineart_arch_001-002）

---

## 🔗 相关项目

- **MemPalace** — 语义检索层（https://github.com/zhaokid33-create/MemPalace）
- **Hermes Agent** — 桌面 AI 助手（配置在 `C:/Users/kid/AppData/Local/hermes/`）
- **Claude Code** — 终端 AI 助手（记忆在 `C:/Users/kid/.claude/`）

---

## 📜 许可证

个人项目，未指定许可证。

---

## 👤 作者

**kid** 
研究方向：城市更新 + 仿生算法+ AI 辅助设计

GitHub: [@zhaokid33-create](https://github.com/zhaokid33-create)

---

## 更新日志

- **2026-09-24** — 初次上传 GitHub，完善项目文档
- **2026-05-05** — 建立三级风格库结构，渲染/线稿双轨并行
- **2026-04-21** — 系统架构文档化
- **2026-04-18** — 建筑案例库自动编译功能上线
- **2026-04-13** — Brain 系统初始化，集成 MemPalace
