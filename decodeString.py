
# Python program to decode a string 
# The string is returned as decoded for 's'
def decode(s):
    intstack = []
    stringstack = []
    temp = ""
    result = ""
    i = 0
    # Traversing the string
    while i < len(s):
        count = 0
 
        # If number, convert it into number
        # and push it into intstack.
        if (s[i] >= '0' and s[i] <='9'):
            while (s[i] >= '0' and s[i] <= '9'):
                # using Python ord() function which returns the Unicode code 
                #  from a given character
                count = count * 10 + ord(s[i]) - ord('0')
                i += 1
            i -= 1
            intstack.append(count)
 
        # If closing bracket ']', pop element until
        # '[' opening bracket is not found in the
        # character stack.
        elif (s[i] == ']'):
            temp = ""
            count = 0
 
            if (len(intstack) != 0):
                count = intstack[-1]
                intstack.pop()
 
            while (len(stringstack) != 0 and stringstack[-1] !='[' ):
                temp = stringstack[-1] + temp
                stringstack.pop()
 
            if (len(stringstack) != 0 and stringstack[-1] == '['):
                stringstack.pop()
 
            # Repeating the popped string 'temo' count
            # number of times.
            for j in range(count):
                result = result + temp
 
            # Push it in the character stack.
            for j in range(len(result)):
                stringstack.append(result[j])
 
            result = ""
 
        # If '[' opening bracket, push it into character stack.
        elif (s[i] == '['):
            if (s[i-1] >= '0' and s[i-1] <= '9'):
                stringstack.append(s[i])
 
            else:
                stringstack.append(s[i])
                intstack.append(1)
 
        else:
            stringstack.append(s[i])
         
        i += 1
 
    # Pop all the element, make a string and return.
    while len(stringstack) != 0:
        result = stringstack[-1] + result
        stringstack.pop()
 
    return result
 

s = "3[a]2[bc]"
s2= "3[a2[c]]"
s3 = "2[abc]3[cd]ef"
print(decode(s))
print(decode(s2))
print(decode(s3))
