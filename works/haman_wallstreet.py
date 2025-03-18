import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper


def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text


class Stock:
    def __init__(self, name, initial_price):
        self.name = name
        self.price = initial_price
        self.history = [initial_price]

    def update_price(self):
        change = random.uniform(-0.05, 0.05) * self.price
        self.price += change
        self.price = max(1, self.price)  # Minimum price is 1
        self.history.append(self.price)


class TradingApp:
    def __init__(self, master):
        self.master = master
        master.title(reshape_text("شبیه‌ساز ترید"))
        master.configure(bg="#222222")  # Dark background

        self.balance = 10000
        self.portfolio = {}
        self.stocks = self.create_stocks()

        # Styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background="#222222", foreground="white")
        style.configure("TButton", background="#333333",
                        foreground="white", borderwidth=0, relief="flat")
        style.map("TButton",
                  background=[("active", "#555555")])
        style.configure("TCombobox", background="#333333",
                        foreground="white", borderwidth=0, relief="flat")

        # Login Page
        self.login_label = ttk.Label(
            master, text=reshape_text("نام کاربری:"), style="TLabel")
        self.login_label.pack(pady=5)
        self.login_entry = ttk.Entry(master)
        self.login_entry.pack(pady=5)

        self.password_label = ttk.Label(
            master, text=reshape_text("رمز عبور:"), style="TLabel")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(master, text=reshape_text(
            "ورود"), command=self.login, style="TButton")
        self.login_button.pack(pady=10)

    def login(self):
        # Basic login validation
        if self.login_entry.get() and self.password_entry.get():
            self.show_main_page()
        else:
            print("Login failed")

    def show_main_page(self):
        # Clear login widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Main Page
        self.balance_label = ttk.Label(self.master, text=reshape_text(
            f"موجودی: {self.balance:.2f} $"), style="TLabel")
        self.balance_label.pack(pady=10)

        stock_names = [stock.name for stock in self.stocks]
        self.stock_combo = ttk.Combobox(
            self.master, values=stock_names, state="readonly")
        self.stock_combo.pack(pady=5)
        self.stock_combo.set(stock_names[0])
        self.stock_combo.bind("<<ComboboxSelected>>", self.update_chart)

        self.buy_button = ttk.Button(self.master, text=reshape_text(
            "خرید"), command=self.buy_stock, style="TButton")
        self.buy_button.pack(pady=5)
        self.sell_button = ttk.Button(self.master, text=reshape_text(
            "فروش"), command=self.sell_stock, style="TButton")
        self.sell_button.pack(pady=5)

        # Portfolio Display
        self.portfolio_label = ttk.Label(
            self.master, text=reshape_text("سبد سهام:"), style="TLabel")
        self.portfolio_label.pack(pady=10)
        self.portfolio_text = tk.Text(
            self.master, height=5, width=30, bg="#333333", fg="white")
        self.portfolio_text.pack(pady=5)
        self.update_portfolio_display()

        # Chart Display
        self.fig, self.ax = plt.subplots(facecolor="#222222")
        self.ax.set_facecolor("#222222")
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(pady=10)

        self.update_chart()

        # Start Price Updates
        self.master.after(2000, self.update_prices)

    def create_stocks(self):
        names = [
            "اپل", "مایکروسافت", "آمازون", "گوگل", "تسلا", "فیسبوک", "علی‌بابا", "تنسنت", "سامسونگ", "جی‌پی مورگان",
            "برکشایر هاتاوی", "ویزا", "مسترکارت", "جانسون اند جانسون", "پروکتر اند گمبل", "نستله", "یونایتدHealth", "ورایزون", "AT&T", "وال‌مارت",
            "اکسون‌موبیل", "شورون", "رویال داچ شل", "توتال", "بی‌پی", "سینوپک", "پتروچاینا", "لوک‌اویل", "گازپروم", "سابیک",
            "هوم‌دیپو", "مک‌دونالدز", "نایکی", "کوکاکولا", "پپسی‌کو", "استارباکس", "دیزنی", "نتفلیکس", "هیلتون", "ماریوت",
            "تویوتا", "فولکس‌واگن", "دایملر", "بی‌ام‌و", "هوندا", "جنرال موتورز", "فورد", "نیسان", "هیوندای", "رنو",
            "بوئینگ", "ایرباس", "لاکهید مارتین", "ریتیان", "نورثروپ گرومن", "جنرال داینامیکس", "BAE Systems", "لئوناردو", "تالس", "میتسوبیشی",
            "زیمنس", "جنرال الکتریک", "ABB", "اشنایدر الکتریک", "هانیول", "3M", "داو کمیکال", "باسف", "بایر", "سانوفی",
            "سیتی‌گروپ", "بانک‌آو‌آمریکا", "ولز فارگو", "گلدمن ساکس", "مورگان استنلی", "HSBC", "ICBC", "چاینا کانستراکشن بانک", "آگریکالچرل بانک آو چاینا", "بانک آو چاینا",
            "اوراکل", "اینتل", "IBM", "SAP", "اکسنچر", "تاتا", "Infosys", "Capgemini", "Wipro", "HCL",
            "لویی ویتون", "هرمس", "شنل", "گوچی", "پرادا", "دیور", "کارتیر", "تیفانی", "بولگاری", "رولکس",
            "آدیداس", "پوما", "ریباک", "آندر آرمور", "لوئل‌لمون", "زارا", "اچ اند ام", "یونیکلو", "Gap", "Abercrombie & Fitch",
            "سونی", "ال‌جی", "پاناسونیک", "شارپ", "فیلیپس", "زیمنس", "بوش", "میتسوبیشی الکتریک", "هیتاچی", "توشیبا",
            "کانون", "نیکون", "المپوس", "فوجی‌فیلم", "سونی", "زایس", "لایکا", "هاسلبلاد", "پنتکس", "تامرون",
            "تویوتا", "هوندا", "نیسان", "سوزوکی", "میتسوبیشی", "مزدا", "سوبارو", "ایسوزو", "یاماها", "کاوازاکی",
            "کوماتسو", "هیتاچی", "کوبلکو", "کاترپیلار", "ولو", "Terex", "Liebherr", "JCB", "Hyundai Heavy Industries", "Doosan",
            "بوش", "زیمنس", "جنرال الکتریک", "ABB", "اشنایدر الکتریک", "هانیول", "3M", "داو کمیکال", "باسف", "بایر",
            "تاتا استیل", "آرسلورمیتال", "پوسکو", "نیپون استیل", "جی‌اف‌ای", "والینیک", "اوسکو", "نالکو", "هیندالکو", "ودانتا",
            "بی‌اچ‌پی بیلیتون", "ریوتینتو", "واله", "فورتسکیو", "آنگلو امریکن", "گلنکور", "بایکال", "آلومینیوم روسیه", "نور نیکل", "انتوفاگاستا"
        ]
        stocks = []
        for name in names:
            stocks.append(Stock(reshape_text(name), random.uniform(10, 200)))
        return stocks

    def buy_stock(self):
        stock_name = self.stock_combo.get()
        stock = next((s for s in self.stocks if s.name == stock_name), None)
        if stock:
            quantity = 1  # You can add an entry to specify quantity
            cost = stock.price * quantity
            if self.balance >= cost:
                self.balance -= cost
                if stock_name in self.portfolio:
                    self.portfolio[stock_name] += quantity
                else:
                    self.portfolio[stock_name] = quantity
                self.update_balance_label()
                self.update_portfolio_display()
            else:
                print(reshape_text("موجودی کافی نیست!"))

    def sell_stock(self):
        stock_name = self.stock_combo.get()
        if stock_name in self.portfolio:
            stock = next(
                (s for s in self.stocks if s.name == stock_name), None)
            if stock:
                quantity = 1  # You can add an entry to specify quantity
                if self.portfolio[stock_name] >= quantity:
                    self.portfolio[stock_name] -= quantity
                    self.balance += stock.price * quantity
                    if self.portfolio[stock_name] == 0:
                        del self.portfolio[stock_name]
                    self.update_balance_label()
                    self.update_portfolio_display()
                else:
                    print(reshape_text("تعداد کافی در سبد سهام وجود ندارد!"))
        else:
            print(reshape_text("این سهام در سبد سهام شما وجود ندارد!"))

    def update_prices(self):
        for stock in self.stocks:
            stock.update_price()
        self.update_chart()
        self.master.after(2000, self.update_prices)

    def update_chart(self, event=None):
        self.ax.clear()
        stock_name = self.stock_combo.get()
        stock = next((s for s in self.stocks if s.name == stock_name), None)
        if stock:
            self.ax.plot(stock.history, color='white')
            self.ax.set_title(reshape_text(
                f"نمودار قیمت: {stock.name}"), color='white')
            self.ax.set_xlabel(reshape_text("زمان"), color='white')
            self.ax.set_ylabel(reshape_text("قیمت"), color='white')
            self.ax.tick_params(axis='x', colors='white')
            self.ax.tick_params(axis='y', colors='white')
            self.fig.canvas.draw()

    def update_balance_label(self):
        self.balance_label.config(text=reshape_text(
            f"موجودی: {self.balance:.2f} $"))

    def update_portfolio_display(self):
        self.portfolio_text.delete("1.0", tk.END)
        for stock, quantity in self.portfolio.items():
            self.portfolio_text.insert(
                tk.END, reshape_text(f"{stock}: {quantity}\n"))


root = tk.Tk()
app = TradingApp(root)
root.mainloop()
