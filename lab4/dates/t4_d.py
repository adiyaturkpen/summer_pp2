from datetime import datetime
d1=datetime(2024, 12, 1, 1, 48, 0)
d2=datetime(2025, 6, 11, 15, 0, 0)
s=d2-d1
print(s.total_seconds())
