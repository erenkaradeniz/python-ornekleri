class P1:
	def merhaba(self):
		print("Merhaba ben p1")

class P2:
	def merhaba(self):
		print("Merhaba ben p2")

	def fonk1(self):
		print("ben p2'nin metoduyum")

class C(P1, P2):
	pass


c = C()

c.fonk1()
c.merhaba() # İlk hangisi tanımlandıysa onu çağırır