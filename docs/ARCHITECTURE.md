# Brain 系统架构文档

## 设计理念

Brain 是一个**外置知识库系统**，设计目标是：

1. **持久化**：知识积累不依赖单次对话，跨会话可检索
2. **结构化**：从原始素材（raw）→ 结构化知识（wiki）→ 可复用成果（outputs）
3. **AI 友好**：通过 MemPalace 语义检索，让 AI 助手能快速定位相关知识
4. **人机协同**：Obsidian 可视化管理 + CLI 工具自动化维护

---

## 三层架构

```
┌─────────────────────────────────────────────────────────┐
│                       用户界面层                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Obsidian   │  │  Hermes CLI  │  │ MemPalace    │  │
│  │  (可视化)     │  │  (自动化)     │  │ (语义检索)    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                       数据流转层                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │     raw/     │→ │    wiki/     │→ │   outputs/   │  │
│  │  (原始素材)   │  │ (结构化知识)  │  │ (可复用成果)  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                       存储层                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Markdown    │  │  ChromaDB    │  │  INDEX.md    │  │
│  │   文件系统    │  │ (向量存储)    │  │  (索引文件)   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 核心组件

### 1. brain-wakeup.py

**职责**：Brain 的 CLI 入口，负责知识录入、搜索、索引维护。

**核心功能**：
- `wake-up` — 重建 INDEX.md，生成系统提示词
- `search <query>` — 语义搜索（MemPalace）或 grep 回退
- `add-raw` — 录入原始素材到 raw/
- `update-wiki` — 追加/更新 wiki/topics/
- `compile` — 触发 MemPalace 重新索引
- `delete-*` — 删除 raw/wiki/outputs 中的条目

**设计要点**：
- 独立脚本，无 Hermes 依赖，可在任何环境运行
- UTF-8 强制编码，避免 Windows 中文乱码
- Slug 生成：ASCII 优先，CJK 标题用 MD5 hash

---

### 2. compile_architecture.py

**职责**：建筑案例自动编译脚本，扫描 raw/ 中的案例并生成倒排索引。

**工作流程**：
1. 扫描 `raw/articles/` 和 `raw/links/`
2. 解析案例元数据（项目名称、位置、年份、设计师、风格、手法）
3. 按四个维度生成倒排索引：
   - `outputs/architecture/building_types.md`
   - `outputs/architecture/regions.md`
   - `outputs/architecture/design_methods.md`
   - `outputs/architecture/styles.md`

**定时任务**：
- Windows Task Scheduler 配置（每周五 18:00）
- 通过 `create_task.ps1` 创建

---

### 3. INDEX.md

**职责**：全局索引文件，由 `brain-wakeup.py` 自动维护。

**内容结构**：
```markdown
# Brain Index

## architecture
- [文件名](路径) -- 标题 | updated: 日期

## system
- [文件名](路径) -- 标题 | updated: 日期

## Recent Updates
- 日期 [文件名](路径)
```

**更新时机**：
- 每次调用 `wake-up`
- 每次 `update-wiki` 后自动触发

---

### 4. MemPalace 集成

**职责**：为 Brain 提供语义检索能力。

**配置文件**：`mempalace.yaml`

```yaml
rooms:
  - name: brain_wiki
    path: E:/codex/brain/wiki/
    description: Brain 结构化知识库
    collections:
      - architecture
      - system
```

**工作流程**：
1. `brain-wakeup.py compile` 调用 `mempalace-wakeup.py mine`
2. MemPalace 扫描 `wiki/` 目录，提取文本
3. 通过 embedding 模型生成向量
4. 存储到 ChromaDB（位于 `E:/codex/mempalace/palace/chroma_db/`）
5. 搜索时通过 `brain-wakeup.py search` 调用 MemPalace 语义检索

---

## 数据流转

### 流程 1：网页剪藏 → 案例索引

```
用户浏览建筑网站
    ↓
Obsidian Clipper 剪藏
    ↓
保存到 raw/links/<title>.md
    ↓
每周五 compile_architecture.py 自动运行
    ↓
解析元数据（项目名、位置、风格等）
    ↓
生成倒排索引到 outputs/architecture/
    ↓
AI 助手查询案例库
```

### 流程 2：风格提示词录入 → MemPalace 检索

```
手动创建风格细则文件
    ↓
wiki/topics/architecture/风格细则-style_arch_005-*.md
    ↓
运行 brain-wakeup.py compile
    ↓
MemPalace 索引新文件
    ↓
AI 助手语义搜索："混凝土粗野风格"
    ↓
MemPalace 返回风格细则文档
    ↓
生成提示词
```

### 流程 3：Hermes 调用 Brain

```
用户在 Hermes 中提问："重庆城市更新有哪些参考案例？"
    ↓
百香果调用 brain-search "重庆 城市更新"
    ↓
MemPalace 语义检索 wiki/
    ↓
返回相关文档片段
    ↓
