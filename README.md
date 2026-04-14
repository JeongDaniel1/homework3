# homework3
智能工程学院大一第三次作业
# 丁一平-25356057-第三次人工智能编程作业
## 1. 任务拆解与 AI 协作策略
（描述你如何将6项分析任务分步拆解给 AI？先让 AI 做数据读取，再做可视化，还是一次性让 AI 完成全部代码？）
我每一项任务先大致想了编程思路，在将要求和思路交给AI，AI优化了思路并生成代码，我再一步步debug.
## 2. 核心 Prompt 迭代记录
（展示一次你修改 Prompt 让 AI 代码从'不符合要求'变成'符合规范'的迭代过程） 初代 Prompt：... AI 生成的问题：...（例如：用了 seaborn 替代 matplotlib 画柱状图 / 函数签名不符合要求 / PHF 计算方法错误） 优化后的 Prompt：...
AI生成的函数名是calculate_route_stats，参数名是df, route_column, stops_column，与题目要求的analyze_route_stops(df, route_col='线路号', stops_col='ride_stops')完全不符。
我按照函数名一步步审查并修改。
## 3. Debug 记录
（记录一次解决报错的过程，例如：时区解析报错 / 热力图中文乱码 / ride_stops=0 导致的结果偏差） 报错现象：... 解决过程：...
KeyError: 'hour'
在任务4计算高峰小时系数时，代码试图在peak_hour_records中使用'hour'列。 首先检查错误位置，发现是在peak_hour_records['minute'] = peak_hour_records['交易时间'].dt.minute 
发现原因是之前使用了.copy()创建副本，但后续操作中又引用了原变量

## 4. 人工代码审查（逐行中文注释） （贴出任务4 PHF 计算的核心代码，并加上你自己的逐行中文注释） ```python # 贴入代码及注释 ```
# 1. 高峰小时识别：统计全天各小时刷卡量，输出高峰小时
# 筛选上车刷卡记录（仅统计刷卡类型=0的记录）
onboard_records = df[df['刷卡类型'] == 0]

# 按小时分组，统计每小时的刷卡量
hourly_volume = onboard_records.groupby('hour').size()

# 找出刷卡量最大的小时（高峰小时）
peak_hour = hourly_volume.idxmax()  # 获取最大值的索引，即高峰小时
peak_volume = hourly_volume.max()   # 获取最大值，即高峰小时刷卡量

# 2. 5分钟粒度统计：在高峰小时内，以5分钟为时间窗口进行聚合
# 筛选高峰小时内的所有记录
peak_hour_records = onboard_records[onboard_records['hour'] == peak_hour].copy()

# 从交易时间中提取分钟数，用于5分钟分组
peak_hour_records['minute'] = peak_hour_records['交易时间'].dt.minute

# 将分钟数按5分钟间隔分组（例如0-4分为一组，5-9分为一组等）
# 使用整数除法 //5 再乘以5，得到5分钟窗口的起始分钟
peak_hour_records['minute_group'] = (peak_hour_records['minute'] // 5) * 5

# 按5分钟窗口分组统计刷卡量
five_min_volume = peak_hour_records.groupby('minute_group').size()

# 找出最大5分钟刷卡量及对应的窗口起始时间
max_5min_volume = five_min_volume.max()      # 最大5分钟刷卡量
max_5min_period = five_min_volume.idxmax()   # 对应窗口起始分钟

# 计算PHF5：高峰小时刷卡量 ÷ (12 × 高峰小时内最大5分钟刷卡量)
# 公式解释：高峰小时有12个5分钟，PHF5是实际流量与理论最大流量的比值
PHF5 = peak_volume / (12 * max_5min_volume)

# 3. 15分钟粒度统计：在高峰小时内，以15分钟为时间窗口进行聚合
# 类似5分钟分组，但使用15分钟间隔
peak_hour_records['minute_group_15'] = (peak_hour_records['minute'] // 15) * 15

# 按15分钟窗口分组统计刷卡量
fifteen_min_volume = peak_hour_records.groupby('minute_group_15').size()

# 找出最大15分钟刷卡量及对应的窗口起始时间
max_15min_volume = fifteen_min_volume.max()      # 最大15分钟刷卡量
max_15min_period = fifteen_min_volume.idxmax()   # 对应窗口起始分钟


