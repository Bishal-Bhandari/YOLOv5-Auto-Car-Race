# carLoc2 is the opp vech with 142 on left and 408 on right
def carSelect(resultVal, carLoc1, carLoc2):
    x = resultVal.pandas().xyxy[0]  # im predictions (pandas)
    y = x.name
    for i in y:
        if i == "Mine":
            continue
        else:
            if carLoc1[0] == carLoc2[0]:
                if carLoc2[0] == 142:
                    carLoc1[0] += 266
                elif carLoc2[0] == 408:
                    carLoc1[0] -= 266
                else:
                    continue
            else:
                continue