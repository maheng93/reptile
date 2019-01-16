import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/f?kw=" + tieba_name + "&fr=search&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def get_url_list(self):
        url_list = []
        for i in range(100):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "wb+") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("LOL")
    tieba_spider.run()
