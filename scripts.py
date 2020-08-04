def list_ready():
    print('\n$==============================================================================$')
    print("Creates and prints a list to copy to clipboard.")
    the_str = input("Enter list elements separated by spaces: ")
    lst = []
    for i in range(len(the_str)):
        if the_str[i] != ' ':
            lst.append(the_str[i])
    
    print(lst)
    print('\n$==============================================================================$')
    