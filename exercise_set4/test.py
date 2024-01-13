from binary import say_hello

say_hello()


def loop(max_value):
    counter = 0
    for i in range(max_value):
        counter = counter + 1
    print (counter)

for i in range(100):
    loop(i)