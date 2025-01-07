import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='Birthday of the user in DDMMYYYY format'
    )

    parser.add_argument(
        '--name',
        type=str,
        default='Pattaratron',
        help='Input the name of the user'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World!, {who}!!")

def cal_days_since_birthday(bd):
    today = datetime.today()
    birth_date = datetime.strptime(bd, '%d%m%Y')

    if birth_date > today:
        raise ValueError("The birthday cannot be in the future!")

    delta = today - birth_date
    return delta.days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    days_since_birthday = cal_days_since_birthday(input_v.bd)
    print(f'It has been {days_since_birthday} days since your birthday!')

