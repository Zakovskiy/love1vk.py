from utils import objects


class User:

    def __init__(self, client) -> None:
        self.client = client

    def get_info(self, target_uid: int, target_user_is_friend: bool = True,
        referer: int = 7, sex: int = 2) -> objects.UserInfo:
        """ Получение информации о пользователе

        **Параметры**
            - **target_uid** : VK User ID
            - **target_user_is_friend** : (bool) является ли пользователь вашим другом
            - **referer** : (int) тип (чего-то) откуда вы нажали на пользователя
            - **sex** : пол пользователя(?)
        """
        data = {
            "target_uid": target_uid,
            "target_user_is_friend": target_user_is_friend,
            "referer": referer,
            "sex": sex
        }
        result = self.client.request("user/getInfo.php", _data=data)
        if not result.get("data"):
            raise Exception(result["message"])
        return objects.UserInfo(result.get("data", {})).UserInfo

    def search(self, limit_per_part: int = 5, min_level: int = 1, age_min: int = 14,
        age_max: int = 16, vf: bool = False, sex: int = 1) -> objects.Search:
        """ Поиск пользователей

        **Параметры**
            - **limit_per_part** : максимальное кол-во юзеров (макс. - 100)
            - **min_level** : минимальный уровень юзеров
            - **age_min** : минимальный возраст юзеров
            - **age_max** : максимальный возраст юзеров
            - **vf** : только верифицированные юзеры
            - **sex** : пол юзеров
        """
        data = {
            "limit_per_part": limit_per_part,
            "min_level": min_level,
            "age_max": age_max,
            "age_min": age_min,
            "vf": vf,
            "sex": sex,
        }
        result = self.client.request("user/search.php", _data=data)
        return objects.Search(result.get("data")).Search

    def get_users(self, user_ids: str, fields: str = "age") -> dict:
        """ Получение пользователей

        **Параметры**
            - **user_ids** : айди разделенные через запятую
            - **fields** : поля по которым их получать
        """
        data = {
            "uids": user_ids,
            "fields": fields,
        }
        result = self.client.request("user/get.php", _data=data)
        return result

    def add_to_favorite(self, target_uid: int) -> objects.Code:
        """ Добавление пользователя из избранных
    
        **Параметры**
            - **target_uid** : VK User ID
        """
        data = {
            "target_uid": target_uid,
        }
        result = self.client.request("user/addToFav.php", _data=data)
        return objects.Code(result).Code


    def remove_from_favorite(self, target_uid: int) -> objects.Code:
        """ Удаление пользователя из избранных
    
        **Параметры**
            - **target_uid** : VK User ID
        """
        data = {
            "target_uid": target_uid,
        }
        result = self.client.request("user/removeFromFav.php", _data=data)
        return objects.Code(result).Code

    def update_background(self, image_url: str) -> objects.Code:
        """
        Изменить фон

        **Параметры**
            - **image_url** : Ссылка на изображение от вк хоста
        """
        data = {
            "imgUrl": image_url,
        }
        result = self.client.request("user/updateBg.php", _data=data)
        return objects.Code(result).Code

    def get_stocks(self) -> dict:
        """ ? """
        result = self.client.request("user/getStocks.php", _data={})
        return result

    def update_age(self, birthdate) -> objects.Code:
        """ Изменить возраст """
        data = {
            "bdate": birthdate,
        }
        result = self.client.request("user/updateAge.php", _data=data)
        return objects.Code(result).Code

    def update_region(self, country_id: int, region_id: int) -> dict:
        """ Изменить город в профиле """
        data = {
            "country_id": country_id,
            "region_id": region_id,
        }
        result = self.client.request("user/updateRegion.php", _data=data)
        return result

    def change_status(self, text: str) -> objects.Code:
        """ Изменение статуса """
        data = {
            "text": text,
        }
        result = self.client.request("user/changeStatus.php", type="post", _data=data)
        return objects.Code(result).Code

    def buy_invisible(self, period_index: int) -> objects.Code:
        """ Покупка невидимки """
        data = {
            "period_index": period_index,
        }
        result = self.client.request("user/buyInvisible.php", _data=data)
        return objects.Code(result).Code

    def extend_invisible(self) -> objects.Code:
        result = self.client.request("user/extendInvisible.php", _data={})
        return objects.Code(result).Code

    def get_text_colors_and_ratings(self, user_ids: str) -> dict:
        """
        
        *Параметры**
            - **user_ids** : айди разделенные через запятую
        """
        data = {
            "uids": user_ids
        }
        result = self.client.request("user/getTextColorsAndRatings.php", _data=data)
        return result

    def get_top_list(self, all: bool = True) -> objects.Top:
        """ Рейтинг пользователей """
        result = self.client.request("user/top.php", _data={"all": all})
        return objects.Top(result.get("data", {})).Top

    def inc_balance(self, action_id: int = 6) -> objects.Code:
        """ Загадочная функция, которая может как и дать вам несколько монет, так и забрать... """
        result = self.client.request("user/incBalance.php", _data={"action_id": action_id})
        return objects.Code(result).Code

    def get_self_balance(self) -> objects.Balance:
        """ Получить текущий баланс """
        result = self.client.request("user/getSelfBalance.php")
        return objects.Balance(result).Balance

    def on_group_subscribe(self) -> objects.Code:
        """ Получить бонус за подписку на группу """
        result = self.client.request("user/onGroupSubscribe.php")
        return objects.Code(result).Code

    def check_warns(self) -> objects.Warns:
        """ Получить все предупреждения """
        result = self.client.request("user/checkWarns.php")
        return objects.Warns(result).Warns

    def user_secret_name_inc_wall_posts(self) -> objects.Code:
        """ ? """
        result = self.client.request("user/secretName/incWallPosts.php")
        return objects.Code(result).Code

    def buy_emoji_subscribe(self, price: int = 10) -> dict:
        """ Покупка смайликов

        **Параметры**
            - **price** : стоимость
        """
        data = {
            "price": price,
        }
        result = self.client.request("user/buyEmojiSubscribe.php", _data=data)
        return result

    def complaint(self, type: int, user_id: int) -> dict:
        """ Подача жалобы на пользователя

        **Параметры**
            - **type** : тип причины
            - **user_id** : айди юзера
        """
        data = {
            "type": type,
            "uid": user_id,
        }
        result = self.client.request("user/complaint.php", _data=data)
        return result