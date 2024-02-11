#REMOVE PASS AND FIX THIS FUNCTION
def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    input1 = input("Enter the first string: ")
    input2 = input("Enter the second string: ")
    
    result = anagram(input1, input2)
    print(result)

