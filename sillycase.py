my_string = "codingdojo"

def sillycase(my_string):
    str_len = int(len(my_string) / 2)
    return(my_string[:str_len].lower() + my_string[str_len:].upper())


print(sillycase(my_string))
