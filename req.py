import requests
r = requests.get("https://site.financialmodelingprep.com/developer/docs/realtime-stock-quote-api#Stock-Price-list")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1" : 4,
#     "p2" : 8
# }
#
# r2 = requests.post(url = url, data = data)