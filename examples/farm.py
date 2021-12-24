"""
Фарм монеток с помощью Бонусов только через ВК аккаунт.
В день можно фармить  по 20 монет.
"""
import lovevk
import time

token = ""
_id = 0

love = lovevk.Client(token, _id)

for i in range(20):
    love.viral_get_next_answer_id(_id)
    print(love.viral_create_answer(_id))
    time.sleep(0.5)