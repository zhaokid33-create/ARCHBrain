# 风格细则：style_arch_004 / 胶片草地

- style_id: style_arch_004
- machine_name: style_arch_004
- human_name.zh: 胶片草地
- human_name.en: Filmic Grassland
- aliases: 草地处理, Grassland Grading
- source: C:\Users\kid\Pictures\4.PNG
- scope_lock: 仅用于草地部分纹理处理（exclusive）

## 命名变更记录
- 2026-05-05: 孤屋青岭 -> 草地处理
- 2026-05-05: 草地处理 -> 胶片草地（当前）

## 用途锁定
该风格专门用于“草地区域”的纹理与质感处理，不用于整图风格迁移。

允许：
- 草地粗糙度/颗粒/绒面质感增强
- 草地受光与阴影层次优化
- 草地材质替换（保持地形与构图）

禁止：
- 建筑体量与立面风格改写
- 天空、山体主色整体重映射
- 全画面风格覆盖

## 局部编辑约束模板
- 仅修改草地区域纹理与材质表现
- 保持建筑、山体、天空、道路、人物位置与形态不变
- 保持原始构图、透视、体量关系不变
- 禁止新增文字、水印、logo

## 视觉DNA
- 构图：纵向画幅；小屋位于下1/3；大面积山体负空间；斜向坡线引导。
- 体量：小体量双坡顶建筑嵌入大尺度连续草坡。
- 材质：草地绒面漫反射；墙体浅米灰；屋顶棕灰风化质感。
- 光影：低角度侧光；深阴影；电影化明暗分区。
- 色彩：低饱和冷绿主导，暖灰作为建筑微对比。

## 主色板
- #07373E
- #0B4A4D
- #1E5F5D
- #6F7E5D
- #A59A7A
- #7D6C57

## texture_profile
```yaml
terrain_grass:
  roughness: 0.72
  specular: 0.10
  anisotropy: 0.18
  grain: 0.35
  seam_density: 0.08
  weathering: 0.40
mountain_surface:
  roughness: 0.78
  specular: 0.06
  anisotropy: 0.22
  grain: 0.30
  seam_density: 0.05
  weathering: 0.32
cabin_wall:
  roughness: 0.62
  specular: 0.12
  anisotropy: 0.05
  grain: 0.28
  seam_density: 0.20
  weathering: 0.55
cabin_roof:
  roughness: 0.48
  specular: 0.22
  anisotropy: 0.42
  grain: 0.25
  seam_density: 0.45
  weathering: 0.60
```

## render_mode要点
- 保持构图与地形体量不变
- 低角度侧光 + 深冷阴影
- 低饱和冷绿分级，避免过锐化/过饱和

## lineart_mode要点
- 低密度线稿，强调坡线与体块边界
- 以明暗块替代高频排线

## 负向约束
结构扭曲、透视错误、比例失衡、过饱和、过锐化、脏噪点、文字水印、logo、塑料感
