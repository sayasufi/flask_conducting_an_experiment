import time
flag = True


def start_external_function(count):
    global flag
    flag = True
    current = 0
    with open("source/temp.txt", "w") as file:
        file.write(f"{0} {0}")
    while current < count and flag:
        do_something()
        # Увеличиваем значение переменной current
        current += 1
        with open("source/temp.txt", "w") as file:
            file.write(f"{current} {count}")




def do_something():
    print("Hello World!")
    time.sleep(1)


def stop_external_function():
    global flag
    flag = False
    print("Stopping")
    with open("source/temp.txt", "w") as file:
        file.write(f"{0} {0}")
