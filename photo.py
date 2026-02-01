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
    pass

cities = {
    "Москва": City("Москва", "Photo/Images/Moscow.jpg", "Photo/Maps/MoscowMap.jpg"),
    "Санкт-Петербург": City("Санкт-Петербург", "Photo/Images/Saint_Petersburg.jpg",
                            "Photo/Maps/Saint_PetersburgMap.jpg"),
    "Краснодар": City("Краснодар", "Photo/Images/Krasnodar.jpg", "Photo/Maps/KrasnodarMap.jpg"),
    "Екатеринбург": City("Екатеринбург", "Photo/Images/Ekaterinburg.jpg", "Photo/Maps/EkaterinburgMap.jpg"),
    "Ростов-на-Дону": City("Ростов-на-Дону", "Photo/Images/Rostov_on_Don.jpg", "Photo/Maps/Rostov_on_DonMap.jpg"),
    "Новосибирск": City("Новосибирск", "Photo/Images/Novosibirsk.jpg", "Photo/Maps/NovosibirskMap.jpg"),
    "Казань": City("Казань", "Photo/Images/Kazan.jpg", "Photo/Maps/KazanMap.jpg"),
    "Нижний Новгород": City("Нижний Новгород", "Photo/Images/Nizhniy_Novgorod.jpg",
                            "Photo/Maps/Nizhniy_NovgorodMap.jpg"),
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
    "Набер-ные Челны": City("Набер-ные Челны", "Photo/Images/Naberezhnye_Chelny.jpg", "Photo/Maps/Naberezhnye_ChelnyMap.jpg"),
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
    "Красноярск": Gerb("Красноярск", "Photo/Gerbs/Krasnodar.jpg"),
    "Пермь": Gerb("Пермь", "Photo/Gerbs/Perm.jpg"),
    "Воронеж": Gerb("Воронеж", "Photo/Gerbs/Voronezh.jpg"),
    "Волгоград": Gerb("Волгоград", "Photo/Gerbs/Volgograd.jpg"),
    "Саратов": Gerb("Саратов", "Photo/Gerbs/Saratov.jpg"),
    "Тольятти": Gerb("Тольятти", "Photo/Gerbs/Tolyatti.jpg"),
    "Ижевск": Gerb("Ижевск", "Photo/Gerbs/Izhevsk.png"),
    "Барнаул": Gerb("Барнаул", "Photo/Gerbs/Barnaul.jpg")
}

attractions = {
    "Кремль": Attractions("Кремль", "Photo/Attractions/Kremlin.jpg"),
    "Эрмитаж": Attractions("Эрмитаж", "Photo/Attractions/Hermitage.jpg"),
    "НГАТОБ": Attractions("НГАТОБ", "Photo/Attractions/NGATOB.jpg"),
    "Храм на Крови": Attractions("Храм на Крови", "Photo/Attractions/Temple_the_Blood.jpg"),
    "Нижегородский кремль": Attractions("Нижегородский кремль", "Photo/Attractions/Novgorod_Kremlin.jpg"),
    "Казанский кремль": Attractions("Казанский кремль", "Photo/Attractions/Kazan_Kremlin.jpg"),
    "Кировка (улица)": Attractions("Кировка (улица)", "Photo/Attractions/Kirovka.jpg"),
    "Омская крепость": Attractions("Омская крепость", "Photo/Attractions/Omsk_Fortress.png"),
    "Набережная Волги": Attractions("Набережная Волги", "Photo/Attractions/Volga_Embankment.jpg"),
    "Набережная Дона": Attractions("Набережная Дона", "Photo/Attractions/Embankment_Don.jpg"),
    "Монумент Дружбы": Attractions("Монумент Дружбы", "Photo/Attractions/Monument_Friendship.jpg"),
    "Мамаев курган": Attractions("Мамаев курган", "Photo/Attractions/Mamaev_Kurgan.jpg"),
    "Набережная Космонавтов": Attractions("Набережная Космонавтов", "Photo/Attractions/Cosmonauts_Embankment.jpg"),
    "Нагорный парк": Attractions("Нагорный парк", "Photo/Attractions/Nagorny_Park.jpg"),
    "Дом-музей Ленина": Attractions("Дом-музей Ленина", "Photo/Attractions/House_Museum.jpg"),
    "Заповедник «Столбы»": Attractions("Заповедник «Столбы»", "Photo/Attractions/Nature_Reserve.jpg"),
    "Музей «Гото Предестинация»": Attractions("Музей «Гото Предестинация»", "Photo/Attractions/Goto_Predestination.jpg"),
    "Парк Галицкого": Attractions("Парк Галицкого", "Photo/Attractions/Galitsky_Park.jpg"),
    "Мост Влюблённых": Attractions("Мост Влюблённых", "Photo/Attractions/Bridge_Lovers.jpg"),
    "Памятник «Первопоселенец»": Attractions("Памятник «Первопоселенец»", "Photo/Attractions/Monument_Pioneer_Settler.jpg")
}
