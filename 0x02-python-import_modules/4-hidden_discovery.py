#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_of_names = dir(hidden_4)

    for list in range(len(list_of_names)):
        if not list_of_names[list] .startwith("__"):
            print(list_of_names[list])


# if __name__ == "__main__":
#     import hidden_4

#     name_list = dir(hidden_4)

#     for name in range(len(name_list)):
#         if not name_list[name].startswith('__'):
#             print(name_list[name])