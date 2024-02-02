import requests


def main():
    url = "http://localhost:5000/test"
    data = {"probando": "uno, dos, tres"}
    response = requests.post(url, data=data)
    return response

if __name__ == "__main__":
    result = main()
    print(result)