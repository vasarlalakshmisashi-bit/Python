#write a python function to reverse the string SITSAIML using stack 
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print("the reversed string is:", reverse_string("luv u amma"))
#write a python funtion to check the given sting is balanced parasethesis or not using stack
def is_balanced_parentheses(s):
    stack = []
    opening = "({["
    closing = ")}]"
    match = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0
    #sort the elements of the stack using recursion
def sort_stack(stack):
    if not stack:
        return

    top = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, top)
    return stack
def insert_sorted(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
        return
    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print("the sorted stack is:", sorted_stack)
