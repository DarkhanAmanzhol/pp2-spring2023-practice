n = int(input())

names = set()
grades_sum = {}
grades_count = {}

for _ in range(n):
    name, grade = input().split(' ', 1)
    names.add(name)
    grades_sum[name] = grades_sum.get(name, 0) + int(grade)
    grades_count[name] = grades_count.get(name, 0) + 1

for name in names:
    print(name, grades_sum[name]/grades_count[name])