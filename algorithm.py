numberOfQuestions = int(input("Enter number of questions"))
difficulty = input("Enter difficulty: easy, medium or hard, in lowercase")
title = input("Enter title:")
rc = input ("Enter RC:").replace('"',"'")
source = input("Enter source:")
category = input("Enter category:")


questions = ["","","","","","","","",""]
i=0
while i<numberOfQuestions:
    question = input("Enter the question: ").replace('"',"'")
    optionA = input("Paste all the OPTIONS together and code will take care of the rest: ").replace('"',"'")
    optionB = input("").replace('"',"'")
    optionC = input("").replace('"',"'")
    optionD = input("").replace('"',"'")
    optionE = input("").replace('"',"'")

    solution = input("Enter the solution in lowercase a,b,c,d,e: ")
    explanation = input("Enter the explanation:")


    a = optionA.replace("(A) ","").replace("A. ", "")
    b = optionB.replace("(B) ","").replace("B. ", "")
    c = optionC.replace("(C) ","").replace("C. ", "")
    d = optionD.replace("(D) ","").replace("D. ", "")
    e = optionE.replace("(E) ","").replace("E. ", "") 


    str = f''' 
        {"{"}
        "ques": "{question}",
        "a": "{a}",
        "b": "{b}",
        "c": "{c}",
        "d": "{d}",
        "e": "{e}",
        "solution": "{solution}",
        "explanation":"{explanation}"
        {"}"}
        '''
    questions[i]=str

    i=i+1

returnString = rf'''
{"{"}
  "title":"{title}",
  "rc": "{rc}",
  "ques1": {questions[0]},
  "ques2": {questions[1]},
  "ques3": {questions[2]}, 
  "ques4": {questions[3]},
  "ques5": {questions[4]},
  "ques6": {questions[5]},
  "ques7": {questions[6]},
  "ques8": {questions[7]},
  "ques9": {questions[8]},  
  "difficulty":"{difficulty}",
  "source":"{source}",
  "numberOfQuestions":{numberOfQuestions},
  "category":"{category}"
{"}"}

'''

returnString = returnString.replace('"ques4": "",','').replace('"ques5": "",','').replace('"ques6": "",','').replace('"ques7": "",','').replace('"ques8": "",','').replace('"ques9": "",','')

f = open("outputFile.txt", "w")
f.write(returnString)
f.close()
