import requests


def post_name():
    url = "http://127.0.0.1:5000/pynames"
    data = {"name": "walter"}
    response = requests.post(url, data=data)
    print(response.text)
    return response

def get_names():
    url = "http://127.0.0.1:5000/names"
    response = requests.get(url)
    print(response.text)
    return response

if __name__ == "__main__":
    result = post_name()
    print(result)