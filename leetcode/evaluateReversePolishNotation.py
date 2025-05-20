        stack = []

        operators = ["+", "-", "*", "/"]

        for token in tokens:

            if token in operators:

                result = 0
                num1 = 0
                num2 = 0

                if token == "+":

                    num1 = stack.pop()
                    num2 = stack.pop()

                    result = num1 + num2
                
                    stack.append(result)

                elif token == "-":

                    num1 = stack.pop()
                    num2 = stack.pop()

                    result = num2 - num1
                
                    stack.append(result)

                elif token == "*":

                    num1 = stack.pop()
                    num2 = stack.pop()

                    result = num1 * num2
                
                    stack.append(result)   

                elif token == "/":

                    num1 = stack.pop()
                    num2 = stack.pop()

                    result = int(float(num2) / num1)
                
                    stack.append(result)     
            
            else:
                stack.append(int(token))

        return stack[0]   