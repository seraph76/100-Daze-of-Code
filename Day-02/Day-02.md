# [100 Daze of Code](https://github.com/seraph76/100-Daze-of-Code) - Day 02

<div align="center">

### CodeWars Challenges

</div>

### **Task 1: Testing 1-2-3**

> Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
> Write a function which takes a list of strings and returns each line prepended by the correct number.
> The numbering starts at 1. The format is n: string. Notice the colon and space in between.
> 
>Examples:
>
> * number([]) # => []
>
> * number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

**_My Solution_**

```python
def solve1(lst):
    temp = []
    for idx, item in enumerate(lst, start=1):
        temp.append(f"{idx}: {item}")
    return temp

```
---

### **Task 2: Holiday VI - Shark Pontoon**

> Your friend invites you out to a cool floating pontoon around 1km off the beach. Among other things, the pontoon has
> a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out. 
> As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!
> You need to work out if the shark will get to you before you can get to the pontoon. 
> To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead,
> or swim when you realise you can make it! 
>
> You are given 5 variables: `sharkDistance` = distance the shark needs to cover to eat you in metres, 
> `sharkSpeed` = how fast it can move in metres/second, `pontoonDistance` = how far you need to swim to safety in metres,
> `youSpeed` = how fast you can swim in metres/second, `dolphin` = a boolean, if true, you can half the swimming speed 
> of the shark as the dolphin will attack it. If you make it, return `"Alive!"`, if not, return `"Shark Bait!"`.

**_My Solution_**

```python
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    your_time = pontoon_distance/you_speed
    if dolphin:
        shark_speed = shark_speed/2
        shark_time = shark_distance/shark_speed
    else:
        shark_time = shark_distance / shark_speed
    if not you_speed or pontoon_distance / you_speed > shark_distance / shark_speed:
        return 'Shark Bait!'
    elif not shark_speed or pontoon_distance / you_speed < shark_distance / shark_speed:
        return 'Alive!'
```