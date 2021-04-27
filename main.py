#***basic setup for the game***

# import pygame module in this program
import pygame, random, math
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
display_surface = pygame.display.set_mode((X, Y))
  
# set the pygame window name
pygame.display.set_caption('Encrypted')
  
#set background (purchased from https://www.vectorstock.com/royalty-free-vector/streaming-binary-code-background-vector-22605661)
image = pygame.image.load("background_image.png")
image = pygame.transform.scale(image, (900, 625))

#set fonts
pygame.font.init()
smallfont = pygame.font.SysFont('couriernew', 16)
midfont = pygame.font.SysFont('couriernew', 20)
largefont = pygame.font.SysFont('couriernew', 30)
titlefont = pygame.font.SysFont('couriernew', 100)

#***initialize variables for game***
stage = "title"
userinput = ""
guess_length = 0
word_length = 0
nextstage = False 
rotate = 0

#***set arrays for game***
Letters_array = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
bi_numbers = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001"]
list1 = [["the", "kitchen", [["in the", "cabinet"], ["in the", "fridge"], ["in the", "drawer"], ["in the", "freezer"], ["in the", "pantry"]]], ["the", "dining", [["under the", "table"], ["under the", "rug"], ["under the", "chair"], ["under the", "placemat"], ["under the", "vase"]]], ["the", "living", [["under the", "table"], ["under the", "rug"], ["under the", "chair"], ["under the", "lamp"], ["under the", "couch"]]], ["your", "bedroom", [["under the", "pillow"], ["in the", "dresser"], ["in the", "closet"], ["in the", "bookcase"], ["under the", "bed"]]]]
list2 = [["the", "shed", [["in the", "toolbox"], ["on your", "bicycle"], ["behind the", "shovel"]]], ["the", "yard", [["in the", "bushes"], ["in the", "flowers"], ["on the", "appletree"]]], ["the", "garden", [["in the", "tomatoes"], ["in the", "lettuce"], ["in the", "pumpkins"]]], ["the", "doghouse", [["on the", "side"], ["on the", "roof"], ["on the", "back"]]], ["the", "porch", [["under the", "table"], ["on the", "chair"], ["behind the", "plant"]]]]
list3 = [["look", "under", "the", "doormat"], ["look", "at", "the", "computer"], ["look", "in", "your", "backpack"], ["look", "in", "your", "shoes"], ["look", "in", "your", "desk"], ["look", "under", "the", "tv"], ["look", "in", "the", "washer"], ["look", "in", "the", "dryer"], ["look", "in", "the", "microwave"]]

#***begin puzzle setup***

#generate random numbers to make puzzles
randnum_one = random.randint(0,3)
randnum_two = random.randint(0, 4) 
randnum_three = random.randint(0, 4)
randnum_four = random.randint(0, 2)
randnum_five = random.randint(0, 4)
randnum_six = random.randint(2,24)
randnum_seven = random.randint(2, 24)

#puzzle one
answer_one = list1[randnum_one][1] #the answer
#generate encoded version based off of answer
code_one = ""
for i in answer_one:
    index = letters.index(i.upper())
    code_one = code_one + numbers[index]
puzzle_one = list1[randnum_one][0]
#account for the case that need "room" added to the end in the note
if answer_one == "living" or answer_one == "dining":
    room = " room"
else:
    room = ""

#puzzle two
answer_two = list1[randnum_one][2][randnum_two][1]
#generate encoded version based off of answer
code_two = ""
for i in answer_two:
    index = letters.index(i.upper())
    code_two = code_two + bi_numbers[index]
puzzle_two = list1[randnum_one][2][randnum_two][0] 

#puzzle three
answer_three = list2[randnum_three][1]
puzzle_three = list2[randnum_three][0]
#generate encoded version based off of answer
code_three = ""
for i in answer_three:
    index = letters.index(i.upper())
    index = math.floor((index + 1 + randnum_six) % 26)
    code_three = code_three + letters[index]
puzzle_three = list2[randnum_three][0] 

