import pandas as pd

def page_recommendations(friendship, likes):

    # 1. 找到 user=1 的朋友（friendship 是双向的）
    friends = pd.concat([
        friendship.loc[friendship['user1_id'] == 1, 'user2_id'],
        friendship.loc[friendship['user2_id'] == 1, 'user1_id']
    ]).unique()

    # 2. 用户1 已喜欢的页面
    liked_by_user1 = likes.loc[likes['user_id'] == 1, 'page_id'].unique()

    # 3. 朋友喜欢的页面
    friend_pages = likes[likes['user_id'].isin(friends)]

    # 4. 去掉用户自己已喜欢的页面并去重
    recommended = (
        friend_pages.loc[~friend_pages['page_id'].isin(liked_by_user1), 'page_id']
        .drop_duplicates()
        .rename('recommended_page')
        .to_frame()
    )

    return recommended
