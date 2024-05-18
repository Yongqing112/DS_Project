from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from caculate import caculate
from caculate import not_higher_education_and_not_get_job
 
files = glob('./未升學未就業情形(按群別分）/*.csv')
# print(files)

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
print(df)
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 篩選我們要的資料
# 目標: 先看出未升學未就業人數最多 -> 根據就業概況分析學校可以提供什麼幫助增加升學率
# 學年度
# 國立私立
# 學程別
# 群科別 就業概況 比例

# 正在接受職業訓練人數
# data = caculate(df, 106, "正在接受職業訓練人數")

# temp = caculate(df, 107, "正在接受職業訓練人數")
# data = pd.concat([data, temp], ignore_index=True) 

# temp = caculate(df, 108, "正在接受職業訓練人數")
# data = pd.concat([data, temp], ignore_index=True) 

# temp = caculate(df, 109, "正在接受職業訓練人數")
# data = pd.concat([data, temp], ignore_index=True) 

# temp = caculate(df, 110, "正在接受職業訓練人數")
# data = pd.concat([data, temp], ignore_index=True) 
columns = ["正在接受職業訓練人數", "正在軍中服役人數", "需要工作而未找到人數", "健康不良在家休養人數", "準備出國人數", "其他人數"]
data = pd.DataFrame()
data = not_higher_education_and_not_get_job(df, data, 106, 110, columns)

# 正在軍中服役人數
# temp = caculate(df, 106, "正在軍中服役人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 107, "正在軍中服役人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "正在軍中服役人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "正在軍中服役人數")
# data = pd.concat([data, temp], ignore_index=True) 

# temp = caculate(df, 110, "正在軍中服役人數")
# data = pd.concat([data, temp], ignore_index=True) 

# 需要工作而未找到人數
# temp = caculate(df, 106, "需要工作而未找到人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 107, "需要工作而未找到人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "需要工作而未找到人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "需要工作而未找到人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 110, "需要工作而未找到人數")
# data = pd.concat([data, temp], ignore_index=True)

# 補習或準備升學人數
# temp = caculate(df, 106, "補習或準備升學人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 107, "補習或準備升學人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "補習或準備升學人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "補習或準備升學人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 110, "補習或準備升學人數")
# data = pd.concat([data, temp], ignore_index=True)

# 健康不良在家休養人數
# temp = caculate(df, 106, "健康不良在家休養人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "健康不良在家休養人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "健康不良在家休養人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "健康不良在家休養人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 110, "健康不良在家休養人數")
# data = pd.concat([data, temp], ignore_index=True)

# 準備出國人數

# temp = caculate(df, 106, "準備出國人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 107, "準備出國人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "準備出國人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "準備出國人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 110, "準備出國人數")
# data = pd.concat([data, temp], ignore_index=True)

# 其他人數

# temp = caculate(df, 106, "其他人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 107, "其他人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 108, "其他人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 109, "其他人數")
# data = pd.concat([data, temp], ignore_index=True)

# temp = caculate(df, 110, "其他人數")
# data = pd.concat([data, temp], ignore_index=True)

print(data)
# low_price = df["最低價"]
# end_price = df["收盤價"]

# # 繪圖
plt.plot(data["學年度"], data["正在接受職業訓練人數"])
plt.plot(data["學年度"], data["正在軍中服役人數"])
plt.plot(data["學年度"], data["需要工作而未找到人數"])
# plt.plot(data["學年度"], data["補習或準備升學人數"])
plt.plot(data["學年度"], data["健康不良在家休養人數"])
plt.plot(data["學年度"], data["準備出國人數"])
plt.plot(data["學年度"], data["其他人數"])
# # plt.plot(date, low_price)
# # plt.plot(date, end_price)
ax = plt.gca()
ax.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
plt.xlabel("學年度")    # x軸標籤
plt.ylabel("人數")    # y軸標籤
plt.legend(["正在接受職業訓練人數", "正在軍中服役人數", "需要工作而未找到人數", "健康不良在家休養人數", "準備出國人數", "其他人數"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("未升學未就業情形")    # 主標題
plt.grid(True)    # 是否有網格?

# 儲存圖片
plt.savefig("pandas_chart.png")
# # 顯示圖片
plt.show()

