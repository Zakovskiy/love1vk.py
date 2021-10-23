from utils import objects
import websocket
import requests
import json
import time
import random
from websocket import create_connection
from pprint import pprint
from secrets import token_hex
import hashlib
import threading

# md5(api_id + '_' + viewer_id + '_' + api_secret)

class Client:

	def __init__(self, auth_key:str, user_id:int, session_key:str=None, client_type:int=1, websocket:bool=False, mobi:bool=False):
		"""
			В библиотеке возможно авторизация как через ВК так и через ОдноКлассники
			auth_key = специальный ключ, который от игр вк или ОК нельзя никак сгенерировать
				или получить через какой-то запрос отдельно, поэтому, вам придется отслеживать
				запросы игры, и так получать его
			user_id = айди вашего аккаунта ВК или OK
			session_key = специальный ключ, если вы будете юзать ОК. Для вк оставляйте пустым
			client_type = 1 - ВК, 2 - ОК
		"""
		self.auth_key = auth_key
		self.mobi = str(mobi)
		self.viewer_id = str(user_id)
		self.client_type = client_type
		self.session_key = session_key
		self.pc_fingerprint = "eb312822100c2618a3a608cd910dd131"
		self.api = "https://igra.love/web/"
		self.version = None
		if websocket:
			self.create_connection()
		self.get_boot_data()

	def create_connection(self):
		self.socket = create_connection(f"wss://igra.love/web/websocket?viewer_id={self.viewer_id}&auth_key={self.auth_key}&client_type={self.client_type}&api_id=4333086&tab_id=0")
		self.utc()

	def listen(self):
		data = json.loads(self.socket.recv()[0])
		if data["1"] == 5:
			return
		return data

	def send(self, data):
		return self.socket.send(json.dumps(data))

	def get_boot_data(self, first_name:str="Игрок", last_name:str="Игрок", photo:str=".!.", sex:int=1):
		data = {
			"fp":"634e957afe267c18b46fcb8441de63ff",
			"mobi": self.mobi,
			"first_name":first_name,
			"last_name":last_name,
			"photo_100":photo,
			"photo_200":photo,
			"sex":f"{sex}",
			"guests_limit":"1",
			"referrer":"library_zakovskiy"
		}
		if self.client_type == 2:
			data.update({
				"name_cases":"Игрок,+,Игрок,+,Игрок,+,Игрок,+,Игрок,+",
				"update_name":"true",
				"ok_avatar_url":photo,
				"ok_fn":first_name,
				"ok_ln":last_name
			})
		else:
			data.update({
				"name_cases_json_array":"[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]",
				"user_id":self.viewer_id,
				"hash":""
			})
		request = self.request("getBootData.php", "post", data)
		if request["code"] == 200:
			data = objects.BootData(request["data"]).BootData
			self.version = data.version
			return data
		return None

	def viral_get_data(self):
		return self.request("viral/getData.php")

	def get_room(self, target_room_id:int=None, force:bool=True):
		data = {
			"pc_fingerprint":self.pc_fingerprint,
			"is_mobi":self.mobi,
			"force":force
		}
		if target_room_id: data["target_room_id"] = f"1_{target_room_id}"
		return self.request("room/v3/getRoom.php", _data=data)

	def get_room_list(self):
		return self.request("room/v3/getRoomList.php")

	def ping_rooms(self, room_top:bool=True):
		return self.request("ping.php", _data={"room_top":room_top})

	def user_get_info(self, target_uid:int, target_user_is_friend:bool=True, referer:int=7, sex:int=2):
		data = {
			"target_uid":target_uid,
			"target_user_is_friend":target_user_is_friend,
			"referer":referer,
			"sex":sex
		}
		result = self.request("user/getInfo.php", _data=data)
		if result["code"] == 200: return objects.UserInfo(result["data"]).UserInfo
		return None

	def user_update_region(self, country_id:int, region_id:int):
		data = {
			"country_id":country_id,
			"region_id":region_id
		}
		return self.request("user/updateRegion.php", _data=data)

	def user_top(self, all:bool=True):
		return self.request("user/top.php", _data={"all":all})

	def user_inc_balance(self, action_id:int=6):
		return self.request("user/incBalance.php", _data={"action_id":action_id})

	def user_get_self_balance(self):
		return self.request("user/getSelfBalance.php")

	def user_get_daily_bonus(self):
		return self.request("user/getDailyBonus.php")

	def user_on_group_subscribe(self):
		return self.request("user/onGroupSubscribe.php")

	def wheeloffortune_freespin_receive(self, id):
		return self.request("wheeloffortune/freespin/receive.php", _data={"id":id})

	def wheeloffortune_spin(self):
		return self.request("wheeloffortune/spin.php")

	def wheeloffortune_freespin_send_spin(self, target_uid:int):
		return self.request("wheeloffortune/freespin/sendSpin.php", _data={"target_uid":target_uid})

	def wheeloffortune_check_spins(self):
		return self.request("wheeloffortune/checkSpins.php")

	def send_private_message(self, text, target_uid, room_id, type:int=50, free:bool=True):
		data = {
			"text":text,
			"target_uid":target_uid,
			"room_id":f"1_{room_id}",
			"free":free,
			"type":type
		}
		return self.request("privatemessage/add.php", _data=data)

	def room_get_uids(self, room_id:int):
		return self.request("room/v3/getUids.php", _data={"r":f"1_{room_id}"})

	def room_chat_new_level(self, exp):
		return self.request("room/v3/chat/newLevel.php", _data={"exp":exp})

	def room_chat_send_message(self, room_id:int, message:str, to:int=None):
		data = {
			"r":f"1_{room_id}",
			"m":message,
			"to":str(to)
		}
		return self.request("room/v3/chat/add.php", "post", _data=data)

	def room_chat_send_sticker(self, room_id:int, message:str, config:list):
		data = {
			"r":f"1_{room_id}",
			"m":message,
			"serialized_config":json.dumps(config)
		}
		return self.request("room/v3/chat/addSticker.php", "post", _data=data)

	def room_add_answer(self, room_id:int, a, q:str="males"):
		data = {
			"r":f"1_{room_id}",
			"a":a,
			"q":q
		}
		return self.request("room/v3/addAnswer.php", _data=data)

	def room_chat_toggle_like(self, room_id:int, message_id:str):
		data = {
			"message_id":message_id,
			"room_id":f"1_{room_id}"
		}
		return self.request('room/v3/chat/toggleLike.php', _data=data)

	def room_toggle_block(self, room_id:int, target_uid:int, value:bool=True):
		data = {
			"r":f"1_{room_id}",
			"target_uid":target_uid,
			"value":value
		}
		return self.request("room/v3/toggleBlock.php", _data=data)

	def room_radio_vote(self, room_id:int, vote:bool=True):
		data = {
			"vote":vote,
			"r":f"1_{room_id}"
		}
		return self.request("room/v3/radio/vote.php", _data=data)

	def room_radio_add(self, room_id:int, track:list, price:int=0):
		data = {
			"r":f"1_{room_id}",
			"track":json.dumps(track),
			"price":price
		}
		return self.request("room/v3/radio/add.php", _data=data)

	def room_radio_remove(self, room_id:int, id):
		data = {
			"id":id,
			"r":f"1_{room_id}"
		}
		return self.request("removeRadioTrack.php", _data=data)

	def room_add_game_gift(self, room_id:int, target_uid:int, gift_id:int, coords:list, count:int=1, action_id:int=1, v:int=1):
		data = {
			"r":f"1_{room_id}",
			"v":v,
			"target_uid":target_uid,
			"gift_id":gift_id,
			"coordsJson":json.dumps(coords),
			"count":count,
			"action_id":action_id
		}
		return self.request("room/v3/addGameGift.php", "post", _data=data)

	def room_add_bot(self, room_id, sex, by_one:bool=True):
		data = {
			"r":f"1_{room_id}",
			"bot_sex":sex,
			"by_one":by_one
		}
		return self.request("room/v3/addBot.php", _data=data)

	def money_box_get(self):
		return self.request("moneybox/get.php")

	def viral_create_answer(self, target_uid:int, question_id:int=1381, share:bool=True, answer_id:int=1384, sender_male:bool=True, recipient_male:bool=True, ws:bool=False):
		data = {
			"target_uid":target_uid,
			"question_id":question_id,
			"share":share,
			'answer_id':answer_id,
			"sender_male":sender_male,
			"recipient_male":recipient_male,
			"ws":ws
		}
		return self.request("viral/createAnswer.php", _data=data)

	def viral_get_next_answer_id(self, target_uid:int):
		extra = self.md5(f"{self.viewer_id}_{target_uid}_{int(time.time())}_{self.version}")
		return self.request("viral/getNextAnswerId.php", _data={"target_uid":target_uid, "extra":extra})

	def viral_open_answer(self, id:int):
		return self.request("viral/openAnswer.php", _data={"id":id})

	def viral_buy_extra(self):
		return self.request("viral/buyExtra.php")

	def viral_get_left_time_when_can_answer(self):
		return self.request("viral/getLeftTimeWhenCanAnswer.php")

	def comment_add(self, target_uid:int, text:str, target_user_is_friend:bool=False, is_anonymous:bool=False):
		extra = self.md5(f"{self.viewer_id}_{target_uid}_{int(time.time())}_{self.version}")
		data = {
			"target_uid":target_uid,
			"text":text,
			"target_user_is_friend":target_user_is_friend,
			"is_anonymous":is_anonymous,
			"extra":extra
		}
		return self.request("comment/add.php", "post", _data=data)

	def comment_delete(self, comment_id, comment_owner_id):
		data = {
			"comment_id":comment_id,
			"comment_owner_id":comment_owner_id
		}
		return self.request("comment/delete.php", _data=data)

	def utc(self):
		self.send({"action":"utc", "viewer_id":self.viewer_id})

	def hand_shaking(self):
		self.send({"action":"hand-shaking", "viewer_id":self.viewer_id})

	def room_answer(self, room_id):
		self.send({"action":"room/answer","r":f"1_{room_id}","q":"lottery","a":"1_11","viewer_id":self.viewer_id,"cb":1633799484972})

	def md5(self, string):
		m = hashlib.md5()
		m.update(string.encode())
		return m.hexdigest()

	def request(self, method, type:str="get", _data:dir={}):
		_data.update({
			"ts":int(time.time()),
			"client_type":self.client_type
		})
		if self.client_type == 2:
			_data.update({
				"auth_sig":self.auth_key,
				"session_key":self.session_key,
				"logged_user_id":self.viewer_id
			})
		else:
			_data.update({
				"auth_key":self.auth_key,
				"api_id":4333086,
				"viewer_id":self.viewer_id,
			})
		if type == "get":
			data = "?"
			for k in _data:
				data += f"&{k}={_data[k]}"
			result = requests.get(f"{self.api}{method}{data}").json()
		else:
			result = requests.post(f"{self.api}{method}", data=_data).json()

		return result