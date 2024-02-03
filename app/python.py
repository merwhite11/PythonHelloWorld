import requests


def main():
    url = "http://127.0.0.1:5000/names"
    data = {"name": "sam"}
    response = requests.post(url, data=data)
    print(response.text)
    return response

def get_names():
    url = "http://127.0.0.1:5000/names"
    response = requests.get(url)
    print(response.text)
    return response

if __name__ == "__main__":
    result = get_names()
    print(result)