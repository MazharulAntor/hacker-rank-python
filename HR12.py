if __name__ == '__main__':
    N = int(input())

    numbers = []
    command = ""
    position = None
    value = None
    printList = []
    for _ in range(N):
        command = input()
        if command.startswith("insert"):
            _, position, value = command.split()
            position = int(position)
            value = int(value)
            numbers.insert(position, value)
        elif command.startswith("print"):
            printList.append(numbers.copy())
        elif command.startswith("remove"):
            _, value = command.split()
            value = int(value)
            numbers.remove(value)
        elif command.startswith("append"):
            _, value = command.split()
            value = int(value)
            numbers.append(value)
        elif command.startswith("sort"):
            numbers.sort()
        elif command.startswith("pop"):
            numbers.pop()
        elif command.startswith("reverse"):
            numbers.reverse()
        else:
            pass

    for number in printList:
        print(number)
