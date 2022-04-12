import time
import datetime
import pygame as p
from itertools import cycle
import sys

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
a='' #사용자가 입력한 값을 담는 변수


#게임 초기화면
w=800; y=600

#색상 지정
white=(255,255,255)
ash=(166,166,166)
black=(0,0,0)
blue=(0,112,192)
olive=(116, 127, 0)

p.init()
font_korail = p.font.Font('korailfont.ttf',18) #폰트
clock = p.time.Clock()
screen=p.display.set_mode((w,y)) #화면 사이즈 지정

tmepsize=(200,60)
temp=p.Surface((200,60))
temp.fill(blue)
temp.blit(temp,(390,60))
#깜빡이는 글자만 따로 지정해주기
start_text = font_korail.render('',True,ash)

blink_a=screen
blink_rect=p.draw.rect(screen,black,[100,180,0,0])
blink_screens=blink_rect
blink_screen=blink_rect

BLINK_EVENT = p.USEREVENT + 0 #텍스트 깜박이기 이벤트

#역명 바꿔서 출력
change_a=screen
change_rect=p.draw.rect(screen, white, [200,60,190,20])
change=screens=change_rect
change_screen=change_rect
CHANGESTATION=p.USEREVENT #역명바꾸기
                     
#이전 화면 이미지 텍스트 남은거 지우는 변수
cover_rect=p.draw.rect(screen,white,[100,180,0,0])
cover_screenWite=cover_rect
cover_screenBlack=cover_rect

def draw_text(screen,showText,fontsize,color,x,y):
    font_korail = p.font.Font('korailfont.ttf',18) #폰트
    font=p.font.Font('korailfont.ttf',fontsize)
    text=font.render(showText,True,color)
    text_rect=text.get_rect(center=(x,y))
    screen.blit(text,text_rect)
    p.display.update()
    
def draw_textbg(screen,showText,fontsize,color,bgcolor,x,y):
    font_korail = p.font.Font('korailfont.ttf',18) #폰트
    font=p.font.Font('korailfont.ttf',fontsize)
    text=font.render(showText,True,color,bgcolor)
    text_rect=text.get_rect(center=(x,y))
    screen.blit(text,text_rect)
    p.display.update()

def reset_game():
    global done, playing,cnt,msg,w,y,white,ash,black,blue,screen,blink_a,blink_rect,blink_screen,blink_screens,BLINK_EVENT,start_text
    playing=False; cnt=0; msg=0 #게임 데이터 초기화
    
    screen.fill(black)
    p.display.set_caption("Subway Typing Game") #윈도우 창 타이틀

    #초기화면 게임 타이틀
    p.title_img=p.image.load('.\\img\\title2.png') 
    p.title_img=p.transform.scale(p.title_img,(500,120))
    screen.blit(p.title_img,(w/5,50))

    #초기화면 중앙 게일방법설명상자
    # screen,showText,fontsize,color,x,y

    p.draw.rect(screen, ash, [100,180,600,300]) #x,y,w,h

    draw_text(screen, '기관사가 되어 지하철을 정시 운행하자', 18, blue, 400, 220)
    draw_text(screen, '조금이라도 실수하면... 연착의 시작!', 18, blue, 400, 250)
    draw_text(screen, '[게임 방법]', 18, white, 400, 300)
    draw_text(screen, '1. 나타나는 역명을 순서대로 입력해준다', 18, white, 400, 350)
    draw_text(screen, '2. 역명과 다르게 입력할 경우 열차 운행이 지연된다', 18, white, 400, 380)
    draw_text(screen, '3. 승객의 민원이 3번 접수 되면 게임 종료', 18, white, 400, 410)

    #텍스트 깜박이게 하기위해서
    start_text = font_korail.render('[PRESS SPACEBAR TO START]',True,ash)
    screen.blit(start_text, (w/3,520))

    #blink_rect x, y
    b_x=398; b_y=530
    blink_rect=start_text.get_rect()
    blink_rect.center=(b_x,b_y)
    off_text_screen=p.Surface(blink_rect.size)
    blink_screens=cycle([start_text,off_text_screen])
    blink_screen=next(blink_screens)
    p.time.set_timer(BLINK_EVENT, 1000)
    # blink()

