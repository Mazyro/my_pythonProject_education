import os
import sys
#$ FUNCTION=multiply python3 home_task_11.py 1 2


if not os.environ.get("FUNCTION"):
    os.environ.setdefault("FUNCTION", "add")


# os.environ
# print(os.environ["FUNCTION"])

if __name__ == '__main__':

    try:
        a, b = sys.argv[1:]
    except ValueError:
        exit(2)
    try:
        if os.environ['FUNCTION'] == 'add':
            c = int(a) + int(b)
        elif os.environ['FUNCTION'] == 'multiply':
            c = int(a) * int(b)
        elif os.environ['FUNCTION'] == 'divide':
            c = int(a) / int(b)
        elif os.environ['FUNCTION'] == 'minus':
            c = int(a) - int(b)
        else:
            exit(2)
        print(c)
    except ValueError:
        exit(2)
        print(ValueError)

    print(os.environ["FUNCTION"])
