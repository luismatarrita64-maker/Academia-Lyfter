def list_words(list, n):
    result = []
    for text in words :
        if len(text) > n :
            result.append(text)
    return result

words = ["hello", "python", "sun", "programming"] 
n = int(input("enter the number :"))

result = (list_words(list,n))
print (result)