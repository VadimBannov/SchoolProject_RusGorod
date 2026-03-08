class ImageEntity:
    def __init__(self, name, photo_path):
        self.name = name
        self.photo_path = photo_path


class City(ImageEntity):
    def __init__(self, name, photo_path, map_path):
        super().__init__(name, photo_path)
        self.map_path = map_path

class Gerb(ImageEntity):
    pass

class Attractions(ImageEntity):
    def __init__(self, name, photo_path, information):
        super().__init__(name, photo_path)
        self.information_path = information

cities = {
    "Москва": City("Москва", "Photo/Images/Moscow.jpg", "Photo/Maps/MoscowMap.jpg"),
    "Санкт-Петербург": City("Санкт-Петербург", "Photo/Images/Saint_Petersburg.jpg", "Photo/Maps/Saint_PetersburgMap.jpg"),
    "Краснодар": City("Краснодар", "Photo/Images/Krasnodar.jpg", "Photo/Maps/KrasnodarMap.jpg"),
    "Екатеринбург": City("Екатеринбург", "Photo/Images/Ekaterinburg.jpg", "Photo/Maps/EkaterinburgMap.jpg"),
    "Ростов-на-Дону": City("Ростов-на-Дону", "Photo/Images/Rostov_on_Don.jpg", "Photo/Maps/Rostov_on_DonMap.jpg"),
    "Новосибирск": City("Новосибирск", "Photo/Images/Novosibirsk.jpg", "Photo/Maps/NovosibirskMap.jpg"),
    "Казань": City("Казань", "Photo/Images/Kazan.jpg", "Photo/Maps/KazanMap.jpg"),
    "Нижний Новгород": City("Нижний Новгород", "Photo/Images/Nizhniy_Novgorod.jpg", "Photo/Maps/Nizhniy_NovgorodMap.jpg"),
    "Челябинск": City("Челябинск", "Photo/Images/Chelyabinsk.jpg", "Photo/Maps/ChelyabinskMap.jpg"),
    "Омск": City("Омск", "Photo/Images/Omsk.jpg", "Photo/Maps/OmskMap.jpg"),
    "Самара": City("Самара", "Photo/Images/Samara.jpg", "Photo/Maps/SamaraMap.jpg"),
    "Уфа": City("Уфа", "Photo/Images/Ufa.jpg", "Photo/Maps/UfaMap.jpg"),
    "Красноярск": City("Красноярск", "Photo/Images/Krasnoyarsk.jpg", "Photo/Maps/KrasnoyarskMap.jpg"),
    "Пермь": City("Пермь", "Photo/Images/Perm.jpg", "Photo/Maps/PermMap.jpg"),
    "Воронеж": City("Воронеж", "Photo/Images/Voronezh.jpg", "Photo/Maps/VoronezhMap.jpg"),
    "Волгоград": City("Волгоград", "Photo/Images/Volgograd.jpg", "Photo/Maps/VolgogradMap.jpg"),
    "Саратов": City("Саратов", "Photo/Images/Saratov.jpg", "Photo/Maps/SaratovMap.jpg"),
    "Тольятти": City("Тольятти", "Photo/Images/Tolyatti.jpg", "Photo/Maps/TolyattiMap.jpg"),
    "Ижевск": City("Ижевск", "Photo/Images/Izhevsk.jpg", "Photo/Maps/IzhevskMap.jpg"),
    "Барнаул": City("Барнаул", "Photo/Images/Barnaul.jpg", "Photo/Maps/BarnaulMap.jpg"),
    "Ульяновск": City("Ульяновск", "Photo/Images/Ulyanovsk.jpg", "Photo/Maps/UlyanovskMap.jpg"),
    "Иркутск": City("Иркутск", "Photo/Images/Irkutsk.png", "Photo/Maps/IrkutskMap.jpg"),
    "Тюмень": City("Тюмень", "Photo/Images/Tyumen.jpg", "Photo/Maps/TyumenMap.jpg"),
    "Кемерово": City("Кемерово", "Photo/Images/Kemerovo.jpg", "Photo/Maps/KemerovoMap.jpg"),
    "Рязань": City("Рязань", "Photo/Images/Ryazan.jpg", "Photo/Maps/RyazanMap.jpg"),
    "Томск": City("Томск", "Photo/Images/Tomsk.jpg", "Photo/Maps/TomskMap.jpg"),
    "Астрахань": City("Астрахань", "Photo/Images/Astrakhan.jpg", "Photo/Maps/AstrakhanMap.jpg"),
    "Пенза": City("Пенза", "Photo/Images/Penza.jpg", "Photo/Maps/PenzaMap.jpg"),
    "Норильск": City("Норильск", "Photo/Images/Norilsk.jpg", "Photo/Maps/NorilskMap.jpg"),
    "Набережн. Челны": City("Набережн. Челны", "Photo/Images/Naberezhnye_Chelny.jpg", "Photo/Maps/Naberezhnye_ChelnyMap.jpg"),
    "Липецк": City("Липецк", "Photo/Images/Lipetsk.png", "Photo/Maps/LipetskMap.jpg"),
    "Киров": City("Киров", "Photo/Images/Kirov.jpg", "Photo/Maps/KirovMap.jpg"),
    "Чебоксары": City("Чебоксары", "Photo/Images/Cheboksary.jpg", "Photo/Maps/CheboksaryMap.jpg"),
    "Брянск": City("Брянск", "Photo/Images/Bryansk.jpg", "Photo/Maps/BryanskMap.jpg"),
    "Ставрополь": City("Ставрополь", "Photo/Images/Stavropol.jpg", "Photo/Maps/StavropolMap.jpg"),
    "Махачкала": City("Махачкала", "Photo/Images/Makhachkala.jpg", "Photo/Maps/MakhachkalaMap.jpg"),
    "Севастополь": City("Севастополь", "Photo/Images/Sevastopol.jpg", "Photo/Maps/SevastopolMap.jpg"),
    "Тверь": City("Тверь", "Photo/Images/Tver.jpeg", "Photo/Maps/TverMap.jpg"),
    "Сочи": City("Сочи", "Photo/Images/Sochi.jpg", "Photo/Maps/SochiMap.jpg"),
    "Ярославль": City("Ярославль", "Photo/Images/Yaroslavl.jpg", "Photo/Maps/YaroslavlMap.jpg"),
    "Калининград": City("Калининград", "Photo/Images/Kaliningrad.jpg", "Photo/Maps/KaliningradMap.jpg"),
    "Курск": City("Курск", "Photo/Images/Kursk.jpg", "Photo/Maps/KurskMap.jpg"),
    "Вологда": City("Вологда", "Photo/Images/Vologda.jpg", "Photo/Maps/VologdaMap.jpg"),
    "Вел. Новгород": City("Вел. Новгород", "Photo/Images/Veliky_Novgorod.jpg", "Photo/Maps/Veliky_NovgorodMap.jpg"),
    "Орёл": City("Орёл", "Photo/Images/Eagle.jpg", "Photo/Maps/EagleMap.jpg"),
    "Мурманск": City("Мурманск", "Photo/Images/Murmansk.jpg", "Photo/Maps/MurmanskMap.jpg"),
    "Краснодон": City("Краснодон", "Photo/Images/Krasnodon.jpg", "Photo/Maps/KrasnodonMap.jpg"),
    "Белгород": City("Белгород", "Photo/Images/Belgorod.jpg", "Photo/Maps/BelgorodMap.jpg"),
    "Анапа": City("Анапа", "Photo/Images/Anapa.jpg", "Photo/Maps/AnapaMap.jpg"),
    "Ессентуки": City("Ессентуки", "Photo/Images/Essentuki.jpg", "Photo/Maps/EssentukiMap.jpg")
}

