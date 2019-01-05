import sys
import io
import urllib.request as dw # alias

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "https://post-phinf.pstatic.net/20161017_243/1476630494401TkViK_PNG/2.png?type=w1200"
htmlUrl = "http://google.com"

savePath1 = "C:/test1.jpg"
savePath2 = "C:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

# type 1
saveFile1 = open(savePath1, 'wb') # w : wright, r : read, a : add, b means binary
saveFile1.write(f)
saveFile1.close()

# type 2
with open(savePath2, 'wb') as saveFile2: # with를 벗어나는 구간에서 자동으로 close가 호출됨
    saveFile2.write(f2)


print("다운로드 완료")

# urlretrieve 저장 > open('r') > 변수에 할당 > 파싱 > 저장
# 파싱이 필요없는 데이터의 경우 이 함수가 유리함

# urlopen 변수 할당 > 파싱 > 저장 (db, ...)
# 필요로 하는 것을 분석을 통해서 파싱해야 할 경우 이 함수가 유리함
