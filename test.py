money = 998 
transter = 2000
print('ต้องการโอน ', 2000)

while money < (transter + 15):
	print('คุณมีเงิน', money)
	print('กรุณาโอนเงินเข้าบัญชี เงินไม่พอโอน')
	get_money = int(input('ฝากเงินเท่าไหร่ ?: '))
	money = money + get_money
	print('---')

print('คุณมีเงิน', money)
print("โอนได้เลย")
print('เหลือเงินในบัญชี: ', money - (transter+15))

