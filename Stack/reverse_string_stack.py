def reverse_string_stack(my_string):
    """This function reverses string using stack"""
    for letter in my_string:
        stack.push(letter)

    for letter in stack:
        new_string += stack.pop()
    return new_string
