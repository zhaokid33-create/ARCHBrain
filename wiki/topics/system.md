# system

tags: []
updated: 2026-04-18
sources: []

# 百香果知识调用标准流程

updated: 2026-04-18

## 查询流程（信息调用）

```
1. MemPalace 快速定位
   brain_search 关键词 → 找到相关条目在哪个层级/文件
   目的：缩短上下文，不盲目读大文件

2. outputs 优先读取
   去 outputs/architecture/ 读对应索引
   （案例总索引、building_types、regions、design_methods、README）
   目的：outputs 是精简导航层，快速确认方向和范围

3. 按需下钻 wiki
   outputs 定位后，去 wiki/topics/architecture/ 读专题或案例库详情
   目的：获取结构化知识内容

4. raw 是最后手段
   wiki 没有才去 raw 找原始素材
   找到后必须编译回 wiki + 同步下游索引

5. 联网补充是兜底
   brain 完全没有才联网
   补充后必须写回 wiki + 同步所有相关下游索引
```

层级与信息密度对应：
```
MemPalace → 定位（最低token消耗）
outputs   → 导航（精简索引）
wiki      → 内容（结构化知识）
raw       → 原料（未编译素材）
web       → 兜底（外部补充）
```

## 新增信息流程（信息写入）

```
1. 判断信息类型
   - 理论文章 → wiki 专题 + 更新 design_methods/styles
   - 建筑案例 → wiki 案例库 + 更新案例总索引/building_types/regions
   - 不是案例也不是理论 → 视内容决定层级

2. 查总索引查重
   先查 outputs/案例总索引.md，有则补充信息，没有则新建

3. 写入 wiki
   大文件分块写入，每次控制在 200 行左右
   先 write_file 创建基础结构，再 terminal append 追加内容

4. 同步所有下游索引（系统一致性原则）
   上游改了，下游必须同步
   案例类：案例总索引 + building_types + regions（+ styles/design_methods 视情况）
   理论类：design_methods 或 styles（视内容）
   不需要更新的索引：不动
```

## 系统一致性原则

- 信息系统存在层级关联和索引，上游修改必须追踪到所有下游
- 任何对案例名称/内容的修改，同步到：building_types、regions、案例总索引
- 判断哪些下游需要更新：看信息类型，不多也不少
- 删除/重命名前必须备份（血泪教训）

## Update 2026-04-18

# 破坏性操作原则（最高优先级）

updated: 2026-04-18

## 核心规则

- **删除、重命名、覆盖任何文件前，必须先告知 kid 并等待确认**
- **执行前先备份到临时目录**（如 `E:\codex\brain\_backup\`）
- 没有 Ctrl+Z，操作不可逆
- 读取、整理、新建 → 自由执行
- 删除、覆盖、重命名 → 必须授权

## 背景

曾经因 cleanup 脚本使用过激正则，将手动整理的毕设专题 wiki 和 styles/design_methods 内容一并删除，被迫从 raw notes 重建。代价惨重。

## 操作前检查清单

1. 这个操作会不会删除或覆盖现有内容？
2. 如果会 → 先备份，再告知 kid，等确认
3. 如果不会 → 正常执行

## 备份方式

```python
import shutil
shutil.copy(src, r'E:\codex\brain\_backup\文件名_backup_YYYYMMDD.md')
```

