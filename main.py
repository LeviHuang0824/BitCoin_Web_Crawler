# IDE VSCode
# 開始分頁顯示圖示
# %%
import requests as res
import pandas as pd

# 貨幣單位
currency_unit = "twd"  # Taiwan
# currency_unit = "usd" # USA
# 資料存放的網址
url = f"https://www.coingecko.com/price_charts/1/{currency_unit}/90_days.json"
response = res.get(url)  # Get請求
# 把Json格式轉換成dict格式並取得value值
data = response.json()["stats"]
# print(data) # Output -> 2-D List
df = pd.DataFrame(data)
# print(df)
df.columns = ["datetime", "twd"]
# print(df)
# 把datetime資料轉換成日期格式
df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")
# 把DataFrame格式轉換成圖表顯示
# plot() 繪製圖表時，會把index當成x軸，指定的Series當成y軸
df.index = df["datetime"]
# 繪製原始資料折線圖
# df["twd"].plot(kind="line",figsize=[10,5])
# 加入平均線資料
# 抓取前168筆資料做平均運算(每筆資料間隔時間約為1hr)
df["ma7"] = df["twd"].rolling(window=168).mean()
# 168hr=7days，7天均線
df[["twd", "ma7"]].plot(kind="line", figsize=[15, 5])

# %%