gerbs = {
    "Москва": Gerb("Москва", "Photo/Gerbs/Moscow.jpeg"),
    "Санкт-Петербург": Gerb("Санкт-Петербург", "Photo/Gerbs/Saint_Petersburg.jpg"),
    "Краснодар": Gerb("Краснодар", "Photo/Gerbs/Krasnodar.jpg"),
    "Нижний Новгород": Gerb("Нижний Новгород", "Photo/Gerbs/Nizhniy_Novgorod.jpg"),
    "Самара": Gerb("Самара", "Photo/Gerbs/Samara.jpg"),
    "Омск": Gerb("Омск", "Photo/Gerbs/Omsk.jpg"),
    "Челябинск": Gerb("Челябинск", "Photo/Gerbs/Chelyabinsk.jpg"),
    "Казань": Gerb("Казань", "Photo/Gerbs/Kazan.jpg"),
    "Екатеринбург": Gerb("Екатеринбург", "Photo/Gerbs/Ekaterinburg.jpg"),
    "Новосибирск": Gerb("Новосибирск", "Photo/Gerbs/Novosibirsk.jpg"),
    "Ростов-на-Дону": Gerb("Ростов-на-Дону", "Photo/Gerbs/Rostov-on-Don.jpg"),
    "Уфа": Gerb("Уфа", "Photo/Gerbs/Ufa.jpg"),
    "Красноярск": Gerb("Красноярск", "Photo/Gerbs/Krasnoyarsk.jpg"),
    "Пермь": Gerb("Пермь", "Photo/Gerbs/Perm.jpg"),
    "Воронеж": Gerb("Воронеж", "Photo/Gerbs/Voronezh.jpg"),
    "Волгоград": Gerb("Волгоград", "Photo/Gerbs/Volgograd.jpg"),
    "Саратов": Gerb("Саратов", "Photo/Gerbs/Saratov.jpg"),
    "Тольятти": Gerb("Тольятти", "Photo/Gerbs/Tolyatti.jpg"),
    "Ижевск": Gerb("Ижевск", "Photo/Gerbs/Izhevsk.png"),
    "Барнаул": Gerb("Барнаул", "Photo/Gerbs/Barnaul.jpg"),
    "Анапа": Gerb("Анапа", "Photo/Gerbs/Anapa.jpg"),
    "Ульяновск": Gerb("Ульяновск", "Photo/Gerbs/Ulyanovsk.jpg"),
    "Иваново": Gerb("Иваново", "Photo/Gerbs/Ivanovo.jpg"),
    "Тверь": Gerb("Тверь", "Photo/Gerbs/Tver.jpg"),
    "Хабаровск": Gerb("Хабаровск", "Photo/Gerbs/Khabarovsk.jpg"),
    "Якутск": Gerb("Якутск", "Photo/Gerbs/Yakutsk.jpg"),
    "Тюмень": Gerb("Тюмень", "Photo/Gerbs/Tyumen.jpg"),
    "Пенза": Gerb("Пенза","Photo/Gerbs/Penza.jpg"),
    "Магнитогорск": Gerb("Магнитогорск", "Photo/Gerbs/Magnitogorsk.jpg"),
    "Калининград": Gerb("Калининград", "Photo/Gerbs/Kaliningrad.jpg")
}

