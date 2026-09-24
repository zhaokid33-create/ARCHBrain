# 风格细则：lineart_arch_001 / 素描平面

- style_id: lineart_arch_001
- machine_name: lineart_arch_001
- human_name.zh: 素描平面
- human_name.en: Sketch Plan
- aliases: 建筑平面线稿, 高留白测绘风, 极简场地图
- source: C:\Users\kid\Pictures\d268e9144055fb0ca21450e34a28cadb_reencode.jpg
- mode: lineart

## 风格摘要
建筑总平/场地平面线稿风格，采用正投影俯视表达。以高留白、克制线权、结构优先为核心，强调理性制图感与安静图面气质。

## 视觉DNA
- 构图：偏置T形总体组织，信息集中于中部，四周大面积留白。
- 视角：orthographic top view（正投影俯视），非透视图。
- 线权系统：
  - 一级：外轮廓/主体边界（最粗最黑）
  - 二级：内部墙体/结构分隔（中等）
  - 三级：铺装/构造细部（细线）
  - 四级：植被/环境痕迹（淡灰轻线）
- 线型：轮廓硬边清晰，结构线规整理性，细节线克制服务造型。
- 明暗组织：不做体块渲染，以线密度与线粗细形成层次。
- 材质表达：铺装以重复线组/网格提示；植被用符号化轻笔触。
- 留白策略：大留白主导，主体“漂浮”于纸面，增强呼吸感与秩序感。

## lineart_mode 模板要点
- 纯黑白线稿，禁彩色。
- 保持正投影平面视角，禁止透视化。
- 外轮廓最强，结构线次之，细部线最轻。
- 以结构识别优先，避免装饰性过绘。
- 背景与边缘保持高留白，信息集中在主体。
- 允许少量铺装网格与植被符号，禁止噪声化纹理。

## 可复制提示词（CN）
```text
黑白建筑总平线稿，正投影俯视，场地平面表达；主体采用清晰外轮廓粗线，内部结构与分隔使用中等线权，铺装与细部使用细线；图面高留白，信息集中于主体区域，背景克制简洁；植被以符号化轻线表示；整体呈现理性、安静、档案式制图气质。
```

## Copy-ready Prompt (EN)
```text
Monochrome architectural site plan lineart, orthographic top view, clean drafting style; strong outer contour lines for main massing, medium-weight interior structure lines, thin detail lines for paving and minor elements; large white negative space, information concentrated around the core composition; sparse symbolic vegetation marks; calm, rational, archival architectural drawing mood.
```

## 参数建议
- steps: 24-36
- guidance: 5.0-6.8
- denoise(img2img): 0.25-0.45
- line_weight: outer=high, structure=mid, detail=low
- seed: 固定

## 负向约束
CN：结构扭曲，透视错误，线条抖动，线权混乱，轮廓粘连，过度涂黑，过密交叉排线，脏噪点，文字水印，logo，重影，彩色渲染，3D体积光。

EN: structural distortion, wrong perspective, jittery lines, inconsistent line weight, merged contours, overfilled blacks, dense cross-hatching noise, dirty artifacts, watermark, logo, ghosting, color rendering, volumetric 3D lighting.

## 记录
- 2026-05-05: 首次收录，命名为“素描平面”。
- 2026-05-05: 采用 MemPalace 故障回退路径（L1->L2->L3 最小读取）完成入库。