# SCHRÖDINGER — Django fan site

## Запуск
1. Установи Python 3.11+.
2. `python -m venv .venv`
3. Windows: `.venv\\Scripts\\activate` / macOS/Linux: `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. `python manage.py runserver`

Открой http://127.0.0.1:8000/ и админку http://127.0.0.1:8000/admin/.

В админке можно добавлять цитаты и изображения галереи. Для изображений используются URL, поэтому проект не содержит защищённых авторским правом кадров из аниме.
