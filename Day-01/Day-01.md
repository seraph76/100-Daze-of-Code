# [100 Daze of Code](https://github.com/seraph76/100-Daze-of-Code) - Day 01

<div align="center">

### HackerRank Challenges

</div>

**Task: Print Function**

> Without using any string methods, print a list of integers from 1 through `n` as a string, without spaces. 
> *Example:*
>* *Input:* n = 5
>* *Output:* '12345'

**_My Solution_**

```python
def solve1():
    n = int(input())
    res = [str(i) for i in range(1, n+1)]
    return ''.join(res)
```

---

**Task: Python If-Else**

> Given an integer `n` perform the following conditional actions:
>* If `n` is odd, print `Weird`
>* If `n` is even and in the inclusive range of `2 to 5`, print `Not Weird`
>* If `n` is even and in the inclusive range of `6 to 20`, print `Weird`
>* If `n` is even and greater than 20, print `Not Weird`

**_My Solution_**

