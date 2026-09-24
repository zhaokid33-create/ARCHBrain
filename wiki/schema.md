# Brain Schema — AI Processing Rules

## Layers

| Layer   | Path         | Rule                                       |
|---------|--------------|--------------------------------------------|
| raw     | raw/         | NEVER modify. Append-only source material. |
| wiki    | wiki/topics/ | AI-maintained. Upsert by topic slug.       |
| outputs | outputs/     | AI-generated. Timestamped, never edited.   |

## Wiki Page Format

Every file in `wiki/topics/` must follow this structure:

```
# <Topic Title>

tags: [tag1, tag2, tag3]
updated: YYYY-MM-DD
sources: [raw/articles/foo.md, ...]

## Summary
One paragraph overview.

## Key Points
- Point 1 (max 7 total)
- Point 2

## Details
Extended content, examples, context.

## Links
- 
- 
```

## Compile Rules (raw → wiki)

1. Read source file from raw/
2. Extract: title, core points (max 7), key terms, related topics
3. Check wiki/topics/ for existing page with same slug
4. If exists: merge Key Points (deduplicate), update Summary, append new sources
5. If new: create page using format above
6. Update INDEX.md entry for this topic

## Output Format

- `outputs/qa/<slug>-YYYYMMDD.md` — question + answer pairs
- `outputs/summaries/<slug>-YYYYMMDD.md` — condensed summary of a raw source
- `outputs/projects/<slug>.md` — ongoing project notes (upsert allowed)

## Slug Rules

- Lowercase, hyphens only, no spaces
- Example: "Machine Learning Basics" → `machine-learning-basics`

## INDEX.md Format

Auto-maintained by brain-wakeup.py. Each entry:
```
- [topic-slug](wiki/topics/topic-slug.md) — one-line description | updated: YYYY-MM-DD
```

## Architecture Case Compile Rules (建筑案例专项)

编译建筑类 wiki 时，识别为建筑案例后额外执行：

1. 提取以下字段：
   - 地区（国家/城市）→ 写入 `outputs/architecture/regions.md`
   - 风格/流派 → 写入 `outputs/architecture/styles.md`
   - 建筑类型 → 写入 `outputs/architecture/building_types.md`
   - 设计方法/策略 → 写入 `outputs/architecture/design_methods.md`
2. 每个条目格式：`- 案例名称` + 一行关键词说明
3. 追加到对应分类下，不覆盖已有内容

## 检索流程

1. 快速定位 → `outputs/architecture/` 下按关键词找案例名+wiki链接
2. 详细信息 → 跳转对应 `wiki/topics/architecture/` 页面（底层由 mempalace 向量索引支撑）

## Daily Usage

1. See useful content → `brain-wakeup.py add-raw notes "<title>" "<content>"`
2. Weekly → `brain-wakeup.py compile` (mines wiki into MemPalace)
3. Need knowledge → ask agent: "基于brain总结XX" or call `brain_search`
