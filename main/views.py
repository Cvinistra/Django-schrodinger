from django.shortcuts import render
from django.http import Http404
from .models import Quote, GalleryItem

# Version key art / licensed or reference imagery. The site labels these as reference art,
# not as official ownership claims. Replace URLs with assets you are licensed to host.
VERSION_ART = {
    "manga": "https://www.chamblinbookmine.com/cdn/shop/files/102536.jpg",
    "tv2001": "https://br.web.img3.acsta.net/pictures/23/08/02/19/47/0710781.jpg",
    "ultimate": "https://media.fetch.fm/media/uploads/sleeves/2013/MANG5286_DVD_Hellsing_5-8_2D.jpg",
}

CHARACTERS = [
    {"slug":"alucard","name":"Алукард","en":"Alucard","faction":"Hellsing","role":"Вампир / главный боевой актив","image": "https://imfdb.org/images/thumb/6/68/HellsingE03_03.jpg/600px-HellsingE03_03.jpg", "manga_image":"https://www.chamblinbookmine.com/cdn/shop/files/102536.jpg", "tv_image":"https://imfdb.org/images/thumb/6/68/HellsingE03_03.jpg/600px-HellsingE03_03.jpg", "ultimate_image":"https://i0.wp.com/filmmusiccentral.com/wp-content/uploads/2019/05/maxresdefault.jpg?fit=1200%2C675&ssl=1", "text":"Древнейший вампир и главное оружие семьи Хеллсинг.","story":"Алукард связан с семьёй Хеллсинг после поражения от Абрахама Ван Хеллсинга. В основной истории он служит Интегре и сталкивается с Искариотом и Millennium.","quote":"Give me your orders, my Master."},
    {"slug":"integra","name":"Интегра Хеллсинг","en":"Integra Fairbrook Wingates Hellsing","faction":"Hellsing","role":"Глава Хеллсинга","image":"https://static.wikia.nocookie.net/hellsing/images/7/71/IntegraAnime.png/revision/latest?cb=20250110142250", "manga_image":"https://i.pinimg.com/originals/22/79/9f/22799f41eba0a21de9c4829c536cf8c1.jpg", "tv_image":"https://static.wikia.nocookie.net/hellsing/images/7/71/IntegraAnime.png/revision/latest?cb=20250110142250", "ultimate_image":"https://i.pinimg.com/originals/22/79/9f/22799f41eba0a21de9c4829c536cf8c1.jpg", "text":"Последняя глава семьи Хеллсинг и командир Алукарда.","story":"После смерти отца Интегра защищает право возглавить организацию. Она остаётся человеком, но именно её воля удерживает Хеллсинг как действующую силу.","quote":"You did your duty. Farewell."},
    {"slug":"seras","name":"Серас Виктория","en":"Seras Victoria","faction":"Hellsing","role":"Бывшая полицейская / вампир","image":"https://images5.alphacoders.com/709/709900.jpg", "manga_image":"https://www.chamblinbookmine.com/cdn/shop/files/102536.jpg", "tv_image":"https://pbs.twimg.com/media/GZds4lIWQAAf-H7.png", "ultimate_image":"https://imgix.ranker.com/user_node_img/4215/84280808/original/hellsing-ultimate-photo-u18?auto=format&dpr=2&fit=crop&fm=pjpg&q=60&w=650", "text":"Полицейская, превращённая Алукардом в вампира.","story":"Серас получает выбор между смертью и новой жизнью. После обращения она проходит собственный путь от человека, отрицающего свою природу, до самостоятельного бойца Хеллсинга.","quote":"I'm not afraid of anything anymore."},
    {"slug":"walter","name":"Уолтер С. Дорнез","en":"Walter C. Dornez","faction":"Hellsing / Millennium","role":"Дворецкий, ветеран и мастер проволоки","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Старый слуга семьи Хеллсинг и легендарный боец.","story":"В молодости Уолтер участвовал вместе с Алукардом в операции 1944 года. В основной линии его судьба оказывается связана с Millennium и трагическим выбором между прошлым и настоящим.","quote":"A gentleman should always be prepared."},
    {"slug":"anderson","name":"Александр Андерсон","en":"Alexander Anderson","faction":"Iscariot","role":"Священник / боец Искариота","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Главный полевой противник Алукарда со стороны Искариота.","story":"Андерсон служит Ватикану и охотится на нечисть. Его конфликт с Алукардом постепенно превращается в личное противостояние двух существ, которые по-разному понимают человеческую природу.","quote":"Amen!"},
    {"slug":"major","name":"Майор","en":"The Major","faction":"Millennium","role":"Командир Millennium","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Архитектор войны Millennium.","story":"Майор переживает события 1944 года и десятилетиями готовит новую войну. Для него конфликт является самостоятельной целью, а не просто средством достижения политического результата.","quote":"My friends, I love war."},
    {"slug":"schrodinger","name":"Шрёдингер","en":"Schrödinger","faction":"Millennium","role":"Офицер / посланник Майора","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Котоподобный офицер с парадоксальной природой существования.","story":"Шрёдингер служит Майору как посланник и разведчик. Его способность быть одновременно «везде и нигде» становится одной из ключевых деталей финальной части истории.","quote":"I am everywhere and nowhere."},
    {"slug":"pip","name":"Пип Бернадотт","en":"Pip Bernadotte","faction":"Hellsing / Wild Geese","role":"Командир наёмников","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Командир Wild Geese, нанятых Интегрой.","story":"После уничтожения части бойцов Хеллсинга Интегра нанимает Wild Geese. Пип становится союзником Серас и играет важную роль в обороне организации.","quote":"Looks like it's my turn."},
    {"slug":"maxwell","name":"Энрико Максвелл","en":"Enrico Maxwell","faction":"Iscariot","role":"Руководитель 13-го отдела","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Высокопоставленный руководитель Искариота.","story":"Максвелл рассматривает Хеллсинг и Алукарда как угрозу. Его амбиции становятся особенно разрушительными во время войны за Лондон.","quote":"For the glory of God."},
    {"slug":"heinkel","name":"Хайнкель Вульф","en":"Heinkel Wolfe","faction":"Iscariot","role":"Полевой агент","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Боевой агент Искариота и напарница Юмиэ.","story":"Хайнкель действует на передовой и участвует в столкновениях между Хеллсингом, Millennium и Искариотом.","quote":"—"},
    {"slug":"yumie","name":"Юмиэ Такаги","en":"Yumie Takagi","faction":"Iscariot","role":"Монахиня / мечница","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Монахиня и мечница Искариота.","story":"Юмиэ показывает наиболее экстремальную сторону 13-го отдела. Её история тесно связана с Хайнкель и дополнительной мангой Cross Fire.","quote":"—"},
    {"slug":"doctor","name":"Доктор","en":"The Doctor","faction":"Millennium","role":"Главный учёный","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Учёный, создающий искусственных вампиров Millennium.","story":"Доктор продолжает исследования нацистской программы и создаёт технологическую основу армии Millennium.","quote":"—"},
    {"slug":"captain","name":"Капитан","en":"The Captain","faction":"Millennium","role":"Оборотень / телохранитель Майора","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Молчаливый оборотень и телохранитель Майора.","story":"Капитан — один из сильнейших бойцов Millennium. Его противостояние с Уолтером связано с событиями Второй мировой войны.","quote":"—"},
    {"slug":"rip","name":"Рип ван Винкль","en":"Rip van Winkle","faction":"Millennium","role":"Офицер / вампир","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Вампир Millennium с мушкетом и магическими пулями.","story":"Рип участвует в захвате авианосца Eagle. После поражения её сущность становится частью сил Алукарда.","quote":"Punish all without distinction."},
    {"slug":"zorin","name":"Зорин Блиц","en":"Zorin Blitz","faction":"Millennium","role":"Офицер Werwolf","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Командир Millennium, использующая иллюзии.","story":"Зорин возглавляет нападение на поместье Хеллсинга. Её способности особенно опасны против людей, которые не умеют сопротивляться психологическим атакам.","quote":"—"},
    {"slug":"luke","name":"Люк Валентайн","en":"Luke Valentine","faction":"Millennium","role":"Вампир","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Спокойный и самоуверенный брат Яна Валентайна.","story":"Люк атакует штаб Хеллсинга и пытается сразиться с Алукардом, переоценивая собственные возможности.","quote":"What... is that gun?!"},
    {"slug":"jan","name":"Ян Валентайн","en":"Jan Valentine","faction":"Millennium","role":"Вампир / командир атаки","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Грубый и самоуверенный брат Люка.","story":"Ян руководит первой атакой на штаб Хеллсинга. Его нападение становится демонстрацией силы Millennium и армии гулей.","quote":"—"},
    {"slug":"tubalcain","name":"Тубалкаин Альгамбра","en":"Tubalcain Alhambra","faction":"Millennium","role":"Вампир","image":VERSION_ART["ultimate"],"manga_image":VERSION_ART["manga"],"tv_image":VERSION_ART["tv2001"],"ultimate_image":VERSION_ART["ultimate"],"text":"Вампир Millennium, использующий смертельно острые карты.","story":"Тубалкаин сталкивается с Алукардом и Серас в Бразилии. Его поражение даёт Хеллсингу важную информацию о Millennium.","quote":"—"},
    {"slug":"incognito","name":"Инкогнито","en":"Incognito","faction":"Hellsing 2001","role":"Оригинальный антагонист TV-версии","image":VERSION_ART["tv2001"],"manga_image":"", "tv_image":VERSION_ART["tv2001"],"ultimate_image":"", "text":"Антагонист, созданный специально для телевизионной версии 2001 года.","story":"Инкогнито не относится к основной манга/Ultimate-линии. Его арка занимает финальную часть TV-сериала и завершается противостоянием с Алукардом в Tower of London.","quote":"—"},
]

