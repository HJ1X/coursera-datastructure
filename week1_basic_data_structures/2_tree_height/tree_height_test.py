import os
import sys
import subprocess

try:
    tests = int(sys.argv[1])
except:
    tests = int(input('You forgot to give test argument: '))

right_answers, wrong_answers = 0, 0

for test in range(1, tests + 1):
    # generating file names
    name_test = str(test)
    if test < 10:
        name_test = '0' + str(test)
    name_result = name_test + '.a'

    # running test
    command = 'type tests\\' + name_test + ' | python tree_height.py'
    test_result = os.system(command)

    # checking result
    answer = os.system('type tests\\' + name_result)
    if test_result == answer:
        right_answers += 1
    else:
        wrong_answers += 1

print('right_answers = ', right_answers)
print('wrong_answers = ', wrong_answers)