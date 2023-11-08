## Table of content

- [简介](#%E7%AE%80%E4%BB%8B)
- [性能](#%E6%80%A7%E8%83%BD)
- [changelog](#changelog)
- [how to run demo](#how-to-run-demo)
- [常见Q&A](#%E5%B8%B8%E8%A7%81qa)
- [作者提供的服务](#%E4%BD%9C%E8%80%85%E6%8F%90%E4%BE%9B%E7%9A%84%E6%9C%8D%E5%8A%A1)
    - [提供app逆向成品数据](#1%E6%8F%90%E4%BE%9Bapp%E9%80%86%E5%90%91%E6%88%90%E5%93%81%E6%95%B0%E6%8D%AE)
    - [提供web成品数据](#4%E6%8F%90%E4%BE%9Bweb%E6%88%90%E5%93%81%E6%95%B0%E6%8D%AE)
    - [提供小红书、b站推广服务](#5%E6%8F%90%E4%BE%9B%E5%B0%8F%E7%BA%A2%E4%B9%A6b%E7%AB%99%E6%8E%A8%E5%B9%BF%E6%9C%8D%E5%8A%A1)
    - [提供逆向单个api的源码服务](#6%E5%88%9B%E5%BB%BA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E8%B4%A6%E5%8F%B7%E6%8C%87%E5%8D%97)
    - [创建小红书账号指南](#7%E6%8F%90%E4%BE%9B%E9%80%86%E5%90%91%E5%8D%95%E4%B8%AAapi%E7%9A%84%E6%BA%90%E7%A0%81%E6%9C%8D%E5%8A%A1)
- [作者联系方式、寻求帮助、合作](#%E4%BD%9C%E8%80%85%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F--%E5%AF%BB%E6%B1%82%E5%B8%AE%E5%8A%A9--%E5%90%88%E4%BD%9C)
- [Star History](#star-history)
- [请作者喝咖啡吧](#%E8%AF%B7%E4%BD%9C%E8%80%85%E5%96%9D%E5%92%96%E5%95%A1%E5%90%A7)


![Static Badge](https://img.shields.io/badge/author-submato-gree)
![Static Badge](https://img.shields.io/badge/GitHub-blue?logo=GitHub&labelColor=black)
![Static Badge](https://img.shields.io/badge/author-3.7%2F3.8-blue?logo=Python&label=python&labelColor=black)
![Static Badge](https://img.shields.io/badge/Node.js-v18.16.1-blue?logo=Node.js&labelColor=black)
![Static Badge](https://img.shields.io/badge/java-1.8-blue?logo=java&labelColor=black)


## 感谢下列Sponsors对本仓库赞助

---



*[成为赞助者，展示你的产品在这里](https://github.com/submato/xhscrawl/blob/main/service/service_index/ad.md)*

---

## 上当受骗提醒

最近发现本仓库有被上传至CSDN进行售卖，但并无实质性代码在内，但由于骗子原封不动的复制了代码内有我的qq联系方式，购买的用户找到我索要售后。

作者声明：除GitHub外，没有在任何平台进行代码售卖，请谨慎鉴别，上当受骗作者一律不负责

如您有购买需求，请认准QQ号 1162466610

## 简介

小红书的api都有加密，主要就是x-s。本项目是用python逆向小红书x-s，小红书会定期更新加密的js，本项目会持续更新，欢迎star。（最近一次更新时间为2023.5.31，早购买早享受哦～）

## 性能
1. 本项目采用js计算，不使用playwright/selenium调用浏览器内核的方式。因为起浏览器太耗资源了，如果有高并发、多账号需求的生产环境很难容忍。
2. 整个请求(包括本地计算xs、发起请求、小红书处理请求、返回数据)，10次平均耗时在800ms左右，速度十分可观

<img width="75" heigth="75" alt="image" src="https://github.com/submato/xhscrawl/assets/55040284/4845e6e9-a8b1-42cd-9822-6a1a5658ef8e">


## changelog

[changelog](https://github.com/submato/xhscrawl/blob/main/changelog.md) 


## how to run demo
- python环境
  - execjs包
  - 等其他import依赖
- java环境
- node js环境，需要支持ES13的 node js版本，也就是node js版本要晚于June 2022
- 找到demo/xhs.py，将自己需要的参数、cookie进行手动替换运行即可


## 常见Q&A

[常见Q&A](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md) 

## 作者提供的服务

### 1.提供app逆向成品数据

提供app爬虫的成品数据
- 交付方式：txt、excel、csv等等格式中的一种
- 价格：根据难度 x元/千条

### 5.提供小红书、b站推广服务
请联系作者，获取价格表

### 6.创建小红书账号指南

[创建小红书账号指南](https://github.com/submato/xhscrawl/blob/main/service/service_index/account_manual.md)   


### 7.提供逆向单个api的源码服务


作者提供逆向单个api的源码，
- 代码以最简单朴素的方式编写。
- 有详细的运行文档，接口文档，每一个参数都有说明。
- 保证能够跑起来，因为代码原因跑不起来直接退款，都是做技术的，不玩那些虚。

| 名称    | 
| ------------------------------------ |
|[发送评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/comment.md)                   |
| [获取笔记详情](https://github.com/submato/xhscrawl/blob/main/service/service_index/note_detail.md)    |
| [笔记搜索](https://github.com/submato/xhscrawl/blob/main/service/service_index/search.md)                  |
| [获取笔记评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/get_comment.md)                  |
| [收藏笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/collect_note.md)                |
| [给笔记点赞](https://github.com/submato/xhscrawl/blob/main/service/service_index/like_note.md)  
| [获取用户所有笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_notes.md)  |
| [获取用户详情](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_info.md)  |
| [获取关键词搜索推荐信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/search_keyword_recommend.md)  |
| [homefeed首页推荐](https://github.com/submato/xhscrawl/blob/main/service/service_index/homefeed.md)  |
| [自动发布笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/creat_note.md) |
| [消息-评论和@列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/mentions.md)  |
| [消息-赞和收藏](https://github.com/submato/xhscrawl/blob/main/service/service_index/likes.md)  |
| [消息-新增关注列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/connections.md)  |
| [未读通知数](https://github.com/submato/xhscrawl/blob/main/service/service_index/unread.md)  |
| 若没有你需要的接口,联系作者有偿开发，[提需前必看](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md) <br>QQ：1162466610(回复很快的,但禁止白嫖！！！)                |

**付费后你将获得**
  - 源文件(包含3个文件，v01.00重构后，不依赖本项目):授人以渔，之后想怎么用就怎么用。
    - js文件：js逆向文件，提供xs逆向。
    - py文件：主运行文件，以易懂为主要目标进行编写，就像demo一样一看就懂。
    - md文件：how to run的保姆教程，包括如何获取cookie、笔记id是什么等
    - 添加作者微信，加入讨论群
## 作者联系方式 || 寻求帮助 || 合作
联系作者前请务必查阅[常见Q&A](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md)
。能回答你90%的问题，节省自己、作者的宝贵时间。

QQ ：1162466610 (回复很快，但禁止白嫖！！！)


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=submato/xhscrawl&type=Date)](https://star-history.com/#submato/xhscrawl&Date)
