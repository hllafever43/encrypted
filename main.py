# import pygame module in this program
import pygame, random
from pygame.locals import *
  
# initiate pygame
pygame.init()
  
# define colors
black = pygame.Color('0x000000')
white = pygame.Color('0xFFFFFF')
green = pygame.Color('0x00FF00')
  
# set window size
X = 900
Y = 500
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('Encryption')
  
# set background
image = pygame.image.load("background_image.png")
image = pygame.transform.scale(image, (900, 625))

# set fonts
pygame.font.init()
smallfont = pygame.font.SysFont('couriernew', 16)
midfont = pygame.font.SysFont('couriernew', 20)
largefont = pygame.font.SysFont('couriernew', 30)
titlefont = pygame.font.SysFont('couriernew', 100)

stage = "title"
userinput = ""
guess_length = 0
word_length = 0
Letters_array = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
bi_numbers = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001"]
nextstage = False 
rotate = 0

def unlockstage():
    return True

def relockstage():
    return False

def dec_rotate(rotate):
    if rotate == 0:
        rotate = 25
    else:
        rotate -= 1
    return rotate

def inc_rotate(rotate):
    if rotate == 25:
        rotate = 0
    else:
        rotate += 1
    return rotate

def makeNote(surface, text, color, rect, font, aa=False, bkg=None):
    y = rect.top + 10
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width-20 and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left+10, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def draw_borders(s, x, y, w, h, bw, c, word, stage, userinput): #surface, x, y, width, height, border width, color
    if stage == "one":
        letters = [word[i:i+2] for i in range(0, len(word), 2)]
        center = ((w+bw)*(len(letters))/2)
        
        for i in range(len(letters)):
            letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50,w,h)) 
            code = largefont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+(540/2) - center + 7,y+59))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+(540/2) - center + 16,y+59+bw+h))   
    
    if stage == "two":
        letters = [word[i:i+5] for i in range(0, len(word), 5)]
        center = ((w+bw)*(len(letters))/2)
        
        for i in range(len(letters)):
            letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50,w,h)) 
            code = smallfont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+(540/2) - center + 5,y+65))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+(540/2) - center + 20,y+59+bw+h))

    if stage == "three":
        letters = list(word)
        center = ((w+bw)*(len(letters))/2)
        
        for i in range(len(letters)):
            letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50,w,h)) 
            code = largefont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+(540/2) - center + 17,y+59))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+(540/2) - center + 16,y+59+bw+h))   

    if stage == "four":
        letters = [word[i:i+2] for i in range(0, len(word), 2)]
        center = ((w+bw)*(len(letters))/2)
        
        for i in range(len(letters)):
            letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50,w,h)) 
            code = largefont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+(540/2) - center + 7,y+59))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(540/2) - center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+(540/2) - center + 16,y+59+bw+h))  

    if stage == "five":
        words = list(word)
        letters1 = []
        letters2 = []
        for i in words:
            for j in i:
                if words.index(i) < 3:
                    letters1.append(j)
                else:
                    letters2.append(j)
            #if words.index(i) < 3:
                #letters1.append(" ")
        center1 = ((w+bw)*(len(letters1))/2)
        center2 = ((w+bw)*(len(letters2))/2)
        count = 0

        for i in range(len(letters1)):
            if letters1[i] != " ":
                    letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(870/2) - center1,y+20,w,h)) 
                    code = midfont.render(letters1[i], False, green)
                    display_surface.blit(code, (x+(bw+w)*i+(870/2) - center1 + 7,y+29))
                    guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+870/2 - center1,y+20+bw+h,w,h)) 
                    if i < len(userinput) and  len(userinput) <= len(letters1):
                        guess = largefont.render(userinput[i], False, white)
                        display_surface.blit(guess, (x+(bw+w)*i+(870/2) - center1 + 16,y+29+bw+h)) 
            
        
        for i in range(len(letters2)):
            letterbox = pygame.draw.rect(s, black,(x+(bw+w)*i+(870/2) - center2,y+140,w,h)) 
            code = midfont.render(letters2[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+(870/2) - center2 + 7,y+149))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+870/2 - center2,y+140+bw+h,w,h)) 
            if i < len(userinput) and letters2[i] != " " and len(userinput) >= len(letters1):
                for j in range(len(letters1)):
                    guess = largefont.render(userinput[j], False, white)
                    display_surface.blit(guess, (x+(bw+w)*j+(870/2) - center1 + 16,y+29+bw+h))
                guess = largefont.render(userinput[i + len(letters1) - 2], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+(870/2) - center2 + 16,y+140+bw+h)) 

            


