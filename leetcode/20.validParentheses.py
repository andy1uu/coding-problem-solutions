class Solution:
    def isValid(self, s: str) -> bool:

        # Creates a stack to store all the open brackets.
        brackets = []

        # If there is only one bracket in the string...
        if len(s) == 1:

            # Return false because the one bracket has no partner.
            return False

        # For each letter in the input string...
        for letter in s:

            # If the letter is any of the open brackets...
            if letter == "(" or letter == "{" or letter == "[":

                # Push the open bracket onto the stack.
                brackets.append(letter)

            # Else if the letter is ")"
            elif letter == ")":

                # If there is an open bracket in the stack and it is "("
                if len(brackets) > 0 and brackets[len(brackets) - 1] == "(":

                    # Remove the bracket from the stack.
                    brackets.pop()

                # Else there is no open bracket or some other bracket on top...
                else:

                    # Return False because the parentheses are not valid.
                    return False

            # Else if the letter is "}"
            elif letter == "}":

                # If there is an open bracket in the stack and it is "{"
                if len(brackets) > 0 and brackets[len(brackets) - 1] == "{":

                    # Remove the bracket from the stack.
                    brackets.pop()

                # Else there is no open bracket or some other bracket on top...
                else:

                    # Return False because the parentheses are not valid.
                    return False

            # Else if the letter is "]"
            elif letter == "]":

                # If there is an open bracket in the stack and it is "["
                if len(brackets) > 0 and brackets[len(brackets) - 1] == "[":

                    # Remove the bracket from the stack.
                    brackets.pop()

                # Else there is no open bracket or some other bracket on top...
                else:

                    # Return False because the parentheses are not valid.
                    return False

        # Check the length of the stack after going through the entire string
        # to see if there are any more open brackets and return the result.
        return len(brackets) == 0
