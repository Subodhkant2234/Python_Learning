def sum_of_input(a, b):
    if(type(a) == int and type(b) == int):
        return a+b
    if(type(a) == str and type(b) == str):
        return a+ " "+b
    else:
        return -1

def main():
    return sum_of_input("test", 6)

if __name__ == "__main__":
    ret = main()
    if(ret < 0):
        print("Error: argument need to be same")
