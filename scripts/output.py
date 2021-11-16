from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
f = open("output.txt", "w")
f.write(current_time)