#puzzle four
answer_four = list2[randnum_three][2][randnum_four][1]
puzzle_four = list2[randnum_three][2][randnum_four][0]
#generate encoded version based off of answer
code_four = ""
for i in answer_four:
    index = letters.index(i.upper())
    index = math.floor((index + 1 + randnum_seven) % 26)
    code_four = code_four + numbers[index]

#puzzle five
answer_five = list3[randnum_five]
code_five = [[], [], [], []]
#generate encoded version based off of answer
for i in answer_five:
        l = list(i)
        code_five[answer_five.index(i)] = random.sample(l, len(l))
#***end puzzle setup***

#function to ture a list into a string for easy display
#parameters: a list (s)
def listToString(s): 
    string = "" 
 
    for elem in s: 
        string += elem 

    return string 

#function to unlock the next stage when correct answer is entered
def unlockstage():
    return True

#function to lock the next stage until the correct answer is entered
def relockstage():
    return False

#function to decrease rotation of caesar cipher key
#parameter: a number (rotate)
def dec_rotate(rotate):
    if rotate == 0:
        rotate = 25
    else:
        rotate -= 1
    return rotate

#function to increase rotation of caeser cipher key
#parameter: a number (rotate)
def inc_rotate(rotate):
    if rotate == 25:
        rotate = 0
    else:
        rotate += 1
    return rotate

#function to make words wrap into a given rectangle
#parameters: pygame surface (surface), the text to display in the rectangle (text), the color of the text (color), the box to wrap the words within (rect), the font for the text (font)
def makeNote(surface, text, color, rect, font):
    #spacing setup
    y = rect.top + 10
    lineSpacing = -2

    # figure out the font's height
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1
        # check if the line of text will fit heightwise
        if y + fontHeight > rect.bottom:
            break

        # find the length of the line
        while font.size(text[:i])[0] < rect.width-20 and i < len(text):
            i += 1

        # if wrap, end on last word     
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # display
        image = font.render(text[:i], False, color)
        surface.blit(image, (rect.left+10, y))
        y += fontHeight + lineSpacing

        # remove already displayed text for the next go
        text = text[i:]
    return text

