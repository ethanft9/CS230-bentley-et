columns = ['Name', 'Metres', 'Year', 'Type', 'Main use', 'Country', 'City', 'Lat', 'Lon']

def freq_data(data, count_item, value):
    freq = 0
    index = columns.index(count_item)
    for i in range(len(data)):
        if data[i][index] == value:
            freq += 1
    return freq

def append_data(data, count_item, value, append_item):
    count_index = columns.index(count_item)
    append_index = columns.index(append_item)
    list = []
    for i in range(len(data)):
        if data[i][count_index] == value:
            list.append(data[i][append_index])
    print(list)

    return freq


def average(data, target_item, value, filter_item = "Country"):
    values_list = []
    filter_index = columns.index(filter_item)
    value_index = columns.index(value)
    print(filter_index)

    print(target_item)

    for i in range(len(data)):
       if data[i][filter_index] == target_item:
           values_list.append(data[i][value_index])
    print(data[i][filter_index])
    print(values_list)

    calculation = npy.mean(values_list)
    return calculation


