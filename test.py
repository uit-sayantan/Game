def check_goal(target,source):
    target=list(str(target))
    source=list(str(source))
    value = ['-' for _ in range(len(target))]
    
    for i in range(0,len(target)):
        if source[i] == target[i]:
            value[i]='green'
        elif source[i] in target:
            value[i]='yellow'
        else:
            value[i]='red'
    print(value)

check_goal(1234,5222)

print(''.join(['1','2']))