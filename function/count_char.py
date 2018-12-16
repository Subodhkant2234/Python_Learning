x = -1
def char_count(a, b):
    global x
    for var in a:
        if(var == b):
            x = 1
    return x

def main():
    p = input("Enter a String:")
    q = input("Enter a character:")
    print("Char status", char_count(p , q))

if __name__ == "__main__":
    main()    
     
