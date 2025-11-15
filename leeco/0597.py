import pandas as pd

# 假设你的数据已读入 df1, df2
# df1 = FriendRequest
# df2 = RequestAccepted

# 1. 求唯一好友申请数
total_requests = df1[['sender_id', 'send_to_id']].drop_duplicates().shape[0]

# 2. 求唯一通过的申请数
accepted_requests = df2[['requester_id', 'accepter_id']].drop_duplicates().shape[0]

# 3. 计算通过率
accept_rate = 0 if total_requests == 0 else round(accepted_requests / total_requests, 2)

# 4. 输出 DataFrame
result = pd.DataFrame({'accept_rate': [accept_rate]})
result
