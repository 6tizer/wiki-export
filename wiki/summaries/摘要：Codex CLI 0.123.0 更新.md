---
title: 摘要：Codex CLI 0.123.0 更新
type: summary
tags: []
status: 已审核
confidence: low
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68818faf49efe9a480fbb4
notion_url: https://www.notion.so/Tizer/ac0bb3212bc64a7fa82f77fd77e33836
notion_id: ac0bb321-2bc6-4a7f-a82f-77fd77e33836
---

## 一句话摘要

Codex CLI 0.123.0 发布，新增 Amazon Bedrock 提供方与 AWS Profile 支持，补强 `/mcp verbose` 诊断能力，并修复 VS Code WSL 终端中的 Unicode / dead-key 输入问题。

## 关键洞察

- 这次更新的重点不是新交互范式，而是围绕 **企业接入、诊断可见性、终端兼容性** 做工程化补强。

- Bedrock provider + AWS Profile support，说明 Codex CLI 正在更好地适配已有云边界与企业云账户体系。

- `/mcp verbose` 提供更完整的 MCP 诊断与资源信息，有助于排查工具接入、资源发现和运行时异常。

- VS Code WSL 终端的 Unicode / dead-key 修复，属于影响日常使用流畅度的基础体验改进。

- 原始信息较短，当前更适合作为版本更新摘要，而不是深度概念拆解材料。

## 提取的概念

- 暂无（原文信息较短，本次未单独提取 concept / entity）

## 原始文章信息

- 作者：@Codex_Changelog

- 来源：X书签

- 发布时间：2026-04-23

- 原文链接：[https://x.com/Codex_Changelog/status/2047127816919978277](https://x.com/Codex_Changelog/status/2047127816919978277)

- 关联发布页：[https://github.com/openai/codex/releases/tag/rust-v0.123.0](https://github.com/openai/codex/releases/tag/rust-v0.123.0)

## 个人评注

这类更新对 Tizer 的价值，在于它反映了 Coding Agent 工具链正在从“能用”走向“更易接入、更易排障、更适合团队环境”。其中 Bedrock 支持对应企业云内落地场景，`/mcp verbose` 对内容流水线和多工具编排排障尤其重要，而终端兼容性修复则直接影响日常 CLI 使用稳定性。