def draw_helpbox(s, x, y, w, h, bw, c, stage): #surface, x, y, width, height, border width, color
    center = ((w+bw)*(len(letters))/2)
    
    if stage == "one":
        for i in range(len(letters)):
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40,w,h)) 
            numberboxes = midfont.render(numbers[i], False, green)
            display_surface.blit(numberboxes, (x+(bw+w)*i+(20) + 4,y+45))
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40+bw+h,w,h)) 
            letterboxes = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes, (x+(bw+w)*i+(22) + 8,y+45+bw+h))

    if stage == "two":
        j = 0
        k = 0
        for i in range(len(letters)):
            if i%5 == 0:
                j += 1
                k = 0
            pygame.draw.rect(s, black,((x-100+j*50)+(bw+w+50)*j,y-35+(h+bw)*k,w,h))
            letterboxes = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes,((x-100+j*50)+(bw+w+50)*j+8,y-35+(h+bw)*k+5))
            pygame.draw.rect(s, black,((x-100+j*50)+(bw+w+50)*j+35,y-35+(h+bw)*k,w*2+10,h))
            numberboxes = midfont.render(bi_numbers[i], False, green)
            display_surface.blit(numberboxes, ((x-100+j*50)+(bw+w+50)*j+35+5,y-35+(h+bw)*k+5))
            k += 1

    if stage == "three":
        for i in range(len(letters)):
            spin = (i+rotate)%25
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40,w,h)) 
            letterboxes1 = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 8,y+45))
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40+bw+h,w,h)) 
            letterboxes2 = midfont.render(letters[spin], False, white)
            display_surface.blit(letterboxes2, (x+(bw+w)*i+(22) + 8,y+45+bw+h))

    if stage == "four":
        for i in range(len(letters)):
            spin = (i+rotate)%25
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20,w,h)) 
            letterboxes1 = midfont.render(numbers[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 2,y+25))
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20+bw+h,w,h)) 
            letterboxes1 = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 8,y+25+bw+h))
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20+bw*2+h*2,w,h)) 
            letterboxes2 = midfont.render(letters[spin], False, white)
            display_surface.blit(letterboxes2, (x+(bw+w)*i+(22) + 8,y+25+bw*2+h*2))



list1 = [["the", "kitchen", [["in the", "cabinet"], ["in the", "fridge"], ["in the", "drawer"], ["in the", "freezer"], ["in the", "pantry"]]], ["the", "dining", [["under the", "table"], ["under the", "rug"], ["under the", "chair"], ["under the", "placemat"], ["under the", "vase"]]], ["the", "living", [["under the", "table"], ["under the", "rug"], ["under the", "chair"], ["under the", "lamp"], ["under the", "couch"]]], ["your", "bedroom", [["under the", "pillow"], ["in the", "dresser"], ["in the", "closet"], ["in the", "bookcase"], ["under the", "bed"]]]]

list2 = [["the", "shed", [["in the", "toolbox"], ["on your", "bicycle"], ["behind the", "shovel"]]], ["the", "yard", [["in the", "bushes"], ["in the", "flowers"], ["on the", "appletree"]]], ["the", "garden", [["in the", "tomatoes"], ["in the", "lettuce"], ["in the", "pumpkins"]]], ["the", "doghouse", [["on the", "side"], ["on the", "roof"], ["on the", "back"]]], ["the", "porch", [["under the", "table"], ["on the", "chair"], ["behind the", "plant"]]]]

list3 = [["look", "under", "the", "doormat"], ["look", "at", "the", "computer"], ["look", "in", "your", "backpack"], ["look", "in", "your", "shoes"], ["look", "in", "your", "desk"], ["look", "under", "the", "tv"], ["look", "in", "the", "washer"], ["look", "in", "the", "dryer"], ["look", "in", "the", "microwave"]]


#randomlist = ["six random numbers"] #four for choosing words to encode/scramble, two for the Caesar ciphers
#randomlist[0] = random function (repeat for each index num)

