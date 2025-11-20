import pandas as pd

# 示例数据
data = {
    'product_id': [1, 2, 1, 1, 2, 3],
    'new_price': [20, 50, 30, 35, 65, 20],
    'change_date': ['2019-08-14','2019-08-14','2019-08-15','2019-08-16','2019-08-17','2019-08-18']
}

df = pd.DataFrame(data)
df['change_date'] = pd.to_datetime(df['change_date'])

# 查询日期
target_date = pd.to_datetime('2019-08-16')

# 找出每个产品在目标日期前的最新价格
latest_prices = df[df['change_date'] <= target_date].sort_values('change_date').groupby('product_id').tail(1)

# 创建所有产品的列表（包括没有变动的产品）
all_products = pd.DataFrame({'product_id': df['product_id'].unique()})

# 合并价格，没有变动的用初始价格 10
result = all_products.merge(latest_prices[['product_id', 'new_price']], on='product_id', how='left')
result['price'] = result['new_price'].fillna(10).astype(int)
result = result[['product_id', 'price']]

print(result)
