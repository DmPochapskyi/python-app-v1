import requests

def test_home():
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
    print("Test passed: Server responded correctly.")

if __name__ == "__main__":
    try:
        test_home()
    except AssertionError as e:
        print("Test failed: AssertionError")
        raise
    except Exception as e:
        print(f"Test failed: {e}")
        raise
