with open("myfile.txt", "w") as file:
    file.write("Hello, world!")

with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