#separate page for puzzle setup? creates a single array [[puzzle, answer, response] * 5]
#   would include lists, random num stuff,
randnum_one = random.randint(0,3)
randnum_two = random.randint(0, 4) 
randnum_three = random.randint(0, 4)
randnum_four = random.randint(0, 2)
randnum_five = random.randint(0, 4)
randnum_six = random.randint(1,25)
randnum_seven = random.randint(1, 25)

answer_one = list1[randnum_one][1]
code_one = ""
for i in answer_one:
    index = letters.index(i.upper())
    code_one = code_one + numbers[index]
puzzle_one = list1[randnum_one][0]
if answer_one == "living" or answer_one == "dining":
    room = " room"
else:
    room = ""

print(answer_one)

answer_two = list1[randnum_one][2][randnum_two][1]
code_two = ""
for i in answer_two:
    index = letters.index(i.upper())
    code_two = code_two + bi_numbers[index]
puzzle_two = list1[randnum_one][2][randnum_two][0] 

print(answer_two)

answer_three = list2[randnum_three][1]
puzzle_three = list2[randnum_three][0]
code_three = ""
for i in answer_three:
    index = letters.index(i.upper())
    index = (index + randnum_six) % 25
    code_three = code_three + letters[index]
puzzle_three = list2[randnum_three][0] 
print(answer_three)

answer_four = list2[randnum_three][2][randnum_four][1]
puzzle_four = list2[randnum_three][2][randnum_four][0]
code_four = ""
for i in answer_four:
    index = letters.index(i.upper())
    index = (index + randnum_seven) % 25
    code_four = code_four + numbers[index]

print(answer_four)

answer_five = list3[randnum_five]
code_five = [[], [], [], []]
for i in answer_five:
        print(i)
        l = list(i)
        print(l)
        code_five[answer_five.index(i)] = random.sample(l, len(l))
        #code_five[i] = random.sample(i, len(i))
print(answer_five)
print(code_five)

