


#元组
def index_1():
    # Tuple 可以放任意类型的数据类型
    num_list = [1, 2, 3, 4]
    str_list = ['Chile', 'b', 'c']
    mix_list = ['a', 1, 1.0, num_list, str_list]
    mix_tuple = ('chile', 111, 2.2, 'a', num_list)  # 不可赋值

    print(num_list[0])#1
    print(mix_list[1])#1

    print(mix_tuple)#('chile', 111, 2.2, 'a', [1, 2, 3, 4])

    # 不可赋值，否则报错
    #mix_tuple[1] = 1  # TypeError: 'tuple' object does not support item assignment
    #print()




if __name__ == '__main__' :
    index_1()
