### Question A01

```python
for _ in range(int(input())):
    X, Y = map(int, input().split())
    if X < Y:
        print("FIRST")
    elif X > Y:
        print("SECOND")
    else:
        print("ANY")
        
```

### Question A02

```python
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x < y:
        print("NO")
    elif x >= y:
        print("YES")

```

### Question A03

```python
t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    if(n <= m-k):
        print("YES")
    else:
        print("NO")
        
```

### Question A04

```python
t = int(input())
print("\n")
for i in range(t):
    Pi = input().split(" ")
    Pi[0] = int(Pi[0])
    Pi[1] = int(Pi[1])
    Pi[2] = int(Pi[2])
    print(str(Pi[0]-Pi[1]+Pi[2]))

```

### Question A05

```python
n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    if(z >= x) and (z < y):
        print("yes")
    else:
        print("NO")

```

### Question A06

```python
t = int(input())
for i in range(t):
    k, x = map(int, input().split())
    a = ((k*7)-(x))
    print(a)

```

### Question A07

```python
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if (a > b) and (a > c):
        print("alice")
    elif (b > c) and (b > a):
        print("bob")
    elif (c > a) and (c > b):
        print("charlie")

```
