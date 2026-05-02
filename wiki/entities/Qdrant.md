---
title: Qdrant
type: entity
tags:
- RAG/检索
- 知识管理
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fb5b5c5fc1ff4620bed4688b02f8efff
notion_id: fb5b5c5f-c1ff-4620-bed4-688b02f8efff
---

## 定义

Qdrant 是由德国公司 Qdrant Solutions GmbH 开发的高性能向量数据库，核心代码用 Rust 编写，专为 AI 嵌入向量存储与语义检索设计。支持自托管（Apache 2.0 开源）和云服务（Qdrant Cloud）。

**GitHub**：qdrant/qdrant | License: Apache 2.0 | 2023 年完成 750 万美元种子轮

## 核心优势

- **Rust 构建**：查询速度快，内存效率高

- **向量量化**：最多降低 97% RAM 占用

- **Payload 过滤**：强大的「先过滤再检索」能力，精确语义匹配

- **多云支持**：AWS/GCP/Azure 均可部署

- **免费层**：云版本提供 1GB RAM + 4GB 磁盘免费额度

## 与同类产品对比

| 产品 | 定位 | 特点 |

| --- | --- | --- |

| Qdrant | 性能优先 | 自托管友好，Rust 高效 |

| Chroma | 轻量 Python 原生 | 本地开发原型首选 |

| Pinecone | 全托管 SaaS | 快速上线，无运维 |

| Weaviate | 混合检索 | BM25 + 语义混合搜索 |

| Milvus | 大规模分布式 | 亿级向量，云原生 |

## 典型用法

与 LangChain 搭配：使用 QdrantVectorStore 接口，对 S3 多格式文件（PDF/图片/文本）进行向量化存储和语义检索。

## 来源引用

- [摘要：LangChain + Qdrant：30 分钟搭建一条 S3 多格式文件语义检索流水线](summaries/摘要：LangChain + Qdrant：30 分钟搭建一条 S3 多格式文件语义检索流水线.md)

- [摘要：用 Rust 从零构建企业级 GEO 平台，这个时代，就该考虑为AI 搜索重新定义品牌可见度](summaries/摘要：用 Rust 从零构建企业级 GEO 平台，这个时代，就该考虑为AI 搜索重新定义品牌可见度.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493249&idx=1&sn=4e3fc5d69bcceb0789e115e5d7d05d7d&chksm=c0cf5ae96e93e68df92027ef56ea2eb1500853b7aefb103779b186837e67324c8f6fd346df90#rd)）

## 关联概念

- [GEO](concepts/GEO.md)

- [Ollama](entities/Ollama.md)
