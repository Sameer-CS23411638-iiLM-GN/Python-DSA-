def infixToPostfix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    stack = []
    result = []

    for char in expression:
        if char.isalnum():
            result.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # remove '('

        else:  # operator
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return "".join(result)

exp = "A+B*(C-D)"
print(infixToPostfix(exp))

print(infixToPostfix("A+B"))         # AB+
print(infixToPostfix("(A+B)*C"))     # AB+C*
print(infixToPostfix("A+B*C"))       # ABC*+
print(infixToPostfix("A*(B+C)/D"))   # ABC+*D/

#INFIX TO POSTFIX
def infixToPostfix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    stack = []
    result = []

    for ch in expression:
        # If operand → add to result
        if ch.isalnum():
            result.append(ch)

        # If opening bracket → push
        elif ch == '(':
            stack.append(ch)

        # If closing bracket → pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        # If operator
        else:
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[ch] or
                   (precedence[stack[-1]] == precedence[ch] and ch != '^'))):
                result.append(stack.pop())
            stack.append(ch)

    # Pop remaining operators
    while stack:
        result.append(stack.pop())

    return "".join(result)
exp = "A+B*(C-D)"
print(infixToPostfix(exp))


#POSTFIX TO INFIX

def postfixToInfix(expression):
    stack = []

    for ch in expression:
        # If operand → push to stack
        if ch.isalnum():
            stack.append(ch)
        else:
            # Pop two operands
            op2 = stack.pop()
            op1 = stack.pop()

            # Form infix expression
            new_expr = "(" + op1 + ch + op2 + ")"

            # Push back to stack
            stack.append(new_expr)

    # Final element is the answer
    return stack[-1]

exp = "AB+CD-*"
print(postfixToInfix(exp))