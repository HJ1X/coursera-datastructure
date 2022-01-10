# pyright: reportMissingImports=false

import os
import subprocess
import sys
import check_brackets  # type: ignore


def remove_next_line(string):
    string_arr = list(string)
    string_arr.pop()
    string = "".join(string_arr)
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

    # running test

    # command = 'type tests\\' + name_test + ' | python check_brackets.py'
    # test_result = os.system(command)

    script_dir = os.path.dirname(__file__)
    rel_path = "tests/" + name_test
    test_filename = os.path.join(script_dir, rel_path)
    with open(test_filename) as test_file:
        test_data = test_file.read()

    test_data = remove_next_line(test_data)

    test_result = str(check_brackets.find_mismatch(test_data))

    # checking result
    script_dir = os.path.dirname(__file__)
    rel_path = "tests/" + name_answer
    answer_filename = os.path.join(script_dir, rel_path)
    with open(answer_filename) as answer_file:
        answer = answer_file.read()

    answer = remove_next_line(answer)

    print(test_result, answer, "\n")
    # print(type(test_result), type(answer))

    if test_result == answer:
        right_answers += 1
    else:
        wrong_answers += 1


print("right_answers = ", right_answers)
print("wrong_answers = ", wrong_answers)
