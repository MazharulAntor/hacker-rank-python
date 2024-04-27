def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    score_stuart = score_kevin = 0

    for i in range(len(string)):
        if string[i] not in vowel:
            score_stuart += len(string) - i
        else:
            score_kevin += len(string) - i

    if score_stuart > score_kevin:
        print(f"Stuart {score_stuart}")
    elif score_stuart < score_kevin:
        print(f"Kevin {score_kevin}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
