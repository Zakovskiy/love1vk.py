class BootData:

	def __init__(self, data:dir):
		self.json = data
		self.is_viral_tab_disabled = None
		self.bonus_per_game_win = None
		self.hp = None
		self.vp200 = None
		self.viral_questions = []
		self.total_photo_views = None
		self.slE = None
		self.b1 = None
		self.photos_is_available_for_room = None
		self.b3 = None
		self.balance = None
		self.price = None
		self.warns = None
		self.b9 = None
		self.lvd = None
		self.exp = None
		self.recent_liked_photos = []
		self.wins = None
		self.invis = None
		self.roomGifts = []
		self.editor_is_activated = None
		self.received = None
		self.is_admin = None
		self.is_money_box_disabled = None
		self.spin_gifts_array = []
		self.price_per_anonymous_comment = None
		self.is_VK_link_hidden = None
		self.rg = None
		self.daily_bonuses = []
		self.self_room_id = None
		self.canFN = None
		self.notifications = []
		self.status = None
		self.canWF = None
		self.vp100 = None
		self.total_price = None
		self.is_self_room_activated = None
		self.total_guests = None
		self.time_of_last_reset_notifications_counter = None
		self.version = None

	@property
	def BootData(self):
		self.is_viral_tab_disabled = self.json["isViralTabDisabled"]
		self.bonus_per_game_win = self.json["bonusPerGameWin"]
		self.hp = self.json["hp"]
		self.vp200 = self.json["vp200"]
		self.viral_questions = self.json["viralQuestions"]
		self.total_photo_views = self.json["totalPhotoViews"]
		self.slE = self.json["slE"]
		self.b1 = self.json["b1"]
		self.photos_is_available_for_room = self.json['photosIsAvailableForRoom']
		self.b3 = self.json["b3"]
		self.balance = self.json["balance"]
		self.price = self.json["price"]
		self.warns = self.json["warns"]
		self.b9 = self.json["b9"]
		self.lvd = self.json["lvd"]
		self.exp = self.json["exp"]
		self.recent_liked_photos = self.json['recentLikedPhotos']
		self.wins = self.json["wins"]
		self.invis = self.json["invis"]
		self.room_gifts = self.json["roomGifts"]
		self.editor_is_activated = self.json["editorIsActivated"]
		self.received = self.json["received"]
		self.is_admin = self.json["isAdmin"]
		self.is_money_box_disabled = self.json["isMoneyBoxDisabled"]
		for spin_gift in self.json["spinGiftsArray"]:
			self.spin_gifts_array.append(SpinGift(spin_gift).SpinGift)
		self.price_per_anonymous_comment = self.json["pricePerAnonymousComment"]
		self.is_VK_link_hidden = self.json["isVKLinkHidden"]
		self.rg = self.json["rg"]
		self.daily_bonuses = self.json["dailyBonuses"]
		self.self_room_id = self.json["selfRoomId"]
		self.canWF = self.json["canWF"]
		self.canFN = self.json["canFN"]
		self.notifications = self.json["notifications"]
		self.status = self.json["status"]
		self.vp100 = self.json["vp100"]
		self.total_price = self.json["totalPrice"]
		self.is_self_room_activated = self.json["isSelfRoomActivated"]
		self.total_guests = self.json["totalGuests"]
		self.time_of_last_reset_notifications_counter = self.json["timeOfLastResetNotificationsCounter"]
		self.version = self.json["v"]
		return self

