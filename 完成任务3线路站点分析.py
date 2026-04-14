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
# 任务3：线路站点分析
print("\n" + "=" * 60)
print("任务3：线路站点分析")
print("=" * 60)

# 定义函数 analyze_route_stops（严格按照题目要求）
def analyze_route_stops(df, route_col='线路号', stops_col='ride_stops'):
    """
    计算各线路乘客的平均搭乘站点数及其标准差。
    
    Parameters
    ----------
    df : pd.DataFrame
        预处理后的数据集
    route_col : str
        线路号列名
    stops_col : str
        搭乘站点数列名
        
    Returns
    -------
    pd.DataFrame
        包含列：线路号、mean_stops、std_stops，按 mean_stops 降序排列
    """
    # 按线路号分组，计算平均搭乘站点数和标准差
    result = df.groupby(route_col)[stops_col].agg(['mean', 'std']).reset_index()
    result.columns = [route_col, 'mean_stops', 'std_stops']
    
    # 按 mean_stops 降序排列
    result = result.sort_values('mean_stops', ascending=False)
    
    return result

# 调用函数并打印结果
print("1. 各线路平均搭乘站点数统计：")
route_analysis = analyze_route_stops(df)
print("   前10行结果：")
print(route_analysis.head(10))

# 使用seaborn水平条形图可视化前15条线路
print("\n2. 生成线路站点分析图...")
plt.figure(figsize=(10, 8))
top15_routes = route_analysis.head(15)

# 绘制水平条形图
sns.barplot(data=top15_routes, y='线路号', x='mean_stops', palette="Blues_d", orient='h')

# 设置图表属性
plt.title('前15条线路平均搭乘站点数', fontsize=16)
plt.xlabel('平均搭乘站点数', fontsize=12)
plt.ylabel('线路号', fontsize=12)
plt.xlim(0)  # x轴从0开始

# 保存图像
plt.tight_layout()
plt.savefig('route_stops.png', dpi=150)
print("   线路站点分析图已保存为 route_stops.png")

