from datetime import datetime


def is_morning(hour: int) -> bool:
    return hour > 3 and hour < 12

def is_afternoon(hour: int) -> bool:
    return hour > 11 and hour < 17

def greet(hour: int) -> None:
    if is_morning(hour):
        print("Hello good morning!")
        return

    if is_afternoon(hour):
        print("Hello good afternoon!")
        return

    print("Hello good evening!")


greet(datetime.now().hour)
