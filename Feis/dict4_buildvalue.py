l = list(range(5))

print(l)

print([v+10 for v in l])

print({v:v+10 for v in l})



s= 'hello world'

print({c.upper():c for c in s})