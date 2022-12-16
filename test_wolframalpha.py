import wolframalpha

q = input('Question: ')

app_id = '7GU4T-TA5TPW5REV'

client = wolframalpha.Client(app_id)

res = client.query(q)

ans = next(res.results).text


print(ans)

