def order_words(text):
    #Here we convert the string into a list, separating it with a hyphen.
    list = text.split("-")
    # Sort the list alphabetically
    list.sort()
    #Here we combine the list again into a string with hyphens
    result = "-".join(list)
    return result

text = "python-variable-function-computer-monitor"
order = order_words(text)
print(order)

