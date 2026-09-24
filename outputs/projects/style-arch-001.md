# 风格库条目 style_arch_001 - 金属几何建筑模型极简棚拍

date: 2026-05-04

# 风格库条目 v1.1

- machine_name: style_arch_001
- human_name.zh: 冷灰金属体块极简风
- human_name.en: Cool Gray Metallic Massing Minimalism
- model: Gemini nanobanana2
- source_image: C:/Users/kid/Pictures/style_probe_001.png (re-encoded for analysis)
- version: v1.0
- mode_support: render_mode, lineart_mode

## 1) 视觉元素拆解

### 构图
- 竖构图，主体居中偏下，留白充足。
- 单体建筑模型静物拍摄，前中后景分层清晰。
- 方体+圆柱对比，门洞形成视觉穿透与导视。
- 轻微三维透视，可见正立面、侧面与顶部关系。

### 光影
- 柔和定向棚拍光（偏左前上方），硬阴影很少。
- 高光集中在棱边与圆柱曲面，阴影平滑过渡。
- 开窗和门洞形成深色空腔，对比强但不刺眼。

### 色彩
- 低饱和冷中性：银灰、铅灰、浅蓝灰。
- 以明度对比为主，色相对比弱。
- 局部微暖反射（轻微棕灰）作为材质噪声。

### 材质
- 主体为拉丝金属薄板感，半哑光到丝光。
- 可见拼接、打磨、轻微划痕，强调手作工业痕迹。
- 硬质、冷感、理性，结构表达优先。

### 成像特征
- 工作室静物摄影语言，干净背景。
- 中等景深，主体整体清晰。
- 高锐度但不过度锐化，动态范围稳定。

### 情绪
- 克制、理性、当代、实验性。
- 展陈感强，偏建筑概念模型审美。

## 2) 纹理特征画像

- macro_texture: 中等密度、非均匀、方向性弱
- micro_texture: 细拉丝 + 轻划痕 + 拼接边缘毛刺极少
- roughness: 0.42-0.58
- specular: 中等（边缘高于面）
- anisotropy: 轻微
- aging_wear: 轻旧化（工艺磨痕）
- grain/noise: 画面干净，颗粒弱
- tactile_impression: 冷硬、干燥、轻磨砂
- texture_keywords_cn: 金属拉丝, 手作拼接, 半哑光工业面
- texture_keywords_en: brushed metal, handcrafted seams, semi-matte industrial surface

## 3) 风格总结

### 中文
一句话：以冷灰金属体块和柔光棚拍构成的极简建筑模型风，强调方圆体量对比与结构穿透。
扩展：该风格核心是“体块秩序 > 装饰细节”。通过低饱和冷色和均匀背景抬高主体辨识度，借助门洞与窄窗形成深度节奏。材质以拉丝金属与轻工艺痕迹为识别锚点，情绪克制、理性，适合建筑概念展示、竞赛气质图、当代设计陈列图。

### English
One-line: A cool-gray metallic massing style for architectural concept models, using soft studio lighting and minimalist staging to emphasize geometric contrast and spatial penetration.
Extended: The style prioritizes massing order over decoration. Low-saturation neutral tones and a clean background improve object readability, while apertures and slit windows create depth rhythm. Brushed metal and subtle fabrication marks act as key texture anchors. The mood is restrained and rational, ideal for concept architecture visuals and design exhibition renders.

## 4) 命名
- machine_name: style_arch_001
- human_name.zh: 冷灰金属体块极简风
- human_name.en: Cool Gray Metallic Massing Minimalism
- rationale: 建筑域（arch）+ 首条序号；中文名包含色调（冷灰）、材质（金属）、形体语言（体块）和审美指向（极简）。

## 5) Gemini nanobanana2 提示词

### A) render_mode

#### CN 正向
建筑概念模型风格渲染，主体为现代几何体量建筑，方形主盒体与竖向圆柱附体组合，保留门洞穿透与窄竖窗节奏，竖幅居中构图，前中后层次清晰，大面积干净留白背景；柔和棚拍定向光从左前上方照射，阴影边缘柔化，高光集中在金属棱边与圆柱曲面；整体低饱和冷灰配色（银灰、铅灰、浅蓝灰），以明度对比塑形；材质为拉丝金属薄板，半哑光，带轻微拼接痕迹与细划痕；成像干净、细节克制、理性当代、展陈质感。

#### CN 负向
过饱和色彩，霓虹灯氛围，杂乱背景，道具堆积，木纹或织物主材质，塑料感反射，镜面过曝，阴影死黑，结构扭曲，透视错误，开窗比例异常，过度锐化光晕，噪点脏污，水印文字logo。

