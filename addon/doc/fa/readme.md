# دیده‌بان منابع (Resource Monitor) #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* دانلود [نسخه‌ی پایدار][1]
* NVDA compatibility: 2017.4 to 2019.3

این افزونه، اطلاعاتی درباره‌ی عملکرد CPU، میزان استفاده از حافظه، و دیگر
اطلاعات مربوط به استفاده از منابع سیستم را در اختیارتان میگذارد.

# کلیدهای میانبر #

* NVDA+Shift+E، مقدار استفاده‌شده از رم، میانگین کارکرد پردازنده و در صورت
  موجود بودن، اطلاعات باتری را ارائه میدهد.
* NVDA+Shift+1، میانگین بارِ CPU و چنانچه CPU چندهسته‌ای باشد، بارِ هر هسته
  را اعلام میکند.
* NVDA+Shift+2 و NVDA+Shift+5، فضای استفاده‌شده و فضای کلی رم فیزیکی و رم
  مجازی را اعلام میکند.
* NVDA+Shift+3، فضای استفاده‌شده و کل فضای درایوهای ثابت و قابل حمل متصل‌شده
  به رایانه را اعلام میکند.
* NVDA+Shift+4، درصدِ باتری، وضعیت شارژ، زمان باقی‌مانده در صورت شارژ نشدن،
  و یک هشدار اگر باتری ضعیف یا خیلی ضعیف باشد را اعلام میکند.
* NVDA+Shift+6، معماری CPU (۳۲ یا ۶۴ بیتی)، شماره نسخه‌ی ویندوز و شماره‌ی
  بسته‌ی خدماتی (service pack) را اعلام میکند.
* NVDA+Shift+7، زمان بالا بودن سیستم را اعلام میکند.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## تذکراتی در مورد استفاده از افزونه ##

این افزونه جای task manager و دیگر برنامه‌های اطلاعات سیستم که برای ویندوز
طراحی شده‌اند را نمیگیرد. همچنین، نکات زیر را نیز به یاد داشته باشید:

* اطلاعاتی که در مورد کارکرد CPU اعلام میشود، برای پردازنده‌های منطقی است،
  نه هسته‌های فیزیکی. این در مورد پردازشگرهایی که از hyper-threading استفاده
  میکنند قابل ملاحظه است؛ زمانی که تعداد CPU دو برابر تعداد هسته‌های آن است.
* چنانچه دیسک‌ها درگیر فعالیت سنگینی مانند کپی فایل‌های بزرگ باشند، ممکن است
  هنگام به‌دست‌آوردن اطلاعات میزان استفاده از دیسک، تأخیرهایی به وجود بیاید.
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## نسخه‌ی 18.04

نسخه‌ی 18.04.x آخرین نسخه‌ایست که از ویندوزهای قدیمیتر از ویندوز 7 SP1
پشتیبانی میکند.

* آخرین انتشاری است که ویندوز سرور 2003، ویستا و سرور 2008 را پشتیبانی
  میکند.
* شناسایی بهتر انتشارهای ویندوز ۱۰ و تشخیص دادن ساخت‌های پیش‌نمایش عمومی
  (public) و داخلی (insider).

## نسخه‌ی 17.12

* پشتیبانی از پردازشگرهای ۶۴ بیتی ARM در ویندوز ۱۰.

## نسخه‌ی 17.09

مهم: نسخه‌ی 17.09.x، آخرین نسخه‌ایست که از ویندوز XP پشتیبانی میکند.

* آخرین نسخه‌ای که روی ویندوز XP اجرا میشود.
* ویندوز ۱۰ ساخت 16278 و بعد از آن به عنوان نسخه‌ی 1709 شناسایی
  میشوند. بازبینی کوچکی از افزونه، وقتی نسخه‌ی پایدار ساخت 1709 منتشر شود،
  در دسترس قرار خواهد گرفت.

## نسخه‌ی 17.07.1

* پشتیبانی مجدد از ویندوز XP که در نسخه‌ی 17.02 قطع شده بود.

## نسخه‌ی 17.05

* اعلام زمان بالا بودن سیستم؛ زمانی که از آخرین بوت سیستم سپری شده است؛
  NVDA+Shift+7).

