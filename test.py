import requests

if __name__ == "__main__":
    print("This is a bad request and returns: ")
    r = requests.post("http://10.0.0.197:8000/score", json={"some-key":"some-value"})
    print(r)
    print(r.content)
    print("This is another bad request and returns: ")
    r = requests.post("http://10.0.0.197:8000/score", json={"some-key":"some-value"})
    print(r)
    print(r.content)
    print("This is a good request and returns: ")
    r = requests.post("http://10.0.0.197:8000/score", json={"x1":4.21,"x2":7.3})
    print(r.json())