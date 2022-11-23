g={
    '1': ['2','3','4'],
    '2': ['1', '5'],
    '3': ['1','4','7'],
    '4': ['1','3','5','6'],
    '5': ['2','4','6'],
    '6': ['4','5','7'],
    '7': ['3','6']
}
stack=[]
def dfs(stack,g,node):
    if node not in stack:
        stack.append(node)
        for friend in g[node]:
            dfs(stack,g,friend)
    return stack
print(dfs(stack,g,'1'))