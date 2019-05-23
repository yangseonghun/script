from tkinter import *
from tkinter import font
import http.client
import urllib.request
from io import BytesIO
import urllib
from PIL import Image, ImageTk

import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("1200x700+100+100")
DataList = []
url = str("")


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
    url = DataList.index(value) - 2
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
    selectText.insert(INSERT, DataList[DataList.index(value) - 1])
    selectText.insert(INSERT, "\n")
    selectText.insert(INSERT, '주소 : ')
    selectText.insert(INSERT, DataList[DataList.index(value) - 3])
    selectText.insert(INSERT, "\n")



    selectText.pack()
    selectText.place(x=30, y=580)



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
                 "&MobileApp=AppTest&MobileOS=ETC&pageNo=1&startPage=1&numOfRows=10&pageSize=10&listYN=Y&arrange=A&contentTypeId=12&keyword=" + encText)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read().decode('utf-8')

        parseData = parseString(response_body)

        GeoInfoWhere = parseData.childNodes
        #print(GeoInfoLibrary)
        row = GeoInfoWhere[0].childNodes[1].childNodes[0].childNodes

        global DataList
        DataList.clear()
        for item in row:
            list = item.childNodes
            for lis in list:
                if lis.nodeName == 'addr1':
                    #print('주소: ',lis.firstChild.nodeValue)
                    DataList.append(lis.firstChild.nodeValue)
                    #RenderText.insert(END, '주소: ')
                    #RenderText.insert(END, lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '\n')
                if lis.nodeName == 'addr2':
                    #print('주소: ',lis.firstChild.nodeValue)
                    pass
                if lis.nodeName == 'firstimage':
                    #print('사진1: ',lis.firstChild.nodeValue)
                    DataList.append(lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '사진1 : ')
                    #RenderText.insert(list_count, lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '\n')
                if lis.nodeName == 'tel':
                    #print('전화번호: ',lis.firstChild.nodeValue)
                    DataList.append(lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '연락처: ')
                    #RenderText.insert(list_count, lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '\n')
                if lis.nodeName == 'title':
                    #print('시설명: ',lis.firstChild.nodeValue)
                    DataList.append(lis.firstChild.nodeValue)
                    RenderText.insert(END, lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '시설명: ')
                    #RenderText.insert(list_count, lis.firstChild.nodeValue)
                    #RenderText.insert(list_count, '\n\n')
    else:
        print("Error!")


def SearchWhere2():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("api.visitkorea.or.kr")
    encText = urllib.parse.quote("서울")
    url = "/openapi/service/rest/KorService/searchKeyword?ServiceKey=vI6iJQ67m77QdQNRKPolJItYH7UHkXtO5gb7xohugYFEwoSQueRopRItR%2BxijJqtggX3PvDvMYm2vPRotrTN4g%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&MobileOS=ETC&pageNo=1&numOfRows=10&listYN=Y&arrange=A&contentTypeId=12&keyword="
    conn.request("GET", url + encText, None)
    req = conn.getresponse()
    global DataList
    DataList.clear()




def InitRenderText():
    global RenderText

   # RenderTextScrollbar =Scrollbar(g_Tk)
    #RenderTextScrollbar.pack()
    #RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Listbox(g_Tk, width=40, height=30, borderwidth=12, relief='ridge')
    #RenderText = Text(g_Tk, width=30, height=27, borderwidth=12, relief='ridge')
                      #,yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=800, y=215)
    #RenderTextScrollbar.config(command= RenderText.yview)
    #RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)

    RenderText.configure(state = 'disabled')




InitTopText()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitSelectLabel()

g_Tk.mainloop()