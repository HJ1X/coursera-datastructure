#Imports
from collections import namedtuple
from collections import deque



#### ----------------------------------------------------------------------- Required functions -------------------------------------------------------------------- ####

def is_empty(buffer):
    if not buffer: return True
    else: return False

def is_full(buffer):
    if len(buffer) == buffer.maxlen:
        return True
    else:
        return False

#### --------------------------------------------------------------------------------------------------------------------------------------------------------------- ####

buffer_package = namedtuple('buffer_package', ['finish_time', 'start_time'])
package = namedtuple('package', ['arrival_time', 'processing_time'])
response = namedtuple('response', ['was_dropped', 'start_time'])


def process(curr_package, buffer):

    # Removing completed packages
    if not is_empty(buffer):
        popped_package = buffer.popleft()
        while popped_package.finish_time <= curr_package.arrival_time:
            if is_empty(buffer):
                break
            popped_package = buffer.popleft()
        else:
            buffer.appendleft(popped_package)

    # Adding current package to buffer
    if not is_full(buffer):
        if is_empty(buffer):
            start_time = curr_package.arrival_time
        else:
            popped_package = buffer.pop()
            start_time = popped_package.finish_time
            buffer.append(popped_package)
        finish_time = start_time + curr_package.processing_time
        buffer.append(buffer_package(finish_time, start_time))
        return response(was_dropped=False, start_time=start_time)
    
    return response(was_dropped=True, start_time=-1)


def process_packages(buffer_size, packages):

    # Initializing buffer and response variables
    buffer = deque([], maxlen=buffer_size)
    responses = []

    # Processing requests separately
    for package in packages:
        response = process(package, buffer)
        responses.append(response)

    return responses


def main():
    buffer_size, no_of_packages = map(int, input().split())
    packages = []
    for i in range(no_of_packages):
        arrival_time, processing_time = map(int, input().split())
        packages.append(package(arrival_time, processing_time))
    responses = process_packages(buffer_size, packages)

    for response in responses:
        print(response.start_time if not response.was_dropped else -1)


if __name__ == '__main__':
    main()