# infinite loop
while True :
    while stage == "title":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))

        pygame.draw.rect(display_surface, black,(X/2-300,Y/2-125,600,250))
        title = titlefont.render('ENCRYPTED', False, white)
        display_surface.blit(title, (X/2-270,Y/2-90))

        if X/2-185+130 > mouse[0] > X/2-185 and Y/2+30+50 > mouse[1] > Y/2+30:
            pygame.draw.rect(display_surface, white,(X/2-185,Y/2+30,130,50))        
            exitbutton = largefont.render('x exit', False, black)
            display_surface.blit(exitbutton, (X/2-175,Y/2+40))

            if click[0] == 1:
                pygame.quit()
                quit() 
        else:
            pygame.draw.rect(display_surface, black,(X/2-185,Y/2+30,130,50))        
            exitbutton = largefont.render('x exit', False, white)
            display_surface.blit(exitbutton, (X/2-175,Y/2+40))

        if X/2+15+150 > mouse[0] > X/2+15 and Y/2+30+50 > mouse[1] > Y/2+30:
            pygame.draw.rect(display_surface, white,(X/2+15,Y/2+30,150,50)) 
            startbutton = largefont.render('start >', False, black)
            display_surface.blit(startbutton, (X/2+25,Y/2+40))
            if click[0] == 1:
                stage = "intro"
        else:
            pygame.draw.rect(display_surface, black,(X/2+15,Y/2+30,150,50)) 
            startbutton = largefont.render('start >', False, white)
            display_surface.blit(startbutton, (X/2+25,Y/2+40))
    
        pygame.display.update()

    while stage == "intro":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))

        box = pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))
        makeNote(display_surface, "One hot summer day, you feel terribly bored. Your friends and siblings are all busy. It's too hot to play outside and there's nothing interesting to do inside. So, with nothing else to do, you sit on the couch and idly watch tv. Then the doorbell rings. You stand up and go to answer it. hoping it'll be one of your friends. But when you open the door...no one is there. There's only an envelope laying on the doormat. You look around, pick it up, and open it:", white, box, smallfont)

        notebox = pygame.draw.rect(display_surface, white, (X/2 - 250, Y/2 - 90, 500, 220))
        makeNote(display_surface, "Hey, kiddo. Since you've been bored for a couple days now, I figured I would try to help make your summer break more interesing. Do you want to play a game? I've made a few puzzles and hidden them around the house. If you can solve the puzzle on each note, you'll win a prize. If you want to play, the next note is in the " + code_one + room + ". Love, Dad :)", black, notebox, smallfont)

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            nextstage = unlockstage()
            if click[0] == 1 and nextstage == True:
                stage = "one"
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()

    while stage == "one":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == K_BACKSPACE and nextstage == False:
                    if len(userinput) > 0:
                        userinput = userinput[:-1]
                        guess_length -= 1
                        print(userinput)

                if event.key in Letters_array and guess_length < word_length:
                    userinput = userinput + pygame.key.name(event.key)
                    guess_length += 1
                    print(userinput)

        word_length = len(answer_one)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "Those numbers... " + code_one + room + ". It looks like it's some kind of code? In the envelope, you find another piece of paper with a line of letters and numbers - maybe it can help you decode the word?", black, notebox, smallfont)

        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-25), 30, 30, 2, black, stage)
        helptext = smallfont.render("Use this key to change numbers into letters", False, black)
        display_surface.blit(helptext, (X/2-205,Y/2-20))


        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        #makeNote(display_surface, "Type to try decoding it", black, codebox, smallfont)
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))


        draw_borders(display_surface, (X/2-110), (Y/2-230), 50, 50, 3, green, code_one, stage, userinput)

        if userinput == answer_one:
            nextstage = unlockstage()

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            if click[0] == 1 and nextstage == True:
                stage = "two"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()
    
    while stage == "two":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == K_BACKSPACE and nextstage == False:
                    if len(userinput) > 0:
                        userinput = userinput[:-1]
                        guess_length -= 1
                        print(userinput)

                if event.key in Letters_array and guess_length < word_length:
                    userinput = userinput + pygame.key.name(event.key)
                    guess_length += 1
                    print(userinput)

        word_length = len(answer_two)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "You go to the " + answer_one + room + ". There's an envelope on the floor. You pick it up and read: Nice work! You solved the first puzzle! Now for the next one - it's similar to the last one but uses \"binary\" numbers instead. In this room, look " + puzzle_two + " " + code_two, black, notebox, smallfont)

        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2+25), 30, 30, 2, black, stage)

        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))

        draw_borders(display_surface, (X/2-110), (Y/2-230), 60, 50, 3, green, code_two, stage, userinput)

        if userinput == answer_two:
            nextstage = unlockstage()

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            if click[0] == 1 and nextstage == True:
                stage = "three"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()


    while stage == "three":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == K_BACKSPACE and nextstage == False:
                    if len(userinput) > 0:
                        userinput = userinput[:-1]
                        guess_length -= 1
                        print(userinput)

                if event.key in Letters_array and guess_length < word_length:
                    userinput = userinput + pygame.key.name(event.key)
                    guess_length += 1
                    print(userinput)

        word_length = len(answer_three)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "You look " + puzzle_two + " " + answer_two + " and see another envelope. Opening it, you read: Doing great, kiddo! Let's make things a bit more complicated. Go to the " + code_three + " to look for the next puzzle :)" , black, notebox, smallfont)

        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-20), 30, 30, 2, black, stage)
        helptext = smallfont.render("Click the arrows until you find the correct key, then use it to solve the code", False, black)
        display_surface.blit(helptext, (X/2-395,Y/2-20))

        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))

        draw_borders(display_surface, (X/2-110), (Y/2-230), 50, 50, 3, green, code_three, stage, userinput)

        if X/2-315-40 < mouse[0] < X/2-315 and Y/2+110+40 > mouse[1] > Y/2+110:
            pygame.draw.rect(display_surface, white,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, black)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))
            if click[0] == 1 and nextstage == False:
                rotate = dec_rotate(rotate)
                pygame.time.wait(400)
                print(rotate)
        else:
            pygame.draw.rect(display_surface, black,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, white)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))

        if X/2+315+40 > mouse[0] > X/2+315 and Y/2+110+40 > mouse[1] > Y/2+110:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, black)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))
            if click[0] == 1 and nextstage == False:
                rotate = inc_rotate(rotate)
                pygame.time.wait(400)
                print(rotate)
        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, white)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))

        if userinput == answer_three:
            nextstage = unlockstage()
        
        if X/2-315-120 < mouse[0] < X/2-315 and Y/2+180+50 > mouse[1] > Y/2+180:
            pygame.draw.rect(display_surface, white,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, black)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))
            if click[0] == 1:
                hint = midfont.render("The first letter is " + answer_three[0], False, white)
                display_surface.blit(hint, (X/2-305,Y/2+195))

        else:
            pygame.draw.rect(display_surface, black,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, white)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            if click[0] == 1 and nextstage == True:
                stage = "four"
                userinput = ""
                guess_length = 0
                rotate = 0
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()

    while stage == "four":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == K_BACKSPACE and nextstage == False:
                    if len(userinput) > 0:
                        userinput = userinput[:-1]
                        guess_length -= 1
                        print(userinput)

                if event.key in Letters_array and guess_length < word_length:
                    userinput = userinput + pygame.key.name(event.key)
                    guess_length += 1
                    print(userinput)

        word_length = len(answer_four)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "Those numbers..." + answer_one + ". It looks like it's some kind of code? In the envelope, you find another piece of paper with a line of letters and numbers - maybe it can help you decode the word?", black, notebox, smallfont)

        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-30), 30, 30, 2, black, stage)

        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))

        draw_borders(display_surface, (X/2-110), (Y/2-230), 50, 50, 3, green, code_four, stage, userinput)

        if X/2-315-40 < mouse[0] < X/2-315 and Y/2+110+40 > mouse[1] > Y/2+110:
            pygame.draw.rect(display_surface, white,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, black)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))
            if click[0] == 1 and nextstage == False:
                rotate = dec_rotate(rotate)
                pygame.time.wait(400)
                print(rotate)
        else:
            pygame.draw.rect(display_surface, black,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, white)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))

        if X/2+315+40 > mouse[0] > X/2+315 and Y/2+110+40 > mouse[1] > Y/2+110:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, black)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))
            if click[0] == 1 and nextstage == False:
                rotate = inc_rotate(rotate)
                pygame.time.wait(400)
                print(rotate)
        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, white)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))

        if userinput == answer_four:
            nextstage = unlockstage()

        if X/2-315-120 < mouse[0] < X/2-315 and Y/2+180+50 > mouse[1] > Y/2+180:
            pygame.draw.rect(display_surface, white,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, black)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))
            if click[0] == 1:
                hint = midfont.render("The first letter is " + answer_four[0], False, white)
                display_surface.blit(hint, (X/2-305,Y/2+195))

        else:
            pygame.draw.rect(display_surface, black,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, white)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            if click[0] == 1 and nextstage == True:
                stage = "five"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()
    
    while stage == "five":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == K_BACKSPACE and nextstage == False:
                    if len(userinput) > 0:
                        userinput = userinput[:-1]
                        guess_length -= 1
                        print(userinput)

                if event.key in Letters_array and guess_length < word_length:
                    userinput = userinput + pygame.key.name(event.key)
                    guess_length += 1
                    print(userinput)

        word_length = 0
        for i in answer_five:
            word_length += len(i)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,870,145))
        makeNote(display_surface, "Those numbers..." + answer_one + ". It looks like it's some kind of code? In the envelope, you find another piece of paper with a line of letters and numbers - maybe it can help you decode the word?", black, notebox, smallfont)

        codebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-80,870,255))
        #codetext = smallfont.render("Type to try decoding it", False, black)
        #display_surface.blit(codetext, (X/2+40,Y/2-220))

        draw_borders(display_surface, (X/2-435), (Y/2-80), 50, 50, 3, green, code_five, stage, userinput)

        if userinput == answer_five:
            nextstage = unlockstage()

        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True:
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            if click[0] == 1 and nextstage == True:
                stage = "done"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()

    while stage == "done":
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        stagetext = largefont.render('DONE', False, white)
        display_surface.blit(stagetext, (X/2-100,Y/2))

        if X/2+60 > mouse[0] > X/2-60 and Y/2+180+50 > mouse[1] > Y/2+180:
            pygame.draw.rect(display_surface, white,(X/2-60,Y/2+180,120,50)) 
            nextbutton = largefont.render('done', False, black)
            display_surface.blit(nextbutton, (X/2-35,Y/2+190))
            nextstage = unlockstage()
            if click[0] == 1 and nextstage == True:
                stage = "title"
                nextstage = relockstage()

        else:
            pygame.draw.rect(display_surface, black,(X/2-60,Y/2+180,120,50)) 
            nextbutton = largefont.render('done', False, white)
            display_surface.blit(nextbutton, (X/2-35,Y/2+190))
        
        pygame.display.update()