import matplotlib.pyplot as plt
import numpy as np

# 讀檔並建立各年月份溫度的list
with open("Temperature.txt") as f:
    lines = f.read()
    T = lines.split("\n")
    data = []
    temp_list = []
    for i in range(1, len(T)):
        data.append([T[i]])
    for i in range(len(data)):
        temperatures = [float(x) for x in data[i][0].split(",")]
        del temperatures[0]
        temp_list.append(temperatures)

years = np.array(range(2013, 2022))  # 建立年份和月份
months = np.array(range(1, 13))

# 建立第一個子圖
fig1 = plt.figure(figsize=(10, 6))
for i in range(len(temp_list)):
    temperatures = temp_list[i]
    plt.plot(months, temperatures, label=years[i])

plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")
plt.xlabel("Month")
plt.ylabel("Temperature in Degree C")
plt.legend(loc="lower center")
plt.grid(False)
plt.xticks(np.arange(1, 13, step=1))
plt.savefig("lab14_01.png")  # 儲存第一張子圖

# 建立第二個子圖
fig2 = plt.figure(figsize=(10, 6))
monthly_mean = np.mean(temp_list, axis=0)
mean_temperatures = [round(monthly_mean[i], 2) for i in range(len(monthly_mean))]

plt.plot(months, mean_temperatures, marker="o", mec="r", mfc="r")
plt.title("Tainan Monthly Mean Temperature Of 2013 To 2021")
plt.xlabel("Month")
plt.ylabel("Temperature in Degree C")

# 繪製平均線並標示平均值
total_mean = round(np.mean(mean_temperatures), 2)
plt.axhline(
    y=total_mean, ls="--", color="red", label=f"Mean of 9 Years: {total_mean}°C"
)

# 計算標籤的位置
x_text = 1.5
y_text = total_mean + 0.1

plt.text(
    x_text,
    y_text,
    f"{total_mean}°C",
    color="black",
    va="bottom",
    ha="right",
    backgroundcolor="none",
)

# 標示每個點的數值
for i, txt in enumerate(mean_temperatures):
    plt.annotate(
        f"{txt}°C",
        (months[i], mean_temperatures[i]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
    )

plt.legend(fontsize=8)
plt.grid(False)
plt.xticks(np.arange(1, 13, step=1))
plt.savefig("lab14_02.png")  # 儲存第二張子圖

# 合併兩張圖片
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
axes[0].imshow(plt.imread("lab14_01.png"))
axes[0].axis("off")
axes[1].imshow(plt.imread("lab14_02.png"))
axes[1].axis("off")
plt.subplots_adjust(wspace=0.1)
plt.savefig("lab14_03.png", bbox_inches="tight", pad_inches=0.1)
