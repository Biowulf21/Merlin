body = "The NAME is DATE and TIME"
for word in (("NAME", "GBRIEL"), ("DATE", "OTEN"), ("TIME","oten2")):
    body = body.replace(*word)
print(body)