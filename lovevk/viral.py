import json


class Viral:

    def __init__(self, client) -> None:
        self.client = client

    def create_answer(self, target_uid: int, question_id: int = 1381, share: bool = True, answer_id: int = 1384,
        sender_male: bool = True, recipient_male: bool = True, ws: bool = False):
        data = {
            "target_uid": target_uid,
            "question_id": question_id,
            "share": share,
            'answer_id': answer_id,
            "sender_male": sender_male,
            "recipient_male": recipient_male,
            "ws": ws
        }
        return self.client.request("viral/createAnswer.php", _data=data)

    def get_next_answer_id(self, target_uid: int):
        extra = self.client.md5(f"{self.viewer_id}_{target_uid}_{int(time.time())}_{self.version}")
        data = {
            "target_uid": target_uid,
            "extra": extra
        }
        return self.client.request("viral/getNextAnswerId.php", _data=data)

    def open_answer(self, id: int):
        data = {
            "id": id
        }
        return self.client.request("viral/openAnswer.php", _data=data)

    def buy_extra(self):
        return self.client.request("viral/buyExtra.php")

    def get_left_time_when_can_answer(self):
        return self.client.request("viral/getLeftTimeWhenCanAnswer.php")

    def get_data(self):
        return self.client.request("viral/getData.php")