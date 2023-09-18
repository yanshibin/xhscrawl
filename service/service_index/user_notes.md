# 用户发布的稿件

## 可以干什么
获取用户发布的稿件

## api
/api/sns/web/v1/user_posted

## 数据Demo：

```json
"success":true,
    "msg":"成功",
    "data":{
        "cursor":"",
        "notes":[
            {
                "user":{
                    "nick_name":"abby huang",
                    "avatar":"https://sns-avatar-qc.xhscdn.com/avatar/6072114ba6cf27d7b3152d64.jpg",
                    "user_id":"582f71fb5e87e7473ea57207",
                    "nickname":"abby huang"
                },
                "interact_info":{
                    "liked":false,
                    "liked_count":"337",
                    "sticky":false
                },
                "cover":{
                    "file_id":"",
                    "height":1280,
                    "width":1707,
                    "url":"https://sns-img-qc.xhscdn.com/3f9c5c9d-196a-56f3-dc9b-42b1372d0821",
                    "trace_id":""
                },
                "note_id":"6506e5e5000000001500b477",
                "type":"normal",
                "display_title":"怎么带女佣回中国🇨🇳"
            },
        ],
        "has_more":false
    },
    "code":0
}
```


## 如何获取
由于评论接口逆向难度大，并且提供了两个接口，同时作者是大厂程序员，利用晚上下班时间逆向，所以是500有偿提供。

## 获取后会得到什么
1. 一个markDown格式的保姆式运行教程
2. 一个js逆向文件
3. 一个源代码文件
