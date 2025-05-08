from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import os
from dotenv import load_dotenv
import json

# 加载环境变量
load_dotenv()

def send_sms(phone_number, sign_name, template_code, template_param):
    client = AcsClient(
        os.getenv("ACCESS_KEY_ID"),
        os.getenv("ACCESS_KEY_SECRET"),
        os.getenv("REGION_ID")
    )
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    request.add_query_param('PhoneNumbers', phone_number)
    request.add_query_param('SignName', sign_name)
    request.add_query_param('TemplateCode', template_code)
    request.add_query_param('TemplateParam', json.dumps(template_param))

    response = client.do_action_with_exception(request)
    return response

if __name__ == "__main__":
    phone_number = os.getenv("TEST_PHONE_NUMBER")
    sign_name = os.getenv("TEST_SIGN_NAME")
    template_code = os.getenv("TEST_TEMPLATE_CODE")
    template_param = json.loads(os.getenv("TEST_TEMPLATE_PARAM"))  # 从字符串解析为字典
    response = send_sms(phone_number, sign_name, template_code, template_param)
    print(str(response, encoding='utf-8'))