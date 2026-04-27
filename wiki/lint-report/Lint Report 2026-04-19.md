---
title: Lint Report 2026-04-19
type: lint-report
tags:
- 知识管理
---

## 检查日期
2026-04-19
## 总体健康度
🔴 0 / 100
过期草稿积压（~100条）是本次评分骤降的主因；引用结构化存在系统性问题（60% affected rate）同步拉低质量基线。
## 全库统计
## 孤岛条目
检测方法：标题命中初筛（推理层匹配 concept/entity 名称是否出现在 summary 标题中）。由于 SQL 限制无法做全量精确检测（无法用动态 LIKE 自连接），以下为推理层疑似孤岛，建议人工抽查确认。
疑似孤岛（标题未在任何 summary 中匹配）：
- 跨交易所套利
- 传播飞轮
- FRED
- Bregman 投影
- 整数规划
- find-skills
- Fanout Backlog
- ClawJacked
- Polymarket Analytics
- XHS Bridge
- ERC-8004
- QClaw
- CVD 背离
- program.md
- 内部人士买入筛查
- 书签 AI 管道
- 原生多模态 Embedding
- Context Agent
- SafePal
- Fiat24
注：以上仅为初筛结果，部分 concept 可能在 summary 正文中以 <mention-page> 引用，需二次验证。估计实际孤岛数量 ~20 条，建议 Fixer 用 Notion search 逐条验证。
## 过期草稿
以下 concept/entity 页面处于 草稿 状态，且创建时间超过 7 天（即 2026-04-11 批次全部），共约 100 条。
代表性列表（前30条）：
全量清单共约 100 条（2026-04-11 批次全部），因 SQL 返回结果完整，可直接批处理。大多数页面引用为纯文本，需先修复引用后再晋升状态。
## 过时内容
无。所有非豁免条目的最后编译时间均在 30 天内（最早 2026-04-11，距今 8 天）。7 个系统元 concept 页（Wiki Lint Agent、Wiki Fixer 等）最后编译时间为 null，按规则豁免。
## 重复疑似
### A. 完全同名重复
无（SQL GROUP BY 检查：summary、concept、entity 均无完全同名重复对）。
### B. 近似同名重复（归一化后）
Concept / Entity 近似重复（4 对）：
π0.6 / π0.7 和 MiniMax M2.5 / M2.7 建议保留为独立版本词条，各自记录该版本特性，但应在词条间建立关联引用。3D Gaussian Splatting / 3D 高斯泼溅 建议合并为一条，保留英文名，中文名作为别称。Prompt Cache / Prompt Caching 建议合并。
Summary 近似重复：无（SQL GROUP BY 检查无完全同名；推理层归一化匹配未发现近似重复对）。
## 状态异常
无。所有条目状态字段均已设置（SQL 查询返回 0 行）。
## 标签异常
无缺失标签。所有 concept/entity 页面均包含至少 1 个标签。
无废弃标签。AI Agent、MCP、Notion 均未在 concept/entity 中使用（SQL 检查返回 0 行）。
## 标签分布统计
以下按单标签维度估算（条目可同时有多个标签）：
LLM 标签频次偏高（~450），部分原因是具体模型产品（如 GPT-Image-2、Gemma 4、MiniMax M2.x 等）被标记为 LLM+concept，建议审查是否应改为 entity 类型。
## 类型启发式筛查结果
以下 concept 页面疑似应重分类为 entity（建议人工确认，不自动判定）：
## 标签分类合理性检查
从 Phase 2 抽样（10 页）结合推理层标签规则审查，发现以下疑似误分类：
开发工具 vs Coding Agent 边界：当前库中存在多个 AI 编程 Agent（如 Claude Code 相关概念）被归为「开发工具」而非「Coding Agent」的情况，建议 Fixer 搜索标签为「开发工具」且名称含 Claude/Codex/Gemini CLI 的条目并重贴标签。
## 引用结构化检查
### 抽样统计（10 页，均来自 2026-04-11 草稿/审核中批次）
### 系统性判定
## 🚨 系统性问题：引用结构化缺失
草稿状态的 concept/entity 页面（主要是 2026-04-11 批次，约 100 条）普遍使用纯文本来源引用（X tweet URL、markdown 链接），缺少 <mention-page> 结构化链接。审核中页面多为「混合模式」（同时有纯文本和 mention-page）。
- 影响估算：整个 2026-04-11 草稿批次约 100 条需修复；后续批次情况待进一步抽样确认
- 纯靠 Fixer 逐条修复（每条需 loadPage + search + updatePage）效率极低，预计 ≥100 条
- 推荐建立专项「引用升级员」Autofill Agent 批量处理（见👤人工介入项）
## 计分明细
## 状态晋升建议
批量晋升路径：引用升级员修复 mention-page 后 → Fixer 对内容完整（有定义+关键要点+mention-page）的 2026-04-11 草稿条目批量晋升为「审核中」
## 改进建议
### 🤖 自动修复项（Fixer 可直接执行）
1. 重复合并：3D Gaussian Splatting + 3D 高斯泼溅
1. 重复合并：Prompt Cache + Prompt Caching
1. 类型修正：SafePal → entity
1. 类型修正：FRED → entity
1. 类型修正：Fiat24 → entity
1. 孤岛引用修复（小批量）
1. 状态晋升：个人超级智能 → 审核中
