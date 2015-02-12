def prop_parens(str):
    count = 0
    for paren in str:
        if paren == '(':
            count += 1
        if paren == ')':
            count -= 1
        if count < 0:
            return -1
    if count == 0:
        return 0
    else:
        return 1