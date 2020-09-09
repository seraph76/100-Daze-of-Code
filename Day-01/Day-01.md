# [100 Daze of Code](https://github.com/seraph76/100-Daze-of-Code) - Day 01

<div align="center">

### HackerRank Challenges

</div>

**Task 1: Print Function**

> Without using any string methods, print a list of integers from 1 through `n` as a string, without spaces.
> *Example:*
>* Input: n = 5
>* Output: '12345'

**_My Solution_**

```python
def solve1():
    n = int(input())
    res = [str(i) for i in range(1, n+1)]
    return ''.join(res)
```

---

**Task 2: Python If-Else**

> Given an integer `n` perform the following conditional actions:
>* If `n` is odd, print `Weird`
>* If `n` is even and in the inclusive range of `2 to 5`, print `Not Weird`
>* If `n` is even and in the inclusive range of `6 to 20`, print `Weird`
>* If `n` is even and greater than 20, print `Not Weird`

**_My Solution_**

```python
def solve2():
    n = int(input())
    res = ['Weird', 'Not Weird']
    if n % 2 == 1 or n % 2 == 0 and n in range(6, 21):
        return res[0]
    elif n % 2 == 0 and n in range(2, 6) or n > 20:
        return res[1]
```
