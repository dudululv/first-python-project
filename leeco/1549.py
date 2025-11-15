import pandas as pd

# 示例数据
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Winston', 'Jonathan', 'Annabelle', 'Marwan', 'Khaled']
})

orders = pd.DataFrame({
    'order_id': [1,2,3,4,5,6,7,8,9,10],
    'order_date': pd.to_datetime(['2020-07-31','2020-07-30','2020-08-29','2020-07-29',
                                  '2020-06-10','2020-08-01','2020-08-01','2020-08-03',
                                  '2020-08-07','2020-07-15']),
    'customer_id': [1,2,3,4,1,2,3,1,2,1],
    'product_id': [1,2,3,1,2,1,1,2,3,2]
})

products = pd.DataFrame({
    'product_id': [1,2,3,4],
    'product_name': ['keyboard','mouse','screen','hard disk'],
    'price': [120,80,600,450]
})

# 1. 合并 Orders 和 Products 获取 product_name
df = orders.merge(products[['product_id','product_name']], on='product_id', how='left')

# 2. 找到每个 product_id 的最新 order_date
latest_dates = df.groupby('product_id')['order_date'].max().reset_index()
latest_dates.rename(columns={'order_date':'latest_order_date'}, inplace=True)

# 3. 合并回 df，筛选最新订单
df = df.merge(latest_dates, on='product_id')
latest_orders = df[df['order_date'] == df['latest_order_date']]

# 4. 选择需要列并排序
result = latest_orders[['product_name','product_id','order_id','order_date']].sort_values(
    by=['product_name','product_id','order_id']
).reset_index(drop=True)

print(result)
