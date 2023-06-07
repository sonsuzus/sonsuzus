make_leave = lambda n: 4 * n + 1

group_count = 5
leave_width = 3
total_width = make_leave(group_count + leave_width - 2)
space = 20

for i in range(group_count):
    for j in range(leave_width):
        leaveCount = make_leave(i + j)
        leaveStr = leaveCount * '*'
        leaveStr = space * ' ' + leaveStr.center(total_width)
        print(leaveStr)

woodStr = (space * ' ' + (leave_width * '*').center(total_width) + '\n') * leave_width
print(woodStr)