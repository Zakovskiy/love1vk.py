import json
import threading
import time
from websocket import create_connection
from sys import _getframe as getframe
from enum import IntEnum


class SocketHandler:
    def __init__(self, client):
        self.socket_url = "wss://igra.love/web/websocket"
        self.client = client

    def create_connection(self):
        """ Создание вебсокета """
        self.socket = create_connection(f"{self.socket_url}?viewer_id={self.client.viewer_id}&auth_key={self.client.auth_key}&client_type={self.client.client_type}&api_id=4333086&tab_id=0")
        self.utc()
        threading.Thread(target=self.recvier).start()

    def recvier(self):
        while 1:
            data = json.loads(self.socket.recv())
            data = json.loads(str(data[0]))
            self.client.handle_socket_message(data)

    def send(self, data: dict) -> None:
        """ Отправление неких данных на вебсокет """
        data.update({
            "viewer_id": self.client.viewer_id,
            "cb": round(time.time() * 1000)
        })
        self.socket.send(json.dumps(data))

    def utc(self):
        self.send({"action": "utc"})

    def hand_shaking(self):
        self.send({"action": "hand-shaking"})

    def room_answer(self, room_id: int):
        self.send({"action": "room/answer", "r": f"{self.client.room_iders}_{room_id}", "q": "lottery", "a": "1_11"})

    def ad_left_time(self):
        self.send({"action": "ad/leftTime"})

    def ping(self, room_id: int, is_away: bool = True):
        self.send({
            "action": "pingRoom",
            "room_id": room_id,
            "is_away": is_away
        })

    def ad_reward(self):
        ts = round(time.time() * 1000)
        sign = self.md5(f"{ts}_{self.client.version}_{self.client.version}")
        values = {
            "ts": ts,
            "sign": sign
        }
        secret = urllib.parse.quote(html.unescape(base64.b64encode(json.dumps(values).encode()).decode()), safe='~()*!\'')[::-1]

        o = {
            "action": "ad/reward",
            "payload": ("".join(secret)).replace("D3%", "=")
        }
        self.send(o)
        return self.listen()

class Callbacks:
    def __init__(self):
        self.handlers = {}
        self.types = {
            5: self.room_change,
            3: self.warns_change,
            9: self.access_denied,
            4: self.new_guest,
            7: self.comment,
            6: self.new_notification,
            8: self.server_will_reboot,
            10: self.update_room_gifts,
            11: self.admin_review_photo,
            13: self.add_photos,
            14: self.change_state,
            15: self.user_add_to_favorite,
            16: self.user_remove_from_favorite,
            17: self.admin_reject_photo,
            18: self.new_private_message,
            19: self.change_balance,
            21: self.update_freq_gifts,
            100: self.unknown,
            22: self.unknown,
            777: self.unknown,
        }
        t = 0
        #print(self.room_types.items())

    def resolve(self, data):
        return self.types.get(data["1"], 100)(data)

    def event(self, type):
        def register_handler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
            else:
                self.handlers[type] = [handler]
            return handler

        return register_handler

    def call(self, type, data):
        if type in self.handlers:
            for handler in self.handlers[type]:
                handler(data)

    def room_change(self, data: dict):
        for i in json.loads(data["2"]["3"]):
            type = i[0]
            data = i[2]
            if not data:
                return
            if type == 1:
                for command in data:
                    self.call(getframe(0).f_code.co_name, command)
            else:
                self.call(getframe(0).f_code.co_name, i)

    def warns_change(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def access_denied(self, data: dict):
        return True

    def new_guest(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def comment(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def new_notification(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def server_will_reboot(self, data: dict):
        return True

    def update_room_gifts(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"]["1"])

    def admin_review_photo(self, data: dict):
        return True

    def add_photos(self, data: dict):
        return True

    def change_state(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def user_add_to_favorite(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def user_remove_from_favorite(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def admin_reject_photo(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def new_private_message(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def change_balance(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def update_freq_gifts(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

    def unknown(self, data: dict):
        self.call(getframe(0).f_code.co_name, data["2"])

class Events:
    class Room(IntEnum):
        ROUND_START = 2
        ROUND_PAUSED = 3
        ROUND_WAITING = 4
        CREATE_USER = 5
        REMOVE_USER = 6
        UPDATE_USER_ON_ENTER_ROOM = 7
        SEND_GIFT = 8
        REMOVE_GIFT = 9
        USER_EXP_TODAY = 10
        USER_GIFT_COUNT_TOTAL = 11
        USER_GIFT_COUNT_SENT = 12
        USER_GIFT_COUNT_RECEIVED = 13
        USER_LOTTERY_WINS = 14
        USER_RADIO_LIKES_COUNT = 15
        USER_AWAY = 16
        VIEWER_ANSWER = 17
        ROUND_ANSWER = 18
        VIEWER_PRIVATE_MESSAGE_COUNTER_CHANGES = 19
        VIEWER_PRIVATE_MESSAGES_CHANGE = 20
        USER_ANSWER_STATE = 21
        USER_WASTEFUL = 22
        USER_POPULAR = 23
        USER_DJ = 24
        USER_FORTUNATE = 25
        USER_LOTTERY_BET = 26
        NEW_CHAT_MESSAGES = 27
        RADIO = 28
        RADIO_VOTES = 29
        RADIO_COOL_LIKE = 30
        RADIO_LIST = 31
        CROWN_VOTE = 32
        ROOM_INVITE = 33
        EXIT_REASON = 34
        RESQUE = 35
        INTERRUPT_CURRENT_TRACK = 36
        SENT_GIFTS_PER_ROOM = 37
        RECEIVED_GIFTS_PER_ROOM = 38
        PLACE_PURCHASE_IN_QUEUE = 39
        PLACE_CONFIRM_TO_QUEUE = 40
        QUEUE_IS_CHANGED = 41
        QUEUE_IS_REORDER = 42
        USER_HAS_BDATE_TODAY = 43
        CHOOSE_COUPLE_ROUND = 44
        USERS_COOL_LIKES = 45
        USER_CHANGE_AVATAR = 46
        LOADING_ROUND = 47
        CHANGE_LIKES_OF_CHAT_MESSAGE = 48
        MERGE_CHAT_MESSAGE = 49
        USER_NAME_UPDATE = 50
        REMOVE_CHAT_MESSAGES = 51
        CHANGE_SUB_STATE_OF_ROUND_CHOOSE_EACH_OTHER = 52
