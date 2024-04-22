if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scoreList = list(arr)


    def score(scoreList):
        scoreList.sort(reverse=True)
        newList = []
        for i in scoreList:
            if i not in newList:
                newList.append(i)
        return newList


    newList = score(scoreList)
    print(newList[1])
