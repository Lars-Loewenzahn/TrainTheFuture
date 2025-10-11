with open("./quotes.txt", "r+") as file:
    print(file.read())
    print("Enter the author name")
    name = input()
    file.write(f"\n\n({name})\n")
    file.seek(0)
    print(file.read())