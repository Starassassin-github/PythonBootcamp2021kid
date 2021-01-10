Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota' , 'izusu' , 'suzuki']
>>> mycar = garage.pop(-1)
>>> 
>>> print(mycar)
suzuki
\
>>> print(garage)
['toyota', 'izusu']
>>> garage.append('benz')
>>> print(garage)
['toyota', 'izusu', 'benz']
>>> garage[1] = 'tesla
SyntaxError: EOL while scanning string literal
>>> 
>>> SyntaxError: EOL while scanning string literal
SyntaxError: invalid syntax
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'benz']
>>> print(len(garage))
3
>>> user = ['z','r','t','b','n','p']
>>> user.sort()
>>> print(user)
['b', 'n', 'p', 'r', 't', 'z']
>>> user.sort(reverse=True)
>>> user
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(user))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(user)
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in user:
	print(u)

	
z
t
r
p
n
b
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> users.reverse()
>>> for u in users:
	print(U)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(U)
NameError: name 'U' is not defined
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> for u in users:
	print('สวั่่่สดี', u)
	print('สวัสดี'+ u)

	
สวั่่่สดี z
สวัสดีz
สวั่่่สดี r
สวัสดีr
สวั่่่สดี t
สวัสดีt
สวั่่่สดี b
สวัสดีb
สวั่่่สดี n
สวัสดีn
สวั่่่สดี p
สวัสดีp
>>> 