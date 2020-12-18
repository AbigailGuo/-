def find_j(i, data, time, delta):
    index = i+1
    max_slope = max((data[index]+delta-data[i])/(time[index]-time[i]), (data[index]-delta-data[i])/(time[index]-time[i]))
    min_slope = min((data[index]+delta-data[i])/(time[index]-time[i]), (data[index]-delta-data[i])/(time[index]-time[i]))
    final_index = index
    index += 1
    while index < len(data):
        slope = (data[index]-data[i])/(time[index]-time[i])
        if min_slope <= slope <= max_slope:
            final_index = index
            max_slope = max((data[index] + delta - data[i]) / (time[index] - time[i]),
                            (data[index] - delta - data[i]) / (time[index] - time[i]))
            min_slope = min((data[index] + delta - data[i]) / (time[index] - time[i]),
                            (data[index] - delta - data[i]) / (time[index] - time[i]))
            index += 1
        else:
            break
    return final_index


def sample_points(data, time, delta):
    index = 0
    sample_index = [index]
    while index < len(data):
        next_point = find_j(index, data, time, delta)
        sample_index.append(next_point)
        index = next_point
    return sample_index




