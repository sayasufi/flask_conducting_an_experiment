import time

flag = True


def start_external_function(count, timer):
    global flag
    flag = True
    current = 0
    while current < count and flag:
        do_something(timer)
        # Увеличиваем значение переменной current
        current += 1
        with open("temp.txt", "w") as file:
            file.write(f"{current} {count}")
    if not flag:
        with open("temp.txt", "w") as file:
            file.write(f"{0} {0}")


def do_something(timer):
    global flag
    print("Hello World!")
    start_time = time.time()
    while flag:
        if time.time() - start_time >= timer:
            break
        time.sleep(1)


def stop_external_function():
    global flag
    flag = False
    print("Stopping")
    with open("temp.txt", "w") as file:
        file.write(f"{0} {0}")
