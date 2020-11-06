sign_index= {
    "(" : 1,
    "+" : 2,
    "-" : 2,
    "*" : 3,
    "/" : 3,
    ")" : 4
}
 
def calc(code):
    data = code.split(" ")
    stack1 = []
    stack2 = []
    for x in data:
        if x not in sign_index:
            stack1.append(x)
        else:
            if x == "(":
                stack2.append(x)
            elif x == ")":
                stack2_top = stack2[-1]
                while (len(stack2) != 0) and (stack2_top != "("):
                    stack1.append(stack2_top)
                    stack2.pop()
                    if len(stack2) != 0:
                        stack2_top = stack2[-1]
                stack2.pop()
            else:
                if len(stack2) != 0:
                    stack2_top = stack2[-1]
                    while (len(stack2) != 0) and (sign_index[stack2_top] >= sign_index[x]):
                        stack1.append(stack2_top)
                        stack2.pop()
                        if len(stack2) != 0:
                            stack2_top = stack2[-1]
                stack2.append(x)
    for _ in range(len(stack2)):
        item = stack2.pop(-1)
        stack1.append(item)
    return stack1

print(calc(input()))