
def parenthesis(count, current, opening, closing):
    output = ''
    if len(current) == count * 2:
        return current
    if opening == count:
        output += (parenthesis(count, current + ')', opening, closing + 1))



print(parenthesis(2, '', 0, 0))
