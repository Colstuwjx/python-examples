# coding=utf-8

import copy


def new_color():
    colours1 = ["red", "green"]
    # both colours1\colours2
    # pointed to the array
    colours2 = colours1
    print "colours1 addr: {}, colours2 addr: {}".format(id(colours1),
                                                        id(colours2))

    # pointed address changed
    # NOTE: 题外话，这里和其他语言不一样的是:
    # 即便赋予了常量数组，colours2依然是可以赋值改变的
    # 并且可以正常做append等操作，这与其他语言存在差异.
    colours2 = ["rouge", "vert"]
    print "colours1 addr: {}, colours2 addr: {}".format(id(colours1),
                                                        id(colours2))


def new_color_with_change():
    colours1 = ["red", "green"]
    colours2 = colours1
    colours2[1] = "blue"
    # colours1 will also be changed.
    print "colours1 value: {}, colours2 value {}".format(colours1, colours2)


def list_with_copy():
    list1 = ['a', 'b', 'c', 'd']
    list2 = copy.copy(list1)
    print "list2 addr: {} is different to list1's: {}".format(id(list1), id(list2))

    # change list2 item will not change list1
    list2[1] = 'x'
    print "list2 value is {}, while list1 is {}".format(list2, list1)


def list_with_deepcopy():
    list1 = ['a', 'b', ['c', 'd']]
    list2 = copy.copy(list1)

    # change the nested value in list1
    # will also effect on list2
    list1[0] = 's'
    list1[2][0] = 'x'
    print "list2 nested array addr: {} will be same to list1's: {}".format(
        id(list1[2]),
        id(list2[2])
    )
    print "list2 value: {}, list1 is: {}".format(list2, list1)

    # deepcopy removed the side effect
    # it will recursively copy the object to new one.
    list3 = copy.deepcopy(list1)
    list1[0] = 's1'
    list1[2][0] = 's2'
    list3[0] = 's3'
    list3[2][0] = 's4'
    print "list3 nested array addr: {}, which is a new addr!".format(
        id(list3[2])
    )
    print "thus, list3 value: {} is also separate to list1: {}".format(
        list1, list3)


def main():
    # NOTE: denote the method to run case.
    new_color()
    # new_color_with_change()
    # list_with_copy()
    # list_with_deepcopy()

if __name__ == "__main__":
    main()
