# coding=utf-8
# 不加上就無法使用中文註解
import random
from flask import *

app = Flask(__name__)


# 設定根目錄(通常代表首頁)之路由
# 使用render_template函式讓首頁的路由能夠回傳html檔(簡單架構)給前端，來顯示首頁畫面，而不是僅用return文字的方式
@app.route("/")
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾)
    return render_template("lab13.html")


# 設定路由為/set
# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存
@app.route("/student_data", methods=["POST"])
def root():
    data = request.form.to_dict()  # 將表單資料轉換為字典
    print("\n姓名:", data["string1"])  # 使用鍵來取得表單資料
    print("student_ID:", data["string2"], "\n")  # 使用鍵來取得表單資料
    return "ok"  # 回傳ok


# 定義剪刀石頭布的選項
options = ["r", "s", "p"]


# 設定猜拳遊戲的路由
@app.route("/rsp", methods=["GET"])
def play_rps():
    choice = request.args.get("choice")

    if choice in options:
        computer_choice = random.choice(options)
        if choice == computer_choice:  # 判斷電腦和玩家出拳是否相同
            result = "It's tie!"  # 如果電腦和玩家出拳相同，則結果為平手
        elif (  # 判斷電腦和玩家出拳，此為USER贏的情況
            (choice == "r" and computer_choice == "s")
            or (choice == "s" and computer_choice == "p")
            or (choice == "p" and computer_choice == "r")
        ):
            result = "You win!"  # USER贏的情況則回傳You win
        else:  # 判斷電腦和玩家出拳，此為USER輸的情況
            result = "You lose!"  # USER輸的情況則回傳You lose
        print("\ncomputer:", computer_choice, "user:", choice, "\n")
        return result
    else:  # USER輸入r、s、p以外的內容，則會顯示 " 輸入有誤，請重新出拳 "
        return "輸入有誤，請重新出拳"


app.run(host="0.0.0.0", port=3000, debug=True)