class UserInfo:

	def __init__ (self, data:dir):
		self.json = data
		self.last_name = None
		self.first_name = None
		self.pid = None
		self.photos = []
		self.country_id = None
		self.room_id = None
		self.game_counter_1 = None
		self.balance = None
		self.exp = None
		self.game_counter_2 = None
		self.game_counter_3 = None
		self.gifts = None
		self.wins = None
		self.owner = None
		self.comments = []
		self.sex = None
		self.vf = None
		self.photo_200 = None
		self.photo_100 = None
		self.is_VK_link_hidden = None
		self.harem_price = None
		self.region_id = None
		self.rg = None
		self.background = None
		self.sign_in = None
		self.fn_gen = None
		self.online = None
		self.age = None
		self.status = None

	@property
	def UserInfo(self):
		self.age = self.json["age"]
		self.sex = self.json["sex"]
		self.exp = self.json["exp"]
		self.first_name = self.json["fn"]
		self.last_name = self.json["ln"]
		self.photo_100 = self.json["p100"]
		self.photo_200 = self.json["p200"]
		self.vf = self.json["vf"]
		self.pid = self.json["pid"]
		self.photos = self.json["photos"]
		self.country_id = self.json["countryId"]
		self.room_id = self.json["roomId"]
		self.game_counter_1 = self.json["gameCounter1"]
		self.balance = self.json["balance"]
		self.game_counter_2 = self.json["gameCounter2"]
		self.game_counter_3 = self.json["gameCounter3"]
		self.gifts = self.json["gifts"]
		self.wins = self.json["wins"]
		self.owner = self.json["owner"]
		for comment in self.json["comments"]:
			self.comments.append(Comment(comment).Comment)
		self.is_VK_link_hidden = self.json["isVKLinkHidden"]
		self.harem_price = self.json["haremPrice"]
		self.region_id = self.json["regionId"]
		self.rg = self.json["rg"]
		self.background = self.json["background"]
		self.sign_in = self.json["signIn"]
		self.fn_gen = self.json["fnGen"]
		self.online = self.json["online"]
		self.age = self.json["age"]
		self.status = self.json["status"]
		return self

class Comment:

	def __init__ (self, data:dir):
		self.json = data
		self.id = None
		self.comments = None
		self._from = None
		self.last_reply = None
		self.pub = None
		self.text = None
		self.to = None
		self.ts = None
		self.upd = None
		self.from_exp = None
		self.from_age = None
		self.from_photo_url = None
		self.from_full_name = None
		self.from_vf = None
		self.to_exp = None
		self.to_age = None
		self.to_photo_url = None
		self.to_full_name = None
		self.to_vf = None

	@property
	def Comment(self):
		self.id = self.json["_id"]
		self.comments = self.json['comments']
		self._from = self.json["from"]
		self.last_reply = self.json["lastReply"]
		self.pub = self.json["pub"]
		self.text = self.json["text"]
		self.to = self.json["to"]
		self.ts = self.json["ts"]
		self.upd = self.json["upd"]
		self.from_exp = self.json["fromExp"]
		self.from_age = self.json["fromAge"]
		self.from_photo_url = self.json["fromPhotoUrl"]
		self.from_full_name = self.json["fromFullName"]
		self.from_vf = self.json["fromVF"]
		self.to_exp = self.json["toExp"]
		self.to_age = self.json["toAge"]
		self.to_photo_url = self.json["toPhotoUrl"]
		self.to_full_name = self.json["toFullName"]
		self.toVF = self.json["toVF"]
		return self

class SpinGift:

	def __init__ (self, data:dir):
		self.json = data
		self.id = None
		self.f = None
		self.r = None
		self.s = None
		self.t = None
		self.v = None
		self.age = None
		self.sex = None
		self.exp = None
		self.first_name = None
		self.last_name = None
		self.photo_100 = None
		self.photo_200 = None
		self.vf = None

	@property
	def SpinGift(self):
		self.id = self.json["_id"]
		self.f = self.json["f"]
		self.r = self.json["r"]
		self.s = self.json["s"]
		self.t = self.json["t"]
		self.v = self.json["v"]
		self.age = self.json["age"]
		self.sex = self.json["sex"]
		self.exp = self.json["exp"]
		self.first_name = self.json["fn"]
		self.last_name = self.json["ln"]
		self.photo_100 = self.json["p100"]
		self.photo_200 = self.json["p200"]
		self.vf = self.json["vf"]
		return self
	