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
		self.is_viral_tab_disabled = self.json.get("isViralTabDisabled")
		self.is_viral_tab_disabled = None
		self.bonus_per_game_win = self.json.get("bonusPerGameWin")
		self.bonus_per_game_win = None
		self.hp = self.json.get("hp")
		self.vp200 = self.json.get("vp200")
		self.viral_questions = self.json.get("viralQuestions")
		self.total_photo_views = self.json.get("totalPhotoViews")
		self.slE = self.json.get("slE")
		self.b1 = self.json.get("b1")
		self.photos_is_available_for_room = self.json.get('photosIsAvailableForRoom')
		self.b3 = self.json.get("b3")
		self.balance = self.json.get("balance")
		self.price = self.json.get("price")
		self.warns = self.json.get("warns")
		self.b9 = self.json.get("b9")
		self.lvd = self.json.get("lvd")
		self.exp = self.json.get("exp")
		self.recent_liked_photos = self.json.get('recentLikedPhotos')
		self.wins = self.json.get("wins")
		self.invis = self.json.get("invis")
		self.room_gifts = self.json.get("roomGifts")
		self.editor_is_activated = self.json.get("editorIsActivated")
		self.received = self.json.get("received")
		self.is_admin = self.json.get("isAdmin")
		self.is_money_box_disabled = self.json.get("isMoneyBoxDisabled")
		for spin_gift in self.json.get("spinGiftsArray", []):
			self.spin_gifts_array.append(SpinGift(spin_gift).SpinGift)
		self.price_per_anonymous_comment = self.json.get("pricePerAnonymousComment")
		self.is_VK_link_hidden = self.json.get("isVKLinkHidden")
		self.rg = self.json.get("rg")
		self.daily_bonuses = self.json.get("dailyBonuses")
		self.self_room_id = self.json.get("selfRoomId")
		self.canWF = self.json.get("canWF")
		self.canFN = self.json.get("canFN")
		self.notifications = self.json.get("notifications")
		self.status = self.json.get("status")
		self.vp100 = self.json.get("vp100")
		self.total_price = self.json.get("totalPrice")
		self.is_self_room_activated = self.json.get("isSelfRoomActivated")
		self.total_guests = self.json.get("totalGuests")
		self.time_of_last_reset_notifications_counter = self.json.get("timeOfLastResetNotificationsCounter")
		self.version = self.json.get("v")
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
		self.age = self.json.get("age")
		self.sex = self.json.get("sex")
		self.exp = self.json.get("exp")
		self.first_name = self.json.get("fn")
		self.last_name = self.json.get("ln")
		self.photo_100 = self.json.get("p100")
		self.photo_200 = self.json.get("p200")
		self.vf = self.json.get("vf")
		self.pid = self.json.get("pid")
		self.photos = self.json.get("photos")
		self.country_id = self.json.get("countryId")
		self.room_id = self.json.get("roomId")
		self.game_counter_1 = self.json.get("gameCounter1")
		self.balance = self.json.get("balance")
		self.game_counter_2 = self.json.get("gameCounter2")
		self.game_counter_3 = self.json.get("gameCounter3")
		self.gifts = self.json.get("gifts")
		self.wins = self.json.get("wins")
		self.owner = self.json.get("owner")
		for comment in self.json.get("comments", {}):
			self.comments.append(Comment(comment).Comment)
		self.is_VK_link_hidden = self.json.get("isVKLinkHidden")
		self.harem_price = self.json.get("haremPrice")
		self.region_id = self.json.get("regionId")
		self.rg = self.json.get("rg")
		self.background = self.json.get("background")
		self.sign_in = self.json.get("signIn")
		self.fn_gen = self.json.get("fnGen")
		self.online = self.json.get("online")
		self.age = self.json.get("age")
		self.status = self.json.get("status")
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
		self.id = self.json.get("_id")
		self.comments = self.json.get('comments')
		self._from = self.json.get("from")
		self.last_reply = self.json.get("lastReply")
		self.pub = self.json.get("pub")
		self.text = self.json.get("text")
		self.to = self.json.get("to")
		self.ts = self.json.get("ts")
		self.upd = self.json.get("upd")
		self.from_exp = self.json.get("fromExp")
		self.from_age = self.json.get("fromAge")
		self.from_photo_url = self.json.get("fromPhotoUrl")
		self.from_full_name = self.json.get("fromFullName")
		self.from_vf = self.json.get("fromVF")
		self.to_exp = self.json.get("toExp")
		self.to_age = self.json.get("toAge")
		self.to_photo_url = self.json.get("toPhotoUrl")
		self.to_full_name = self.json.get("toFullName")
		self.toVF = self.json.get("toVF")
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
		self.id = self.json.get("_id")
		self.f = self.json.get("f")
		self.r = self.json.get("r")
		self.s = self.json.get("s")
		self.t = self.json.get("t")
		self.v = self.json.get("v")
		self.age = self.json.get("age")
		self.sex = self.json.get("sex")
		self.exp = self.json.get("exp")
		self.first_name = self.json.get("fn")
		self.last_name = self.json.get("ln")
		self.photo_100 = self.json.get("p100")
		self.photo_200 = self.json.get("p200")
		self.vf = self.json.get("vf")
		return self
	
