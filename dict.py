dict={'Alice': 24,'Neha': 23,'Shivam':22,'Soumik':25}
print(dict)
name=input("enter the student's name: ")
if name in dict.keys():
    print(f"{name}'s marks:  {dict[name]}")
else:
    print("Student not found")