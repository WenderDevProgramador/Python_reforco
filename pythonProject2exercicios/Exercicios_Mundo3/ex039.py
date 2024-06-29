#Crie um código em python que teste se o site está acessivel pelo computador usado.

import urllib
import urllib.request
print( ' ')
try:
    site = urllib.request.urlopen('https://alternative.me/crypto/fear-and-greed-index/#google_vignette')
except urllib.request.URLError:
    print('Site não acessível no momento.')
else:
    print('Site acessado com sucesso!')
    
print( ' ')