sec = 196
day = sec // 86400
hour = sec % 86400 // 3600
minute = sec % 3600 // 60
secund = sec % 60
print(day, ":", hour, ":", minute, ":", secund)
