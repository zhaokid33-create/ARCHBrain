# 风格细则：lineart_arch_002 / 素描轴测

- style_id: lineart_arch_002
- machine_name: lineart_arch_002
- human_name.zh: 素描轴测
- human_name.en: Sketch Axonometric
- aliases: 轴测线稿, 建筑地形轴测素描, 结构拼贴轴测
- source: C:\Users\kid\Pictures\f50ab88852b74eaffbfe23abc4a1cf67_reencode.jpg
- mode: lineart

## 风格摘要
以轴测骨架组织建筑与地形关系，用素描式线密度而非灰涂塑造层次。图面呈现“结构理性 + 手绘纹理”的并置特征，留白大，黑实面少量点锚。

## 视觉DNA
- 构图：对角线推进（左下->右上），前中后层级清晰，信息分区有疏密梯度。
- 投影：轴测体系为主（平行线不收敛），局部允许手绘漂移与拼贴式信息叠加。
- 线权系统：
  - 一级：主轮廓/切线（重）
  - 二级：结构分缝/构件线（中）
  - 三级：材质纹理/地形线（细）
  - 四级：远景弱信息/气氛线（极轻）
- 线型：直线结构 + 短线簇 + 点描混合；排线顺形体走向。
- 明暗组织：少量深黑锚点 + 线密度中灰 + 大面积留白高光。
- 材质表达：
  - 岩石：碎短线与不规则块
  - 土坡：顺坡向连续线
  - 混凝土/砌体：规则分缝网格
  - 金属构架：直线重复、节点清晰
- 留白策略：背景与非核心区主动留白，避免满版填充。

## lineart_mode 模板要点
- 轴测骨架优先，禁止明显透视收束。
- 黑白单色线稿，禁止彩色与照片化渐变。
- 四级线权协同，优先靠密度差控制主次。
- 建筑硬边与地形手绘纹理并置。
- 黑实面仅作锚点（少量），白场占主导。
- 拼贴式信息可存在，但主体结构必须可读。

## 可复制提示词（CN）
```text
黑白建筑地形轴测线稿，平行投影骨架，建筑与山体/河谷关系清晰；主轮廓重线，结构分缝中线，地形与材质纹理使用细线与点描，排线顺形体走向；少量深黑面作为视觉锚点，大面积留白保持图纸呼吸感；整体气质理性、克制、学术制图感。
```

## Copy-ready Prompt (EN)
```text
Monochrome architectural-terrain axonometric line drawing, parallel projection structure, clear relationship between building mass and topography; strong primary contours, medium structural seams, fine texture lines and stippling for terrain/materials with form-following hatching; sparse deep-black anchors and dominant white negative space; rational, restrained, academic drafting mood.
```

## 参数建议
- steps: 26-40
- guidance: 5.2-6.8
- denoise(img2img): 0.28-0.48
- projection_lock: axonometric (vanishing_strength 0.0-0.15)
- line_weight: contour=high, structural=mid, texture=low, atmosphere=very_low
- whitespace_ratio: 0.65-0.80
- solid_black_ratio: 0.03-0.08
- seed: 固定

## 负向约束
CN：单点/双点透视强收敛，结构扭曲，比例失衡，线条抖动，线权混乱，过密同向排线，过度涂黑，照片化灰阶渐变，彩色渲染，脏噪点，文字水印，logo，重影。

EN: strong one/two-point perspective convergence, structural distortion, broken proportions, jittery lines, inconsistent line weight, over-dense uniform hatching, overfilled blacks, photo-like smooth grayscale gradients, color rendering, dirty noise, watermark, logo, ghosting.

## 记录
- 2026-05-05: 首次收录，命名为“素描轴测”。
- 2026-05-05: 原图解析异常后重编码为 reencode.jpg 再完成提取与入库。