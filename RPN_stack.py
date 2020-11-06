def calc(code):
      data = code.split(" ")
  stack1 = []
  stack2 = []
  for a in data:
    if a == "+":
      stack2.append(a)
      if ("*" in stack2) or ("/" in stack2):
        for _ in range(len(stack2)-1):
          item = stack2.pop(-2)
          stack1.append(item)
      if (stack2.count("+")>1) or ("-" in stack2):
        item = stack2.pop(-2)
        stack1.append(item)
    elif a == "-":
      stack2.append(a)
      if ("*" in stack2) or ("/" in stack2):
        for _ in range(len(stack2)-1):
          item = stack2.pop(-2)
          stack1.append(item)
      if (stack2.count("-")>1) or ("+" in stack2):
        item = stack2.pop(-2)
        stack1.append(item)
    elif a == "*":
      if len(stack2)>0:
        stack2.append(a)
        if (stack2[-2]=="*") or (stack2[-2]=="/"):
          item = stack2.pop(-2)
          stack1.append(item)
      if len(stack2)==0:
        stack2.append(a)
    elif a == "/":
      if len(stack2)>0:
        stack2.append(a)
        if (stack2[-2]=="*") or (stack2[-2]=="/"):
          item = stack2.pop(-2)
          stack1.append(item)
      if len(stack2)==0:
        stack2.append(a)
    else:
      stack1.append(a)
  for _ in range(len(stack2)):
    item = stack2.pop(-1)
    stack1.append(item)
  return stack1

print(calc(input()))