## نسخه‌ی 17.02

* متعلقات psutil به نسخه‌ی 5.0.1 به‌روز شد.
* در زمان بررسی میزان استفاده از دیسک، NVDA دیگر در بعضی سیستم‌ها، هنگامی که
  یک رسانه‌ی قابل حمل به‌درستی توسط سیستم شناسایی نشده، مثلا کارتی داخل
  کارت‌خوان قرار ندارد، پنجره‌ی خطا نشان نمیدهد.

## نسخه‌ی 16.08

با آغاز به انتشار نسخه‌ی 16.08، انتشارهای افزونه به صورت سال.ماه.بازبینی
نشان داده میشوند.

* نسخه‌های گوناگونی از ویندوز ۱۰ حالا به‌درستی شناسایی میشوند (مانند 1607
  برای بیلد 14393).
* نسخه بیلدهای ویندوز ۱۰ (بعد از نصب به‌روزرسانی‌ها) به‌درستی شناخته میشوند
  (مثل 14393.51).
* چنانچه در حال استفاده از نسخه‌های پیش‌نمایش داخلی (Insider Preview) باشید،
  این مورد توسط افزونه شناسایی میشود.

## تغییرات در نسخه‌ی 4.5 ##

* منبع فایل‌های افزونه به GitHub منتقل شده است. میتوانید آنرا در این نشانی
  بیابید: https://github.com/josephsl/resourcemonitor.
* ویندوز سرور 2016 به‌درستی شناسایی میشود.

## تغییرات در نسخه‌ی 4.0 ##

* متعلقات psutil به نسخه‌ی 2.2.1 به‌روز شد.
* عملکرد افزونه، هنگام دریافت اطلاعات مربوط به بار CPU، به مقدار زیادی بهبود
  یافت.
* پشتیبانی از شناسایی ویندوز ۱۰ افزوده شد.
* در ویندوز ۱۰، شماره‌ی ساخت ویندوز (build number) هم اعلام خواهد شد.
* میتوانید برای دسترسی به راهنمای افزونه، از مدیر افزونه‌ها استفاده کنید.

## تغییرات در نسخه‌ی 3.1 ##

* دیده‌بان منابع بطور رسمی از ویندوز 8.1 پشتیبانی میکند.
* ترجمه‌ها به‌روز شد.

## تغییرات در نسخه‌ی 3.0 ##

* متعلقات psutil به نسخه‌ی 1.2.1 به‌روز شد.
* اعلام نسخه‌ی جاری ویندوز، معماری CPU و در صورت موجود بودن، بسته‌ی خدماتی
  (service pack) (NVDA+Shift+6).
* توانایی تغییر کلیدهای میانبر افزونه (NVDA 2013.3 یا بالاتر).
* توانایی کپی اطلاعات هرکدام از منابع در کلیپ‌برد با فشردن فرمان مربوط، دو
  بار پشت سر هم.

## تغییرات در نسخه‌ی 2.4 ##

* زبان‌های جدید: چینی (ساده‌شده)، اوکراینی.
* ترجمه‌ها به‌روز شد.

## تغییرات نسخه‌ی 2.3 ##

* ترجمه‌ی بلغاری افزوده شد.

## تغییرات در نسخه‌ی 2.2 ##

* افزونه به این زبان‌ها ترجمه شد: آراگونیایی، آلمانی، اسلوواکیایی،
  اسلوونیایی، اسپانیولی، ایتالیایی، پرتغالی برزیلی، تامیل، ترکیه‌ای، روسی،
  ژاپنی، عربی، فرانسوی، فنلاندی، کره‌ای، کرواتی، گالیسیایی، لهستانی،
  مجارستانی، نپالی و هلندی.

## تغییرات در نسخه‌ی 2.1 ##

* Psutil dependency به نسخه‌ی 0.6.1 به‌روز شد.
* تأخیر طولانی در زمان به‌دست آوردن اطلاعات درایوها برطرف شد.
* پاکسازیِ کد.

## تغییرات در نسخه‌ی 2.0 ##

* پشتیبانی از ترجمه و توضیحات ترجمه افزوده شد.

## تغییرات در نسخه‌ی 1.0 ##

* انتشار اولیه

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
