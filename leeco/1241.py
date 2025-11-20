import pandas as pd
import numpy as np

# 示例数据
data = {
    'sub_id': [1, 2, 1, 12, 3, 5, 3, 4, 9, 10, 6],
    'parent_id': [None, None, None, None, 1, 2, 1, 1, 1, 2, 7]
}

df = pd.DataFrame(data)

# 去重
df = df.drop_duplicates()
print(df)
# # 所有帖子
# posts = df[df['parent_id'].isna()]['sub_id'].drop_duplicates().to_frame('post_id')

# # 所有评论
# comments = df[df['parent_id'].notna()]

# # 统计每个帖子的唯一评论数
# comment_count = comments.groupby('parent_id')['sub_id'].nunique().reset_index()
# comment_count.columns = ['post_id', 'number_of_comments']

# # 左连接帖子，未评论的帖子补0
# result = posts.merge(comment_count, on='post_id', how='left').fillna(0)
# result['number_of_comments'] = result['number_of_comments'].astype(int)

# # 按 post_id 排序
# result = result.sort_values('post_id').reset_index(drop=True)

# print(result)
