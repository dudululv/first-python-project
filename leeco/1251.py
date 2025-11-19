import pandas as pd

# 假设数据已读入 prices, units_sold
# prices: product_id, start_date, end_date, price
# units_sold : product_id, purchase_date, units

import pandas as pd

# 假设 prices, units_sold 已经加载
prices['start_date'] = pd.to_datetime(prices['start_date'])
prices['end_date'] = pd.to_datetime(prices['end_date'])

if not units_sold.empty:
    units_sold['purchase_date'] = pd.to_datetime(units_sold['purchase_date'])

# 1. 如果 UnitsSold 为空，直接让销量为 0
if units_sold.empty:
    result = prices[['product_id']].drop_duplicates()
    result['average_price'] = 0
    print(result)
else:
    # 2. 正常情况：先按 product_id merge
    df = units_sold.merge(prices, on='product_id', how='left')

    # 3. 过滤 purchase_date 落在价格区间
    df = df[
        (df['purchase_date'] >= df['start_date']) &
        (df['purchase_date'] <= df['end_date'])
    ]

    # 4. 计算金额
    df['amount'] = df['units'] * df['price']

    # 5. 聚合
    result = (
        df.groupby('product_id')
          .agg(total_amount=('amount','sum'),
               total_units=('units','sum'))
          .reset_index()
    )

    # 6. 合并以包含所有产品
    result = prices[['product_id']].drop_duplicates().merge(result, on='product_id', how='left')

    # 7. 计算平均售价
    result['average_price'] = (result['total_amount'] / result['total_units']).fillna(0)

    # 8. 四舍五入
    result['average_price'] = result['average_price'].round(2)

    print(result[['product_id', 'average_price']])

print(result)
