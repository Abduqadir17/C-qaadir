#QUESTION 7-1
def test_square_root(a,x):
    while True:
        print(x)
        y=(x+ a/x)/2
        if y==x:
            break
        x=y
print(test_square_root(4,3))
       


#QUESTION 7-2  
def eval_loop():
    while True:
        user_input = input("Enter a python exprssion(or 'done' to finish):")
        if user_input =="done":
            break
        else:
            result =eval(user_input)
            print("Result:", result)

#QUESTION 7-3
            
