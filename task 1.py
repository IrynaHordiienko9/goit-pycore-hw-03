from datetime import datetime

def get_days_from_today(date):
   
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        difference  = today - input_date
        return difference.days
    except ValueError:
        raise ValueError

print(get_days_from_today('2020-10-09'))