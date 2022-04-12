import time
import datetime
import pygame as p
from itertools import cycle
import sys

words=['장암','도봉산','수락산','마들','노원']

#게임에 필요한 변수 초기화
done = False #창끄기 여부
playing=False #게임 여부 확인
cnt=0 #통과한 역 수
msg=0 #민원수 (민원수 3통 되면 게임 오버)
s=[] #set 초기화 (역명을 담는 그릇)
q=''
index=0 #for문 인덱스
typingAcess=False #타이핑권한 불가 초기화
start_time=0 #시작시간 초기화
delay=False #오류나면 딜레이 줌
input_text=''#사용자가 입력하는 값 담음

#게임 초기화면
w=800; y=600

#색상 지정
white=(255,255,255)
ash=(166,166,166)
black=(0,0,0)
blue=(0,112,192)
olive=(116, 127, 0)

p.init()
font_korail = p.font.Font("korailfont.ttf",18) #폰트
clock = p.time.Clock()
screen=p.display.set_mode((w,y)) #화면 사이즈 지정

def draw_text(screen,showText,fontsize,color,x,y):
    font_korail = p.font.Font("korailfont.ttf",18) #폰트
    font=p.font.Font("korailfont.ttf",fontsize)
    text=font.render(showText,True,color)
    text_rect=text.get_rect(center=(x,y))
    screen.blit(text,text_rect)
    p.display.update()
    
def draw_textbg(screen,showText,fontsize,color,bgcolor,x,y):
    font_korail = p.font.Font("korailfont.ttf",18) #폰트
    font=p.font.Font("korailfont.ttf",fontsize)
    text=font.render(showText,True,color,bgcolor)
    text_rect=text.get_rect(center=(x,y))
    screen.blit(text,text_rect)
    p.display.update()

#파일오픈->set에 단어 담음
def get_station():
    fname="seven.txt"
    f=open(fname,"r")
    while True:
        line=f.readline()
        if not line : break
        line=line.strip()
        s.append(line)
        # for event in p.event.get():# User did something
        #     if event.type == p.QUIT:# If user clicked close
        #         done=True # Flag that we are done so we exit this loop
        #         sys.exit() #윈도우창 x 누르면 꺼짐
    f.close()   

def input_station():
    global screen,q,white,olive,index,s,cnt,msg

def msg_img(msg):
    if msg==0 or msg==1:
        #열차내부(기본/1회 미스)
        p.inner_img=p.image.load('.\\img\\greenbg.jpg') 
        p.inner_img=p.transform.scale(p.inner_img,(800,300))
        screen.blit(p.inner_img,(0,118))
        p.display.flip()
    elif msg==2: pass
        #열차내부(2회 미스)
        #p.inner_img=p.image.load('.\\img\\orangebg.jpg').convert()

    elif msg==3: pass
        #열차내부(3회 미스)
        #p.inner_img=p.image.load('.\\img\\redbg.jpg').convert()


def gStart():
    global done, playing,cnt,msg,w,y,white,ash,black,blue,cover_rect,cover_screenWite,start_text,index,q,s,words
    for i in words:
        p.init()
        screen.fill(white)
        
        p.draw.rect(screen,black, [-10,120,820,300],2) #x,y,w,h 열차내부 이미지에다가 테두리 넣어줌
        q=i #i번째 역명 가져옴
        draw_text(screen,q, 30,olive, 390, 90)
        p.display.flip()
        print(q)

        a=input()
        if q==a: 
            cnt+=1;
            print("일치")
            draw_textbg(screen,'\t\t\t\t\t\t\t\t\t\t\t\t\t', 30,white,white, 390, 90)
            p.display.flip()
            draw_text(screen,q, 30,white, 390, 90)   
            p.display.flip()
        else : 
            msg+=1
            msg_img(msg)  
            
          
def run():
    global blink_a,blink_rect,blink_screen,blink_screens,BLINK_EVENT,w,playing,cover_screenWite,cover_rect,white,input_text
    while True:
        for event in p.event.get():# User did something
            if event.type == p.QUIT:# If user clicked close
                done=True # Flag that we are done so we exit this loop
                sys.exit() #윈도우창 x 누르면 꺼짐
            if event.type==p.KEYDOWN:
                if event.key == p.K_RETURN: #엔터 누르면 반환
                    print(input_text) 
        p.display.flip()
        clock.tick(30)  
        
gStart()
run()

p.quit()