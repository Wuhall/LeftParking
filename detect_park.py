import argparse
import cv2
import base64
import time
import os
import json
from datetime import datetime, time as dt_time
from dotenv import load_dotenv
from ali_sms import send_sms
from dashscope_client import analyze_image

# 加载环境变量
load_dotenv()

def capture_frame_and_encode(cap):
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return None, None

    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    return jpg_as_text, frame

def is_within_daytime():
    current_time = datetime.now().time()
    return dt_time(6, 0) <= current_time <= dt_time(19, 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Camera monitoring script')
    parser.add_argument('--frequency', type=int, required=True, help='Execution frequency in minutes')
    parser.add_argument('--mode', choices=['all', 'day'], required=True, help='Execution mode: all day or daytime only')
    args = parser.parse_args()

    # 打开摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    try:
        while True:
            if args.mode == 'all' or (args.mode == 'day' and is_within_daytime()):
                image_base64, frame = capture_frame_and_encode(cap)
                if image_base64:
                    # 使用阿里百炼接口分析图片
                    result = analyze_image(image_base64)
                    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Response: {result}")

                    if "没有" in result:
                        phone_number = os.getenv("TEST_PHONE_NUMBER")
                        sign_name = os.getenv("TEST_SIGN_NAME")
                        template_code = os.getenv("TEST_TEMPLATE_CODE")
                        template_param = json.loads(os.getenv("TEST_TEMPLATE_PARAM"))  # 从字符串解析为字典
                        response = send_sms(phone_number, sign_name, template_code, template_param)
                        print(str(response, encoding='utf-8'))

                time.sleep(args.frequency * 60)
            else:
                time.sleep(60)
    finally:
        cap.release()