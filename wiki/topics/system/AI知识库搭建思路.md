# AI知识库搭建思路

tags: [知识管理, AI, 外置大脑, agent-system, architecture]
updated: 2026-04-13
sources: [raw/notes/ai-2026-04-13.md]

## Summary
三层架构的个人AI知识库系统，实现agent无关的外置大脑。人只负责投喂原料，AI负责整理和检索。

## Key Points
- raw/：原始素材仓，只进不出，永不修改
- wiki/：AI自动维护的结构化知识库，人类极少手动编辑
- outputs/：AI生成的问答、报告、总结等可复用成果
- 日常只需把内容丢进raw，每周让AI编译到wiki
- 需要用知识时直接问AI：基于wiki总结XX/给我XX方案

## Details
搭建流程：
1. 建库（三层目录）
2. 投喂（丢进raw）
3. AI规则（schema定义格式）
4. 自动编译（raw提炼到wiki）
5. 使用（自然语言提问）

日常极简流程：
- 看到有用内容 → 丢进raw
- 每周一次 → AI编译到wiki
- 需要用知识 → 直接问AI

## Links
- 
- 
- 

