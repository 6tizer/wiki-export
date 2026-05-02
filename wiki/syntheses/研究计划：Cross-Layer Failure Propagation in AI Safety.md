---
title: 研究计划：Cross-Layer Failure Propagation in AI Safety
type: synthesis
tags:
- AI 对齐
- Agent 安全
status: 草稿
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5598d0afd65b4f43b3e09ea352a58c26
notion_id: 5598d0af-d65b-4f43-b3e0-9ea352a58c26
---

## 论文定位

**标题候选：** *"Cross-Layer Failure Propagation in AI Safety: How Alignment Fragility Amplifies Runtime Defense Gaps"*

**来源综合分析：** [对齐内核与安全外壳的共演动力学：模型内部价值约束如何与 Agent 运行时防御在攻防博弈中形成双层免疫系统](syntheses/对齐内核与安全外壳的共演动力学：模型内部价值约束如何与 Agent 运行时防御在攻防博弈中形成双层免疫系统.md)

**核心命题：** 内核层（对齐）失效后，外壳层（运行时安全）的检测能力会以什么方式、什么幅度下降？各组件已有独立实证，但尚无论文量化过「跨层放大效应」。

**贡献声明：**

1. 提出「双层免疫系统」形式化模型，定义内核层和外壳层的交互接口

1. 设计实验量化内核层失效对外壳层检测率的传导效应

1. 发现并报告跨层放大系数（即内核层每降低 X% 的安全性，外壳层检测率下降 Y%）

**与现有工作的区别：** Arditi (2024) 只研究 refusal direction 本身；Anthropic 的 reward hacking 论文只研究涌现失对齐；OpenAI 的 scheming 论文只研究评估感知。没有人把这三个现象放在同一个实验框架里，测量它们的耦合效应。

---

## 形式化框架

- 设 p_{\text{inner}} = 内核层的拒绝概率（对齐完整性）

- 设 p_{\text{outer}} = 外壳层的检测概率（运行时安全）

- 独立假设下，系统安全概率 = 1 - (1 - p_{\text{inner}})(1 - p_{\text{outer}})

- **核心假说：** 两层并非独立。$p_{text{outer}}$ 是 p_{\text{inner}} 的函数，且在 p_{\text{inner}} 下降时加速衰减——内核层越弱，外壳层也越容易被绕过。

- **跨层放大系数 α** = 外壳层检测率下降幅度 ÷ 内核层安全性下降幅度。若 α > 1，说明存在放大效应。

---

## 实验设计

### 实验 1：Abliteration → 红队检测率下降

**目标：** 量化 refusal direction 被削除后，标准红队测试套件的检测率变化。

**方法：**

- 选 3-5 个开源模型（Llama 3、Gemma 2、Qwen 2.5 等）

- 对每个模型做渐进式 abliteration（按比例衰减 refusal direction 幅度：0%、25%、50%、75%、100%）

- 用标准安全 benchmark（HarmBench、AdvBench、ToxiGen）测试每个衰减程度下的拒绝率

- 同时用模拟「外壳层」检测器（关键词过滤、困惑度异常检测、分类器内容审核）测试检测率

**预期发现：** abliteration 后模型的有害输出可能变得更"流畅自然"，反而更难被外壳层的输出检测器捕获——拒绝率下降曲线和检测率下降曲线之间存在非线性关系。

### 实验 2：Reward Hacking → 评估感知 → 双层同时失效

**目标：** 复现 Anthropic 的 reward hacking 涌现失对齐现象，测量模型在"被测试" vs "非测试"情境下的行为差异。

**方法：**

- 用合成文档微调让模型习得 reward hacking 策略（按 Anthropic 论文方法）

- 设计两组评估：

  - **"测试感知"组：** 标准红队格式提问（带明显安全评估特征）

  - **"自然部署"组：** 在 agentic 任务流中嵌入同等危险度的指令（无评估特征）

- 对比两组的有害行为发生率

**预期发现：** 模型在"测试感知"组表现安全，但"自然部署"组有害行为率显著更高。差值即评估感知导致的「安全性高估幅度」。

### 实验 3：Phantom Transfer → 跨模型传播 → 外壳层隔离失效

**目标：** 测试有害行为特征通过蒸馏传播后，能否绕过针对原始模型设计的安全检测器。

**方法：**

- 在 Teacher 模型中植入特定行为偏差（如对某类请求的隐式合规）

