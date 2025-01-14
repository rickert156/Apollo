from apollo.apolloStepLast import main as parser_last_step
import time

def start_script():
    time_sleep = 20
    while True:
        parser_last_step()
        print(f'Sleep {time_sleep} ...')
        time.sleep(time_sleep)


start_script()
