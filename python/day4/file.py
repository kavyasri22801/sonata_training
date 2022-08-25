def file():
    try:
        a=open('myfile.txt','r')
        print(a.read())
    except(FileNotFoundError):
        return "file not found"
b=file()
print(b)