import threading
import time

def main() -> None:
    while True:
        t1 = threading.Thread(target=one, args=('one',))
        t2 = threading.Thread(target=two, args=('two',))
        t3 = threading.Thread(target=three, args=('three',))

        t1.start()
        t2.start()
        time.sleep(1)
        t3.start()

def one(string: str) -> None:
    print(string)

def two(string: str) -> None:
    print(string)

def three(string: str) -> None:
    print(string)
    assert 1 == 2

if __name__ == '__main__':
    main()