百香果基于检索结果回答
```

---

## 目录约定

### raw/ — 只进不出

- **用途**：存储原始素材，永不删除（除非手动清理）
- **来源**：
  - Obsidian Clipper 网页剪藏 → `raw/links/`
  - 手动笔记 → `raw/notes/`
  - 文章保存 → `raw/articles/`
  - 图片截图 → `raw/media/`
- **约束**：
  - 不直接读取（避免污染上下文）
  - 通过编译脚本转化为 wiki/

### wiki/ — 结构化知识

- **用途**：AI 编译的、高质量的、可检索的知识条目
- **结构**：
  - `topics/architecture/` — 建筑类知识
  - `topics/system/` — 系统类知识
- **格式规范**：
  - Markdown frontmatter（tags, updated, parent）
  - 清晰的标题层级
  - 内部链接用 `[[双链]]`
- **约束**：
  - 中文内容必须用 `write_file` 直写，不走 `brain_add(wiki)`
  - 大文件分块写入（>200 行）

### outputs/ — 可复用成果

- **用途**：编译生成的索引、问答对、项目记录
- **子目录**：
  - `architecture/` — 建筑案例倒排索引
  - `projects/` — 项目记录（风格库迁移、系统配置等）
  - `qa/` — 问答对（未来规划）
  - `summaries/` — 编译日志

---

## 风格库架构（重点）

### 三级结构

```
第一级（总入口）
  └─ 提示词风格库.md

第二级（工作流层，双轨并行）
  ├─ 风格库工作流与参考模板.md（渲染图风格）
  └─ 线稿风格库工作流与参考模板.md（线稿图风格）

第三级（风格细则层）
  ├─ 风格细则-style_arch_001-金属模型.md
  ├─ 风格细则-style_arch_002-模型投影.md
  ├─ 风格细则-style_arch_003-水粉草地.md
  ├─ 风格细则-style_arch_004-胶片草地.md
  ├─ 风格细则-lineart_arch_001-素描平面.md
  └─ 风格细则-lineart_arch_002-素描轴测.md
```

### 编号规则

- **渲染图风格**：`style_arch_###`（从 001 开始）
- **线稿图风格**：`lineart_arch_###`（从 001 开始）
- **独立递增**：两条轨道编号互不干扰

### 检索协议

1. AI 助手收到风格请求
2. 先读取第一级（总入口），确认结构
3. 根据场景判定（渲染/线稿），读取对应第二级工作流
4. MemPalace 语义检索定位具体风格细则
5. 只读取命中的 1-3 个文件（避免全量加载）

---

## Obsidian 集成

### 插件配置

- **obsidian-clipper** — 网页剪藏，快捷键 `Ctrl+Shift+C`
- **open-in-terminal** — 右键菜单"Open in Terminal"
- **terminal** — 内置终端，运行 `brain-wakeup.py` 等脚本

### 工作区布局

```
┌─────────────┬──────────────────────┬─────────────┐
│             │                      │             │
│  文件列表    │     关系图谱视图      │  反向链接    │
│  搜索       │     (默认打开)        │  出链       │
│  书签       │                      │  标签       │
│             │                      │  大纲       │
│             │                      │             │
└─────────────┴──────────────────────┴─────────────┘
```

### 自动忽略规则

```json
{
  "userIgnoreFilters": ["raw/"]
}
```

raw/ 目录不参与关系图谱，避免噪音。

---

## 安全和隐私

### 敏感信息处理

- Brain 不存储 API 密钥、密码等敏感信息
- `.gitignore` 已配置排除：
  - `secrets/`
  - `.env`
  - `*.key`
  - `*.token`

### 备份策略

- **本地备份**：定期复制 `E:/codex/brain/` 到外部硬盘
- **云备份**：通过 GitHub 私有仓库备份（不含 raw/media/ 大文件）
- **MemPalace 向量库**：`mempalace/palace/chroma_db/` 单独备份

---

## 性能优化

### 索引优化

- MemPalace 只索引 `wiki/`，不索引 `raw/`（避免低质量内容）
- 使用增量索引（只扫描新文件/更新文件）

### 搜索优化

- 优先语义搜索（MemPalace），回退到 grep
- 限制返回结果数量（默认 top 5）

### 文件系统优化

- `INDEX.md` 缓存最近更新的 10 个文件
- 大文件（>200 行）分块读取

---

## 扩展性

### 未来规划

1. **多模态支持**：索引 `raw/media/` 中的图片（通过 CLIP embedding）
2. **QA 对生成**：自动从 wiki/ 生成问答对到 `outputs/qa/`
3. **版本控制**：集成 Git，追踪 wiki/ 的历史变更
4. **Web 界面**：提供 Web UI，方便非技术用户查看和搜索

### 插件开发

可以开发 Obsidian 插件，直接调用 Brain CLI：

```javascript
// 示例：在 Obsidian 中调用 brain-wakeup.py
const { exec } = require('child_process');

exec('python E:/codex/brain/brain-wakeup.py search "黏菌算法"', (error, stdout, stderr) => {
    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});
```

---

## 参考资料

- [Zettelkasten 方法](https://zettelkasten.de/)
- [Building a Second Brain](https://www.buildingasecondbrain.com/)
- [How to Take Smart Notes](https://takesmartnotes.com/)

---

最后更新：2026-09-24
