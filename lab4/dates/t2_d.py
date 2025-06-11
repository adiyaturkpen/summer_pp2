from datetime import datetime, timedelta
d1=datetime.now()
d2=d1-timedelta(days=1)
d3=d1+timedelta(days=1)
print("Вчера:", d2)
print("Сегодня:", d1)
print("Завтра:", d3)
