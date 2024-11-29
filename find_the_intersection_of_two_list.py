def find_intersection(set1, set2):
    myIntersection = set1.intersection(set2)
    return myIntersection
 
set1 = set(map(int, input("Enter numbers of the first set, separated by spaces: ").split()))
set2 = set(map(int, input("Enter numbers of the second set, separated by spaces: ").split()))
 
result = find_intersection(set1, set2)
print("Intersection of set1 and set2:", result)
