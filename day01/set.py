my_set = {1,2,3,4,5,5}
print(my_set)

java = {"유재석","김병만","양세형"}
python = set(["유재석","박명수"])

print(java& python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

