def filter3(data, filter):
    newdata = []
    for x in data:
        if x["turma"] == filter:
            newdata.append(x)
    return newdata