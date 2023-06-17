def print_colors():
    print("\033[4mForeground Colors\033[0m")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            print(u"\u001b[38;5;" + code + "m " + code.ljust(4), end="")
        print(u"\u001b[0m")

    print("\033[4mBackground Colors\033[0m")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            print(u"\u001b[48;5;" + code + "m " + code.ljust(4), end="")
        print(u"\u001b[0m")

print_colors()
