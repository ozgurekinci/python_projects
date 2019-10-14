def count_substring(string, sub_string):
    
    # x = [string.find(sub_string,i) for x in string]
    # y = string.split(sub_string)
    # return y
    # return len(y)-1  
    x=0
    for i in range(len(string)):
        if string.find(sub_string,string.index(i)):
            x += 1
            i += len(sub_string)
        else:
            pass

    # return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)