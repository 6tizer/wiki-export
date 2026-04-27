---
title: Lint Report 2026-04-20
type: lint-report
tags:
- 知识管理
---

## 检查日期
2026-04-20（北京时间 22:00 定时触发）
## 总体健康度
🔴 0 / 100
主要扣分项：260 条过期草稿（创建超7天，状态仍为草稿）+ 1条系统性引用结构问题（早期批次纯文本引用比例严重超标）
## 全库统计
## 孤岛条目
由于 summary 与 concept/entity 无结构化 relation 字段，精确孤岛检测需借助 Notion search 二次验证。本次通过名称在 summary 标题中匹配（Phase 1 初筛），以下条目高度疑似孤岛（名称极为细分，summary 标题中未命中）：
- Bregman 投影（concept，Crypto/DeFi）
- 整数规划（concept，Crypto/DeFi）
- 三层追问链（concept，Agent 编排）
- 投资人压力测试（concept，工作流）
- X 列表（concept，知识管理）
- 存在姿态三角形（concept，Agent 编排）
- 历史人物人格唤醒（concept，Agent 编排）
注：以上为 Phase 1 初筛结果，建议 Fixer 用 Notion search 对每条进行验证后再决定是否标记孤岛。
## 过期草稿
共 260 条 concept/entity 页面处于草稿状态且创建超过 7 天（截止 2026-04-13 之前创建）。
以下为早期批次代表样本（2026-04-11 创建）：
- SuperHQ（entity，Coding Agent，创建 04-11，纯文本引用）
- SuperConductor（entity，Coding Agent，创建 04-11）
- Nezha（entity，Coding Agent，创建 04-11）
- Meta Superintelligence Labs（entity，LLM，创建 04-11）
- 评估感知（concept，LLM，创建 04-11，✅ 引用结构化，建议升审核中）
- Dageno（entity，Agent 框架，创建 04-11）
- Fanout Backlog（concept，商业/生态，创建 04-11，✅ 引用结构化，建议升审核中）
- ClawJacked（concept，OpenClaw/安全/隐私，创建 04-11，✅ 引用结构化，建议升审核中）
- LLM Graph Transformer（concept，LLM，创建 04-11，✅ 引用结构化，建议升审核中）
- OpenClaw 安全实践指南（concept，OpenClaw/安全/隐私，创建 04-11，✅ 引用结构化，建议升审核中）
- OpenClaw Context Engine（concept，OpenClaw/记忆系统，创建 04-11，纯文本引用）
- 四层 Fallback 链（concept，LLM，创建 04-11，纯文本引用）
- Slash 命令工作流（concept，Agent 编排，创建 04-11）
- 斜杠命令工作流（concept，Agent 编排，创建 04-11，⚠️ 疑似与上条重复）
完整列表共 260 条，不逐一展示。建议 Fixer 批量处理：引用结构完整者升审核中，纯文本引用者先修复引用再升级。
## 过时内容
无。所有非豁免条目的最后编译时间均在 2026-03-21 之后（或无编译时间但属于豁免系统元页面）。
豁免的 7 个系统元 concept 页（最后编译时间为 null，正常）：
- 关于 Gap Agent / Wiki Lint Agent / Wiki Fixer / Wiki Compiler / Wiki QA Agent / Wiki Synthesizer / Notion AI（Wiki 协调者）
## 重复疑似
### A. concept/entity 完全同名重复
无。
### B. concept/entity 归一化后近似重复
1 对：
### C. summary 完全同名重复
1 组：
- 摘要：Heat Seeking Missile for Pain — 出现 2 次（Compiler 重复触发同一源文章导致）
### D. summary 近似同名重复
本次未对全部 1094 条 summary 做归一化对比（数据量过大），仅检查完全同名。如需全量近似检测，建议 Fixer 执行专项脚本。
## 状态异常
无。所有 3235 条非 index/lint-report 条目均已设置状态字段，0 条缺失。
## 标签异常
无。0 条 concept/entity 缺失标签。0 条使用已弃用标签（AI Agent、MCP、Notion 标签均未发现使用）。
## 标签分布统计
以下为 concept+entity 各标签使用频次（单标签或含该标签的组合）：
注：上表为单主标签（仅含该标签，不含其他标签）的数量；多标签组合中含该标签的总数更高。LLM 是最大标签类，占比最重，建议持续关注分类合理性。
## 类型启发式筛查结果
以下 concept 条目疑似应被归类为 entity，建议人工确认：
计分规则：每 3 个确认的类型误分类扣 -3 分。以上为疑似，不自动判定，等待人工确认。
## 标签分类合理性检查
基于 Phase 2 抽样（8页）+ 推理层分析：
发现的疑似误分类：
整体标签分类质量较好，未发现明显系统性误分类。
## 引用结构化检查
### 🚨 系统性问题警报
抽样规模： 8 页（来自 2026-04-11 草稿批次，分层抽样）
统计结果：
汇总指标：
- Affected page rate：3/8 = 37.5% ≥ 30% 阈值 → 🚨 系统性问题
- Plain-text rate（全部引用中纯文本占比）：7/13 = 53.8% ≥ 20% 阈值 → 🚨 系统性问题
判定： 早期 Compiler 批次（2026-04-11）普遍存在纯文本引用问题。部分引用的是 X 推文 URL 或 GitHub README，而非 summary 页面的 <mention-page> 结构化引用。估计 260 条草稿中至少 90-100 条存在此问题，全库概算 ≥400 条需修复。
仅靠 Wiki Fixer 逐条修复不现实，强烈建议建立专项自动化 Autofill Agent（引用升级员）批量处理。
## 计分明细
最终健康分：🔴 0 / 100
## 状态晋升建议
以下为 Phase 2 抽样中发现的可晋升页面（引用结构完整）：
注：上述 5 条为 Phase 2 抽样中确认达标的条目。260 条过期草稿中还有大量类似情况，建议 Fixer 批量扫描、批量晋升。
## 改进建议
### 🤖 自动修复项（Fixer 可直接执行）
