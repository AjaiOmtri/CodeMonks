def change_provider(money, denomination_list):
    change = []
    for denom_tuple in denomination_list:
        if money == 0:
            break
        elif money >= denom_tuple[1]:
            change.append((denom_tuple[0], money//denom_tuple[1]))
            money = money%denom_tuple[1]
        else:
            continue
    return change


if __name__ == '__main__':
    std_denomination_list = [('quater', 25), ('dime', 10), ('nickel', 5), ('penny', 1)]
    custom_denom_list = [('ajay', 60), ('keerthi', 12), ('shiva', 2), ('naga', 1)]
    assert(change_provider(10, denomination_list=std_denomination_list) == [('dime', 1)])
    assert(change_provider(11, denomination_list=std_denomination_list) == [('dime', 1), ('penny', 1)])
    assert(change_provider(135, denomination_list=custom_denom_list) == [('ajay', 2), ('keerthi', 1), ('shiva', 1), ('naga', 1)])
    assert(change_provider(135, denomination_list=std_denomination_list) == [('quater', 5), ('dime', 1)])
