def main ():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    except ValueError as e: 
        print(e)
        return
    
    finally:
        print("Hey, I am inside finally block")

main()