import sys

def main():
 
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Довідка: Це простий скрипт, що демонструє роботу sys.argv")
            return


    print("командна строка")

if __name__ == "__main__":
    main()
