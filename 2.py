import re
vopros = input("Введите вопрос: ")
def proverka(vopros):
    if (vopros.find("балл") != -1) or (vopros.find("Балл") != -1):
	    d = (True,);
	    result = re.findall('\d{2}.\d{2}.\d{2}', vopros)
	    if str(*result) != "":
	    	d = (True, *result);
    else:
	    d = (False,);
    return d
print(proverka(vopros))