TV_EPISODES = [
    (1,"The Undead","Чеддер","Алукард уничтожает вампира-священника и спасает смертельно раненую Серас, превратив её в вампира."),
    (2,"Club M","Новая жизнь Серас","Серас учится существовать в новом теле и участвует в охоте на двух молодых вампиров."),
    (3,"Sword Dancer","FREAK-чипы","Появляется технология искусственных вампиров, связанная с чипами, имплантируемыми людям."),
    (4,"Innocent as a Human","Секретная съёмка","Распространение записи убийства угрожает секретности Хеллсинга."),
    (5,"Brotherhood","Атака Валентайнов","Ян и Люк Валентайн атакуют штаб Хеллсинга вместе с армией гулей."),
    (6,"Dead Zone","Последствия","Алукард и Люк сталкиваются напрямую, а Уолтер демонстрирует своё боевое мастерство."),
    (7,"Duel","Искариот","Хеллсинг восстанавливается после атаки, а Алукард встречается с Андерсоном."),
    (8,"Kill House","Расследование","Интегра и Серас расследуют происхождение FREAK-чипов и исчезновение доказательств."),
    (9,"Red Rose Vertigo","Ложная операция","Ситуация вокруг одной из операций Хеллсинга оказывается гораздо опаснее, чем кажется."),
    (10,"Master of Monster","Прошлое Интегры","Раскрываются события детства Интегры и её первая встреча с Алукардом."),
    (11,"Transcend Force","Предательство","Интегра оказывается втянута в заговор, а угроза становится одновременно политической и сверхъестественной."),
    (12,"Total Destruction","Tower of London","Хеллсинг оказывается между британскими силами и сверхъестественной угрозой."),
    (13,"Hellfire","Алукард против Инкогнито","Финал TV-линии: Интегра и Уолтер пытаются выжить, а Алукард вступает в последний бой с Инкогнито."),
]