attractions = {
    "Кремль": Attractions("Кремль", "Photo/Attractions/Kremlin.jpg", "Москва — Кремль\nРасположен в самом сердце города, на берегу реки Москвы.\nИнтересные факты:\n1) История кремля начинается в XV веке.\n2) На территории расположены древние соборы.\n3) Кремль является официальной резиденцией Президента РФ."),
    "Эрмитаж": Attractions("Эрмитаж", "Photo/Attractions/Hermitage.jpg", "Санкт-Петербург — Эрмитаж\nНаходится на Дворцовой набережной.\nИнтересные факты:\n1) Основан в 1764 году Екатериной II.\n2) Один из крупнейших музеев мира.\n3) Главное здание — Зимний дворец."),
    "Театр оперы и балета": Attractions("Театр оперы и балета", "Photo/Attractions/NGATOB.jpg", "Новосибирск — Театр оперы и балета\nНаходится на площади Ленина.\nИнтересные факты:\n1) Крупнейшее театральное здание России.\n2) Открыт в 1945 году.\n3) Известен большим куполом без внутренних опор."),
    "Храм на Крови": Attractions("Храм на Крови", "Photo/Attractions/Temple_the_Blood.jpg", "Екатеринбург — Храм на Крови\nНаходится на месте дома Ипатьева.\nИнтересные факты:\n1) Построен на месте гибели семьи Романовых.\n2) Освящён в 2003 году.\n3) Является местом паломничества."),
    "Нижегородский кремль": Attractions("Нижегородский кремль", "Photo/Attractions/Novgorod_Kremlin.jpg", "Нижний Новгород — Нижегородский кремль\nНаходится в центре Нижнего Новгорода.\nИнтересные факты:\n1) Построен в XVI веке.\n2) Имеет 13 башен.\n3) Включает музеи и административные здания."),
    "Казанский кремль": Attractions("Казанский кремль", "Photo/Attractions/Kazan_Kremlin.jpg", "Казань — Казанский кремль\nНаходится в историческом центре Казани.\nИнтересные факты:\n1) Объект Всемирного наследия ЮНЕСКО.\n2) Здесь находится мечеть Кул-Шариф.\n3) Отражает русско-татарскую культуру."),
    "Кировка (улица)": Attractions("Кировка (улица)", "Photo/Attractions/Kirovka.jpg", "Кировка (улица) — Челябинск\nРасположена в центральной части города; пешеходная улица и культурная зона.\nИнтересные факты:\n1) Истоки улицы XIX века — раньше здесь располагались ремесленные и торговые ряды.\n2) Улица украшена современными скульптурами и арт-объектами местных художников.\n3) На Кировке регулярно проходят уличные фестивали, концерты и ярмарки."),
    "Омская крепость": Attractions("Омская крепость", "Photo/Attractions/Omsk_Fortress.png", "Омская крепость — Омск\nРасположена в историческом центре у реки Иртыш; ядро городской застройки XVIII–XIX вв.\nИнтересные факты:\n1) Крепость изначально возводилась как военное укрепление для освоения Сибири.\n2) Вокруг крепости формировались административные и торговые кварталы Омска.\n3) Сегодня сохранившиеся фрагменты и музеи демонстрируют фортификационную историю региона."),
    "Набережная Волги": Attractions("Набережная Волги", "Photo/Attractions/Volga_Embankment.jpg", "Набережная Волги — Самара\nТянется вдоль берега Волги и служит главной прогулочной зоной города.\nИнтересные факты:\n1) Одна из самых длинных городских набережных на Волге с множеством смотровых точек.\n2) Здесь расположены памятники, пляжи и места для спортивных мероприятий.\n3) Набережная — центр летних фестивалей и массовых праздников в регионе."),
    "Набережная Дона": Attractions("Набережная Дона", "Photo/Attractions/Embankment_Don.jpg", "Ростов-на-Дону — Набережная Дона\nНаходится в Ростове-на-Дону, на правом берегу реки Дон.\nИнтересные факты:\n1) Популярное место прогулок и отдыха.\n2) Украшена скульптурами и фонтанами.\n3) Здесь проходят городские праздники."),
    "Монумент Дружбы": Attractions("Монумент Дружбы", "Photo/Attractions/Monument_Friendship.jpg", "Уфа — Монумент Дружбы\nНаходится в Уфе, на высоком берегу реки Белой.\nИнтересные факты:\n1) Открыт в 1965 году.\n2) Символизирует дружбу народов.\n3) Является одной из визитных карточек города."),
    "Мамаев курган": Attractions("Мамаев курган", "Photo/Attractions/Mamaev_Kurgan.jpg", "Волгоград — Мамаев курган\nНаходится в Волгограде, на возвышенности над Волгой.\nИнтересные факты:\n1) Посвящён битве за Сталинград.\n2) Включает статую «Родина-мать зовёт!».\n3) Является главным мемориалом города."),
    "Набережная Космонавтов": Attractions("Набережная Космонавтов", "Photo/Attractions/Cosmonauts_Embankment.jpg", "Набережная Космонавтов — Саратов\nНаходится вдоль Волги в центральной части города; популярная прогулочная зона.\nИнтересные факты:\n1) Набережная названа в честь советских космонавтов и украшена памятниками, посвящёнными покорителям космоса.\n2) Здесь проходят городские фестивали, концерты и праздничные мероприятия в летний сезон.\n3) С набережной открываются панорамные виды на Волгу; оборудованы смотровые площадки и прогулочные аллеи."),
    "Нагорный парк": Attractions("Нагорный парк", "Photo/Attractions/Nagorny_Park.jpg", "Нагорный парк — Барнаул\nРасположен на высокой набережной реки Обь; крупная городская рекреационная зона.\nИнтересные факты:\n1) Парк предлагает панорамные виды на город и реку с обзорных площадок.\n2) На его территории находятся памятники и аллеи, созданные в разные эпохи.\n3) Часто используется для городских праздников, ярмарок и семейного отдыха."),
    "Дом-музей Ленина": Attractions("Дом-музей Ленина", "Photo/Attractions/House_Museum.jpg", "Дом-музей Ленина — Ульяновск\nНаходится в историческом центре; мемориальный дом, посвящённый семье Ульяновых.\nИнтересные факты:\n1) Музей сохраняет быт и предметы эпохи, связанные с молодыми годами Ленина.\n2) Экспозиции помогают проследить социальный и культурный контекст конца XIX — начала XX века.\n3) Место служит образовательной площадкой для изучения истории революционного периода."),
    "Заповедник «Столбы»": Attractions("Заповедник «Столбы»", "Photo/Attractions/Nature_Reserve.jpg", "Красноярск — Заповедник «Столбы»\nНаходится в национальном парке «Красноярские Столбы».\nИнтересные факты:\n1) Уникальные скальные образования.\n2) Популярны среди туристов и альпинистов.\n3) Являются природным символом региона."),
    "Музей «Гото Предестинация»": Attractions("Музей «Гото Предестинация»", "Photo/Attractions/Goto_Predestination.jpg", "Музей «Гото Предестинация» (корабль-музей) — Воронеж\nРасположен на берегу; музей-реконструкция парусного судна XVII века.\nИнтересные факты:\n1) Корабль воссоздаёт тип парусного судна, который использовался при становлении российского флота.\n2) Экспозиция посвящена истории судостроения Петра I и раннего флота России.\n3) На палубе проводятся экскурсии, образовательные программы и исторические реконструкции."),
    "Парк Гагарина": Attractions("Парк Гагарина", "Photo/Attractions/Gagarin Park.jpeg", "Челябинск — Парк Гагарина\nНаходится в Челябинске, в центре города.\nИнтересные факты:\n1) Один из крупнейших парков Южного Урала.\n2) Открыт в 1934 году.\n3) Популярное место отдыха горожан."),
    "Мост Влюблённых": Attractions("Мост Влюблённых", "Photo/Attractions/Bridge_Lovers.jpg", "Тюмень — Мост Влюблённых\nНаходится в Тюмени, через реку Тура.\nИнтересные факты:\n1) Пешеходный мост в центре города.\n2) Популярен среди молодожёнов.\n3) Красиво подсвечивается вечером."),
    "Памятник «Первопоселенец»": Attractions("Памятник «Первопоселенец»", "Photo/Attractions/Monument_Pioneer_Settler.jpg", "Памятник «Первопоселенец» — Пенза\nУстановлен в городском парке как символ основания и ранних поселенцев.\nИнтересные факты:\n1) Посвящён первым поселенцам и формированию городской общины в XVII—XVIII вв.\n2) Служит популярным местом для встреч и городских фотосессий.\n3) Вокруг памятника регулярно проходят культурные и патриотические мероприятия."),
    "Русский мост": Attractions("Русский мост", "Photo/Attractions/Russian_bridge.jpg", "Владивосток — Русский мост\nНаходится во Владивостоке, через пролив Босфор Восточный.\nИнтересные факты:\n1) Один из самых длинных вантовых мостов в мире.\n2) Построен к саммиту АТЭС 2012 года.\n3) Соединяет остров Русский с материком."),
    "Кафедральный собор": Attractions("Кафедральный собор", "Photo/Attractions/Cathedral.jpg", "Калининград — Кафедральный собор\nНаходится в Калининграде, на острове Канта.\nИнтересные факты:\n1) Построен в готическом стиле.\n2) Здесь похоронен Иммануил Кант.\n3) Проводятся органные концерты."),
    "Олимпийский парк": Attractions("Олимпийский парк", "Photo/Attractions/Olympic_park.jpg", "Сочи — Олимпийский парк\nНаходится в Сочи, в Адлерском районе.\nИнтересные факты:\n1) Построен к Олимпиаде 2014 года.\n2) Включает современные спортивные объекты.\n3) Используется для фестивалей и концертов."),
    "Жигулёвские горы": Attractions("Жигулёвские горы", "Photo/Attractions/Zhiguli_Mountains.jpg", "Самара — Жигулёвские горы\nНаходится в Самаре, на правом берегу Волги.\nИнтересные факты:\n1) Часть национального парка «Самарская Лука».\n2) Известны живописными видами.\n3) Связаны с историей волжских казаков."),
    "Пермская галерея": Attractions("Пермская галерея", "Photo/Attractions/Perm_Gallery.jpg", "Пермь — Пермская художественная галерея\nНаходится в Перми, в центре города.\nИнтересные факты:\n1) Известна коллекцией деревянной скульптуры.\n2) Основана в 1922 году.\n3) Один из крупнейших музеев Урала."),
    "Выборгский замок": Attractions("Выборгский замок", "Photo/Attractions/Vyborg_Castle.jpg","Выборгский замок — Выборг\nНаходится в исторической части Выборга, у Финского залива.\nИнтересные факты:\n1) Замок основан в XIII веке и неоднократно перестраивался.\n2) Сооружение важно для истории смены власти в Прибалтике.\n3) В замке проходят выставки и культурные мероприятия."),
    "Иволгинский дацан": Attractions("Иволгинский дацан", "Photo/Attractions/Ivolginsky_datsan.jpg", "Иволгинский дацан — Верхняя Иволга\nНаходится недалеко от Улан-Удэ, в Иволгинском районе Бурятии.\nИнтересные факты:\n1) Главный буддийский центр России с религиозной семинарией.\n2) Место паломничества буддистов из разных регионов.\n3) Комплекс известен традиционной бурятской архитектурой и обрядами."),
    "Нарзанная галерея": Attractions("Нарзанная галерея", "Photo/Attractions/Narzannaya_Gallery.jpg", " Нарзанная галерея — Кисловодск\nНаходится в курортной зоне Кисловодска, в центре парка.\nИнтересные факты:\n1) Нарзанная галерея известна минеральными источниками с целебной водой.\n2) Курортная архитектура и парк XIX—XX вв. делают место популярным у туристов.\n3) Здесь проходят бальнеологические процедуры и фестивали здоровья."),
    "Ласточкино гнездо": Attractions("Ласточкино гнездо", "Photo/Attractions/Swallow's_Nest.jpg", "Ласточкино гнездо — Крым\nНаходится на южном берегу Крыма, недалеко от Ялты.\nИнтересные факты:\n1) Небольшая романтическая усадьба на отвесной скале над морем.\n2) Стала символом Крымского побережья и популярным фотоместом.\n3) Имеет богатую историю строительства и реставраций."),
    "Провал и Машук": Attractions("Провал и Машук", "Photo/Attractions/Failure_Mashuk.jpg", "Провал и Машук — Пятигорск\nНаходится в Пятигорске, на склонах горы Машук.\nИнтересные факты:\n1) Провал — карстовая воронка с минеральной водой и легендами.\n2) Машук предлагает панорамы Кавказских гор и лечебные маршруты.\n3) Город известен как центр курортного лечения Кавказских Минеральных Вод.")
}
