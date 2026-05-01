---
title: 摘要：用 Rust 打造多租户 RustClaw 云平台
type: summary
tags:
- 商业/生态
- MCP 协议
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/286467e934924cca90c5d548d3f53024
notion_id: 286467e9-3492-4cca-90c5-d548d3f53024
---

**一句话摘要**：作者用 2500 行 Rust 代码，从零构建了一个支持多租户隔离、MCP 协议、技能市场和跨会话记忆的完整 AI Agent 云平台。

**关键洞察**

- **单二进制部署**：所有组件打包为一个可执行文件，零外部依赖，极低内存占用

- **真正的 Agent Loop**：Tool Calling Loop 最多 20 轮自主决策，每工具 60 秒超时，防止无限循环

- **MCP 协议接入**：通过 stdio 启动 MCP Server 子进程，JSON-RPC 2.0 握手，可无限扩展工具生态

- **Skill 系统**：[SKILL.md](http://skill.md/) 文件驱动的技能系统，接入腾讯 SkillHub + ClaHub 双数据源，Agent 可自动生成新技能

- **多租户隔离**：文件夹 + Apple Container + Linux Namespace/gVisor 三层隔离，每用户独立沙箱、SQLite 历史和记忆文件

**提取的概念**

- RustClaw（多租户 Rust AI Agent 平台）

- MCP 协议

- Tool Calling Loop

- Skill 系统（[SKILL.md](http://skill.md/)）

- OpenClaw 文件式记忆

**原始文章信息**

- 作者：老码小张

- 来源：微信公众号

- 发布时间：2026-04-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247493119](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493119)

**个人评注**：这篇文章与 Tizer 的 OpenClaw 生态高度相关，展示了如何用 Rust 构建类似 OpenClaw 的平台，其中 Skill 系统与 SkillHub 的接入方式对 OpenClaw 插件生态建设有直接参考价值。多租户沙箱设计值得深入研究。