#### EN Positive
Architectural concept model style render, modern geometric massing with a rectangular main block and a vertical cylindrical attachment, preserving a through-opening portal and narrow slit windows; portrait-centered composition with clear foreground-midground-background separation and generous clean negative space. Soft directional studio light from upper-left front, smooth shadow transitions, highlights concentrated on metal edges and cylindrical curvature. Low-saturation cool neutral palette (silver gray, lead gray, pale blue-gray), form defined mainly by luminance contrast. Brushed thin-sheet metal material, semi-matte finish, subtle seam marks and fine scratches. Clean imaging, restrained detail, rational contemporary exhibition mood.

#### EN Negative
oversaturated neon colors, cluttered background, prop-heavy scene, wood/fabric dominant materials, plastic reflections, blown-out speculars, crushed blacks, distorted structure, wrong perspective, broken window proportions, oversharpening halos, dirty noise, watermark, text, logo.

#### 构图控制 Composition Control
- portrait ratio 3:4 or 4:5
- single-object centered-lower placement
- large clean background area
- preserve square-vs-cylinder massing contrast
- emphasize portal opening depth

#### 材质纹理控制 Material/Texture Control
- brushed metal micro-scratches: medium-low
- roughness: 0.42-0.58
- specular: medium, edge-enhanced
- avoid mirror-like chrome
- keep seam/joint hints subtle and realistic

#### 光影控制 Lighting Control
- key light: upper-left front, soft
- fill light: low-medium
- shadow: soft edge, non-crushed
- highlight roll-off: smooth
- no dramatic colored rim lights

#### 色彩脚本 Color Script
- Dominant: cool gray
- Secondary: lead gray
- Accent: pale blue-gray
- Saturation: low
- Contrast curve: gentle S-curve
- Tone intent: rational, clean, industrial minimal

#### 参数建议 Params (nanobanana2)
- guidance/strength: 5.8-7.0
- steps: 30-42
- img2img denoise: 0.32-0.48 (保结构)
- style weight: 0.62-0.78
- texture weight: 0.48-0.65
- fixed seed for reproducibility

### B) lineart_mode

#### CN 正向
将输入线稿转为“冷灰金属体块极简建筑”风格线稿深化：严格保留原始轮廓、透视与体块关系，强调方体与圆柱对比、门洞穿透、窄窗比例；外轮廓线中粗，结构线中细，细节线轻；用克制排线表达金属平面转折与圆柱曲率，背景线条极简并弱化，保持高可读性与后续上色友好。

#### CN 负向
结构漂移，透视跑偏，线条粘连断裂，边缘毛糙噪线，明暗脏块，过度细节堆叠，背景喧宾夺主，随机新增构件，窗洞比例错乱。

#### EN Positive
Transform the input line art into the cool-gray metallic massing architectural style while strictly preserving original contours, perspective, and massing relationships. Emphasize square-vs-cylinder contrast, portal penetration, and slit-window proportions. Use medium-bold outer contours, medium internal construction lines, and light detail lines. Controlled hatching should describe planar metal turns and cylindrical curvature. Keep background lines minimal and subdued for high readability and downstream coloring.

#### EN Negative
structural drift, perspective deviation, merged or broken lines, noisy ragged edges, muddy shadow blocks, over-detailed clutter, distracting background, random added components, broken opening proportions.

#### 构图控制
- lock original line composition
- keep dominant silhouette intact
- simplify background by 40-60%

#### 材质纹理控制
- line density indicates metal plane change
- sparse micro-hatching for brushed surface cue
- no organic fabric-like texture patterns

#### 光影控制
- single key-light logic in value planning
- clear separation of lit/mid/shadow planes
- avoid heavy black fills in openings unless intentional depth

#### 色彩脚本（线稿阶段）
- grayscale planning only: subject / secondary / background
- optional cool-gray annotation tags for later render pass

#### 参数建议
- line clarity: high
- edge sensitivity: medium-high
- line weight range: 0.7-2.1
- simplify pass: 1-2
- structure lock strength: high

## 2026-05-04

# 风格库命名更新

日期: 2026-05-04
条目: style_arch_001

- 原 human_name.zh: 冷灰金属体块极简风
- 新 human_name.zh: 金属模型

备注:
- machine_name 保持不变: style_arch_001
- 英文显示名同步简化为: Metallic Model
- 该命名更新不影响既有 render_mode / lineart_mode 提示词模板，仅更新检索名与调用别名。