PLOT_ARCS = [
    ("MANGA / 01", "Чеддер и Серас", "Алукард прибывает в деревню Чеддер и сталкивается с вампиром-священником. Серас получает выбор между смертью и вампирской жизнью."),
    ("MANGA / 02", "Братья Валентайн", "Ян и Люк атакуют штаб Хеллсинга. Нападение показывает, что за отдельными вампирами стоит организованная сила."),
    ("MANGA / 03", "Бразилия", "Алукард и Серас сталкиваются с Тубалкаином. Следы ведут к Millennium и будущей войне."),
    ("MANGA / 04", "Война Millennium", "Последний батальон возвращается и начинает полномасштабное вторжение в Лондон."),
    ("MANGA / 05", "Искариот", "13-й отдел Ватикана вмешивается в конфликт, превращая противостояние в трёхстороннюю войну."),
    ("MANGA / 06", "Падение Лондона", "Хеллсинг, Искариот и Millennium сражаются одновременно, а город превращается в поле боя."),
    ("MANGA / 07", "Андерсон против Алукарда", "Их финальный бой становится одной из центральных сцен манги и Ultimate."),
    ("MANGA / 08", "Последняя война", "Уолтер, Капитан, Майор и Алукард сходятся в финальных сражениях."),
    ("MANGA / 09", "Финал", "План Майора рушится, а судьба Алукарда и его многочисленных душ приводит к необычному эпилогу."),
]

