def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} not found")


def write_and_append(filename):
    with open(filename, 'w') as f:
        f.write("# hello lets start oops\n")
    with open(filename, 'a') as f:
        f.write("# i think you done with oops\n")


def create_and_read(filename):
    try:
        with open(filename, 'x') as f:
            f.write("this file is created once\n")
    except FileExistsError:
        pass

    with open(filename, 'r') as f:
        print(f.read())


def readline_example(filename):
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"{filename} not found")

        
def advanced_methods(filename):
    with open(filename, 'w') as f:
        f.writelines(['12\n', '34\n', 'hiiii\n'])

    with open(filename, 'r+') as f:
        f.write('Hello how are you\nI am good')
        f.seek(5)
        print("Cursor position:", f.tell())
        f.truncate(10)


if __name__ == "__main__":
    read_file('dictionary.py')
    write_and_append('newfile.txt')
    create_and_read('newfile.txt')
    readline_example('calculator.py')
    advanced_methods('newfile.txt')
    print("Program execution completed")
