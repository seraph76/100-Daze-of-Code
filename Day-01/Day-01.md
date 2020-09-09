# [100 Daze of Code](https://github.com/seraph76/100-Daze-of-Code) - Day 01

### HackerRank Challenges

> Without using any string methods, Print a list of integers from 1 through N as a string, without spaces. 

 *Example:*

* *Input:* n = 5

* *Output:* 12345

**My Solution**

```python
def solve1():
    n = int(input())
    res = [str(i) for i in range(1, n+1)]
    return ''.join(res)
```

---


