from time import mktime, sleep
from os import system
from datetime import datetime, timedelta
from win10toast import ToastNotifier


class CustomToaster:
    def __init__(self, toast: ToastNotifier):
        self.toaster = toast

    def print_to_system(self, message):
        if self.toaster.show_toast('ShutDowner', message, None, 10):
            print(message)


def datetime_to_seconds(date_time: datetime) -> float:
    return date_time.second + (date_time.minute * 60) + (date_time.hour * 3600)


if __name__ == '__main__':
    notifier = CustomToaster(ToastNotifier())
    everything_is_ok = True
    future_timestamp = None
    try:
        needle_time_string = (input("Введите время через которое хотите выключить ПК\nВ формате 'чч:мм:сс':\n"))
        future_timestamp = (mktime(datetime.now().timetuple())) + datetime_to_seconds(
            datetime.strptime(needle_time_string, '%H:%M:%S'))
    except:
        notifier.print_to_system('Что-то пошло не так(')
        everything_is_ok = False

    prev_msg_time = 0
    delay_between_notifications = None
    while everything_is_ok:
        if future_timestamp is None:
            break
        current_timestamp = (mktime(datetime.now().timetuple()))
        difference = future_timestamp - current_timestamp
        if delay_between_notifications is None:
            delay_between_notifications = difference * 0.1
        since_prev_msg = current_timestamp - prev_msg_time
        if difference > 0:
            if since_prev_msg >= delay_between_notifications:
                hms_format = str(timedelta(seconds=difference))
                notifier.print_to_system(f'Компьютер будет выключен через {hms_format}')
                prev_msg_time = current_timestamp
            sleep(5)
        else:
            notifier.print_to_system('Время пришло')
            system('shutdown -s -t 60')
            break
