def solution(my_string):
    m = ["a","e","i","o","u"]
    for i in m:
        while i in my_string:
            my_string = my_string.replace(i, "")
    return my_string