# pyright: reportMissingImports=false

import os
import sys
from collections import namedtuple
import process_packages_func
import process_packages_class


def remove_next_line(string):
    try:
        string_arr = list(string)
        string_arr.pop()
        string = "".join(string_arr)
        return string
    except:
        return string


try:
    tests = int(sys.argv[1])
except:
    tests = int(input("You forgot to give test argument: "))


right_answers, wrong_answers = 0, 0

for test in range(1, tests + 1):
    # generating file names
    name_test = str(test)
    if test < 10:
        name_test = "0" + str(test)
    name_answer = name_test + ".a"

    print(f"Test no.: {test}")

    package = namedtuple('package', ['arrival_time', 'processing_time'])
    
    # RUNNING TEST
    script_dir = os.path.dirname(__file__)
    rel_path = "tests/" + name_test
    test_filename = os.path.join(script_dir, rel_path)
    with open(test_filename) as test_file:
        first_line = (test_file.readline()).rstrip()
        buffer_size, number_of_packages = map(int, first_line.split())
        packages = []
        for i in range(number_of_packages):
            arrival_time, processing_time = map(int, test_file.readline().rstrip().split())
            packages.append(package(arrival_time, processing_time))


    # test_data = remove_next_line(test_data)
    responses = process_packages_func.process_packages(buffer_size, packages)
    test_result = ''
    for response in responses:
        # print(response.start_time if not response.was_dropped else -1)
        test_result += str(response.start_time) + '\n'
    test_result = remove_next_line(test_result)


    # CHECKING RESULT
    script_dir = os.path.dirname(__file__)
    rel_path = "tests/" + name_answer
    answer_filename = os.path.join(script_dir, rel_path)
    with open(answer_filename) as answer_file:
        answer = answer_file.read()

    answer = remove_next_line(answer)
    # print(len(test_result)) 
    # print(len(answer)) 


    if test_result == answer:
        right_answers += 1
    else:
        wrong_answers += 1


print("right_answers = ", right_answers)
print("wrong_answers = ", wrong_answers)