# Brain 外置知识库系统架构

tags: [系统架构, 知识库, 自动化, agent-system]
updated: 2026-04-13
sources: [hermes session]

## Summary
共享知识库，供所有 AI agent 使用，位于 E:\codex\brain\。

## Key Points
- 三层结构：raw（原料）、wiki（结构化知识）、outputs（成果）
- 所有 agent 通过 brain-wakeup.py CLI 读写
- MemPalace 提供 ChromaDB 语义检索
- Hermes 使用 brain 插件，OpenClaw 直接访问文件

## 自动编译脚本
- 文件路径：`E:\codex\brain\compile_architecture.py`
- 功能：扫描 raw/ 中的建筑案例文件，交叉编译到 wiki/ 各维度分类页面
- 定时任务：每周五 18:00，Windows 任务计划程序

## Links
- 
- 
- 
