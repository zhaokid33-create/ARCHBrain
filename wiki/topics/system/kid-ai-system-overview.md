# kid 本机 AI 系统全景

tags: [系统架构, 部署, AI助手]
updated: 2026-04-14
sources: [claude-code memory files]

## Summary
kid 在 E 盘本地部署了一套完整的 AI 工作站，包含两个 agent（OpenClaw/百香果、Hermes）、
一个语义记忆层（MemPalace，已合并进 Brain）、一个外置知识库（Brain），共用 Honoursoft 中转 API。

## 系统清单

| 系统 | 路径 | 启动方式 | 状态 |
|------|------|----------|------|
| OpenClaw (百香果) | E:\codex\openclaw | OpenClaw-Start.bat | 运行中，端口18789 |
| Hermes | E:\codex\hermes | `cd E:\codex\hermes; python -m gateway.run` | 运行中 |
| MemPalace | E:\codex\mempalace | 已合并进 Brain，不单独使用 | 语义索引层 |
| Brain 外置知识库 | E:\codex\brain | brain-wakeup.py | 运行中，Obsidian 可视化 |
| Obsidian | AppData\Local\Obsidian | 桌面启动 | Vault: E:\codex\brain |

## API 配置

- Provider: Honoursoft (OpenAI-compat 中转)
- Base URL: https://us.honoursoft.cn/v1
- Model: claude-sonnet-4-6
- Key: 见 ~/.hermes/config.yaml

## Hermes 配置

- 源码: E:\codex\hermes（版本 0.8.0，Python 3.14）
- 实际配置文件: C:\Users\kid\.hermes\config.yaml
- memory.provider: brain
- auxiliary.vision.provider: auto（自动选 custom/openai-codex）
- Brain 插件: E:\codex\hermes\plugins\memory\brain\__init__.py

## Brain 外置知识库

- 根目录: E:\codex\brain\
- 三层: raw/（原料）、wiki/（结构化知识）、outputs/（成果）
- CLI: `python E:\codex\brain\brain-wakeup.py`
- 语义搜索: `brain-wakeup.py search <query>` → 走 MemPalace brain_wiki wing
- 重新索引: `brain-wakeup.py compile` → mine wiki/ raw/ outputs/

## MemPalace 配置（作为 Brain 的语义层）

- Palace: E:\codex\mempalace\palace\
- Brain wing: brain_wiki，Rooms: wiki / raw / outputs
- 不再单独维护，统一通过 brain-wakeup.py 操作

## OpenClaw 配置

- 工作区: E:\codex\openclaw\workspace\
- 助手身份: 百香果，建筑师 kid 的工作助手
- auth-profiles.json 是 gateway 鉴权唯一来源（不读环境变量）
- 默认模型: honoursoft/claude-haiku-4-5-20251001

## 归档规范

系统配置类 wiki 文件命名：`YYYY-MM-DD-操作简述.md`，存放于 `wiki/topics/`

## 关键踩坑记录

1. Hermes 401: ~/.hermes/config.yaml 不存在时走 auto-detect，GEMINI_API_KEY 被优先选中
2. OpenClaw gateway 模式只读 auth-profiles.json，不读环境变量
3. MemPalace YAML 描述字段只能用 ASCII（Windows GBK 读取）
4. Hermes vision 大图（>5MB base64）honoursoft 静默返回空，需主动 resize
5. `hermes gateway` 命令在 Windows 上静默退出，用 `python -m gateway.run`

## 相关文档
- 
- 

## Update 2026-04-15

# kid 本机 AI 系统全景

tags: [hermes, brain, obsidian, mempalace, system]
updated: 2026-04-15

## Summary
kid 本机 AI 工作系统，以 Hermes Agent 为核心，Brain 为外置知识库，Obsidian 为查阅界面，MemPalace 为语义索引。

## Key Points
- Hermes Agent：本机 AI 助手，CLI + 多平台 gateway
- Brain：E:\codex\brain\ 三层知识库（raw / wiki / outputs）
- Obsidian vault：E:\codex\brain（与 Brain 目录一致，用于管理和查阅 brain 内容）
- MemPalace：E:\codex\mempalace\ 语义索引层
- 每周五 18:00 自动编译：compile_architecture.py

## Pitfalls
1. MemPalace YAML 描述字段只能用 ASCII（Windows GBK 读取）
2. brain-wakeup.py 传中文内容用 @文件路径 方式，避免命令行编码问题

## Links
- 

