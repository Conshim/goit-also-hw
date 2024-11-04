from datetime import datetime

def get_days_from_today(date):

    try:
        date_user = datetime.strptime(date, '%Y-%m-%d')
    
    except ValueError:
        return ('Error format. Please write format YYYY-MM-DD')


    current_date = datetime.today()

    set_days = (current_date - date_user).days

    return set_days

user_input = (input('Enter the date in format YYYY-MM-DD: '))

print(get_days_from_today(user_input))

