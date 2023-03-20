# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        s = list(input().split())
        if s[0]=='insert':
            l.insert(int(s[1]),int(s[2]))
        if s[0]=='remove':
            l.remove(int(s[1]))
        if s[0]=='append':
            l.append(int(s[1]))
        if s[0]=='sort':
            l.sort()
        if s[0]=='pop':
            l.pop()
        if s[0]=='reverse':
            l.reverse()     
        if s[0]=='print':
            print(l)