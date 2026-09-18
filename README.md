# HELLSING ARCHIVE — Django

Фан-архив по Hellsing с раздельными линиями:
- оригинальная манга;
- Hellsing / «Война с нечистью» (TV 2001, 13 серий);
- Hellsing Ultimate (10 OVA);
- The Dawn;
- персонажи и сравнение образов;
- сюжет;
- двуязычные цитаты.

## Запуск
```powershell
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

## Важно про изображения
В демо-архиве используются удалённые reference/key-art изображения. Перед публичным размещением замени их на изображения, права на которые у тебя есть, или храни локальные разрешённые материалы в `static/images/`.
