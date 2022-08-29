from operator import sub


a = int(input())
for i in range(0,a):
    total_friends = int(input())
    course_capacity = int(input())
    number_of_studets_already_registered = int(input())
    remaining_capacity = sub(course_capacity , number_of_studets_already_registered)
    if(total_friends<=remaining_capacity):
        print("YES")
    else:
        print("NO")
    
