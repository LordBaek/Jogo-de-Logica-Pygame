
def nome():
    file = open ("historia.txt", "a")
    file.write("\n")
    file.write(str(input("Insira Nome: ")))
    file.write("\n")
    file.write(str(input("Insira Email: ")))
    file.write("\n")
    file.close()
