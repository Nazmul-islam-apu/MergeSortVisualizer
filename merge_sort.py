import pygame
import random


pygame.font.init()

window = pygame.display.set_mode((900,650))
pygame.display.set_caption("Merge Sort Visualizer")
run = True

width = 900
height = 600
array = [0]*151
arr_color = [(0,204,102)]*151
color_ind = 0
color = [(135,206,235),(255,0,0),(0,0,153),(0,204,102)]

font = pygame.font.SysFont("comicsans",30)
font1 = pygame.font.SysFont("comicsans",20)

def generate_new_arr():
    for i in range(1,151):
        arr_color[i] = color[0]
        array[i] = random.randrange(1,100)

generate_new_arr()

def refill():
    window.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)


def merge_sort(array,l,r):
    mid = (l+r)//2
    if l<r:
        merge_sort(array,l,mid)
        merge_sort(array,mid+1,r)
        merge(array,l,mid,mid+1,r)

def merge(arr,x1,y1,x2,y2):
    i = x1
    j = x2
    temp  = []
    pygame.event.pump()
    while i<=y1 and j<=y2:
        arr_color[i] = color[1]
        arr_color[j] = color[1]
        refill()
        arr_color[i] = color[0]
        arr_color[j] = color[0]
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while(i<=y1):
        arr_color[i] = color[1]
        refill()
        arr_color[i] = color[0]
        temp.append(arr[i])
        i+=1
    while(j<=y2):
        arr_color[j] = color[1]
        refill()
        arr_color[j] = color[0]
        temp.append(arr[j])
        j+=1
    j = 0
    for i in range(x1,y2+1):
        pygame.event.pump()
        arr[i] = temp[j]
        j+=1
        arr_color[i] = color[2]
        refill()
        if y2-x1 == len(arr)-2:
            arr_color[i] = color[3]
        else:
            arr_color[i] = color[0]


def draw():
    text = font.render("Press 'Enter' to start the sorting",1,(0,0,0))
    window.blit(text,(20,20))
    text1 = font.render("Press N for new array", 1, (0, 0, 0))
    window.blit(text1,(20,60))
    text2 = font.render("Algorithm: Merge Sort", 1, (0, 0, 0))
    window.blit(text2,(600,60))
    element_width = (width-150)//150
    boundary_arr = 900/150
    boundary_gap = 550/150
    pygame.draw.line(window,(0,0,0),(0,95),(900,95),6)
    for i in range(1,100):
        pygame.draw.line(window,(224, 224, 224),(0, boundary_gap * i + 100),(900, boundary_gap * i + 100), 1)

    for i in range(1, 151):
        pygame.draw.line(window, arr_color[i],(boundary_arr * i - 3, 100),(boundary_arr * i - 3, array[i] * boundary_gap + 100),element_width)


while run:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                generate_new_arr()
            if event.key == pygame.K_RETURN:
                merge_sort(array,1,len(array)-1)
    draw()
    pygame.display.update()

pygame.quit()
