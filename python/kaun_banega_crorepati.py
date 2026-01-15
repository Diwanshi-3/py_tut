questions=[ ["1. What is the capital of France?","A. London","B. Paris","C. Rome","D. Berlin","B"],
            ["2. Which number comes after 9?","A. 8","B. 9","C. 10","D. 11","C"],
            ["3. Which animal is known as the King of the Jungle?","A. Tiger","B. Elephant","C. Lion","D. Leopard","C"],
            ["4. How many days are there in a week?","A. 5","B. 6","C. 7","D. 8","C"],
            ["5. How many days in a year?","A. 356","B. 365","C. 965","D.675","B"],
            ["6. Which planet is known as the Red Planet?", "A. Earth", "B. Mars", "C. Venus", "D. Jupiter", "B"],
            ["7. What is H2O commonly known as?", "A. Water", "B. Hydrogen", "C. Oxygen", "D. Helium", "A"],
            ["8. Which ocean is the largest?", "A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic", "C"],
            ["9. Who wrote 'Romeo and Juliet'?", "A. Dickens", "B. Shakespeare", "C. Austen", "D. Twain", "B"],
            ["10. What is the boiling point of water in Celsius?", "A. 90", "B. 80", "C. 100", "D. 120", "C"]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
guaranteed=0
guaranteed_levels=[4,9]
for index,question in enumerate(questions,start=0):
    print(f"Question for rs{levels[index]}")
    print(f"{question[0]}")
    print(f"{question[1]}        {question[2]}\n {question[3]}        {question[4]}")
    reply=input("Enter your answer(A-D) or press q for quit:")
    if reply=='q':
        money=levels[index-1]
        break
    elif reply==question[-1]:
        print(f"Correct Answer! you won Rs{levels[index]}")
        money=levels[index]
        if index in guaranteed_levels:
            guaranteed=money
    else:
        print("Wrong answer")
        money=guaranteed
        break
print(f"your home take money is rs {money}")
