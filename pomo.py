from datetime import datetime, timedelta
import time

def get_time():
    return datetime.now()

def start_pomodoro():
    time_pomodoro = timedelta(minutes=25)
    time_pomodoro_end = get_time() + time_pomodoro
    while True:
        delta_time_left = time_pomodoro_end - get_time()
        print('Restam:', int(delta_time_left.seconds / 60), ' minutos e', delta_time_left.seconds % 60 , ' segundos.')
        if delta_time_left <= timedelta(0):
            break
        time.sleep(1)

def main():
    time_break = timedelta(minutes=5)
    print('Aperte uma tecla para iniciar o pomodoro!')
    input()
    start_pomodoro()

if __name__ == "__main__":
    main()