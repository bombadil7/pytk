import sys

def main():
    print("Got %d arguments" % len(sys.argv))
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()
