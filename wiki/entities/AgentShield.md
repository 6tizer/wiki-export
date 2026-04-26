---
title: AgentShield
type: entity
tags:
- Agent 安全
- CLI 工具
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c79735025166474e9aa3960e09238b8e
notion_id: c7973502-5166-474e-9aa3-960e09238b8e
---

## 定义

AgentShield 是 Everything Claude Code 中配置的安全扫描工具，用于检查 Claude Code 相关配置中的漏洞、权限问题与注入风险。

## 关键要点

- 文章提到它内置 **1282 项测试** 与 **102 条静态分析规则**。

- 可扫描 `CLAUDE.md`、MCP 配置以及 hooks 中的潜在安全风险。

- 适合在接入较多 MCP、自动化能力或自定义配置时做安全体检。

- 体现了 Coding Agent 配置不只是效率问题，也涉及安全治理。

## 来源引用

- 《154K Star！Anthropic黑客松冠军的Claude Code配置大公开》

  - 来源文章页面：154K Star！Anthropic黑客松冠军的Claude Code配置大公开

  - 外部链接：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515422&idx=1&sn=6d3cca0b2702fd1b47b8a1771475441b&chksm=e9010047a94039c4cee3023882ada32b6ea1b4fbc65f29420b5c3c14de73f63686f7fec48b39#rd)

  - 示例命令：`npx ecc-agentshield scan`
