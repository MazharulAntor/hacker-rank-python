if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scoreList = [record[1] for record in records]
    nameList = []
    newScoreList = []

    for i in scoreList:
        if i not in newScoreList:
            newScoreList.append(i)
    newScoreList.sort()

    if len(records) > 1:
        for record in records:
            if newScoreList[1] in record:
                nameList.append(record[0])

        nameList.sort()
        for name in nameList:
            print(name)