#function to display contents of codebox
#parameters: surface (s), left of box (x), top of box (y), width of the containing box (boxw), width of box for each letter (w), height of box for each letter (h), border width (bw), border color (c), encoded answer (word), current stage of game (stage), and the user's input (userinput)
def draw_codebox(s, x, y, boxw, w, h, bw, c, word, stage, userinput):

    #different codebox for each stage:
    if stage == "one":
        numbers = [word[i:i+2] for i in range(0, len(word), 2)] #separates numbers
        center = (boxw/2) - ((w+bw)*(len(numbers))/2) #centers boxes
        
        for i in range(len(numbers)):
            #displays coded letters
            codedbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50,w,h)) 
            code = largefont.render(numbers[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+center+7,y+59))
            #display guessed letters from userinput
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+center+16,y+59+bw+h))   
    
    if stage == "two":
        binary_nums = [word[i:i+5] for i in range(0, len(word), 5)] #separates binary numbers
        center = (boxw/2) - ((w+bw)*(len(binary_nums))/2) #centers boxes
        
        for i in range(len(binary_nums)):
            #displays coded letters
            codedbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50,w,h)) 
            code = smallfont.render(binary_nums[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+center+5,y+65))
            #display guessed letters from userinput
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+center+20,y+59+bw+h))

    if stage == "three":
        letters = list(word) #separates letters
        center = (boxw/2) - ((w+bw)*(len(letters))/2) #centers boxes
        
        for i in range(len(letters)):
            #displays coded letters
            codedbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50,w,h)) 
            code = largefont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+center+17,y+59))
            #display guessed letters from userinput
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50+bw+h,w,h)) 
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+center+16,y+59+bw+h))   

    if stage == "four":
        letters = [word[i:i+2] for i in range(0, len(word), 2)] #separates letters
        center = (boxw/2) - ((w+bw)*(len(letters))/2) #centers boxes
        
        for i in range(len(letters)):
            #displays coded letters
            codedbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50,w,h)) 
            code = largefont.render(letters[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+center + 7,y+59))
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center,y+50+bw+h,w,h)) 
            #display guessed letters from userinput
            if i < len(userinput):
                guess = largefont.render(userinput[i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+center+16,y+59+bw+h))  

    if stage == "five":
        #separates letters
        words = list(word) #gets letters
        letters1 = [] #row1 letters
        letters2 = [] #row2 letters
        #puts letters in row 1 or row 2 according to which word they're in
        for i in words:
            for j in i:
                if words.index(i) < 3:
                    letters1.append(j.upper())
                else:
                    letters2.append(j.upper())
            letters1.append(" ")
        center1 = (boxw/2) - ((w+bw)*((len(letters1)-1))/2) #centers boxes
        center2 = (boxw/2) - ((w+bw)*(len(letters2))/2) #centers boxes
        count = 0 #used to account for spaces between words in row1

        #displays words in row 1
        for i in range(len(letters1)):
            if letters1[i] != " ":
                #displays coded letters
                codedbox = pygame.draw.rect(s, black,(x+25+(bw+w)*i+center1,y,w,h)) 
                code = largefont.render(letters1[i], False, green)
                display_surface.blit(code, (x+25+(bw+w)*i+center1 + 15,y+9))
                guessbox = pygame.draw.rect(s, black,(x+25+(bw+w)*i+center1,y+bw+h,w,h)) 
                if i-count < len(userinput):
                    guess = largefont.render(userinput[i-count], False, white)
                    display_surface.blit(guess, (x+25+(bw+w)*i+center1 + 16,y+9+bw+h)) 
            else:
                count += 1

        #display words in row2
        for i in range(len(letters2)):
            #displays coded letters
            codedbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center2,y+130,w,h)) 
            code = largefont.render(letters2[i], False, green)
            display_surface.blit(code, (x+(bw+w)*i+center2 + 15,y+139))
            #display guessed letters from userinput
            guessbox = pygame.draw.rect(s, black,(x+(bw+w)*i+center2,y+130+bw+h,w,h)) 
            if i+len(letters1)-count < len(userinput) and len(userinput) <= len(letters2)+len(letters1)-count:
                guess = largefont.render(userinput[len(letters1)-count+i], False, white)
                display_surface.blit(guess, (x+(bw+w)*i+center2 + 16,y+140+bw+h)) 

