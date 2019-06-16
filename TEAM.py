from tkinter import *
from tkinter import font
import http.client
import urllib.request
from io import BytesIO
import urllib
import telepot
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import spam
import tkinter.messagebox




g_Tk = Tk()
g_Tk.geometry("1200x700+100+100")
DataList = []
SandDataList = []
url = str("")

print (spam.strlen("hello world")) # spam을 이용한 c++ 모듈 test

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[국내 관광지 정보]")
    MainText.pack()
    MainText.place(x=500)# 절대 배치자 해도 그만 안해도그만
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchWhat = Label(g_Tk, font = TempFont, text="[관광지 검색]")
    SearchWhat.pack()
    SearchWhat.place(x=240, y=70)



def InitInputLabel():
    global InputLabel
    TempFont=font.Font(g_Tk, size= 15, weight='bold', family = 'consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width=56 ,borderwidth = 12,
                        relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=210, y= 105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=880, y=110)

def InitSelectLabel():  # 이미지 와 선택시 등 처리
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')



    selectLabel = Label(g_Tk, bg="white", height=22, width=50, borderwidth = 10, relief = 'ridge')
    selectLabel.pack()
    selectLabel.place(x=30, y=215)

    selectLabel_2 = Label(g_Tk, bg="white", height=22, width=50, borderwidth = 10, relief = 'ridge')  # 지도창
    selectLabel_2.pack()
    selectLabel_2.place(x=410, y=215)

    selectText = Text(g_Tk, width=104, height=6, borderwidth=12, relief='ridge')
    selectText.pack()
    selectText.place(x=30, y=580)

def SearchButtonAction():

    RenderText.configure(state='normal')
    #RenderText.get()
    RenderText.delete(0, END)

    SearchWhere()
    RenderText.bind('<<ListboxSelect>>', onselect)

   # RenderText.configure(state='disabled')


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    print(DataList)
    url = DataList.index(value) -4
    url = DataList[url]
    print(url)

    from io import BytesIO
    from PIL import Image, ImageTk
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    ph = ImageTk.PhotoImage(im)

    selectLabel = Label(g_Tk, image=ph, height=330, width=350)
    selectLabel.image = ph
    selectLabel.pack()
    selectLabel.place(x=40, y=225)
    TempFont = font.Font(g_Tk, size=12, family='Consolas')

    selectText = Text(g_Tk,font=TempFont, width=81, height=4, borderwidth=12, relief='ridge')



    selectText.insert(INSERT, '관광지명 : ')
    selectText.insert(INSERT, value)
    selectText.insert(INSERT, "\n")
    selectText.insert(INSERT, '전화 : ')
    selectText.insert(INSERT, DataList[DataList.index(value)-1 ])
    selectText.insert(INSERT, "\n")
    selectText.insert(INSERT, '주소 : ')
    selectText.insert(INSERT, DataList[DataList.index(value) - 5])
    selectText.insert(INSERT, "\n")


    SandDataList.clear()
    SandDataList.append(value)
    SandDataList.append(DataList[DataList.index(value) - 1])
    SandDataList.append( DataList[DataList.index(value) - 5])
    selectText.pack()
    selectText.place(x=30, y=580)
    import http.client
    import requests
    import os
    import sys
    from bs4 import BeautifulSoup
    #-*- coding: utf-8 -*-
    aaaaa = DataList[DataList.index(value) - 3] + "," + DataList[DataList.index(value) - 2]
    client_id = "xa7g0x3u9b"
    client_secret = "AP7M8Nn5SilU5QA9h6tqL85lgr8QpfvjvGuwpbPs"
    url ="https://naveropenapi.apigw.ntruss.com/map-static/v2/raster?w=300&h=300&center="+aaaaa+"&level=16&X-NCP-APIGW-API-KEY-ID={xa7g0x3u9b}"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        with urllib.request.urlopen(request) as a:
            raw_data = a.read()
        imm = Image.open(BytesIO(response_body))
        phm = ImageTk.PhotoImage(imm)
        selectLabel_2 = Label(g_Tk, image=phm, height=340, width=360)
        selectLabel_2.image = phm
        selectLabel_2.pack()
        selectLabel_2.place(x=410, y=215)
    else:
        print("Error Code:" + rescode)

