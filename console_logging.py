import datetime


class Logger:
    def log(self, message):
        current_dt = datetime.datetime.now()
        print(f'[{current_dt.strftime("%Y-%m-%d %H:%M:%S")}]: {message}')


LOGGER = Logger()
