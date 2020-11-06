input_line = input()
num_list = input_line.split(" ")
num_list2 = []
num_list3 = []

#リスト内の*,/と数字を一度だけひっくり返す
def kakewaru(num_list):
  for item in num_list:
    if item == "*":
      ka_index = num_list.index(item)
      num_list[ka_index], num_list[ka_index+1] = num_list[ka_index+1], num_list[ka_index]
      num_list[ka_index+1] = "#"
    elif item == "/":
      wa_index = num_list.index(item)
      num_list[wa_index], num_list[wa_index+1] = num_list[wa_index+1], num_list[wa_index]
      num_list[wa_index+1] = "$"
  for item in num_list:
    a = item.replace("#", "*")
    num_list2.append(a)
  for item in num_list2:
    b = item.replace("$", "/")
    num_list3.append(b)
  return num_list3

num_list3 = kakewaru(num_list)

#リスト内の+,-の位置を取得
th_list = []
for item in num_list3:
  if (item == "+") or (item == "-"):
    c = num_list3.index(item)
    th_list.append(c)

#最後以外の要素は+,-を次の+,-の前に置きたい
#最後の,要素は一番最後に置きたい
def tasuhiku(num_list3):
  for i in range(len(th_list)-1):
    d = num_list3.pop(int(th_list[i]))
    num_list3.insert((int(th_list[i+1])-1),d)
  lasign_num = int(th_list[-1])
  lasign = num_list3.pop(lasign_num)
  num_list3.append(lasign)
  return num_list3

print(tasuhiku(num_list3))