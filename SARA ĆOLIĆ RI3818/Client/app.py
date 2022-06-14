import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "ime": "Sara",
  "prezime": "Colic",
  "username": "scolic3818ri",
  "smer": "ri",
  "prdmeti": [
      {
        "ime": "kti",
        "espb": 6
      },
      {
        "ime": "dos",
        "espb": 8
      },
      {
        "ime": "pvi",
        "espb": 6
      },
      {
        "ime": "asp",
        "espb": 6
      }
  ]
})
headers = {
  'Content-Type': 'application/json'
}


def testFunction():
  print("testing...")



conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)

conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)