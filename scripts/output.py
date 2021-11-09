from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
with open('cron-output.txt', 'w') as f:
    f.write(current_time)