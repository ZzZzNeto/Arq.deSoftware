
def filter_by_age(age, data_list):
    
    def moreThan(person):
        return int(person['idade']) >= age

    return filter(moreThan, data_list)