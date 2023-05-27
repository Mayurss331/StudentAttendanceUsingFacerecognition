import base64


# Encoding the string
encode = base64.b64encode('Asur#123'.encode("utf-8"))
print("str-byte : ", encode)
encode=str(encode)
encode=bytes(encode.encode())
print(encode)
decode = base64.b64decode(encode[2:len(encode)-1]).decode("utf-8")
print("byte-str : ", decode)