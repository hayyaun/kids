### راهنمای تمرین عدد اول

این یک فلوچارت برای برای فهمیدن این که n عدد اول است:

> **گرفتن عدد n**: ابتدا عدد n را از کاربر میگیریم

> **حلقه**: در این حلقه میگردیم به دنبال اینکه ببینیم عدد مورد بررسی n بر عددی قبل از خود بخش پذیر است یا خیر؟
>
> > > در صورتی که بخش پذیر نبود: به پرچم دست نمیزنیم و ادامه میدهیم  
> > > ولی در صورتی که بخش پذیر بود: پرچم را برای همیشه پایین میگیریم و آرزوی ها نقش بر آب شد و این عدد طبق حدس ما عدد اول نبوده!

> **نمایش عدد اول**: در انتها در حلقه بزرگ اعدادی که اول هستند را نمایش می دهیم

### فلوچارت

```mermaid
flowchart TD
    A[Start] --> E[Get n]
    E --> F[Set flag is_prime = True]
    F --> G{Is i in range 2 to n ?}
    G -- No --> I[Print number if is_prime]
    G -- Yes --> H{If n % i == 0}
    H -- Yes --> J[Set is_prime = False]
    J -- No --> B[Break]
    B --> G
    I --> Z[End]
```