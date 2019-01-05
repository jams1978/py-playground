import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "https://post-phinf.pstatic.net/20161017_243/1476630494401TkViK_PNG/2.png?type=w1200"
htmlUrl = "http://google.com"

savePath1 = "C:/test1.jpg"
savePath2 = "C:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")
