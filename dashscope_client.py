from openai import OpenAI
import os

def analyze_image(image_base64):
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    task = "你是一个停车场管理员，你的任务是根据提供的图片，告诉用户停车场的最左边或者最右边是否还有空余车位。如果有空余车位，请回复“有”，如果没有空余车位，请回复“没有”。请不要添加其他内容。"
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{image_base64}"}},
                    {"type": "text", "text": task},
                ],
            },
        ]
    )
    return completion.choices[0].message.content