purchase_time = '14:01'

hour = int(purchase_time.split(':')[0])
mins = int(purchase_time.split(':')[-1])

print(hour, mins)