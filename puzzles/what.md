<div dir="rtl">

# پازل های چیشد؟

تو این سری کد ها مسئله هایی که حل کردیم تو کلاس رو با یه روش دیگه حل می کنم.  
سعی کنید کد رو بخونید و درک کنید که چیشد که اینجوری شد؟  
برای درکش وای نسید کدو نگاه کنید دو ساعت فقط.  
بعد از یه کم فکر کردن شروع کنید کد رو تو یه فایل اجرا کنید برا خودتون.  
می تونید از روش دیباگ کردن که تو راهنما ها گذاشتم برای درک کاری که میکنه استفاده کنید

</div>
 
<div dir="rtl">

### پازل 1

تابع فاکتوریل

راهنمایی:

`N! = N x (N-1)!`

</div>

```python
def factorial(n: int):
    if n:
        return n * factorial(n-1)
    return 1

print("5! = ", factorial(5))

# Output:
# 5! = 120
```

<div dir="rtl">

### پازل 2

تابع فیبوناچی

</div>

```python
def fibonacci(n: int):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return 1


for i in range(5):
    print(f'{fibonacci(i)}', end=' ')

# Output:
# 1 1 2 3 5
```

<div dir="rtl">

### پازل 3

جدول ضرب N x M

این یکی واقعا سخته! چجوری داره کار میکنه ینی؟

</div>

```python
def ptable(x: int, y: int, t: int):

    # اگه خطی باقی نمونده تمومش کن
    if not y:
        return

    # اگه به انتهای خط رسیدی برو خط بعدی
    if not x:
        print() # نقطه سرخط
        return ptable(t, y-1, t)

    # در غیر حالت های بالا بیا بنویس ضربش رو
    print(x * y, end='\t')
    # حالا برو سراغ ستون بعدی
    ptable(x-1, y, t)


n = 5
m = 7
ptable(n, m, n)
```

<div dir="rtl">

### پازل 4

جذر صحبح عدد صحیح

</div>

```python
def jazr(n: int, i: int):
    if i * i < n:
        return i-1
    return jazr(n, i+1)


n = 144
print(f'√{n} = {jazr(n, 0)}')

# Output: 
# √144 = 12
```

<div dir="rtl">

### پازل 5

جابجایی مقدار دو متغیر بدون استفاده از متغیر موقتی t

</div>

```python
a = 5
b = 8
print("before: ", a, b)

b = a + b
a = b - a
b = b - a
print("after:  ", a, b)

# Output:
# before:  5 8
# after:   8 5
```

<div dir="rtl">
