## Table of content
- [简介](https://github.com/submato/xhscrawl#%E7%AE%80%E4%BB%8B)
- [性能](https://github.com/submato/xhscrawl#%E6%80%A7%E8%83%BD)
- [changelog](https://github.com/submato/xhscrawl#changelog)
- [how to run demo](https://github.com/submato/xhscrawl#how-to-run-demo)
- [逆向xs效果](https://github.com/submato/xhscrawl#%E9%80%86%E5%90%91xs%E6%95%88%E6%9E%9C)
- [常见Q&A](https://github.com/submato/xhscrawl#%E5%B8%B8%E8%A7%81qa)
- [作者联系方式 && 寻求帮助](https://github.com/submato/xhscrawl#%E4%BD%9C%E8%80%85%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F--%E5%AF%BB%E6%B1%82%E5%B8%AE%E5%8A%A9)
- [作者提供的服务：](https://github.com/submato/xhscrawl#%E4%BD%9C%E8%80%85%E6%8F%90%E4%BE%9B%E7%9A%84%E6%9C%8D%E5%8A%A1)
    - [创建小红书账号指南](https://github.com/submato/xhscrawl#%E5%88%9B%E5%BB%BA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E8%B4%A6%E5%8F%B7%E6%8C%87%E5%8D%97)
    - [提供xs逆向在线api服务](https://github.com/submato/xhscrawl#%E6%8F%90%E4%BE%9Bxs%E9%80%86%E5%90%91api)
    - [提供逆向单个api的源码服务](https://github.com/submato/xhscrawl#%E6%8F%90%E4%BE%9B%E9%80%86%E5%90%91%E5%8D%95%E4%B8%AAapi%E7%9A%84%E6%BA%90%E7%A0%81%E6%9C%8D%E5%8A%A1)
- [Star History](https://github.com/submato/xhscrawl#star-history)
- [请作者喝咖啡吧](https://github.com/submato/xhscrawl#%E8%AF%B7%E4%BD%9C%E8%80%85%E5%96%9D%E5%92%96%E5%95%A1%E5%90%A7)


![Static Badge](https://img.shields.io/badge/author-submato-gree)
![Static Badge](https://img.shields.io/badge/GitHub-blue?logo=GitHub&labelColor=black)
![Static Badge](https://img.shields.io/badge/author-3.7%2F3.8-blue?logo=Python&label=python&labelColor=black)
![Static Badge](https://img.shields.io/badge/Node.js-v18.16.1-blue?logo=Node.js&labelColor=black)
![Static Badge](https://img.shields.io/badge/java-1.8-blue?logo=java&labelColor=black)


## 简介

小红书的api都有加密，主要就是x-s。本项目是用python逆向小红书x-s，小红书会定期更新加密的js，本项目会持续更新，欢迎star。

## 性能
1. 本项目采用js计算，不使用playwright/selenium调用浏览器内核的方式。因为起浏览器太耗资源了，如果有高并发、多账号需求的生产环境很难容忍。
2. 整个请求(包括本地计算xs、发起请求、小红书处理请求、返回数据)，10次平均耗时在800ms左右，速度十分可观

<img width="150" alt="image" src="https://github.com/submato/xhscrawl/assets/55040284/4845e6e9-a8b1-42cd-9822-6a1a5658ef8e">


## changelog

| 版本     | 日期       | 其他                                   |
| ------ | -------- | ------------------------------------ |
| v00.01 | 2023.07.05 |                                      |
| v00.02 | 2023.08.01 | - 增加从cookie自动获取a1参<br/>- 封装函数 <br/> - 增加一些工具函数|
| v00.03 | 2023.08.09 | - 增加[发送评论](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/comment.md)                   |
| v00.04 | 2023.08.09 | - 增加[获取笔记详情](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/note_detail.md)                   |
|        | 2023.08.10 | - 评论支持中文和@其他人                  |
| v00.05 | 2023.08.10 | - 增加[笔记搜索](https://github.com/submato/xhscrawl/blob/main/service/service_index/search.md)                  |
| v00.06 | 2023.09.02 | - 增加[获取笔记评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/get_comment.md)                   |
| v00.07 | 2023.09.14 | - 增加[收藏笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/collect_note.md) 、[给笔记点赞](https://github.com/submato/xhscrawl/blob/main/service/service_index/like_note.md)            |
| v01.00 | 2023.09.14 | - 代码重构、模块化、解耦  |
| v01.01 | 2023.09.18 | - 增加[获取用户笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_notes.md) |
| v01.02 | 2023.09.18 | - 增加[获取用户信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_info.md) |
| v01.03 | 2023.09.23 | - 增加[获取关键词搜索推荐信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/search_keyword_recommend.md)  |
| v01.04 | 2023.09.24 | - 增加[homefeed首页推荐](https://github.com/submato/xhscrawl/blob/main/service/service_index/homefeed.md) |
| v01.05 | 2023.09.26 | - 增加[自动发布笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/creat_note.md) |
| v01.06 | 2023.09.28 | - 增加[消息-评论和@列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/mentions.md) |
| v01.07 | 2023.09.29 | - update js文件，使其更加友好，加快开发 |
| v01.08 | 2023.09.29 | - 增加[消息-赞和收藏](https://github.com/submato/xhscrawl/blob/main/service/service_index/likes.md) |
| v01.09 | 2023.09.29 | - 增加[新增关注列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/connections.md) |
| v01.10 | 2023.09.29 | - 增加[未读通知数](https://github.com/submato/xhscrawl/blob/main/service/service_index/unread.md) |
| vxx.xx | 0000-00-00 | 若没有你需要的接口,联系作者有偿开发，提需前必看!!:[提需前必看](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/feature_notice.md) <br>QQ：1162466610(回复很快的,但禁止白嫖！！！)                |

## how to run demo
- python环境
  - execjs包
  - 等其他import依赖
- java环境
- node js环境
- 找到demo/xhs.py，将自己需要的参数、cookie进行手动替换运行即可

## 逆向xs效果
![image](https://github.com/wang-zhiyang/xhscrawl/assets/55040284/45c9d9cb-4017-4c47-81a5-2e896ca65ed7)

## 常见Q&A

联系作者前请务必查阅本文档，能回答你90%的问题，节省自己、作者的宝贵时间

常见Q&A：[常见Q&A](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/feature_notice.md) 

## 作者联系方式 && 寻求帮助
联系作者前请务必查阅本文档，能回答你90%的问题，节省自己、作者的宝贵时间
常见Q&A：[常见Q&A](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/feature_notice.md) 

QQ ：1162466610 (回复很快，但禁止白嫖！！！)

## 作者提供的服务

### 创建小红书账号指南

> 实践中发现不少用户需要多个账号，但是苦于没有这么多手机号，同时需求量也不够大，专门贩卖账号的灰产不搭理。

<br/>

本手册意在为这一部分用户提供一个自己获取小红书账号的方法。 怎么样获取到手机号，怎么注册小红书账号，怎么隔离小红书app防止正常使用的app被封设备号、怎么解封被封的手机号，怎么解封被封的设备号。

<br/>

详见：[创建小红书账号指南](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/account_manual.md)   
<br/>

### 提供xs逆向api

作者提供在线逆向api，按次收费。目前正在稳定性测试中，目前还不开放。

### 提供逆向单个api的源码服务
作者提供逆向单个api的源码，代码以最简单朴素的方式编写，每一个参数都有说明，保证能够跑起来

点击链接查看价格、返回数据等等详情

| 名称    | 
| ------------------------------------ |
|[发送评论](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/comment.md)                   |
| [获取笔记详情](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/note_detail.md)    |
| [笔记搜索](https://github.com/submato/xhscrawl/blob/main/service/service_index/search.md)                  |
| [获取笔记评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/get_comment.md)                  |
| [收藏笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/collect_note.md)                |
| [给笔记点赞](https://github.com/submato/xhscrawl/blob/main/service/service_index/like_note.md)  
| [获取用户笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_notes.md)  |
| [获取用户详情](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_info.md)  |
| [获取关键词搜索推荐信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/search_keyword_recommend.md)  |
| [homefeed首页推荐](https://github.com/submato/xhscrawl/blob/main/service/service_index/homefeed.md)  |
| [自动发布笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/creat_note.md) |
| [消息-评论和@列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/mentions.md)  |
| [消息-赞和收藏](https://github.com/submato/xhscrawl/blob/main/service/service_index/likes.md)  |
| [消息-新增关注列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/connections.md)  |
| [未读通知数](https://github.com/submato/xhscrawl/blob/main/service/service_index/unread.md)  |
| 若没有你需要的接口,联系作者有偿开发，提需前必看!!:[提需前必看](https://github.com/wang-zhiyang/xhscrawl/blob/main/service/service_index/feature_notice.md) <br>QQ：1162466610(回复很快的,但禁止白嫖！！！)                |

**付费后你将获得**
  - 源文件(包含3个文件，v01.00重构后，不依赖本项目):授人以渔，之后想怎么用就怎么用。
    - js文件：js逆向文件，提供xs逆向。
    - py文件：主运行文件，以易懂为主要目标进行编写，就像demo一样一看就懂。
    - md文件：how to run的保姆教程，包括如何获取cookie、笔记id是什么等
  - 添加作者微信，加入讨论群
  - 近乎完美的售后


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=submato/xhscrawl&type=Date)](https://star-history.com/#submato/xhscrawl&Date)


## 请作者喝咖啡吧
如果作者的仓库对你有帮助的话，请作者喝杯咖啡支持一下作者吧

<img title="" src="https://github.com/wang-zhiyang/xhscrawl/assets/55040284/89bb6534-5e74-44bb-b728-dc771fe9f2b1" alt="WechatIMG106" width="300">
