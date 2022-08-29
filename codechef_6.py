a = int(input())
for i in range(0,a):
    age_of_chef = int(input())
    min_age = int(input())
    max_age = int(input())
    if(age_of_chef>=min_age and age_of_chef<max_age):
        print("YES")
    else:
        print("NO")