#function to display contents of helpbox
#parameters: surface (s), left of box (x), top of box (y), width of box for each letter (w), height of box for each letter (h), border width (bw), border color (c), current stage of game (stage)
def draw_helpbox(s, x, y, w, h, bw, c, stage):

    #different helpbox for each stage:
    if stage == "one":
        for i in range(len(letters)): #for each letter in the alphabet
            #display numbers
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40,w,h)) 
            numberboxes = midfont.render(numbers[i], False, green)
            display_surface.blit(numberboxes, (x+(bw+w)*i+(20) + 4,y+45))
            #displays the letters that correspond to the numbers
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40+bw+h,w,h)) 
            letterboxes = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes, (x+(bw+w)*i+(22) + 8,y+45+bw+h))

    if stage == "two":
        #used to manage which column letters go in
        j = 0
        k = 0
        for i in range(len(letters)): #for each letter in the alphabet
            if i%5 == 0: #for every five letters, make a new column
                j += 1
                k = 0
            #displays letters
            pygame.draw.rect(s, black,((x-100+j*50)+(bw+w+50)*j,y-35+(h+bw)*k,w,h))
            letterboxes = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes,((x-100+j*50)+(bw+w+50)*j+8,y-35+(h+bw)*k+5))
            #displays "binary" numbers that correspond to each letter
            pygame.draw.rect(s, black,((x-100+j*50)+(bw+w+50)*j+35,y-35+(h+bw)*k,w*2+10,h))
            numberboxes = midfont.render(bi_numbers[i], False, green)
            display_surface.blit(numberboxes, ((x-100+j*50)+(bw+w+50)*j+35+5,y-35+(h+bw)*k+5))
            k += 1 #increment for each letter added to a column

    if stage == "three":
        for i in range(len(letters)): #for each letter in the alphabet
            spin = (i+rotate)%26 #used to rotate the caeser cipher wheel
            #displays letters of the alphabet
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40,w,h)) 
            letterboxes1 = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 8,y+45))
            #displays letters of the alphabet, moved according to the rotate variable
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+40+bw+h,w,h)) 
            letterboxes2 = midfont.render(letters[spin], False, white)
            display_surface.blit(letterboxes2, (x+(bw+w)*i+(22) + 8,y+45+bw+h))

    if stage == "four":
        for i in range(len(letters)):  #for each letter in the alphabet
            spin = (i+rotate)%26 #used to rotate the caeser cipher wheel
            #displays numbers that correspond to each letter
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20,w,h)) 
            letterboxes1 = midfont.render(numbers[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 2,y+25))
            #displays letters of the alphabet
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20+bw+h,w,h)) 
            letterboxes1 = midfont.render(letters[i], False, green)
            display_surface.blit(letterboxes1, (x+(bw+w)*i+(22) + 8,y+25+bw+h))
            #displays letters of the alphabet, moved according to the rotate variable
            pygame.draw.rect(s, black,(x+(bw+w)*i+(20),y+20+bw*2+h*2,w,h)) 
            letterboxes2 = midfont.render(letters[spin], False, white)
            display_surface.blit(letterboxes2, (x+(bw+w)*i+(22) + 8,y+25+bw*2+h*2))


