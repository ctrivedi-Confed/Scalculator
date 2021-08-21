import sys
import re

# logic: (add 3 (multiply 3 2))
# expression = ['(add', '3', '(multiply', '3' , '2']
# reverse
# expression = ['2', '3', '(multiply', '3' , '(add']
# expression = ['2', '3', '*', '3' , '+']
# calculate with first sign
# expression = ['6', '3' , '+']
# same as above and return [9]

# you can also do as many as want as an parameter not limited to 2
# like (add 2 3 4)

# you can also add exponentials and divide or any method at the end where I mentioned

def main():
    # tsking all the command line arguments
    expression = sys.argv[1:]

    #if length is 1 then simply return the value
    if len(expression) == 1:
        print(expression[0])

    # if length > 1 then
    else:
        for x in range(0, len(expression)):
            # replaceing the values in the array of expression with signs
            if expression[x] == '(add':
                expression[x] = '+'
            if expression[x] == '(multiply':
                expression[x] = '*'

        # reverse the array so that i can get first expression to evaluate
        expression = expression[::-1]

        # assigning the max index for evaluation
        # so, if does not in the array then it would not affect evaluation
        plus_index = 555
        mul_index = 555

        while len(expression) >= 2:

            # if the index value is '+' then assigning value
            if '+' in expression:
                plus_index = expression.index('+')

            if '*' in expression:
                mul_index = expression.index('*')

            # this will take minimum of 2 because we already reverse the array
            # so it will give index to evaluate first
            if plus_index < mul_index:
                index = plus_index
            elif plus_index > mul_index:
                index = mul_index

            sum = 0
            multiply = 1

            # if value at index is '+'
            if expression[index] == '+':

                # this will look for all the data above and evaluate sum of them
                for i in range(0, index):
                    sum += int(re.search(r'[0-9]+', expression[i]).group())

                print('After Sum: ', sum)
                # replace the value of all that with answer and extend that with remaining expression
                expression = [str(sum)] + expression[index+1:]

            if len(expression) == 1:
                return

            # same work as '+'
            if expression[index] == '*':

                for i in range(0, index):
                    multiply *= int(re.search(r'[0-9]+', expression[i]).group())

                print('After Multiply: ', multiply)
                expression = [str(multiply)] + expression[index + 1:]

            # you can implement future method such as exponents or divide over here


if __name__ == "__main__":
    main()
