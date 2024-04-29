def merge_the_tools(string, k):
    no_of_substrings = int(len(string) / k)
    counter = 0
    pos = k
    for i in range(no_of_substrings):
        substring = string[counter:pos]
        counter = pos
        pos += k
        final_substring = ""
        for j in range(len(substring)):
            if not substring[j] in final_substring:
                final_substring += substring[j]
        print(final_substring)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
