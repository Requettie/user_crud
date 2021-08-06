import requests

TEST_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Skiing and playing ping pong"
    "active": 1
}

url = "https://127.0.0.1:500/users"

def TEST_USER_CREATION():
    out = requests.post(url,json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("Something went wrong.")

def test_user_deactivate():
    out = requests.delete("%s/2" % URL)
    if out.status_code == 200:
        print(out.json())
    else:
        print("Something went wrong while trying to deactivate a user.")

if __name__ == "__main__":
    test_user_creation()
    test_user_deactivate()