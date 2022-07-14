def carSelect(resultVal):
    x = resultVal.pandas().xyxy[0]  # im predictions (pandas)
    y = x.name
    for i in y:
        if i == "Mine":
            print("This is my car")
        else:
            print("Car alert")