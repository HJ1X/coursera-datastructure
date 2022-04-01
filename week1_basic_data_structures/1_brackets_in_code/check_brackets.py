# python3

from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, nxt in enumerate(text):
        if nxt in "([{":
            # Process opening bracket
            opening_brackets_stack.append((nxt, i))

        if nxt in ")]}":
            # Process closing bracket
            if not opening_brackets_stack: 
                return i + 1
            top = opening_brackets_stack.pop()[0]
            matching = are_matching(top, nxt)
            if not matching:
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack.pop()[1] + 1
    else: 
        return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
