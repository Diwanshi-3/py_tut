data = [
    "ID=EMP01, Name=Ananya, Scores=[78, 85, 90]",
    "ID=EMP02, Name=Riya, Scores=[88, 92]",
    "ID=EMP03, Name=Karan, Scores=[70, 65, 72, 68]"
]
emp=[]
for i in data:
    start=i.find("ID=")+len("ID=")
    end=i.find(",",start)
    ID=i[start:end]
    start=i.find("Name=")+len("Name=")
    end=i.find(",",start)
    Name=i[start:end]
    start=i.find("Scores=")+len("Scores=")
    Scores=i[start:]
    scores_str =Scores[1:-1] 
    temp_scores =scores_str.split(",")
    scores = []
    for s in temp_scores:
        scores.append(int(s.strip()))
    emp_record = [ID, Name, scores]
    emp.append(emp_record)
print(emp)
for e in emp:
    scores=e[2]
    avg=sum(scores)/len(scores)
    print(f"{e[1]} average score is",avg)
