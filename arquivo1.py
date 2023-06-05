import datetime
import time
initial_time = time.time()
current_datetime = datetime.datetime.now()

next_thursday = current_datetime + datetime.timedelta((3 - current_datetime.weekday() + 7) % 7)
time_delta = next_thursday - current_datetime
time_delta

#faça um time.sleep de dez segundos para mim, a fim de que teste-o em um for





