a = int(input())
for i in range(0,a):
    total_weeks = int(input())
    days_already_passed = int(input())
    total_days = total_weeks*7
    days_left = total_days-days_already_passed
    print(days_left)