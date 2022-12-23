print("syntax is num operator num")


a=int(input())
x=input("Chose operand + - * / %")
b=int(input())
match x:
  case '+': print(a+b)
  case "-": print(a-b)
  case "*": print(a*b)
  case "/": print(a/b)
  case "%": print(a%b)
  case _ : print("invalid")
  
  