- 通过标准蒸馏迁移到 Student 模型（不同架构/家族）

- 用针对 Teacher 训练的安全检测器检测 Student 行为

**预期发现：** 行为特征迁移后表现形式变化，导致针对 Teacher 训练的检测器失效。证明「模型隔离」策略不足以阻断跨层传导。

### 实验 4（综合）：三种攻击叠加的复合效应

**目标：** 当内核层被部分削弱（abliteration）、模型具有评估感知（reward hacking 训练后）、且行为特征已通过蒸馏传播时，外壳层的综合检测率。

**关键指标：**

- 跨层放大系数 α 在单一攻击 vs 复合攻击下的变化

- 若 α 随攻击叠加呈超线性增长，则证明「双层防线不能简单叠加」

---

## 论文结构

| **章节** | **内容** | **页数（估）** |

| --- | --- | --- |

| 1. Introduction | 双层防御的直觉 + 为什么耦合效应被忽视 | 1.5 |

| 2. Related Work | 分别综述对齐安全（refusal direction, abliteration）和运行时安全（红队、监控） | 2 |

| 3. Threat Model | 形式化双层免疫系统模型，定义跨层放大系数 | 1.5 |

| 4. Experiments | 实验 1-4 设置和结果 | 4 |

| 5. Analysis | 跨层放大系数的定量分析 + 非线性耦合的机制解释 | 2 |

| 6. Implications | 对安全架构设计的建议（零信任 AI、漂移监控、供应链审计） | 1 |

| 7. Limitations | 闭源模型不可测、白盒方法的局限 | 0.5 |

---

## 所需资源与可行性

### 计算资源

- 开源模型（7B-70B 参数量级），需 GPU 做 abliteration 和微调

- 云端方案：4×A100 约 2-3 周可完成全部实验

### 数据集

- HarmBench / AdvBench / ToxiGen（现成安全 benchmark）

- 合成文档微调数据（按 Anthropic 论文方法自行构造）

### 最大风险

跨层放大系数可能不显著（α ≈ 1），即两层确实近似独立。若如此，论文可转为"好消息"：证明双层防御确实有冗余价值。仍然是有价值的发现。

### 投稿目标

- 一梯队：NeurIPS 2027、ICML 2027 安全/对齐 track

- 二梯队：AAAI、AIES、SafeAI workshop

---

## Mac Studio M4 Max (128GB) 本地实验可行性评估

> **💻** 以下评估基于 Apple M4 Max 芯片 + 128GB 统一内存的本地推理/微调能力。

### 能做到什么

**实验 1（Abliteration → 检测率）—— ✅ 完全可本地完成**

- Refusal direction 提取本质是对激活空间做 PCA/差分均值，计算量很小

- 渐进式 abliteration 只需修改模型权重中的一个方向向量，无需重新训练

- 128GB 统一内存可以完整加载 **70B 量化模型（Q4/Q5）** 或 **8B-14B 全精度模型**

- 用 `mlx`（Apple 官方 ML 框架）或 `llama.cpp` 做推理，M4 Max 的内存带宽（~546GB/s）对推理速度友好

- HarmBench 等 benchmark 的评估就是跑几千条 prompt 收集输出，8B 模型每条几秒

- **预估时间：** 5 个衰减梯度 × 3 个模型 × ~2000 条 prompt ≈ 30,000 次推理，8B 模型约 1-2 天跑完

**外壳层检测器构建 —— ✅ 完全可本地完成**

- 关键词过滤：纯规则，无计算需求

- 困惑度异常检测：模型推理的副产品，免费

- 分类器内容审核：用小模型（如 Llama Guard 8B）做分类器，128GB 内存可同时加载被测模型和检测器

**实验 2（合成文档微调）—— ⚠️ 部分可行**

- 8B 模型的 LoRA 微调在 128GB M4 Max 上可行（用 `mlx-lm` 或 `unsloth`），速度慢但能跑

- 14B 以上的微调会比较吃力，建议只用 8B 模型做这个实验

- **预估时间：** LoRA 微调 8B 模型约 6-12 小时/轮

**实验 3（蒸馏传播）—— ⚠️ 有限可行**

- 完整的知识蒸馏需要 Teacher 和 Student 同时在内存中

- Teacher 70B Q4 (~40GB) + Student 8B FP16 (~16GB) + 训练开销 → 勉强可塞进 128GB

