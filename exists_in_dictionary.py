my_dict={'name':'shahin','age':22,'area':'ctg'}
key=input("enter the key to check: ")
 
if key not in my_dict:
    print("the key isnt exist")
else:
    print(f"the key {key} exists")
