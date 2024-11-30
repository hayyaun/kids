import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        # محاسبه BMI
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        # تعیین وضعیت
        if bmi <= 18.4:
            status = 'Underweight'
        elif 18.4 < bmi <= 24.9:
            status = 'Normal'
        elif 24.9 < bmi <= 39.9:
            status = 'Overweight'
        else:
            status = 'Obese'

        # نمایش نتیجه در پنجره جدید
        show_result(bmi, status)
    except ValueError:
        show_error('Please enter valid numbers for height and weight.')

def show_result(bmi, status):
    # ایجاد پنجره جدید برای نتیجه
    result_window = tk.Toplevel(root)
    result_window.title('BMI Result')
    result_window.geometry('300x200')
    result_window.configure(bg='#e0f7fa')

    result_label = tk.Label(result_window, text=f'Your BMI: {round(bmi, 2)}\nYour Status: {status}',
                             font=('Helvetica', 16, 'bold'), bg='#e0f7fa', fg='#00695c')
    result_label.pack(pady=30)

    ok_button = tk.Button(result_window, text='OK', command=result_window.destroy,
                          font=('Helvetica', 12, 'bold'), bg='#00796b', fg='white')
    ok_button.pack(pady=10)

def show_error(message):
    messagebox.showerror('Input Error', message)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title('BMI Calculator')
root.geometry('400x300')  # اندازه پنجره
root.configure(bg='#b2ebf2')

# ایجاد فیلدهای ورودی روی پس‌زمینه
header = tk.Label(root, text='BMI Calculator', font=('Helvetica', 18, 'bold'), bg='#b2ebf2', fg='#00695c')
header.pack(pady=20)

height_label = tk.Label(root, text='Enter your height (cm):', bg='#b2ebf2', font=('Helvetica', 12))
height_label.pack()

height_entry = tk.Entry(root, font=('Helvetica', 14), width=15, borderwidth=3)
height_entry.pack(pady=5)

weight_label = tk.Label(root, text='Enter your weight (kg):', bg='#b2ebf2', font=('Helvetica', 12))
weight_label.pack()

weight_entry = tk.Entry(root, font=('Helvetica', 14), width=15, borderwidth=3)
weight_entry.pack(pady=5)

# دکمه محاسبه
calculate_button = tk.Button(root, text='Calculate BMI', command=calculate_bmi,
                              font=('Helvetica', 14, 'bold'), bg='#00796b', fg='white', borderwidth=3, relief='raised')
calculate_button.pack(pady=20)

# اجرای حلقه اصلی
root.mainloop()
