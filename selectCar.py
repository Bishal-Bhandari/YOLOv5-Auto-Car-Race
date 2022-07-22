def carSelect(resultVal, calLoc1, carLoc2):
    x = resultVal.pandas().xyxy[0]  # im predictions (pandas)
    y = x.name
    print(calLoc1)
    for i in y:
        if i == "Mine":
            print(i)
        else:
            print(i)