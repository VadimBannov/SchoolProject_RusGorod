class City:
    def __init__(self, name, photo_path, map_path):
        self.name = name
        self.photo_path = photo_path
        self.map_path = map_path

cities = {
    "Москва": City("Москва", "Photo/Images/Moscow.jpg", "Photo/Maps/MoscowMap.jpg"),
    "Санкт Петербург": City("Санкт Петербург", "Photo/Images/Saint_Petersburg.jpg",
                            "Photo/Maps/Saint_PetersburgMap.jpg"),
    "Краснодар": City("Краснодар", "Photo/Images/Krasnodar.jpg", "Photo/Maps/KrasnodarMap.jpg"),
    "Екатеринбург": City("Екатеринбург", "Photo/Images/Ekaterinburg.jpg", "Photo/Maps/EkaterinburgMap.jpg"),
    "Ростов на Дону": City("Ростов на Дону", "Photo/Images/Rostov_on_Don.jpg", "Photo/Maps/Rostov_on_DonMap.jpg"),
    "Новосибирск": City("Новосибирск", "Photo/Images/Novosibirsk.jpg", "Photo/Maps/NovosibirskMap.jpg"),
    "Казань": City("Казань", "Photo/Images/Kazan.jpg", "Photo/Maps/KazanMap.jpg"),
    "Нижний Новгород": City("Нижний Новгород", "Photo/Images/Nizhniy_Novgorod.jpg",
                            "Photo/Maps/Nizhniy_NovgorodMap.jpg"),
    "Челябинск": City("Челябинск", "Photo/Images/Chelyabinsk.jpg", "Photo/Maps/ChelyabinskMap.jpg"),
    "Омск": City("Омск", "Photo/Images/Omsk.jpg", "Photo/Maps/OmskMap.jpg"),
    "Самара": City("Самара", "Photo/Images/Samara.jpg", "Photo/Maps/SamaraMap.jpg"),
    "Уфа": City("Уфа", "Photo/Images/Ufa.jpg", "Photo/Maps/UfaMap.jpg"),
    "Красноярск": City("Красноярск", "Photo/Images/Krasnoyarsk.jpeg", "Photo/Maps/KrasnoyarskMap.jpg"),
    "Пермь": City("Пермь", "Photo/Images/Perm.jpg", "Photo/Maps/PermMap.jpg"),
    "Воронеж": City("Воронеж", "Photo/Images/Voronezh.jpg", "Photo/Maps/VoronezhMap.jpg"),
    "Волгоград": City("Волгоград", "Photo/Images/Volgograd.jpg", "Photo/Maps/VolgogradMap.jpg"),
    "Саратов": City("Саратов", "Photo/Images/Saratov.jpg", "Photo/Maps/SaratovMap.jpg"),
    "Тольятти": City("Тольятти", "Photo/Images/Tolyatti.jpg", "Photo/Maps/TolyattiMap.jpg"),
    "Ижевск": City("Ижевск", "Photo/Images/Izhevsk.jpg", "Photo/Maps/IzhevskMap.jpg"),
    "Барнаул": City("Барнаул", "Photo/Images/Barnaul.jpg", "Photo/Maps/BarnaulMap.jpg"),
    "Ульяновск": City("Ульяновск", "Photo/Images/Ulyanovsk.jpg", "Photo/Maps/UlyanovskMap.jpg"),
    "Иркутск": City("Иркутск", "Photo/Images/Irkutsk.JPG", "Photo/Maps/IrkutskMap.jpg"),
    "Тюмень": City("Тюмень", "Photo/Images/Tyumen.jpg", "Photo/Maps/TyumenMap.jpg")
}
