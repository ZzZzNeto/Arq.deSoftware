def filter1(data, filter):
    newdata = []
    for x in data:
        if x["genero"] == filter:
            newdata.append(x)
    return newdata
