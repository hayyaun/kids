<div dir="rtl">

# پازل های سری اول

### پازل 1

یه تابع درست کن که یه لیست از اعداد بگیره و مجموع اعداد فرد داخلش رو محاسبه کنه

</div>

```python
def sum_all(nums):
  # TODO do something here

a1 = sum_all([2,5,3,8,1])
a2 = sum_all([1,2,3,4,5])
a3 = sum_all([1,1,1,1,1])

print(a1, a2, a3)
# Output: 9 9 5 ✅
```

<div dir="rtl">

### پازل 2

تابعی که نزدیک ترین عدد اول رو نسبت به عدد داده شده پیدا کنه

</div>

```python
def closest_prime(n: int):
  # TODO do something here

a1 = closest_prime(12)
a2 = closest_prime(30)
a3 = closest_prime(8)

print(a1, a2, a3)
# Output: 13 29 7 ✅
```

<div dir="rtl">

### پازل 3

یه تابع درست کن که بزرگ ترین شمارنده مشترک بین دو عدد a و b رو حساب کند

</div>

```python
def bmm(a: int, b: int):
  # TODO do something here

a1 = bmm(18, 24)
a2 = bmm(27, 18)
a3 = bmm(26, 143)

print(a1, a2, a3)
# Output: 6 9 13 ✅
```

<div dir="rtl">

### پازل 4

تابعی که جذر عدد داده شده رو پیدا کنه  
میتونید از روش محاسبه تغریبی کمک بگیرید

</div>

```python
def jazr(n: int):
  # TODO do something here

a1 = jaze(81)
a2 = jaze(49)
a3 = jaze(28)

print(a1, a2, a3)
# Output: 9 7 5.3 ✅
```

<div dir="rtl">

### پازل 5

یه تابع که دوتا محور مختصات بگیره و اونارو با هم جمع کنه

</div>

```python
def sum_coord(coord_a, coord_b):
  # TODO do something here

a1 = sum_coord((0,5), (5,0))
a2 = sum_coord((1,5), (0,-8))
a3 = sum_coord((2,-2), (-2,2))

print(a1, a2, a3)
# Output: (5,5) (1,-3) (0,0) ✅
```

<div dir="rtl">

### پازل 6

یه تابع که یه لیست از اعداد رو بگیره و کمترین عدد رو نمایش بده

</div>

```python
def minimum(nums):
  # TODO do something here

a1 = minimum([1,2,3,4,5,6])
a2 = minimum([20,12,25,32,8,11,91])
a3 = minimum([11,11,10,11])

print(a1, a2, a3)
# Output: 1 8 10 ✅
```

<div dir="rtl">

### پازل 6

یه برنامه که تاس بندازه (تا وقتی کاربر بگه بسه)

</div>

```python
def roll_dice():
  # TODO do something here


for True:
  ask = input('Do you want to roll a dice? (y/n) ')
  if ask != 'y':
    break # stop
  roll_dice()
```
