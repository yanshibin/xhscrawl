# 用户信息

## 可以干什么
包含用户以下信息：

1. 用户名、头像、性别(如果用户有设置)、用户地区(如果用户有设置)、实际ip地区、年龄(如果用户有设置)
2. 简介
3. 用户粉丝数、关注数、点赞于收藏数


## api
向作者购买收费版本～

## 数据Demo：

```json
{
    "code": 0,
    "success": true,
    "msg": "成功",
    "data": {
        "tab_public": {
            "collection": false
        },
        "extra_info": {
            "fstatus": "none"
        },
        "result": {
            "message": "success",
            "success": true,
            "code": 0
        },
        "basic_info": {
            "gender": 0,
            "ip_location": "广东",
            "desc": "📮Xx11_08_",
            "imageb": "https://sns-avatar-qc.xhscdn.com/avatar/62acd39c1f83d1a235742781.jpg?imageView2/2/w/540/format/webp",
            "nickname": "我要去捉鱼",
            "images": "https://sns-avatar-qc.xhscdn.com/avatar/62acd39c1f83d1a235742781.jpg?imageView2/2/w/360/format/webp",
            "red_id": "Xx11_08"
        },
        "interactions": [
            {
                "type": "follows",
                "name": "关注",
                "count": "12"
            },
            {
                "type": "fans",
                "name": "粉丝",
                "count": "1204"
            },
            {
                "type": "interaction",
                "name": "获赞与收藏",
                "count": "7685"
            }
        ],
        "tags": [
            {
                "icon": "http://ci.xiaohongshu.com/icons/user/gender-male-v1.png",
                "name": "18岁",
                "tagType": "info"
            },
            {
                "name": "广东广州",
                "tagType": "location"
            }
        ]
    }
}
```


## 如何获取
由于评论接口逆向难度大，并且提供了两个接口，同时作者是大厂程序员，利用晚上下班时间逆向，所以是800有偿提供。

## 获取后会得到什么
1. 一个markDown格式的保姆式运行教程
2. 一个js逆向文件
3. 一个源代码文件
