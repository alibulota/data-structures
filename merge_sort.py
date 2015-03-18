'''Referenced http://blog.garillot.net/post/9048852162/how-do-you-make-a-recursive-merge-sort-more'''


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) / 2
        left_list = a_list[0:mid]
        right_list = a_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        l_side = 0
        r_side = 0

        for i in range(len(a_list)):
            value_l = left_list[l_side] if l_side < len(left_list) else None
            value_r = right_list[r_side] if r_side < len(right_list) else None

            if (value_l and value_r and value_l < value_r) or value_r is None:
                a_list[i] = value_l
                l_side += 1
            elif (value_l and value_r and value_l >= value_r) or value_l is None:
                a_list[i] = value_r
                r_side += 1
            else:
                raise Exception("Can not merge")