#파일오픈->set에 단어 담음
def get_station():
    fname="seven.txt"
    f=open(fname,"r")
    while True:
        line=f.readline()
        if not line : break
        line=line.strip()
        s.append(line)
    f.close()   

def input_station():
    global screen,q,white,olive,index,s,cnt,msg

def msg_img(msg):
    if msg==0:
        #열차내부(기본/1회 미스)
        p.inner_img=p.image.load('.\\img\\greenbg.jpg') 
        p.inner_img=p.transform.scale(p.inner_img,(800,300))
        screen.blit(p.inner_img,(0,118))
    elif msg==1:
        #열차내부(기본/1회 미스)
        p.inner_img=p.image.load('.\\img\\greenbg.jpg').convert()
        draw_text(screen, '1\t', 18,ash, 700, 40)
    elif msg==2:
        #열차내부(2회 미스)
        p.inner_img=p.image.load('.\\img\\orangebg.jpg').convert()
        draw_text(screen, '2\t', 18,ash, 730, 40)
        # p.inner_img=p.transform.scale(p.inner_img,(800,300))
        # screen.blit(p.inner_img,(0,118))
    elif msg==3:
        #열차내부(3회 미스)
        p.inner_img=p.image.load('.\\img\\redbg.jpg').convert()
        draw_text(screen, '3\t', 18,ash, 760, 40)
        # p.inner_img=p.transform.scale(p.inner_img,(800,300))
        # screen.blit(p.inner_img,(0,118))
        #showreselt() 결과창 보여줌

def again(q):
    global cnt,index,msg
    print("------#"+q+"역에서 정상회복을 위해 노력을 다할 예정입니다...-----")
    print(q)
    a=input()
    if q==a: #퀴즈와 정답이 일치
        print("회복운행 중입니다")
        cnt += 1  
        index+=1  
    else: #틀리면 같은 문제 다시 호출
        msg+=1
        msg_img(msg)
        print("둔갑운행을 할 예정입니다")
        print(msg)
        again(q)

def gStart():
    global done, playing,cnt,msg,w,y,white,ash,black,blue,cover_rect,cover_screenWite,start_text,index,q
    p.init()
    screen.fill(white)
    
    draw_text(screen, '통과한 역\t', 18,ash, 60, 40)
    draw_text(screen, '민원\t', 18,ash, 660, 40)
    
    # draw_text(screen, '1\t', 18,ash, 700, 40)
    # draw_text(screen, '2\t', 18,ash, 730, 40)
    # draw_text(screen, '3\t', 18,ash, 760, 40)
    
    p.draw.rect(screen,black, [-10,120,820,300],2) #x,y,w,h 열차내부 이미지에다가 테두리 넣어줌

    p.inner_img=p.image.load('.\\img\\greenbg.jpg') 
    p.inner_img=p.transform.scale(p.inner_img,(800,300))
    screen.blit(p.inner_img,(0,118))
    
    #역무원 이미지
    p.traine_img=p.image.load('.\\img\\traine.png') 
    p.traine_img=p.transform.scale(p.traine_img,(160,200))
    screen.blit(p.traine_img,(20,420))
    
    #역 표시
    p.draw.rect(screen,black, [-10,60,820,60],2) #x,y,w,h
    draw_text(screen, '이번역은\t\t\t\t\t\t\t\t\t\t\t\t\t\t역입니다.', 30,black, 400, 90)
    #screen.fill(white,[200,60,190,20])
            
    #p.draw.rect(screen,black, [-10,120,820,300],2) #x,y,w,h 열차내부 이미지에다가 테두리 넣어줌

    #역무원 이미지
    p.traine_img=p.image.load('.\\img\\traine.png') 
    p.traine_img=p.transform.scale(p.traine_img,(160,200))
    screen.blit(p.traine_img,(20,420))
    
    #타이핑하는상자
    p.draw.rect(screen,black,(230,480,500,60))
    
    get_station()
    for i in range(len(s)):
        index=i
        q=s[index] #i번째 역명 가져옴
        draw_text(screen,q, 30,olive, 390, 90)
        print(q)
        
        a=input()
        if a==q: 
            cnt+=1; i+=1;
            #screen.fill(white,[200,60,390,90])
            draw_textbg(screen,'\t\t\t\t\t\t\t\t\t\t\t\t\t', 30,white,white, 390, 90)
            print("일치")
            #screen.fill(white)
            draw_text(screen,q, 30,white, 390, 90)
            
            #  #blink_rect x, y
            # b_x=398; b_y=530
            # blink_rect=start_text.get_rect()
            # blink_rect.center=(b_x,b_y)
            # off_text_screen=p.Surface(blink_rect.size)
            # blink_screens=cycle([start_text,off_text_screen])
            # blink_screen=next(blink_screens)
            # p.time.set_timer(BLINK_EVENT, 1000)
            
            #역명 바꿔서 출력
            # change_a=screen
            # change_rect=p.draw.rect(screen, white, [200,60,190,20])
            # change=screens=change_rect
            # change_screen=change_rect
            # CHANGESTATION=p.USEREVENT #역명바꾸기
            
        elif a!=q:
            msg+=1
            msg_img(msg)
            print(msg)
            again(q)     
        
    # for i in range(len(s)):
    #     index=i
    #     q=s[index] #i번째 역명 가져옴
    #     draw_text(screen,q, 30,olive, 390, 90)
    #     print(q)
   
    #     a=input()
    #     if q==a: 
    #         cnt+=1; i+=1;
    #         #screen.fill(white,[200,60,390,90])
    #         #draw_textbg(screen,'\t\t\t\t\t\t\t\t\t\t\t\t\t', 30,white,white, 390, 90)
    #         draw_text(screen,q, 30,white, 390, 90)
            
    #     else : 
    #         msg+=1
    #         msg_img(msg)

   
   #p.draw.rect(screen, ash, [100,180,600,300]) #x,y,w,h
    #draw_text(screen,'가산디지털단지' , 30,olive,390, 90)
    #draw_text(screen,'상봉' , 30,olive,390, 90)

    #p.draw.rect(screen,black, [-10,120,820,300],2) #x,y,w,h
    # p.inner_img=p.image.load('.\\img\\greenbg.jpg') 
    # p.inner_imge_img=p.transform.scale(p.inner_img,(200,200))
    # screen.blit(p.inner_img,(0,118))
  

    # b_x=398; b_y=530
    # cover_rect=start_text.get_rect()
    # cover_rect.center=(b_x,b_y)
    
