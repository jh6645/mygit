from Stack_List import Stack
def is_palindrome(input_string):
    s1=Stack()
    length=len(input_string)
    for i in range(length//2):
        s1.push(input_string[i])
    for i in range((length+1)//2+1,length+1,1):
        a=s1.pop()
        if(a!=input_string[i-1]):
            print(f'at {i},{a} is not {input_string[i]}')
            return False
    return True

print(is_palindrome(input()))