def check_code():
    print("a :",ord("a"),"z :",ord("z"))
    print("A :",ord("A"),"Z :",ord("Z"))
    for i in range(10):print(i,ord(str(i)),end="")
    print()
    print("(",ord("("))
def main():
    check_code()
if __name__=="__main__":
    main()