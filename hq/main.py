# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from datetime import datetime

def check_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"{date_str} is a valid date.")
    except ValueError:
        print(f"{date_str} is not a valid date.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a date in the format 'YYYY-MM-DD' as a command-line argument.")
    else:
        date_to_check = sys.argv[1]
        check_date(date_to_check)


