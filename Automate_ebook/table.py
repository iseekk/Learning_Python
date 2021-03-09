nested_list = [['apples', 'oranges', 'cherries', 'banana'],
               ['Alice', 'Bob', 'Carol', 'David'],
               ['dogs', 'cats', 'moose', 'goose'],
               ['isek', 'leavok', 'zosiek']]


column_width = [max(len(str(item)) for item in column) for column in nested_list]
for line in zip(*nested_list):
    width = (_ for _ in column_width)
    print(" ".join(str(item).rjust(next(width)) for item in line))
