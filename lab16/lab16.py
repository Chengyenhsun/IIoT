import sys
import time
import requests
import Adafruit_DHT


# 定義感測器型號和 GPIO pin
sensor_args = {
    "11": Adafruit_DHT.DHT11,
    "22": Adafruit_DHT.DHT22,
    "2302": Adafruit_DHT.AM2302,
}


sensor = 11
pin = 4

# ThingSpeak API Key
ThingSpeak_WriteApiKey = "M2AX3DL4KUJ9QYI9"
detection_period = 0.5  # 偵測間隔時間（秒）


def get_sensor_data():
    """讀取溫濕度數據"""
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


while True:
    try:

        # 取得目前的溫濕度
        humidity, temperature = get_sensor_data()

        if humidity is not None and temperature is not None:  # 若讀取成功
            # 構建 ThingSpeak API URL
            ThingSpeak_API_URL = (
                f"https://api.thingspeak.com/update?api_key={ThingSpeak_WriteApiKey}&"
                f'field1={"{0:0.1f}".format(temperature)}&'
                f'field2={"{0:0.1f}".format(humidity)}'
            )
            # 發送 GET 請求至 ThingSpeak
            response = requests.get(ThingSpeak_API_URL)

            now = time.ctime()
            # 顯示 HTTP 回應狀態碼和讀取的數據
            print(f"HTTP: {response.status_code}")
            print(
                now + ",",
                "temperature:",
                temperature,
                "度C,",
                "humidity:",
                humidity,
                "%",
            )
        else:
            # 若讀取失敗則輸出錯誤訊息
            print("Failed to get reading. Try again!")

        # 暫停指定的秒數
        time.sleep(detection_period)

    except KeyboardInterrupt:
        sys.exit(0)
