def binary_search_time(N, P, T):
    num_looks = 1
    search_list = [x + 1 for x in range(N)]
    index =len(search_list) // 2 + 1
    while search_list[index] != P:
        if search_list[index] < P:
            search_list = search_list[index+1:]
        elif search_list[index] > P:
            search_list = search_list[:index]
        index = len(search_list) // 2 + 1
        num_looks += 1
    return num_looks * T


def linear_search_time(N, P, T):
    return P * T


i1 = "1"
i2 = "10 8 10 30"
# for _ in range(int(input())):
    # num_names, position, gt, st = [int(x) for x in input().split(" ") if x != '']
for _ in range(int(i1)):
    num_names, position, gt, st = [int(x) for x in i2.split(" ") if x != '']
    linear_time = linear_search_time(num_names, position, gt)
    binary_time = binary_search_time(num_names, position, st)
    if linear_time < binary_time:
        print(1)
    elif binary_time < linear_time:
        print(2)
    else:
        print(0)
