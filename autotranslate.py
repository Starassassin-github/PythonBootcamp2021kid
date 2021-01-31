#autotranslate.py

#pip install googletrans==3.1.0a0
#pip install easyread

#from googletrans import Translator, LANGUAGES
from easyread.translator import Translate
from openpyxl import Workbook
from datetime import datetime

#translator = Translator() # ตัวแปลคำศัพท์
# result = translator.translate('cat',dest='th')
# print(result.text)

article = open('article.txt','r',encoding='utf-8')
article = article.read()
article = article.split()

print('Count: ',len(article))
result = []

for word in article:
	#print(word)
	res = Translate(word)
	if res != None:
		#print(res['meaning'])
		result.append([word,res['meaning']])
		# result.append(['Cat','[N] แมว')

#print(result)
excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab','Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))
