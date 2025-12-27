students = {
    "Diwanshi": {"Age": 18, "Class": "12th"},
    "Rahul": {"Age": 17, "Class": "11th"}
}

print(students["Diwanshi"]["Age"])  
for student, info in students.items():
    print(f"{student} is {info['Age']} years old in {info['Class']}")

#Dictionary Comprehension

dict1={x:x**2 for x in range(11) if x%2==0}
print(dict1)
