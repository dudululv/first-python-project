import pandas as pd

# 示例数据
data = {
    "requester_id": [1, 1, 2, 3],
    "accepter_id":  [2, 3, 3, 4],
    "accept_date":  ["2016/06/03", "2016/06/08", "2016/06/08", "2016/06/09"]
}

df = pd.DataFrame(data)

# requester 和 accepter 都表示获得了一个好友
r = df[['requester_id']].rename(columns={"requester_id": "id"})
a = df[['accepter_id']].rename(columns={"accepter_id": "id"})

# 合并两列
all_friends = pd.concat([r, a])

# 分组统计每个人的好友数
friend_count = all_friends.groupby("id").size().reset_index(name="num")

# 找出 num 最大的人
result = friend_count.sort_values("num", ascending=False).head(1)

print(result)
