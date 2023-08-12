import threading
import urllib2
import time

start = time.time()
urls = ["http://www.google.com", "http://www.Applee.com", "http://www.Microsoft.com", "http://www.instagram.com"]

def chama_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print("'%s\' carregado em %ss" % (url, (time.time() - start)))

threads = [threading.Thread(target=chama_url(), args=(url, )) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Elapsed Time : %s" % (time.time() - start))
