with open("M3\L1\example.txt","r") as file:
    data = file.read()

print(data)
data += "Wie gehts euch heute?"
file.close()

with open("M3\L1\example.txt","w") as file:
    file.write(data)
file.close()
