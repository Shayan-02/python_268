import pandas as pd

def read_and_print_csv(file_path):
    try:
        # خواندن فایل CSV
        data = pd.read_csv("test.csv")

        # چاپ محتوا در خروجی
        print("محتوای فایل CSV:")
        print(data)

    except FileNotFoundError:
        print(f"خطا: فایل {file_path} یافت نشد.")
    except pd.errors.EmptyDataError:
        print(f"خطا: فایل {file_path} خالی است.")
    except pd.errors.ParserError:
        print(f"خطا: مشکل در پردازش فایل {file_path} وجود دارد.")

# مسیر فایل CSV خود را اینجا قرار دهید
csv_file_path = "مسیر/فایل.csv"
read_and_print_csv(csv_file_path)