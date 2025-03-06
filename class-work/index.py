def index(message, sub_message):
    flag = -1
    length = len(message)
    sub_length = len(sub_message)
    if length < sub_length:
        return -1
    else:
        for index in range(length):
            if message[index:index+sub_length] == sub_message:
                flag = index
        return flag




