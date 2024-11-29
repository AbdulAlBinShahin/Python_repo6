def rem(n):
    unique_num=[]
    for element in n:
        if element not in unique_num:
            unique_num.append(element)
    return unique_num
 
num=list(map(int,input("enter num: ").split()))
remove=rem(num)
print(f"unique num is {remove}")