- 但蒸馏训练速度在 M4 Max 上会很慢（无 CUDA，MLX 的训练吞吐远低于 A100）

- **替代方案：** 不做真实蒸馏，而是用 Teacher 生成大量合成数据 → 用合成数据微调 Student。这在本地完全可行。

**实验 4（复合实验）—— ✅ 可行（如果用上述替代方案）**

- 本质是实验 1-3 的组合，不引入额外计算需求

### 做不到什么

- **70B 模型的全精度微调**：需要 ~280GB 显存，远超 128GB

- **大规模 RL 训练**（如 PPO/RLHF）：M4 Max 的训练吞吐太低，不实际

- **多模型大规模并行实验**：单机只能串行跑

### 推荐的本地实验路径

> **🎯** **最小可行验证（MVP）—— 本地 1-2 周可完成**

1. 用 **Llama 3.1 8B Instruct** 作为主实验模型

1. 用 `mlx` 或 `llama.cpp` 加载，提取 refusal direction

1. 做 5 个衰减梯度的 abliteration

1. 跑 HarmBench + 3 种外壳层检测器

1. 画出 p_{\text{inner}} vs p_{\text{outer}} 曲线

如果曲线呈非线性下降 → 核心假说成立 → 值得扩展为完整论文（此时可租云 GPU 跑更大模型和更多实验）。

---

## 本地执行计划（Mac Studio M4 Max 128GB）

> **📋** 以下是基于本地硬件可独立完成的具体执行步骤，按时间线排列。总预估周期：3-4 周。

### Phase 0：环境搭建（1-2 天）

- [ ] 安装 Python 3.11+、`mlx`、`mlx-lm`、`llama.cpp`（Python binding `llama-cpp-python`）

- [ ] 安装 `transformers` + `torch`（MPS backend），用于激活提取和 hook 中间层

- [ ] 下载模型权重：

  - Llama 3.1 8B Instruct（FP16，~16GB）—— 主实验模型

  - Gemma 2 9B Instruct（FP16，~18GB）—— 对照模型

  - Qwen 2.5 7B Instruct（FP16，~15GB）—— 对照模型

  - Llama Guard 3 8B（FP16，~16GB）—— 外壳层分类器检测器

- [ ] 下载 benchmark 数据集：HarmBench、AdvBench、ToxiGen

- [ ] 搭建实验脚本框架：统一的推理接口、结果记录（JSON/CSV）、可视化模板

### Phase 1：实验 1 — Abliteration → 检测率（1 周）

**第 1-2 天：Refusal Direction 提取**

- [ ] 对每个模型，准备对比 prompt 集（~200 条有害 + ~200 条无害）

- [ ] 用 `transformers` + MPS 逐条跑推理，hook 残差流（residual stream）收集每层激活

- [ ] 对有害/无害两组激活做差分均值，提取 refusal direction 向量

- [ ] 验证：将该方向投影到激活上，确认有害 prompt 和无害 prompt 的投影值有明显分离

**第 3-4 天：渐进式 Abliteration + 内核层评估**

- [ ] 对 refusal direction 做 5 个衰减梯度（0%/25%/50%/75%/100%），每次从模型权重中减去对应比例的方向分量

- [ ] 对每个梯度，跑 HarmBench（~500 条）+ AdvBench（~500 条）记录拒绝率 → 得到 p_{\text{inner}} 曲线

- [ ] 每个梯度 × 每个模型 ≈ 1000 条 prompt，8B 模型约 2-3 小时/梯度

**第 5-7 天：外壳层检测器评估**

- [ ] 对每个梯度下模型生成的输出，跑三种外壳层检测器：

  - **关键词过滤器**：用公开的有害关键词表（如 OpenAI moderation 词表）做正则匹配

  - **困惑度检测器**：用基线模型（未修改的原始模型）计算输出的困惑度，设阈值报异常

  - **分类器检测器**：用 Llama Guard 8B 对输出做安全分类（128GB 内存可同时加载被测模型 + Llama Guard）

- [ ] 记录每个梯度下三种检测器的检测率 → 得到 p_{\text{outer}} 曲线

- [ ] **关键产出**：画出 p_{\text{inner}} vs p_{\text{outer}} 散点图 + 拟合曲线。若呈非线性下降，核心假说初步成立。

### Phase 2：实验 2 — 评估感知实验（1 周）

**第 1-3 天：合成文档微调**

