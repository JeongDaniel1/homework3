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

# 任务2：时间分布分析
print("\n" + "=" * 60)
print("任务2：时间分布分析")
print("=" * 60)

# 筛选上车刷卡记录（刷卡类型=0）
onboard_records = df[df['刷卡类型'] == 0]

# (a) 早晚时段刷卡量统计（必须使用numpy）
print("(a) 早晚时段刷卡量统计：")

# 使用numpy布尔索引统计
# 早峰前时段：hour < 7
early_peak_before = np.sum(onboard_records['hour'] < 7)
# 深夜时段：hour >= 22
late_night = np.sum(onboard_records['hour'] >= 22)
total_onboard = len(onboard_records)

print(f"  早峰前时段（< 7:00）刷卡量: {early_peak_before} 次")
print(f"  深夜时段（>= 22:00）刷卡量: {late_night} 次")
print(f"  早峰前时段占比: {early_peak_before/total_onboard*100:.2f}%")
print(f"  深夜时段占比: {late_night/total_onboard*100:.2f}%")

# (b) 24小时刷卡量分布可视化（matplotlib）
print("\n(b) 24小时刷卡量分布可视化...")

# 统计每小时刷卡量
hourly_counts = onboard_records.groupby('hour').size()

# 创建图表
plt.figure(figsize=(12, 6))
hours = range(24)
counts = [hourly_counts.get(h, 0) for h in hours]

# 区分不同时段的颜色
colors = []
for h in hours:
    if h < 7:
        colors.append('red')  # 早峰前用红色
    elif h >= 22:
        colors.append('red')  # 深夜用红色
    else:
        colors.append('skyblue')  # 其他时段用蓝色

# 绘制柱状图
plt.bar(hours, counts, color=colors)

# 设置图表属性
plt.title('24小时刷卡量分布', fontsize=16)
plt.xlabel('小时', fontsize=12)
plt.ylabel('刷卡量（次）', fontsize=12)
plt.xticks(range(0, 24, 2))  # x轴标签步长为2
plt.grid(axis='y', alpha=0.3)

# 添加图例
from matplotlib.patches import Rectangle
early_late_patch = Rectangle((0,0),1,1, color='red', label='早峰前(<7)和深夜(>=22)')
other_patch = Rectangle((0,0),1,1, color='skyblue', label='其他时段')
plt.legend(handles=[early_late_patch, other_patch])

# 保存图像
plt.tight_layout()
plt.savefig('hour_distribution.png', dpi=150)
print("  24小时刷卡量分布图已保存为 hour_distribution.png")

