# Hellsing Archive — Django

Фан-сайт по вселенной Hellsing: манга, Hellsing Ultimate, история создания, персонажи, фракции, цитаты и галерея.

## Локальный запуск

```powershell
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Открыть: http://127.0.0.1:8000/

## Render

Build command:

```text
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

Start command:

```text
gunicorn config.wsgi:application
```

Environment variable:

```text
SECRET_KEY=your-secret-key
```

## Разделы

- `/` — главная
- `/history/` — история манги и адаптаций
- `/characters/` — персонажи и отдельные досье
- `/factions/` — Hellsing / Iscariot / Millennium
- `/quotes/` — цитаты
- `/gallery/` — галерея
- `/admin/` — админка для Quote и GalleryItem

Часть демо-изображений взята из Wikimedia Commons; перед коммерческим или повторным использованием проверяйте лицензию конкретного файла.
