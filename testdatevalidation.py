import datetime



def validate_date(date_text):
    
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%Y.')
        print("ok")
    except ValueError:
        raise ValueError("Incorrect data format")
    


validate_date("12.4.2021.")


def validate_time(time_text):
    
    try:
        datetime.datetime.strptime(time_text, '%H:%M')
        print("ok")
    except ValueError:
        raise ValueError("Incorrect data format")
    

# validate_time("14:30")