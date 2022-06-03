from importlib.resources import contents
import urllib.request

content = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Teorema_de_Bayes").read()
content = str(content)
find = '<span id="'
pos = int(content.index(find) + len(find))

txt = content[pos:pos+4]

print("Meu texto: " + txt)