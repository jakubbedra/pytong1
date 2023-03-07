import time


def isnumeric(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'


def isalpha(char):
    return '0' <= char <= '9'


def isalnum(string):
    for char in string:
        if not isalpha(char) and not isnumeric(char):
            return False
    return True


def correctness_test(filename):
    # generate second file
    with open(filename, 'r') as file:
        ctr = 0
        for line in file:
            if ctr % 2 == 0:
                pass#todo: finish this shit
            ctr += 1

    # compare files
    with open(filename, 'r') as file:
        for line in file:
            if line.isalnum() is not isalnum(line):
                return False
    return True


def performance_test_custom(filename):
    start_time = time.time()

    with open(filename, 'r') as file:
        for line in file:
            isalnum(line)

    end_time = time.time()
    total_time = end_time - start_time

    start_time_loop = time.time()

    with open(filename, 'r') as file:
        for line in file:
            pass

    end_time_loop = time.time()
    total_time_loop = end_time_loop - start_time_loop

    return total_time - total_time_loop


def performance_test_built_in(filename):
    start_time = time.time()

    with open(filename, 'r') as file:
        for line in file:
            line.isalnum()

    end_time = time.time()
    total_time = end_time - start_time

    start_time_loop = time.time()

    with open(filename, 'r') as file:
        for line in file:
            pass

    end_time_loop = time.time()
    total_time_loop = end_time_loop - start_time_loop

    return total_time - total_time_loop


if __name__ == '__main__':
    # correctness test
    filename = 'C:\\Users\\theKonfyrm\\CLionProjects\\pytong1\\cmake-build-debug\\example.txt'
    if not correctness_test(filename):
        print('Correctness test failed!')
    else:
        print('Correctness test passed!')

    # performance test
    print('Performance test for custom function took ', performance_test_custom(filename), ' milliseconds')
    print('Performance test for built-in function took ', performance_test_built_in(filename), ' milliseconds')
