# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

import requests
import re

result = False

link1 = input()
res1 = requests.get(link1)
if res1.status_code == 200:
    link2 = input()
    for link in re.findall(r"<a href=\"(.*)\"", res1.text):
        res = requests.get(link)
        if res.status_code == 200:
            for url in re.findall(r"<a href=\"(.*)\"", res.text):
                if link2 == url:
                    result = True
                    break
            if result:
                break
else:
    result = False

if result:
    print("Yes")
else:
    print("No")