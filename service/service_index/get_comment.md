# 获取笔记评论

## 可以干什么
1. 包含两个接口
   1. 获取评论：https://edith.xiaohongshu.com/api/sns/web/v2/comment/sub/page
   2. 获取评论的子评论：https://edith.xiaohongshu.com/api/sns/web/v2/comment/page
2. 获取笔记所有评论(会自动帮忙翻页)，包括子评论
3. 包括发评论的用户名、id、点赞数等。

## 效果
<img width="1305" alt="image" src="https://github.com/submato/xhscrawl/assets/55040284/a8ff72d9-1b5f-4fff-a3e2-786748472561">

数据Demo：
```json
{
    "target_comment":{
        "id":"64da260d000000002d01a941",
        "user":{
            "id":"5b519a9ee8ac2b35341ab41b",
            "nickname":"momo"
        }
    },
    "id":"64da482c000000002b006e19",
    "user_id":"62821447000000002102428c",
    "user_name":"猴森Ah",
    "content":"哈哈哈哈哈",
    "like_count":"1",
    "at_users":[

    ]
}
```


## 如何获取
由于评论接口逆向难度大，并且提供了两个接口，同时作者是大厂程序员，利用晚上下班时间逆向，所以是600有偿提供。

## 获取后会得到什么
1. 一个markDown格式的保姆式运行教程
2. 一个全新的js逆向文件
3. 一个源代码文件
