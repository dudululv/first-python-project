import pandas as pd

def cumulative_salary(df):
    result = []

    for emp_id, group in df.groupby('id'):
        months = group['month']
        min_m, max_m = months.min(), months.max()

        # 补全月份
        all_months = pd.DataFrame({'month': range(min_m, max_m + 1)})
        merged = all_months.merge(group, on='month', how='left').fillna({'salary': 0})
        merged['salary'] = merged['salary'].astype(int)

        # 滚动 3 月工资
        merged['Salary'] = merged['salary'].rolling(3, min_periods=1).sum()

        # 去掉最大月份
        latest = max_m
        merged = merged[merged['month'] != latest]

        # 只保留员工原本有工资的月份
        merged = merged[merged['month'].isin(months)]

        # 若还有数据，则加入 result
        if not merged.empty:
            merged['id'] = emp_id
            result.append(merged[['id','month','Salary']])

    # 如果 result 有内容再 concat
    if result:
        final = pd.concat(result)
        final = final.sort_values(['id', 'month'], ascending=[True, False])
    else:
        final = pd.DataFrame(columns=['id','month','Salary'])

    return final
