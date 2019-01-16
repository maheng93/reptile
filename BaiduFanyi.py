#coding=utf-8
import requests
import json
import sys

class BaiduFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 "
                          "(KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content)

    def get_ret(self, dict_response):
        """提取翻译的结果"""
        ret = dict_response["trans"][0]["dst"]
        print("result is :", ret)

    def run(self):
        # 1.获取语言类型
        lang_detect_data = {"query": self.trans_str}
        # 1.1 发送post请求，获取响应获取语言类型
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        # 2.准备post请求，获取响应
        trans_data = {"from": "zh", "to": "en", "query": self.trans_str} if lang == "zh" else \
            {"from": "en", "to": "zh", "query": self.trans_str}
        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4.提取翻译结果
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_str = input("请输入需要翻译的语句：")
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()
