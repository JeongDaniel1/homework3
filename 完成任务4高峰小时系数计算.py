import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
import zipfile
warnings.filterwarnings('ignore')

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
plt.rcParams['axes.unicode_minus'] = False
print("《人工智能编程语言》第六次作业 - 公交IC卡刷卡数据分析")
# 1. 高峰小时识别
print("1. 高峰小时识别：")
# 统计全天各小时刷卡量
hourly_volume = onboard_records.groupby('hour').size()

# 找出刷卡量最大的小时
peak_hour = hourly_volume.idxmax()
peak_volume = hourly_volume.max()

print(f"   高峰小时：{peak_hour:02d}:00 ~ {peak_hour+1:02d}:00，刷卡量：{peak_volume} 次")

# 2. 5分钟粒度统计
print("\n2. 5分钟粒度统计：")
# 筛选高峰小时内的记录
peak_hour_records = onboard_records[onboard_records['hour'] == peak_hour]

# 提取分钟数
peak_hour_records = peak_hour_records.copy()
peak_hour_records['minute'] = peak_hour_records['交易时间'].dt.minute

# 按5分钟窗口分组统计
peak_hour_records['minute_group'] = (peak_hour_records['minute'] // 5) * 5
five_min_volume = peak_hour_records.groupby('minute_group').size()

# 找出最大5分钟刷卡量
max_5min_volume = five_min_volume.max()
max_5min_period = five_min_volume.idxmax()

print(f"   最大5分钟刷卡量（{peak_hour:02d}:{max_5min_period:02d}~{peak_hour:02d}:{max_5min_period+5:02d}）：{max_5min_volume} 次")

# 计算PHF5
PHF5 = peak_volume / (12 * max_5min_volume)
print(f"   PHF5 = {peak_volume} / (12 × {max_5min_volume}) = {PHF5:.4f}")

# 3. 15分钟粒度统计
print("\n3. 15分钟粒度统计：")
# 按15分钟窗口分组统计
peak_hour_records['minute_group_15'] = (peak_hour_records['minute'] // 15) * 15
fifteen_min_volume = peak_hour_records.groupby('minute_group_15').size()

# 找出最大15分钟刷卡量
max_15min_volume = fifteen_min_volume.max()
max_15min_period = fifteen_min_volume.idxmax()

print(f"   最大15分钟刷卡量（{peak_hour:02d}:{max_15min_period:02d}~{peak_hour:02d}:{max_15min_period+15:02d}）：{max_15min_volume} 次")

# 计算PHF15
PHF15 = peak_volume / (4 * max_15min_volume)
print(f"   PHF15 = {peak_volume} / (4 × {max_15min_volume}) = {PHF15:.4f}")

# 格式要求输出
print("\n4. 格式要求输出：")
print(f"   高峰小时：{peak_hour:02d}:00 ~ {peak_hour+1:02d}:00，刷卡量：{peak_volume} 次")
print(f"   最大5分钟刷卡量（{peak_hour:02d}:{max_5min_period:02d}~{peak_hour:02d}:{max_5min_period+5:02d}）：{max_5min_volume} 次")
print(f"   PHF5 = {peak_volume} / (12 × {max_5min_volume}) = {PHF5:.4f}")
print(f"   最大15分钟刷卡量（{peak_hour:02d}:{max_15min_period:02d}~{peak_hour:02d}:{max_15min_period+15:02d}）：{max_15min_volume} 次")
print(f"   PHF15 = {peak_volume} / (4 × {max_15min_volume}) = {PHF15:.4f}")
