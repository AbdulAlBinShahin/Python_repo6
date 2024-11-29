num=list(map(int,input("enetr num: ").split()))
element_count={}
for i in num:
    if i in element_count:
        element_count[i]+=1
    else:
        element_count[i]=1
for element,count in element_count.items():
    print(f"Element {element} occurs {count} times")
