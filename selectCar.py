def carSelect(resultVal, carLoc1, carLoc2):
    x = resultVal.pandas().xyxy[0]  # im predictions (pandas)
    y = x.name
    for i in y:
        if i == "Mine":
            continue
        else:
            if carLoc1[0] == carLoc2[0]:
                print("bishal")
            else:
                print("hahah")