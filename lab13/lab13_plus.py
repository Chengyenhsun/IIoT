# coding=utf-8
# 不加上就無法使用中文註解
import json
from flask import *

app = Flask(__name__)

# 建立空字典來存儲店名和評分
store_scores = {}


# 設定根目錄(通常代表首頁)之路由
@app.route("/")
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾)
    return render_template("lab13_plus.html", current_data=store_scores)


# 設定路由為/set
# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存
@app.route("/set", methods=["POST"])
def root():
    global data_dict_string
    data = request.form.to_dict()  # 將表單資料轉換為字典
    print("\nuser input data:", data)  # 使用鍵來取得表單資料

    # 從表單資料中獲取店名和分數
    store_name = data.get("store_name")
    score = data.get("score")

    # 將店名和分數存入字典
    store_scores[store_name] = score

    # 將字典轉換為 JSON 字串
    data_dict_string = json.dumps(store_scores, ensure_ascii=False)

    # 在控制台顯示當前的字典資料
    print("data on server:", store_scores, "\n")

    return render_template("lab13_plus.html", current_data=data_dict_string)


# 設定路由為/reset
@app.route("/reset/<choice>", methods=["GET"])
def reset(choice):
    global store_scores  # 使用 global 關鍵字來在函數內部使用全域變數
    if choice == "y":
        store_scores = {}  # 清空字典
        print("data on server:", store_scores, "\n")
        return render_template("reset.html")  # 回傳 reset.html 畫面
    elif choice == "n":  # 不要reset則回傳當前的data
        return render_template("lab13_plus.html", current_data=data_dict_string)


app.run(host="0.0.0.0", port=3000, debug=True)
