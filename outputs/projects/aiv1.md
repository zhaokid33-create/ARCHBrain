# AI风格提取与提示词风格库工作流v1

date: 2026-05-04

# AI风格提取与提示词风格库工作流 v1

日期: 2026-05-04
适用模型: Gemini nanobanana2
命名策略: 双轨命名（machine_name + human_name）
输出语言: 中英双语
模板策略: 全模块（正向/负向/构图/材质纹理/光影/色彩/参数）

## 1. 输入类型
- A类输入（建库）: 用户发送风格参考图
- B类输入（调用）: 用户发送渲染图 + 指定风格名

## 2. A类流程（建库）
1) 视觉拆解
- 主体与场景
- 构图（视角、焦段感、留白、透视）
- 光影（主光方向、反差、体积雾、高光roll-off）
- 色彩（主色/辅色、饱和度、色温、分离色）
- 材质与纹理（粗糙度、反射、颗粒、噪点、边缘硬度）
- 成像特征（胶片感、锐化、色散、暗角、运动模糊）
- 情绪语义（叙事气质）

2) 风格归纳
- 用3层结构描述: 视觉骨架 / 材质语法 / 后期语法

3) 双轨命名
- machine_name: style_<domain>_<index>
- human_name: 人类可读中文名

4) 提示词模板生成（中英双语）
- 正向提示词模板
- 负向提示词模板
- 构图控制词
- 材质/纹理控制词
- 光影控制词
- 色彩脚本
- 参数建议（Gemini nanobanana2）

5) 入库
- 追加到总风格库（可检索）

## 3. B类流程（调用）
1) 读取目标风格模板
2) 解析用户渲染图的内容要素（主体/功能/场景）
3) 将内容要素填入模板槽位
4) 输出可直接复制的完整提示词（中英双语）

## 4. 风格库单条记录结构
- machine_name
- human_name
- style_summary_cn
- style_summary_en
- visual_elements
- texture_profile
- prompt_template_cn
- prompt_template_en
- negative_prompt_cn
- negative_prompt_en
- control_blocks (composition/material/light/color)
- model_params (nanobanana2)
- use_cases
- avoid_list
- version

## 5. 版本规则
- 新增风格: v1
- 微调词汇: v1.1 / v1.2
- 结构性重写: v2

## 6. 触发口令（建议）
- 建库: “收录风格”
- 调用: “套用风格 <machine_name或human_name>”

