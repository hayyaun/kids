<div dir="rtl">

# پازل های متن ها

سلام به همگی!  
لطفا پازل های زیر رو حل کنید. برای حل فقط خط هایی که TODO دارن رو پاک کنید و جاشون کد درست رو اضافه کنید. جواب نهایی صحیح هم توی خط آخر نوشته شده. اگه جواب بدست اومده شما بعد از اجرای برنامه ای که نوشتید با جواب نهایی فرق داشت احتمالا یه جایی اشتباه کردید و لازمه دوباره تلاش کنید.

### پازل 1

ما میدونیم که تابع درون سیستمی `len()` طول یه متن رو بهمون میده  
ازتون میخام یه تابع درست کنید که یه متن بگیره و همین کارو بکنه دقیقا

</div>

```python
def str_len(s: str):
  # TODO do something here

a1 = str_len("Hello!")
a2 = str_len("Devs are cool!")
a3 = str_len("Yoohoo")

print(a1, a2, a3)
# Output: 6 14 6 ✅
```

<div dir="rtl">

### پازل 2

تابعی که یه متن رو برعکس کنه و تحویل مشتری بده 😂  
یادتونه میشد با `list[:-1]` یه لیست رو برعکس کرد؟

</div>

```python
def str_reverse(s: str):
  # TODO do something here

a1 = str_reverse("Hello")
a2 = str_reverse("Hi!")
a3 = str_reverse("WoW")

print(a1, a2, a3)
# Output: olleH !iH WoW ✅
```

<div dir="rtl">

### پازل 3

یه تابع که بگه یه متن پالیندروم هست یا نه؟  
پالیندروم به متنی میگن که از هر طرف بخونی عین هم باشه. مثل: گرگ

</div>

```python
def palindrome(s: str):
  # TODO do something here

a1 = palindrome("WoW")
a2 = palindrome("()()")
a3 = palindrome("())(")

print(a1, a2, a3)
# Output: True False True ✅
```

<div dir="rtl">

### پازل 4

تابعی که یه متن بگیره و فاصله هارو پاک کنه!  
دیگه راهنمایی نکنم با چی میشد یه آیتم رو از لیست پاک کرد...

</div>

```python
def str_compact(s: str):
  # TODO do something here

a1 = str_compact('Hi Hu Ha')
a2 = str_compact('x x x x x')
a3 = str_compact('G o o d !')

print(a1, a2, a3)
# Output: HiHuHa xxxxx Good! ✅
```

<div dir="rtl">

### پازل 5

یه تابع که یه جمله بگیره و اگه حرف زشت داشت بهمون بگه 😇  
میتونی یه لیست از کلمات بد بسازی و چک کنی که آیا تو متن همچین چیزی دیده شده یا نه  
برای پیدا کردن یه متن داخل یه جمله میتونی از تابع `find()` کمک بگیری.  
یه راه دیگه هم استفاده از `if x in s` هست! که یعنی آیا فلان چیز تو بهمان چیز هست یا نه؟

</div>

```python
def str_bad(s: str):
  # TODO do something here

a1 = str_bad("He is and idiot!")
a2 = str_bad("Everything is fine")
a3 = str_bad("Crazy!")

print(a1, a2, a3)
# Output: True False True ✅
```

<div dir="rtl">

### پازل 6

یه برنامه که متن از مشتری بگیره تا ابد هی پرینتش کنه 😈

</div>

<br/>
<hr/>
<br/>

<div dir="rtl">

برای حل مثال های بیشتر [میتونی بری به این سایت](https://www.w3schools.com/python/exercise.asp?x=xrcise_strings1)

</div>
