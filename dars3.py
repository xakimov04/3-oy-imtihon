lst=[[1,2,3], [-3,4,7], [5,7,-5]]

result = max(lst, key=lambda x: sum(x))
print(result)