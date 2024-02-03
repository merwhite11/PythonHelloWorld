import requests


def main():
    url = "http://127.0.0.1:5000/test"
    data = {"data": "uno, dos, tres"}
    response = requests.post(url, data=data)
    print(response.text)
    return response

if __name__ == "__main__":
    result = main()
    print(result)