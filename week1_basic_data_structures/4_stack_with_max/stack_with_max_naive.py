#python3
import sys
from collections import deque


class StackWithMax():
    def __init__(self):
        self.__stack = deque()
        self.__max = deque()

    def Push(self, a):
        self.__stack.append(a)
        if not self.__max:
            self.__max.append(a)
            return
        if a >= self.__max[-1]:
            self.__max.append(a)

    def Pop(self):
        assert(len(self.__stack))
        val = self.__stack.pop()
        if self.__max[-1] == val:
            self.__max.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "1":
            stack.Push(int(query[1]))
        elif query[0] == "2":
            stack.Pop()
        elif query[0] == "3":
            print(stack.Max())
        else:
            assert(0)