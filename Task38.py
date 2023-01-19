txt = "п абв р абв и абв в абв е абв т "

my_text = list(filter(lambda x: 'абв' not in x, txt.split()))

print("".join(my_text))