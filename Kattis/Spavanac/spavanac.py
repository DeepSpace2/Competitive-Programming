from datetime import datetime, timedelta

new_time = datetime.strptime(input(), '%H %M') - timedelta(minutes=45)
print('{} {}'.format(new_time.hour, new_time.minute))