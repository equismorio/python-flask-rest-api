import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"Tims Basketball","views":100,"likes": 10},
        {"name":"Josephs Orchestra","views":999,"likes": 99},
        {"name":"Moms tik-tok","views":1,"likes": 1}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
# response = requests.put(BASE + "video/1", {"name":"Butch","views":100,"likes": 10})
# print(response.json())
# input()
# response = requests.delete(BASE + "video/2")
# print(response)
# input()
# response = requests.get(BASE + "video/1")
# print(response.json())
# input()
response = requests.get(BASE + "videos")
print(response.json())
