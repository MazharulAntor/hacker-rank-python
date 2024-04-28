def merge_the_tools(string, k):
    no_of_substrings = int(len(string) / k)
    counter = 0
    for i in range(no_of_substrings):
        substring = string[counter:k]
        counter = k
        k += k
        for j in range(len(substring)):

            print(substring)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
