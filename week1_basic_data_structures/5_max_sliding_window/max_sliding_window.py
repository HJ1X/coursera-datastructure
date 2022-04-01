# python3

from collections import deque


# ------------------------------------------------------- Classes --------------------------------------------------- #
class StackWithMax:
    def __init__(self):
        self.__stack = deque()
        self.__max = deque()

    def push(self, a):
        self.__stack.append(a)
        if not self.__max:
            self.__max.append(a)
            return
        if a >= self.__max[-1]:
            self.__max.append(a)

    def pop(self):
        assert(len(self.__stack))
        val = self.__stack.pop()
        if self.__max[-1] == val:
            self.__max.pop()
        return val

    def max(self):
        if not len(self.__stack):
            return -1
        return self.__max[-1]

    def is_empty(self):
        if len(self.__stack):
            return False
        else:
            return True


class QueueUsingStack:
    def __init__(self):
        self.__stack1 = StackWithMax()
        self.__stack2 = StackWithMax()

    def enque(self, value):
        self.__stack1.push(value)

    def deque(self):
        if self.__stack2.is_empty():
            if self.__stack1.is_empty():
                raise IndexError('Could not deque from empty queue')

            while not self.__stack1.is_empty():
                val = self.__stack1.pop()
                self.__stack2.push(val)
            
        return self.__stack2.pop()

    def max(self):
        return max(self.__stack1.max(), self.__stack2.max())


# ---------------------------------------------------- Functions ---------------------------------------------------- #
def max_sliding_deque_relevant_items(sequence, window_size):
    dq = deque()
    maximums = []

    for curr_index in range(len(sequence)):
        
        # removing first element if out of window
        if dq and dq[0] <= curr_index - window_size:
            dq.popleft()

        # Adding new relevant element
        while dq and sequence[curr_index] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(curr_index)

        # Adding maximum after first window
        if curr_index >= window_size - 1:
            maximums.append(sequence[dq[0]])

    return maximums


def max_sliding_window_blocks(sequence, n):
    prefix = []

    for i in range(len(sequence)):
        if i % n == 0:
            prefix.append(sequence[i])
        else:
            prefix.append(max(prefix[i - 1], sequence[i]))

    suffix = [sequence[-1]]
    for i in reversed(range(len(sequence) - 1)):
        if i % n == 0:
            suffix.insert(0, sequence[i])
        else:
            suffix.insert(0, max(suffix[0], sequence[i]))

    maximums = []
    for i in range(len(sequence) - n + 1):
        j = i + n - 1
        maximums.append(max(prefix[j], suffix[i]))

    return maximums


def max_sliding_queue_using_stack(sequence, n):
    maximums = []

    # Initializing window
    window = QueueUsingStack()
    for i in range(n):
        window.enque(sequence[i])
    maximums.append(window.max())

    # Moving window right 
    for i in range(n, len(sequence)):
        window.enque(sequence[i])
        window.deque()
        maximums.append(window.max())

    return maximums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

# ------------------------------------------------------------------------------------------------------------------- #


def main():
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_deque_relevant_items(input_sequence, window_size))


if __name__ == '__main__':
    main()