#***actually running the game***
# infinite loop to keep display
while True :
    #displays title page
    while stage == "title":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT : 
                pygame.quit()
                quit()

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        #displays titlebox and title
        pygame.draw.rect(display_surface, black,(X/2-300,Y/2-125,600,250))
        title = titlefont.render('ENCRYPTED', False, white)
        display_surface.blit(title, (X/2-270,Y/2-90))

        #displays exit button and handles user iteractions with it
        if X/2-185+130 > mouse[0] > X/2-185 and Y/2+30+50 > mouse[1] > Y/2+30: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-185,Y/2+30,130,50))        
            exitbutton = largefont.render('x exit', False, black)
            display_surface.blit(exitbutton, (X/2-175,Y/2+40))
            #if clicked, close game
            if click[0] == 1:
                pygame.quit()
                quit() 
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-185,Y/2+30,130,50))        
            exitbutton = largefont.render('x exit', False, white)
            display_surface.blit(exitbutton, (X/2-175,Y/2+40))

        #displays start button and handles user interactions with it
        if X/2+15+150 > mouse[0] > X/2+15 and Y/2+30+50 > mouse[1] > Y/2+30: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+15,Y/2+30,150,50)) 
            startbutton = largefont.render('start >', False, black)
            display_surface.blit(startbutton, (X/2+25,Y/2+40))
            #if clicked, change to intro stage
            if click[0] == 1:
                stage = "intro"
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+15,Y/2+30,150,50)) 
            startbutton = largefont.render('start >', False, white)
            display_surface.blit(startbutton, (X/2+25,Y/2+40))

        #contiuous display update
        pygame.display.update()

    #displays intro page, explaining the background for the game
    while stage == "intro":
        #ends game if user hits exit button
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))

        #displays box and some background info for the user
        box = pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))
        makeNote(display_surface, "One hot summer day, you feel terribly bored. Your friends and siblings are all busy. It's too hot to play outside and there's nothing interesting to do inside. So, with nothing else to do, you sit on the couch and idly watch tv. Then the doorbell rings. You stand up and go to answer it. hoping it'll be one of your friends. But when you open the door...no one is there. There's only an envelope laying on the doormat. You look around, pick it up, and open it:", white, box, smallfont)

        #displays box with note from father
        notebox = pygame.draw.rect(display_surface, white, (X/2 - 250, Y/2 - 90, 500, 220))
        makeNote(display_surface, "Hey, kiddo. Since you've been bored for a couple days now, I figured I would try to help make your summer break more interesing. Do you want to play a game? I've made a few puzzles and hidden them around the house. If you can solve the puzzle on each note, you'll win a prize. If you want to play, the next note is in the " + code_one + room + ". Love, Dad :)", black, notebox, smallfont)

        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            nextstage = unlockstage()
            #if clicked, move on to next stage
            if click[0] == 1 and nextstage == True:
                stage = "one"
                nextstage = relockstage() #lock the next stage
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update() #continuous display update

    #displays the first page with the first puzzle
    while stage == "one":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            #logs letters when user uses the keyboard
            if event.type == pygame.KEYDOWN :
                #backspace
                if event.key == K_BACKSPACE and nextstage == False: #freezes input when correct answer is entered
                    if len(userinput) > 0: #if userinput has any characters
                        userinput = userinput[:-1] #remove a char from userinput var
                        guess_length -= 1

                #letters
                if event.key in Letters_array and guess_length < word_length: #limits input to only letters and to the length of the answer
                    userinput = userinput + pygame.key.name(event.key) #add letter if valid
                    guess_length += 1

        
        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        #variables for puzzle
        word_length = len(answer_one)

        #display top-left box that contains the exposition/notes with puzzles
        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "Those numbers... " + code_one + room + ". It looks like it's some kind of code? In the envelope, you find another piece of paper with a line of letters and numbers - maybe it can help you decode the word?", black, notebox, smallfont)

        #display bottom box with key for the puzzle
        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-25), 30, 30, 2, black, stage)
        helptext = smallfont.render("Use this key to change numbers into letters", False, black)
        display_surface.blit(helptext, (X/2-205,Y/2-20))

        #display the top-right box with the puzzle and the attempted answers
        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))
        draw_codebox(display_surface, (X/2-110), (Y/2-230), 540, 50, 50, 3, green, code_one, stage, userinput)

        #if the user's input matches the answer, let them go on to the next stage (unlock next button)
        if userinput == answer_one:
            nextstage = unlockstage()

        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            #if clicked, move on to next stage and reset variables
            if click[0] == 1 and nextstage == True:
                stage = "two"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update() #continuous display update
    
    #displays the second page with the second puzzle
    while stage == "two":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            #logs letters when user uses the keyboard
            if event.type == pygame.KEYDOWN :
                #backspace
                if event.key == K_BACKSPACE and nextstage == False: #freezes input when correct answer is entered
                    if len(userinput) > 0: #if userinput has any characters
                        userinput = userinput[:-1] #remove a char from userinput var
                        guess_length -= 1

                #letters
                if event.key in Letters_array and guess_length < word_length: #limits input to only letters and to the length of the answer
                    userinput = userinput + pygame.key.name(event.key) #add letter if valid
                    guess_length += 1

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        #variables for puzzle
        word_length = len(answer_two)

        #display top-left box that contains the exposition/notes with puzzles
        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "You go to the " + answer_one + room + ". There's an envelope on the floor. You pick it up and read: Nice work! You solved the first puzzle! Now for the next one - it's similar to the last one but uses \"binary\" numbers instead. In this room, look " + puzzle_two + " " + code_two, black, notebox, smallfont)

        #display bottom box with key for the puzzle
        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2+25), 30, 30, 2, black, stage)

        #display the top-right box with the puzzle and the attempted answers
        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))
        draw_codebox(display_surface, (X/2-110), (Y/2-230), 540, 60, 50, 3, green, code_two, stage, userinput)

        #if the user's input matches the answer, let them go on to the next stage (unlock next button)
        if userinput == answer_two:
            nextstage = unlockstage()


        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            #if clicked, move on to next stage and reset variables
            if click[0] == 1 and nextstage == True:
                stage = "three"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update() #continuous display update

    #displays the third page with the third puzzle
    while stage == "three":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            #logs letters when user uses the keyboard
            if event.type == pygame.KEYDOWN :
                #backspace
                if event.key == K_BACKSPACE and nextstage == False: #freezes input when correct answer is entered
                    if len(userinput) > 0: #if userinput has any characters
                        userinput = userinput[:-1] #remove a char from userinput var
                        guess_length -= 1

                #letters
                if event.key in Letters_array and guess_length < word_length: #limits input to only letters and to the length of the answer
                    userinput = userinput + pygame.key.name(event.key) #add letter if valid
                    guess_length += 1

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        #variables for puzzle
        word_length = len(answer_three)

        #display top-left box that contains the exposition/notes with puzzles
        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "You look " + puzzle_two + " " + answer_two + " and see another envelope. Opening it, you read: Doing great, kiddo! Let's try a new cipher. This time YOU need to find the right key. You'll probably have to try it a few times before you get it right. Go to the " + code_three + " to look for the next puzzle :)" , black, notebox, smallfont)

        #display bottom box with key for the puzzle
        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-20), 30, 30, 2, black, stage)
        helptext = smallfont.render("Click the arrows until you find the correct key, then use it to solve the code", False, black)
        display_surface.blit(helptext, (X/2-395,Y/2-20))

        #display the top-right box with the puzzle and the attempted answers
        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))
        draw_codebox(display_surface, (X/2-110), (Y/2-230), 540, 50, 50, 3, green, code_three, stage, userinput)

        #displays button to rotate cipher wheel to the left and handles user interaction
        if X/2-315-40 < mouse[0] < X/2-315 and Y/2+110+40 > mouse[1] > Y/2+110: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, black)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))
            #if clicked, move wheel to the left
            if click[0] == 1 and nextstage == False:
                rotate = inc_rotate(rotate)
                pygame.time.wait(400)
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, white)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))

        #displays button to rotate cipher wheel to the right and handles user interaction
        if X/2+315+40 > mouse[0] > X/2+315 and Y/2+110+40 > mouse[1] > Y/2+110: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, black)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))
            #if clicked, move wheel to the right
            if click[0] == 1 and nextstage == False:
                rotate = dec_rotate(rotate)
                pygame.time.wait(400)
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, white)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))

        #if the user's input matches the answer, let them go on to the next stage (unlock next button)
        if userinput == answer_three:
            nextstage = unlockstage()
        
        #displays button to show hint and handles user interaction
        if X/2-315-120 < mouse[0] < X/2-315 and Y/2+180+50 > mouse[1] > Y/2+180: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, black)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))
            #if clicked, show the hint
            if click[0] == 1:
                hint = midfont.render("The first letter is " + answer_three[0], False, white)
                display_surface.blit(hint, (X/2-305,Y/2+195))
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, white)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))

        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            #if clicked, move on to the next stage and reset variables
            if click[0] == 1 and nextstage == True:
                stage = "four"
                userinput = ""
                guess_length = 0
                rotate = 0
                nextstage = relockstage()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update()  #continuous display update

    #displays the fourth page with the fourth puzzle
    while stage == "four":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            #logs letters when user uses the keyboard
            if event.type == pygame.KEYDOWN :
                #backspace
                if event.key == K_BACKSPACE and nextstage == False: #freezes input when correct answer is entered
                    if len(userinput) > 0: #if userinput has any characters
                        userinput = userinput[:-1] #remove a char from userinput var
                        guess_length -= 1

                #letters
                if event.key in Letters_array and guess_length < word_length: #limits input to only letters and to the length of the answer
                    userinput = userinput + pygame.key.name(event.key) #add letter if valid
                    guess_length += 1

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        #variables for puzzle
        word_length = len(answer_four)

        #display top-left box that contains the exposition/notes with puzzles
        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,320,195))
        makeNote(display_surface, "You go and find another envelope: So smart! You're almost there - now you need to look " + puzzle_four + " " + code_four + ". This one is quite tricky, but I think you'll get it. ", black, notebox, smallfont)

        #display bottom box with key for the puzzle
        helpbox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-30,870,200))
        draw_helpbox(display_surface, (X/2-435),(Y/2-30), 30, 30, 2, black, stage)

        #display the top-right box with the puzzle and the attempted answers
        codebox = pygame.draw.rect(display_surface, white, (X/2-110,Y/2-230,545,195))
        codetext = smallfont.render("Type to try decoding it", False, black)
        display_surface.blit(codetext, (X/2+40,Y/2-220))
        draw_codebox(display_surface, (X/2-110), (Y/2-230), 540, 50, 50, 3, green, code_four, stage, userinput)

        #displays button to rotate cipher wheel to the left and handles user interaction
        if X/2-315-40 < mouse[0] < X/2-315 and Y/2+110+40 > mouse[1] > Y/2+110: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, black)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))
            #if clicked, rotate cipher wheel to the left
            if click[0] == 1 and nextstage == False:
                rotate = inc_rotate(rotate)
                pygame.time.wait(400)
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-355,Y/2+110,40,40)) 
            nextbutton = largefont.render('<', False, white)
            display_surface.blit(nextbutton, (X/2-345,Y/2+115))

        #displays button to rotate cipher wheel to the right and handles user interaction
        if X/2+315+40 > mouse[0] > X/2+315 and Y/2+110+40 > mouse[1] > Y/2+110: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, black)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))
            #if clicked, rotate cipher wheel to the left
            if click[0] == 1 and nextstage == False:
                rotate = dec_rotate(rotate)
                pygame.time.wait(400)
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+110,40,40)) 
            nextbutton = largefont.render('>', False, white)
            display_surface.blit(nextbutton, (X/2+325,Y/2+115))

        #if the user's input matches the answer, let them go on to the next stage (unlock next button)
        if userinput == answer_four:
            nextstage = unlockstage()

        #displays button to go to the display the hint and handles user iteractions with it
        if X/2-315-120 < mouse[0] < X/2-315 and Y/2+180+50 > mouse[1] > Y/2+180: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, black)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))
            #if clicked, display the hint
            if click[0] == 1:
                hint = midfont.render("The first letter is " + answer_four[0], False, white)
                display_surface.blit(hint, (X/2-305,Y/2+195))
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-435,Y/2+180,120,50)) 
            nextbutton = largefont.render('hint', False, white)
            display_surface.blit(nextbutton, (X/2-410,Y/2+190))

        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            #if clicked, move on to the next stage and reset variables
            if click[0] == 1 and nextstage == True:
                stage = "five"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update() #continuous display update
    
    #displays the fifth page with the fifth puzzle
    while stage == "five":
        for event in pygame.event.get() :
            #ends game if user hits exit button
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            
            #logs letters when user uses the keyboard
            if event.type == pygame.KEYDOWN :
                #backspace
                if event.key == K_BACKSPACE and nextstage == False: #freezes input when correct answer is entered
                    if len(userinput) > 0: #if userinput has any characters
                        userinput = userinput[:-1] #remove a char from userinput var
                        guess_length -= 1

                #letters
                if event.key in Letters_array and guess_length < word_length: #limits input to only letters and to the length of the answer
                    userinput = userinput + pygame.key.name(event.key) #add letter if valid
                    guess_length += 1

        
        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))

        #variables for puzzle
        word_length = 0
        for i in answer_five:
            word_length += len(i)

        #display top box that contains the exposition/notes with puzzles
        notebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-230,870,115))
        makeNote(display_surface, "You look " + puzzle_four + " " + answer_four + " and find yet another envelope. The note inside of it says: Okay, this is the last one. It's a bit different from the others, but you can do this: " + listToString(code_five[0]) + " " +  listToString(code_five[1]) + " " +  listToString(code_five[2]) + " " +  listToString(code_five[3]) + ". Unscramble the letters to know where to go to find the prize. ", black, notebox, smallfont)

        #display the bottom box with the puzzle and the attempted answers
        codebox = pygame.draw.rect(display_surface, white, (X/2-435,Y/2-110,870,285))
        draw_codebox(display_surface, (X/2-435), (Y/2-80), 870, 50, 50, 3, green, code_five, stage, userinput)

        #if the user's input matches the answer, let them go on to the next stage (unlock next button)
        if userinput == listToString(answer_five):
            nextstage = unlockstage()

        #displays button to go to the next stage and handles user iteractions with it
        if X/2+315+120 > mouse[0] > X/2+315 and Y/2+180+50 > mouse[1] > Y/2+180 and nextstage == True: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, black)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
            #if clicked, move on to next stage and reset variables
            if click[0] == 1 and nextstage == True:
                stage = "done"
                userinput = ""
                guess_length = 0
                nextstage = relockstage()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2+315,Y/2+180,120,50)) 
            nextbutton = largefont.render('next', False, white)
            display_surface.blit(nextbutton, (X/2+340,Y/2+190))
        
        pygame.display.update() #continuous display update

    #displays the ending page with educational notes on making passwords
    while stage == "done":
        #ends game if user hits exit button
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

        #used for mouse interactions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #displays background
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))


        #displays box with exposition
        box = pygame.draw.rect(display_surface, black,(X/2-435,Y/2-240,870,480))
        makeNote(display_surface, "Excited to finish all the puzzles, you go and " + listToString(answer_five[0]) + " " + listToString(answer_five[1]) + " " + listToString(answer_five[2]) + " " + listToString(answer_five[3]) + ". There is...another envelope. You open it, wondering if maybe there's one more puzzle to solve, but inside you find....tickets to the amusement park!! One more note is behind them: " , white, box, smallfont)

        #note displays separate for nice spacing between lines
        #displays note
        notebox = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 - 155, 700, 50))
        makeNote(display_surface, "I knew you could do it, kiddo! To celebrate how smart you are, let's go to the amusement park this weekend :) ", black, notebox, smallfont)

        #displays more of the note
        notebox2 = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 - 110, 700, 95))
        makeNote(display_surface, "Now, there's a reason I wanted to teach you more about puzzles. Now that you've been playing online some, I want you to be safe and use strong passwords. Just like you solved these puzzles, hackers can solve your passwords. To make it harder for them, you should:", black, notebox2, smallfont)

        #displays rules
        rule1 = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 - 30, 700, 50))
        makeNote(display_surface, "1. Use long passwords. The longer passwords take more time for them to figure out.", black, rule1, smallfont)
        rule2 = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 + 20, 700, 50))
        makeNote(display_surface, "2. Use uppercase letters and symbols. Using more than lowercase letters makes it much more difficult for them", black, rule2, smallfont)
        rule3 = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 + 70, 700, 50))
        makeNote(display_surface, "3. Don't use the same password for every account. That way if a hacker does figure out your password, they can't use it for others", black, rule3, smallfont)

        #last note
        notebox3 = pygame.draw.rect(display_surface, white, (X/2 - 350, Y/2 + 115, 700, 55))
        makeNote(display_surface, "I know it seems annoying now, but you'll thank me for it when you're older. Let me know if you want to play again. Love, Dad.", black, notebox3, smallfont)

        #displays done button to go to close the game and handles user iteractions with it
        if X/2+60 > mouse[0] > X/2-60 and Y/2+180+50 > mouse[1] > Y/2+180: #user within hover area
            #highlight button to show hover
            pygame.draw.rect(display_surface, white,(X/2-60,Y/2+180,120,50)) 
            nextbutton = largefont.render('done', False, black)
            display_surface.blit(nextbutton, (X/2-35,Y/2+190))
            nextstage = unlockstage()
            #if clicked, close the game
            if click[0] == 1 and nextstage == True:
                pygame.quit()
                quit()
        else:
            #normal button display when user isn't hovering on it
            pygame.draw.rect(display_surface, black,(X/2-60,Y/2+180,120,50)) 
            nextbutton = largefont.render('done', False, white)
            display_surface.blit(nextbutton, (X/2-35,Y/2+190))
        
        pygame.display.update() #continuous display update