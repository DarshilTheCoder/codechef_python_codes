from operator import add, le, sub


a = int(input())
for i in range(0,a):
    total_population = int(input())
    left_population  = int(input())
    imigrated_population = int(input())
    if(total_population>=left_population):
        total_left_population = add(left_population,imigrated_population)
        leftout_population = sub(total_population,total_left_population)
        print(leftout_population)