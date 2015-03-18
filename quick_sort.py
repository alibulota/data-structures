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


if __name__ == '__main__':
    import timeit

    best = [i for i in xrange(1, 500, 1)]
    worst = [i for i in xrange(-1, 500, 1)]

    def best_case():
        return quick_sort(best)

    def worst_case():
        return quick_sort(worst)

    print "Best Case: {}".format(
        timeit.timeit('best_case()', setup='from __main__ import best_case', number=1000))

    print "Worst Case: {}".format(
        timeit.timeit('worst_case()', setup='from __main__ import worst_case', number=1000))


# Best Case: 30.3696181774
# Worst Case: 30.6029648781
