def proper_parens(text):
    open_paren = text.count('(')
    closed_parens = text.count(')')
    if open_paren == closed_parens:
        return 0

    if closed_parens > open_paren:
        return -1

    if closed_parens < open_paren:
        return 1
