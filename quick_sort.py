def quick_sort(data):
    if len(data) > 1:
        pivot = len(data) / 2
        small_data = []
        big_data = []

        for i, val in enumerate(data):
            if i != pivot:
                if val < data[pivot]:
                    small_data.append(val)
                else:
                    big_data.append(val)

        quick_sort(small_data)
        quick_sort(big_data)
        data[:] = small_data + [data[pivot]] + big_data