def run():
    global blink_a,blink_rect,blink_screen,blink_screens,BLINK_EVENT,w,playing,cover_screenWite,cover_rect,white
    p.init()
    while True:
        for event in p.event.get():# User did something
            if event.type == p.QUIT:# If user clicked close
                done=True # Flag that we are done so we exit this loop
                sys.exit() #윈도우창 x 누르면 꺼짐
            if event.type == BLINK_EVENT:
                blink_screen=next(blink_screens)
                blink_a.blit(blink_screen,blink_rect)
                p.display.flip()
            if event.type==p.KEYDOWN:
                if event.key==p.K_SPACE: #스페이스바 누르면
                    screen.fill(white)
                    #draw_text(screen, '스페이스바 눌린거 맞다~', 18, white, 400, 500)
                    playing=True
                    # cover_screenWite=p.Surface((cover_rect.size))
                    # screen.blit(cover_screenWite,cover_rect)
                    # p.draw.rect(screen,white, [400,600,800,600])
                    # p.display.flip()
                    gStart()
                    # #입력창 위치 받아옴
                    # if event.type==p.MOUSEBUTTONUP:
                    #     x_pos,y_pos=p.mouse.get_pos()
                    #     print(x_pos); print(y_pos)
                    #     #입력창 설정
                    #         #p.draw.rect(screen,black,(230,480,500,60))
                    #     if(x_pos>=230 and x_pos<=730 and y_pos>=480 and y_pos<=540):
                    #         typingAcess=True
                    #         input_text=''
                    #         start_time=time.time()
                    #         if event.type==p.KEYDOWN:
                    #             if typingAcess and not delay:
                    #                 if event.key == p.K_RETURN: #엔터 누르면 반환
                    #                     print(input_text)
                    #                     # if q==input_text:
                    #                     #     cnt+=1
                    #                     #     i+=1
                    #                     # else:
                    #                     #     msg+=1       
        p.display.update()
        p.display.flip()
        clock.tick(60)  
        
reset_game()
run()

p.quit()

#1. 한글은 입력 받을 수 없음
#2. 제시 단어를 순서대로 하나씩 읽어오면 --> 창이 얼어버림