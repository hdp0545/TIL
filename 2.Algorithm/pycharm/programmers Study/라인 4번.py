from heapq import heappush, heappop

pq = []
entry_finder = {}
REMOVED = 999999999


def add_task(task, priority=0):
    if task in entry_finder:
        remove_task(task)
    if priority == REMOVED:
        return
    entry = [priority, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    while pq:
        priority, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return (priority, task)
    else:
        return (False, False)


def solution(arr, brr):
    answer = 0
    minus = [brr[i] - arr[i] for i in range(len(arr))]

    for i in range(len(arr)):
        add_task(i, minus[i])

    pin_left = 0
    pin_right = len(arr)

    while (True):
        power, idx = pop_task()
        if (power == False and idx == False):
            break

        if (idx > pin_left):
            s = sum(minus[pin_left:idx])

            if s:
                minus[idx - 1] -= s

                if (minus[idx - 1] == 0):
                    add_task(idx - 1, REMOVED)
                else:
                    add_task(idx - 1, minus[idx - 1])
                answer += 1

                if minus[pin_left] == 0:
                    pin_left += 1

        if (idx + 1 < pin_right):
            s = sum(minus[idx + 1:pin_right])

            if s:
                minus[idx + 1] -= s

                if (minus[idx + 1] == 0):
                    add_task(idx + 1, REMOVED)
                else:
                    add_task(idx + 1, minus[idx + 1])
                answer += 1

                if minus[pin_right - 1] == 0:
                    pin_right -= 1

        minus[idx] = 0

    return answer


print(solution([137, 47, 129, 223, 6, 204, 156, 159, 6, 26, 124, 176, 29, 78, 3, 173, 64, 71, 237, 73, 117, 74, 32, 15, 144, 94, 68, 143, 48, 211, 230, 200, 66, 101, 98, 12, 218, 43, 122, 201, 178, 9, 157, 35, 138, 48, 187, 225, 51, 232, 174, 34, 20, 118, 83, 193, 39, 114, 27, 188, 198, 87, 241, 221, 183, 214, 46, 221, 171, 102, 135, 93, 144, 188, 231, 238, 172, 132, 179, 218, 12, 109, 101, 57, 250, 190, 42, 155, 138, 106, 172, 145, 89, 24, 48, 243, 51, 190, 241, 153],
[237, 137, 57, 211, 47, 190, 243, 188, 20, 183, 118, 66, 48, 106, 201, 129, 32, 221, 179, 193, 145, 218, 232, 241, 109, 156, 64, 94, 153, 138, 173, 29, 198, 187, 101, 15, 143, 83, 101, 124, 27, 34, 39, 157, 12, 138, 12, 73, 135, 225, 144, 231, 214, 238, 172, 93, 46, 43, 98, 51, 48, 78, 117, 223, 155, 9, 174, 230, 6, 218, 190, 250, 71, 3, 24, 87, 241, 68, 204, 159, 114, 102, 26, 144, 188, 6, 178, 171, 200, 89, 176, 74, 221, 42, 172, 122, 51, 132, 48, 35]))