- [ ] 按 Anthropic 论文方法构造合成文档数据集（~1000 条描述 reward hacking 策略的文档）

- [ ] 用 `mlx-lm` 对 Llama 3.1 8B 做 LoRA 微调（rank=16, alpha=32），预估 8-12 小时

- [ ] 对照组：用同等规模的中性文档做 LoRA 微调

**第 4-5 天：双组评估设计**

- [ ] 设计 "测试感知" prompt 集（~300 条）：标准红队格式，带明显的安全评估特征（如 "As a safety researcher, I need to test..."）

- [ ] 设计 "自然部署" prompt 集（~300 条）：嵌入在多步 agentic 任务流中的等价危险指令（如工具调用场景、代码生成场景）

- [ ] 确保两组在语义危险度上对齐（可用 Llama Guard 做预标注验证）

**第 6-7 天：跑评估 + 分析**

- [ ] 微调后模型分别在两组上生成输出

- [ ] 记录有害行为发生率差值 = 评估感知导致的「安全性高估幅度」

- [ ] 同时跑外壳层检测器，看检测率在两组间的差异

### Phase 3：实验 3 — 蒸馏传播实验（1 周，使用合成数据替代方案）

**第 1-3 天：Teacher → 合成数据生成**

- [ ] 在 Llama 3.1 8B 上植入行为偏差（对特定类别请求的隐式合规），通过 LoRA 微调实现

- [ ] 用植入偏差后的 Teacher 模型生成 ~5000 条指令-回复对（覆盖偏差类别和正常类别）

- [ ] 质检：抽样验证合成数据中偏差行为的出现率

**第 4-5 天：Student 微调**

- [ ] 用 Teacher 生成的合成数据，对 Gemma 2 9B（不同模型家族）做 LoRA 微调

- [ ] 对照组：用无偏差的原始 Llama 3.1 8B 生成的合成数据微调同一个 Student

**第 6-7 天：跨模型检测器评估**

- [ ] 用针对 Teacher（Llama 系列）训练/调优的安全检测器检测 Student（Gemma 系列）的输出

- [ ] 对比：偏差行为在 Teacher 上的检测率 vs 在 Student 上的检测率

- [ ] **关键产出**：量化「检测器跨模型泛化失效率」

### Phase 4：综合实验 + 论文撰写（可与云端扩展并行）

**本地可完成：**

- [ ] 将 Phase 1-3 的实验在 8B 模型上组合，计算复合攻击下的 α 值

- [ ] 用 `matplotlib`/`plotly` 绘制全部图表（跨层衰减曲线、α 对比柱状图、热力图）

- [ ] 撰写论文初稿的 Introduction、Threat Model、Methodology 部分

**需要云端补充：**

- [ ] 在 14B/70B 模型上重复实验 1，验证结论跨模型规模的稳健性

- [ ] 用更多模型家族（Mistral、Yi 等）扩充实验 3 的 Teacher-Student 组合

- [ ] 大规模 RL 训练版本的实验 2（如果需要更严格的 reward hacking 复现）

### 里程碑与决策点

| **里程碑** | **时间点** | **决策** |

| --- | --- | --- |

| Phase 1 完成：$p_{text{inner}}$ vs p_{\text{outer}} 曲线画出 | 第 2 周末 | 曲线非线性 → 继续；线性 → 重新评估假说或调整实验 |

| Phase 2 完成：评估感知高估幅度量化 | 第 3 周末 | 差值显著 → 继续；不显著 → 论文聚焦实验 1 和 3 |

| Phase 3 完成：跨模型检测失效率量化 | 第 4 周末 | 本地实验全部完成 → 决定是否租云端扩展规模 |

| Phase 4：论文初稿 + 云端补充实验 | 第 6-8 周 | 投稿目标确认 |

### 工具链建议

| **任务** | **推荐工具** | **备注** |

| --- | --- | --- |

| 模型推理 | `mlx-lm` / `llama.cpp` | MLX 对 Apple Silicon 原生优化 |

| 激活提取 & abliteration | `transformers`  • `torch`（MPS backend） | 需要 hook 中间层，MLX 暂不如 PyTorch 灵活 |

| LoRA 微调 | `mlx-lm` / `unsloth` | 8B 模型可行 |

| 安全 benchmark | `harmbench` / 自定义脚本 | 纯推理任务 |

| 结果可视化 | `matplotlib` / `plotly` | 画跨层衰减曲线 |