ADAPTATIONS = [
    {"title":"Hellsing — манга","year":"1997–2008","type":"Оригинальная манга","episodes":"10 томов","text":"Оригинальная история Коты Хирано. Манга выходила в Young King OURs и была собрана в десять томов.","tag":"CANON / SOURCE"},
    {"title":"Hellsing: The Dawn","year":"2002–2006 / 2011–2012","type":"Приквел","episodes":"6 глав / 3 коротких OVA","text":"История событий 1944 года, связанная с молодыми Уолтером и Алукардом.","tag":"PREQUEL"},
    {"title":"Hellsing — Война с нечистью","year":"2001–2002","type":"TV-аниме Gonzo","episodes":"13 серий","text":"Первая аниме-адаптация. После ранних эпизодов сюжет идёт собственной дорогой и завершается оригинальной аркой Инкогнито.","tag":"ALTERNATE TIMELINE"},
    {"title":"Hellsing Ultimate","year":"2006–2012","type":"OVA","episodes":"10 OVA","text":"Самая близкая к манге анимационная версия. Она экранизирует основную войну с Millennium и финальную часть истории.","tag":"MANGA-FAITHFUL"},
    {"title":"Hellsing Ultimate Abridged","year":"2010–2018","type":"Фанатская пародия","episodes":"10 эпизодов","text":"Неофициальная комедийная переозвучка. На сайте вынесена отдельно и не смешивается с каноном.","tag":"FAN WORK"},
    {"title":"Live-action проект","year":"анонсирован в 2021","type":"Планируемый фильм","episodes":"не вышел","text":"Проект игровой экранизации, о котором сообщалось в 2021 году. На странице он помечен как анонсированный проект, а не как вышедшая экранизация.","tag":"ANNOUNCED"},
]

FACTIONS = [
    ("HELLSING", "Королевский Орден Протестантских Рыцарей", "Британская секретная организация, занимающаяся сверхъестественными угрозами."),
    ("ISCARIOT", "13-й отдел Ватикана", "Католическая организация, противостоящая нечисти и Хеллсингу."),
    ("MILLENNIUM", "Последний батальон", "Нацистский проект, превратившийся в армию искусственных вампиров."),
    ("WILD GEESE", "Наёмники", "Человеческое подразделение, нанятое Интегрой после тяжёлых потерь Хеллсинга."),
]

QUOTES = [
    {"character":"Алукард","en":"Give me your orders, my Master.","ru":"Отдайте мне приказ, мой хозяин.","source":"Manga / Ultimate","note":"Ключевая формула отношений Алукарда и Интегры."},
    {"character":"Александр Андерсон","en":"Amen!","ru":"Аминь!","source":"Manga / TV / Ultimate","note":"Короткая реплика Андерсона."},
    {"character":"Майор","en":"My friends, I love war.","ru":"Друзья мои, я люблю войну.","source":"Manga / Ultimate","note":"Реплика из знаменитой речи Майора."},
    {"character":"Шрёдингер","en":"I am everywhere and nowhere.","ru":"Я везде и нигде.","source":"Manga / Ultimate","note":"Фраза отражает парадоксальную природу персонажа."},
    {"character":"Люк Валентайн","en":"What... is that gun?!","ru":"Что... это за пушка?!","source":"Ultimate","note":"Реакция Люка на оружие Алукарда."},
    {"character":"Серас Виктория","en":"I'm not afraid of anything anymore.","ru":"Я больше ничего не боюсь.","source":"Manga / Ultimate","note":"Передаёт изменение Серас после принятия своей природы."},
    {"character":"Рип ван Винкль","en":"Punish all without distinction.","ru":"Карать всех без различия.","source":"Manga / Ultimate","note":"Короткая формула, связанная с её боевым образом."},
]

def home(request):
    return render(request, "home.html", {"characters": CHARACTERS[:9], "plot_arcs": PLOT_ARCS[:4], "tv_episodes": TV_EPISODES[:3], "factions": FACTIONS[:3], "quotes": QUOTES[:4], "adaptations": ADAPTATIONS})

def history(request):
    return render(request, "history.html", {"plot_arcs": PLOT_ARCS, "adaptations": ADAPTATIONS})

def plot(request):
    return render(request, "plot.html", {"plot_arcs": PLOT_ARCS, "tv_episodes": TV_EPISODES})

def adaptations(request):
    return render(request, "adaptations.html", {"adaptations": ADAPTATIONS, "tv_episodes": TV_EPISODES})

def characters(request):
    return render(request, "characters.html", {"characters": CHARACTERS})

def character(request, slug):
    person = next((item for item in CHARACTERS if item["slug"] == slug), None)
    if person is None:
        raise Http404("Character not found")
    versions = [
        ("manga", "МАНГА", person.get("manga_image"), "Оригинальная манга Коты Хирано"),
        ("tv2001", "ВОЙНА С НЕЧИСТЬЮ", person.get("tv_image"), "TV-аниме Gonzo, 2001–2002"),
        ("ultimate", "ULTIMATE", person.get("ultimate_image"), "OVA, 2006–2012"),
    ]
    return render(request, "character.html", {"person": person, "versions": versions, "quotes": [q for q in QUOTES if q["character"] == person["name"]]})

def factions(request):
    return render(request, "factions.html", {"factions": FACTIONS})

def quotes(request):
    return render(request, "quotes.html", {"quotes": QUOTES})

def gallery(request):
    return render(request, "gallery.html", {"gallery": GalleryItem.objects.all(), "characters": CHARACTERS, "version_art": VERSION_ART})
