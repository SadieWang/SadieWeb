import requests


class MyClient():
    def queryData(self):
        url = "http://127.0.0.1:5000"
        r = requests.get(url)
        print(r.content)


if __name__ == "__main__":
    my_client = MyClient()
    my_client.queryData()