def SearchWhere():
    import http.client
    from xml.dom.minidom import parse, parseString

    conn = None
    path = InputLabel.get()
    encText = urllib.parse.quote(path)

    server = "api.visitkorea.or.kr"
    servicekey = "vI6iJQ67m77QdQNRKPolJItYH7UHkXtO5gb7xohugYFEwoSQueRopRItR%2BxijJqtggX3PvDvMYm2vPRotrTN4g%3D%3D"
    conn = http.client.HTTPConnection(server)
    conn.request("GET", "/openapi/service/rest/KorService/searchKeyword?serviceKey=" + servicekey +
                 "&MobileApp=AppTest&MobileOS=ETC&pageNo=1&startPage=1&numOfRows=999&pageSize=10&listYN=Y&arrange=A&contentTypeId=12&keyword=" + encText)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read().decode('utf-8')

        parseData = parseString(response_body)

        GeoInfoWhere = parseData.childNodes
        row = GeoInfoWhere[0].childNodes[1].childNodes[0].childNodes

        global DataList
        DataList.clear()
        for item in row:
            list = item.childNodes
            for lis in list:
                if lis.nodeName == 'addr1':
                    DataList.append(lis.firstChild.nodeValue)
                if lis.nodeName == 'firstimage':
                    DataList.append(lis.firstChild.nodeValue)

                if lis.nodeName == 'tel':
                    DataList.append(lis.firstChild.nodeValue)
                if lis.nodeName == 'title':
                    DataList.append(lis.firstChild.nodeValue)
                    RenderText.insert(END, lis.firstChild.nodeValue)

                if lis.nodeName == 'mapx':
                        DataList.append(lis.firstChild.nodeValue)
                if lis.nodeName == 'mapy':
                        DataList.append(lis.firstChild.nodeValue)
    else:
        print("Error!")




def InitTeleButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="텔레그램", command=TeleAction)
    SearchButton.pack()
    SearchButton.place(x=880, y=80)

def TeleAction():
    global bot
    bot = telepot.Bot('817469690:AAHN_b-ew2MjuCIv30qnDikIXCVLNjpvMRc')
    bot.getMe()

    bot.message_loop(Handle)

    print("Listening...")





def Handle(msg):
    global bot
    import http.client
    from xml.dom.minidom import parse, parseString
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg['text'])
    if content_type != 'text':
        bot.sendMessage("763140001", '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return



    conn = None
    path = msg['text']
    encText = urllib.parse.quote(path)

    server = "api.visitkorea.or.kr"
    servicekey = "vI6iJQ67m77QdQNRKPolJItYH7UHkXtO5gb7xohugYFEwoSQueRopRItR%2BxijJqtggX3PvDvMYm2vPRotrTN4g%3D%3D"
    conn = http.client.HTTPConnection(server)
    conn.request("GET", "/openapi/service/rest/KorService/searchKeyword?serviceKey=" + servicekey +
                 "&MobileApp=AppTest&MobileOS=ETC&pageNo=1&startPage=1&numOfRows=999&pageSize=10&listYN=Y&arrange=O&contentTypeId=12&keyword=" + encText)
    req = conn.getresponse()
    if int(req.status) == 200:
        response_body = req.read().decode('utf-8')

        parseData = parseString(response_body)

        GeoInfoWhere = parseData.childNodes

        row = GeoInfoWhere[0].childNodes[1].childNodes[0].childNodes

        for item in row:
            st = str()
            list = item.childNodes
            for lis in list:
                if lis.nodeName == 'addr1':
                    st += "주소 : " + lis.firstChild.nodeValue
                if lis.nodeName == 'tel':
                    st += "\n전화번호 : " + lis.firstChild.nodeValue
                if lis.nodeName == 'title':

                    st += "\n이름 : " + lis.firstChild.nodeValue
                    bot.sendMessage("763140001", st)




def InitsandButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="이메일전송", command=sandAction)
    SearchButton.pack()
    SearchButton.place(x=960, y=80)





def sandAction():
    print(SandDataList)

    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "nariyan1717@gmail.com" # 보내는 사람 email 주소.
    recipientAddr = "nariyan17@naver.com"  # 받는 사람 email 주소.

    msg = MIMEText("관광지명 : " + SandDataList[0] + "\n" + "전화 : " + SandDataList[1] + "\n" + "주소: " + SandDataList[2])
    #msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "관광정보 서비스 이메일이 왔습니다."
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    '''htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    htmlFD.close()'''

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    #msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("nariyan1717@gmail.com","djtotls1717")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()




def InitRenderText():
    global RenderText




    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Listbox(g_Tk, width=40, height=30, borderwidth=12, relief='ridge')
    #RenderText = Text(g_Tk, width=30, height=27, borderwidth=12, relief='ridge')
                      #,yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack(side = RIGHT,fill =Y)
    RenderText.place(x=800, y=215)
    #RenderTextScrollbar.config(command= RenderText.yview)
    #RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)

    RenderText.configure(state = 'disabled')




InitTopText()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitSelectLabel()
InitsandButton()
InitTeleButton()
g_Tk.mainloop()