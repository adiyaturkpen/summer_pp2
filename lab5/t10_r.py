import re
fi=open(r"C:\Users\Lenovo\pp2\pp2-summer\lab5\row.txt", encoding="utf-8")
data=fi.read()
fi.close()
m=re.sub(r"[A-Z]",'_',data)
print(m)