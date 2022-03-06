import json
from utils import objects


class Room:

    def __init__(self, client) -> None:
        self.client = client

    def get_room(self, room_id: int = None, force: bool = True) -> dir:
        """ Получить информацию о комнате и автоматическое присоединение к ней

        **Параметры**
            - **target_room_id** : id комнаты
            - **force** : hz, мб коннект к рандомной руме
        """
        data = {
            "pc_fingerprint": self.pc_fingerprint,
            "is_mobi": self.mobi,
            "force": force,
        }
        if target_room_id: data["target_room_id"] = f"{self.client.room_iders}_{room_id}"
        return self.client.request("room/v3/getRoom.php", _data=data)

    def get_room_list(self) -> dir:
        """ Получение списка комнат """
        return self.client.request("room/v3/getRoomList.php")

    def exit(self, room_id: int) -> dict:
        """ Выход из комнаты

        **Параметры**
            - **room_id** : ID комнаты
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
        }
        return self.client.request("room/v3/exit.php", _data=data)

    def get_user_ids(self, room_id: int) -> dict:
        """ Получение айди пользователей состоящих в комнате

        **Параметры**
            - **room_id** : ID комнаты
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}"
        }
        return self.client.request("room/v3/getUids.php", _data=data)

    def kick_user(self, room_id: int, target_uid: int, reason_id: int = 1,
        anon: bool = True, price: int = 1) -> dict:
        """ Кикнуть пользователя из комнаты

        **Параметры**
            - **target_uid** : VK User ID
            - **reason_id** :
            - **anon** :
            - **price** : цена
        """
        data = {
            "reasonId": reason_id,
            "roomId": f"{self.client.room_iders}_room_id",
            "anon": anon,
            "target_uid": target_uid,
            "price": price,
        }
        return self.client.request("room/v3/kick.php", _data=data)

    def resque_user(self, room_id: int, target_uid: int, price: int = 1) -> dict:
        """ Спасти пользователя от кика
        
        **Параметры**
            - **room_id** : ID комнаты
            - **target_uid** : VK User ID
            - **price** : цена
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "uid": target_uid,
            "price": price,
        }
        return self.client.request("room/v3/resque.php", _data=data)

    def chat_send_message(self, room_id: int, message: str, to: int = None, reply: str = None) -> dict:
        """ Отправка сообщения в чат комнаты

        **Параметры**
            - **room_id** : ID комнаты
            - **message** : Контент сообщения
            - **to** : VK User ID, кому оно адресовано
            - **reply** : Айди пересланного сообщения
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "m": message,
            "to": to,
            "reply": reply,
        }
        return self.client.request("room/v3/chat/add.php", "post", _data=data)

    def chat_send_sticker(self, room_id: int, message: str, config: dict) -> dict:
        """ Отправка стикера в чат комнаты

        **Параметры**
            - **room_id** : ID комнаты
            - **message** : Контент сообщения
            - **config** : Конфиг стикера
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "m": message,
            "serialized_config": json.dumps(config),
        }
        return self.client.request("room/v3/chat/addSticker.php", "post", _data=data)

    def add_answer(self, room_id: int, answer: str, question: str) -> dict:
        """ Голосование за что-либо в комнате """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "a": answer,
            "q": question
        }
        return self.client.request("room/v3/addAnswer.php", _data=data)

    def chat_new_level(self, exp: int) -> dict:
        data = {
            "exp": exp
        }
        return self.client.request("room/v3/chat/newLevel.php", _data=data)

    def chat_toggle_like(self, room_id: int, message_id: str) -> dict:
        """ Поставить лайк на сообщение в комнате

        **Параметры**
            - **room_id** : ID комнаты
            - **message_id** : ID сообщения
        """
        data = {
            "message_id": message_id,
            "room_id": f"{self.client.room_iders}_{room_id}"
        }
        return self.client.request('room/v3/chat/toggleLike.php', _data=data)

    def user_toggle_block(self, room_id: int, target_uid: int, value: bool) -> dict:
        """ Заблокировать/Разблокировать пользователя в руме

        **Параметры**
            - **room_id** : ID комнаты
            - **target_uid** : VK User ID
            - **value** : True - заблокировать, False - разблокировать
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "target_uid": target_uid,
            "value": value
        }
        return self.client.request("room/v3/toggleBlock.php", _data=data)

    def radio_vote(self, room_id: int, vote: bool):
        """ Поставить лайк/дизлайк треку

        **Параметры**
            - **room_id** : ID комнаты
            - **vote** : True - лайк, False - дизлайк
        """
        data = {
            "vote": vote,
            "r": f"{self.client.room_iders}_{room_id}"
        }
        return self.client.request("room/v3/radio/vote.php", _data=data)

    def radio_add(self, room_id: int, track: dict, price: int = 0):
        """ Добавить трек в комнаты

        **Параметры**
            - **room_id** : ID комнаты
            - **track** : Конфиг трека
            - **price** : Оставлять нулевым, если не нужно добавлять его вне списка
        """
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "track": json.dumps(track),
            "price": price,
        }
        return self.client.request("room/v3/radio/add.php", _data=data)

    def radio_remove(self, room_id: int, id: int):
        """ Удаление трека из списка

        **Параметры**
            - **room_id** : ID комнаты
            - **id** : ID трека
        """
        data = {
            "id": id,
            "r": f"{self.client.room_iders}_{room_id}",
        }
        return self.client.request("room/v3/radio/remove.php", _data=data)

    def add_game_gift(self, room_id: int, target_uid: int, gift_id: int, coords: dict,
        count: int = 1, action_id: int = 1, v: int = 1):
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "v": v,
            "target_uid": target_uid,
            "gift_id": gift_id,
            "coordsJson": json.dumps(coords),
            "count": count,
            "action_id": action_id,
        }
        return self.client.request("room/v3/addGameGift.php", "post", _data=data)

    def add_bot(self, room_id: int, sex: int, by_one: bool = True):
        data = {
            "r": f"{self.client.room_iders}_{room_id}",
            "bot_sex": sex,
            "by_one": by_one,
        }
        return self.client.request("room/v3/addBot.php", _data=data)