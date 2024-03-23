class Postfixconverter:
    def __init__(self):
        self.precedence = {"+":1,
                           "-":1,
                           "*":2,
                           "/":2,
                           "^":3}

    def convert(self, infix):
        stack = []
        postfix = []

        for token in infix:
            if type(token) == int or type(token) == float:
                postfix.append(token)

            elif token == "(":
                stack.append(token)

            elif token == ")":
                while len(stack) > 0:
                    operator = stack.pop()
                    if operator == "(":
                        break
                    postfix.append(operator)

            else:
                while (
                    len(stack) > 0 and stack[-1] != "(" and
                    (self.precedence[stack[-1]] > self.precedence[token] or 
                     self.precedence[stack[-1]] == self.precedence[token] and token != "^")
                     ):
                    postfix.append(stack.pop())

                stack.append(token)

        while len(stack) > 0:
            postfix.append(stack.pop())

        return postfix