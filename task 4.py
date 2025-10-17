from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_diff = (birthday_this_year - today).days
        if 0 <= days_diff <= 6:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

users = [ 
        {"name": "Eminem", "birthday": "1972.10.17"},
        {"name": "Jean-Claude Van Damme", "birthday": "1960.10.18"},
        {"name": "Holyfield", "birthday": "1992.10.19"},
        {"name": "Valeriy Borzov", "birthday": "1949.10.20"},
        {"name": "Philippus Orlik,", "birthday": "1672.10.21"},
        {"name": "Alfred Nobel,", "birthday": "1833.10.21"}
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))



