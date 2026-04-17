---
title: Wiki Lint Agent
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/1249bdf6ad334e11ad3d44fde9cb241f
notion_url: https://www.notion.so/5ee3bca30de04d6bb10016ba75368049
notion_id: 5ee3bca3-0de0-4d6b-b100-16ba75368049
---

## 定义

知识 Wiki 系统的**诊断师**角色——只诊断不动手，通过两阶段检查发现 Wiki 的内部质量问题，输出结构化的 lint-report 供 Wiki Fixer 执行修复。

## 两阶段检查架构

### Phase 1：快速检查（纯 SQL，全量覆盖）

不需要 loadPage，全部通过 `querySql` 完成，保证 100% 条目覆盖：

1. **全库统计** — 按类型×状态交叉统计，输出总览表格

1. **过期草稿检测** — `createdTime < 7天前` 且 `状态 = '草稿'` 的 concept/entity

1. **过时内容检测** — `最后编译时间` 为 null 或 > 30 天（豁免 qa 类型和系统元概念）

1. **完全同名重复检测** — `GROUP BY "名称", "类型" HAVING COUNT(*) > 1`

1. **近似重复检测（归一化）** — 分两步：

  - Step A：SQL 查出所有 summary/concept/entity 的名称和 url

  - Step B：在推理层做归一化匹配（lowercase → 去标点/空格/句号 → 统一繁简体 → 去版本号后缀），输出疑似重复对

1. **状态异常检测** — `状态 IS NULL` 的 concept/entity

1. **标签异常检测** — `标签 IS NULL OR 标签 = '[]'` 的 concept/entity + 全量标签分布统计

1. **类型启发式筛查** — SQL 全量查出 concept 名称，在推理层用规则批量筛查「疑似应为 entity」的条目：

  - 规则 A：名称为具体产品/公司/人物名（首字母大写的英文专有名词、含版本号如 `2.0`/`v3`）

  - 规则 B：名称中含有明确的产品后缀（`Tool`、`SDK`、`Platform`、`Protocol`、`CLI`）

  - 规则 C：名称完全是大写缩写+产品名组合（如 `CME FedWatch Tool`）

  - 输出疑似列表，不自动判定，标注「建议人工确认」

### Phase 2：深度检查（需 loadPage，抽样覆盖）

需要加载页面内容的检查项，从 Phase 1 发现的问题条目 + 随机抽样中执行：

1. **引用结构化检查** — 抽样 20 个草稿 concept/entity，检查「来源引用」区块是否使用 `<mention-page>` 结构化链接

1. **标签分类合理性抽查** — 加载 Phase 1 启发式筛查标记的条目 + 随机抽样，人工判断标签是否匹配内容

1. **状态晋升评估** — 综合 Phase 1 数据，判断哪些条目群体应晋升状态

## 输出规范

lint-report 页面必须包含：

- **健康评分**（0-100）+ 计分明细表格

- **全库统计表格**（类型×状态交叉）

- **各检查项的发现**（含具体页面链接）

- **状态晋升建议表格**

- **Fixer 可执行的结构化修复清单**（每条建议标注：修复类型 + 目标页面 URL + 具体操作）

- **待办建议**（需人工介入的项目）

- 报告末尾 @mention Wiki Fixer 触发自动修复

## Fixer 协作协议

- Lint 报告中的「改进建议」须分为两类：

  - **🤖 自动修复项**：Fixer 可直接执行（重复合并、标签修正、类型修正、引用结构化升级）

  - **👤 人工介入项**：需要人类确认（Schema 变更、豁免规则设计、Compiler 逻辑调整）

- Fixer 完成修复后，应在 Lint Report 页面追加「修复记录」区块，列出每项修复的操作和结果

- Lint Agent 在 Recheck 时，只需读取 Fixer 追加的修复记录 + 验证变更页面的属性，无需重新全量扫描

## 关键要点

- **触发方式**：独立 recurrence 每日 14:00（北京时间）自动执行 + @mention 手动触发

- **检查范围**：所有 concept、entity、summary 条目

- **核心原则**：只读 + 只创建报告，绝不修改任何已有页面

- **SQL 规范**：不允许自连接、多条语句、动态 LIKE 拼接。必须分步查询，在推理层做匹配

## 可修改范围

只创建 lint-report，不修改任何已有页面。

## 与其他 Agent 的协作

- **上游**：审查 Wiki Compiler 产出的所有条目

- **下游**：lint-report 自动触发 Wiki Fixer 执行修复（Lint 在报告中 @mention Fixer）

- **Recheck 流程**：Fixer 完成后，Lint Agent 读取修复记录并按清单验证，更新报告分数

- **对比**：[Gap Agent](concepts/Gap Agent.md) 是「外审」（Wiki vs 外部世界），Lint Agent 是「内审」（Wiki 内部质量）

## 关联概念

- Wiki Fixer — 接收 Lint 报告并执行修复，完成后追加修复记录

- [Gap Agent](concepts/Gap Agent.md) — 互补关系：内审 vs 外审
