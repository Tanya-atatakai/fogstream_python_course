string = input()
brackets = []
open_brackets = []
err = False
index = 0
for line in string:
    if line == "{" or line == "}" or line == "[" or line == "]" or line == "(" or line == ")":
        brackets.append(line)

for bracket in brackets:
    if bracket == "{" or bracket == "[" or bracket == "(":
        open_brackets.append(bracket)
    else:
        if len(open_brackets) <= 0:
            err = True
            break
        elif open_brackets[len(open_brackets)-1] == "{" and bracket == "}" or open_brackets[len(open_brackets)-1] == "[" and bracket == "]"or open_brackets[len(open_brackets)-1] == "(" and bracket == ")":
            open_brackets.pop(len(open_brackets)-1)
        else:
            err = True
            break
    index += 1

if index != len(brackets) and err == True:
    print(index+1)
elif index == len(brackets) and len(open_brackets) == 0:
    print("yes")
else:
    print("-1")


