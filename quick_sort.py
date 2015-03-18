def quick_sort(data):
    pivot_list = []
    small_data = []
    big_data = []
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        for i in data:
            if i < pivot:
                small_data.append(i)
            elif i > pivot:
                big_data.append(i)
            else:
                pivot_list.append(i)
        small_data = quick_sort(small_data)
        big_data = quick_sort(big_data)
        return small_data + pivot_list + big_data



        # for i, val in enumerate(data):
        #     if i != pivot:
        #         if val < data[pivot]:
        #             small_data.append(val)
        #         else:
        #             big_data.append(val)

        # quick_sort(small_data)
        # quick_sort(big_data)
        # data[:] = small_data + [data[pivot]] + big_data
