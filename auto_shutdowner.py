from time import mktime, sleep
from os import system
from datetime import datetime, timedelta


def datetime_to_seconds(date_time: datetime) -> float:
    return date_time.second + (date_time.minute * 60) + (date_time.hour * 3600)


if __name__ == '__main__':
    everything_is_ok = True
    future_timestamp = None
    try:
        needle_time_string = (input("Введите время через которое хотите выключить ПК\nВ формате 'чч:мм:сс':\n"))
        future_timestamp = (mktime(datetime.now().timetuple())) + datetime_to_seconds(
            datetime.strptime(needle_time_string, '%H:%M:%S'))
    except:
        print('Что-то пошло не так(')
        everything_is_ok = False

    prev_msg_time = 0
    while everything_is_ok:
        if future_timestamp is None:
            break
        current_timestamp = (mktime(datetime.now().timetuple()))
        difference = future_timestamp - current_timestamp
        since_prev_msg = current_timestamp - prev_msg_time
        if difference > 0:
            if since_prev_msg >= 15:
                hms_format = str(timedelta(seconds=difference))
                print(f'Компьютер будет выключен через {hms_format}')
                prev_msg_time = current_timestamp
            sleep(10)
        else:
            print('Время пришло')
            system('shutdown -s -t 60')
            break
