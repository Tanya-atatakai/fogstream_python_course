def count_brackets(my_string):
    stack = []
    current_position = 0

    open_brackets  = ("(", "[", "{")
    close_brackets = (")", "]", "}")

    for my_char in my_string:
        for bracket in open_brackets:
            if my_char == bracket:
                stack.append(my_char)
                continue
        for bracket in close_brackets:
            if my_char == bracket:
                if len(stack) != 0:
                    old_braket = stack.pop()
                    if open_brackets.index(old_braket) != close_brackets.index(my_char):
                        return current_position
                else:
                    return current_position

        current_position += 1

    if len(stack) == 0:
        return "yes"
    else:
        return -1


new_string = input("Введите строку: ")
result = count_brackets(new_string)
print(result)
