# 2026-04-14 Hermes 图片识别 + Brain-MemPalace 合并配置

tags: [系统配置, Hermes, Vision, Brain, MemPalace]
updated: 2026-04-14
sources: [claude-code session]

## 一、Hermes 图片识别修复

### 问题
- `_VISION_AUTO_PROVIDER_ORDER` 只有 `openrouter` 和 `nous`，不含 `openai-codex`
- 导致 vision auto-detect 找不到可用后端，图片分析静默失败

### 修复
**文件：** `E:\codex\hermes\agent\auxiliary_client.py`
```python
# 修改前
_VISION_AUTO_PROVIDER_ORDER = ("openrouter", "nous")
# 修改后
_VISION_AUTO_PROVIDER_ORDER = ("openrouter", "nous", "openai-codex")
```

### 大图静默失败问题
图片 >5MB base64 时，honoursoft endpoint 返回空内容而不报错。

**文件：** `E:\codex\hermes\tools\vision_tools.py`
- 修改：发送前主动检查是否超过 `_RESIZE_TARGET_BYTES`（5MB），超过先 resize 再发送
- 原逻辑只在 API 报错时才 resize，但 honoursoft 静默返回空

### Tool Schema 修复
`VISION_ANALYZE_SCHEMA` 的 `image_url` 描述补充：
> "Local paths work directly — do NOT say local files are unsupported."

### Claude 模型 Tool-Use Enforcement
- `TOOL_USE_ENFORCEMENT_MODELS` 加入 `"claude"`
- `run_agent.py` 里 claude 模型也注入 `OPENAI_MODEL_EXECUTION_GUIDANCE`
- `OPENAI_MODEL_EXECUTION_GUIDANCE` 的 `<mandatory_tool_use>` 加一条：图片路径 → 调用 vision_analyze

---

## 二、Brain + MemPalace 合并

### 目标
把 MemPalace 的语义向量检索能力嫁接到 Brain，废弃独立的 MemPalace 使用场景。

### 修改

**`E:\codex\brain\brain-wakeup.py`**
- `search()`: `--room brain` 改为 `--wing brain_wiki`（原 wing 名称）
- `compile_brain()`: 分别 mine `wiki/`、`raw/`、`outputs/` 三个子目录，超时改为 600s

**新增文件**
- `E:\codex\brain\mempalace.yaml` — Brain 根目录 palace 配置（wing: brain_wiki）
- `E:\codex\brain\raw\mempalace.yaml` — raw 子目录配置
- `E:\codex\brain\outputs\mempalace.yaml` — outputs 子目录配置

### 使用方式
```bash
# 语义搜索 Brain 全部内容
python E:\codex\brain\brain-wakeup.py search "查询词"

# 新增内容后重新索引
python E:\codex\brain\brain-wakeup.py compile
```

---

## 三、Obsidian 部署

- 版本：1.12.7，安装到 `C:\Users\kid\AppData\Local\Obsidian\`
- Vault 路径：`E:\codex\brain`（直接作为 Obsidian 仓库）

---

## 归档规范（从本日起）

系统配置类文件命名：`YYYY-MM-DD-操作简述.md`
存放位置：`wiki/topics/`
