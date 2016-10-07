f = input()
skobki = []
open_skobki = []
err = False
index = 0
for line in f:
    if line == "{" or line == "}" or line == "[" or line == "]" or line == "(" or line == ")":
        skobki.append(line)

for skobka in skobki:
    if skobka == "{" or skobka == "[" or skobka == "(":
        open_skobki.append(skobka)
    else:
        if len(open_skobki) <= 0:
            err = True
            break
        elif open_skobki[len(open_skobki)-1] == "{" and skobka == "}" or open_skobki[len(open_skobki)-1] == "[" and skobka == "]"or open_skobki[len(open_skobki)-1] == "(" and skobka == ")":
            open_skobki.pop(len(open_skobki)-1)
        else:
            err = True
            break
    index += 1

if index != len(skobki) and err == True:
    print(index)
elif index == len(skobki) and len(open_skobki) == 0:
    print("yes")
else:
    print("-1")

