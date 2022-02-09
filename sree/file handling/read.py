path = r"C:\Users\kadapa astha\PycharmProjects\sree\2\456"
with open(path) as f:
    data = f.read()
    print(data)
    print(f.tell())
    f.seek(0)
    print(f.read(10))
