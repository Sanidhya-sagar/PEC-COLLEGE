# question 5

def sel_sort():
    input_str = input("Enter space separated elements of the list: ")
    input_list = input_str.split(" ")
    out_list = list()
    for i in input_list:
        try:
            out_list.append(int(i))
        except:
            print("Element", i, "not parsable as integer.")

    n = len(out_list)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(out_list[j] < out_list[min]):
                min = j
        out_list[i], out_list[min] = out_list[min], out_list[i]

    print("Sorted list:", out_list)

sel_sort()