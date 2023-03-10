import tkinter as tk 
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image

GREEN = '#8dc24e'

HEIGHT = 700
WIDTH = 900

FULL_EARTH_DESC = 'Our home planet is the third planet from the Sun\n and the only place we know of so far that’s inhabited \nby living things.\n\n\nWhile Earth is only the fifth largest planet\nin the solar system, it is the only world\nin our solar system with liquid water on the surface.\nJust slightly larger than nearby Venus. Earth is\nthe biggest of the four planets closest to the Sun,\nall of which are made of rock and metal.\n\n\nThe name Earth is at least 1,000 years old.\nAll of the planets, except for Earth were named after Greek\nand Roman gods and goddesses.\nHowever, the name Earth is a Germanic word\nwhich simply means “the ground.”'
EARTH_FACT = '" Humans are the primary inahbitants of this beautiful planet, but they treat it very poorly... "'

FULL_JUPITER_DESC = 'Jupiter has a long history surprising \nscientists—all the way back to 1610 when Galileo Galilei \nfound the first moons beyond Earth. \nThat discovery changed the way we see the universe.\n\n\nFifth in line from the Sun, Jupiter is, \nby far, the largest planet in the solar system \nmore than twice as massive as all \nthe other planets combined.\n\n\nJupiter\'s familiar stripes \nand swirls are actually cold, windy clouds \nof ammonia and water, floating in an atmosphere of \nhydrogen and helium. Jupiter’s iconic Great Red Spot \nis a giant storm bigger than Earth that has \nraged for hundreds of years.'
JUPITER_FACT = 'One spacecraft — NASA\'s Juno orbiter — is currently exploring this giant world.'

FULL_NEPTUNE_DESC = 'Dark, cold and whipped by supersonic winds, \nice giant Neptune is the eighth and most distant \nplanet in our solar system.\n\n\nMore than 30 times as far from the Sun as Earth, Neptune \nis the only planet in our solar system not visible to the \nnaked eye and the first predicted by \nmathematics before its discovery. In 2011\nNeptune completed its first 165-year \norbit since its discovery in 1846.\n\n\n NASA\'s Voyager 2 is the only spacecraft \nto have visited Neptune up close. It flew past in \n1989 on its way out of the solar system.'
NEPTUNE_FACT = 'Neptune has 14 moons! \nThe most interesting moon is Triton, a frozen world that is spewing nitrogen ice and dust particles out from below its surface.\nIt was likely captured by the gravitationalnpull of Neptune. It is probably the coldest world in the solar system.'

FULL_MARS_DESC = 'The fourth planet from the Sun, \nMars is a dusty, cold, \ndesert world with a very thin atmosphere.\n\n\nThis dynamic planet has seasons, \npolar ice caps and weather and canyons and \nextinct volcanoes, evidence it was once \nan even more active past\n\n\n Mars is one of the most explored bodies \nin our solar system, and it\'s the only planet \nwhere we\'ve sent rovers to roam the\nalien landscape. NASA currently has three spacecraft \nin orbit, one rover and one lander on the surface.\nIndia and ESA also have spacecraft in orbit above Mars.\nThese robotic explorers have found lots of \nevidence that Mars was much wetter and warmer, \nwith a thicker atmosphere, \nbillions of years ago. NASA launched the next-generation \nPerseverance rover to Mars on July 30,2020.'
MARS_FACT = 'NASA\'s latest robotic mission to the Red Planet, Mars 2020, aims to help future astronauts \nbrave that inhospitable landscape.'

FULL_SATURN_DESC = 'Saturn is the sixth planet from the Sun \nand the second largest planet in our solar system.\n\n\nAdorned with thousands of beautiful ringlets,\n Saturn is unique among the planets. It is\nnot the only planet to have rings—made \nof chunks of ice and rock—but none \nare as spectacular or as complicated as Saturn\'s.\n\n\n Like fellow gas giant Jupiter, Saturn is a massive \nball made mostly of hydrogen and helium.'
SATURN_FACT = 'Nine Earths side by side would almost span Saturn’s diameter. That doesn’t include Saturn’s rings.'

FULL_VENUS_DESC = 'Venus is the second planet from the Sun and our \nclosest planetary neighbor. Similar in structure and size to \nEarth, Venus spins slowly in the opposite direction from \nmost planets.Its thick atmosphere traps heat in a runaway \ngreenhouse effect, making it the hottest planet \nin our solar system with surface temperatures hot enough \nto melt lead. Glimpses below the clouds \nreveal volcanoes and deformed mountains.\n\n\n Venus is named for the ancient Roman goddess of love \nand beauty, who was known as Aphrodite \nto the Ancient Greeks.'
VENUS_FACT = 'With a radius of 3,760 miles, Venus is roughly the same size as Earth — just slightly smaller'

FULL_URANUS_DESC = 'The first planet found with the aid of a telescope\nUranus was discovered in 1781 by astronomer William Herschel\n although he originally thought it was either a comet or a star.\n\n\nIt was two years later that the object was \nuniversally accepted as a new planet, \nin part because of observations by astronomer Johann Elert Bode.\nHerschel tried unsuccessfully to name his discovery \nGeorgium Sidus after King George III. Instead the \nscientific community accepted Bode\'s suggestion to name \nit Uranus, the Greek god of the sky, \nas suggested by Bode.'
URANUS_FACT = 'Uranus is known as the “sideways planet” because it rotates on its side.'

FULL_MERCURY_DESC = 'The smallest planet in our solar system and \nnearest to the Sun, Mercury is only \nslightly larger than Earth\'s Moon.\n\n\n From the surface of Mercury, the Sun would \nappear more than three times as large as it \ndoes when viewed from Earth,\nand the sunlight would be as \nmuch as seven times brighter. Despite its \nproximity to the Sun, Mercury is not the hottest \nplanet in our solar system \nthat title belongs to nearby Venus, \nthanks to its dense atmosphere.'
MERCURY_FACT = 'It is the closest planet to the Sun at a distance of about 36 million miles (58 million kilometers)'

FULL_PLUTO_DESC = 'Pluto—which is smaller than Earth’s Moon\nhas a heart-shaped glacier that’s the size of Texas\nThis fascinating world has blue skies, \nspinning moons, mountains as high as the Rockies\nand it snows—but the snow is red.\n\n\n Pluto’s atmosphere is thin and composed \nmostly of nitrogen, methane and carbon monoxide.\n\n\nPluto got its name from 11-year-old \nVenetia Burney of Oxford, England'
PLUTO_FACT = 'Pluto (minor planet designation: 134340 Pluto) is an icy dwarf planet in the Kuiper belt, a ring of bodies beyond the orbit of Neptune'

root = tk.Tk()
root.title('Welcome to the Planet app!')

def planet(event):
    planet_type = clicked.get() #clicket.get() assigns whatever planet you chose from the dropdownmenu to planet_type

    #Destroy children upon page change ---
    for widget in desc_frame.winfo_children():
        widget.destroy()
    for widget in fact_frame.winfo_children():
        widget.destroy()
    #------------

 #   planet_desc = {
 #       "Earth" : FULL_EARTH_DESC,
 #       "Jupiter" : FULL_JUPITER_DESC,
 #       "Neptune" : FULL_NEPTUNE_DESC,
 #       "Mars" : FULL_MARS_DESC,
 #       "Saturn" : FULL_SATURN_DESC,
 #       "Venus" : FULL_VENUS_DESC,
 #       "Uranus" : FULL_URANUS_DESC,
 #       "Mercury" : FULL_MERCURY_DESC,
 #       "Pluto" : FULL_PLUTO_DESC
 #   }

#    planet_fact = {
#        "Earth" : EARTH_FACT,
##        "Jupiter" : JUPITER_FACT,
 #       "Neptune" : NEPTUNE_FACT,
 #       "Mars" : MARS_FACT,
 #       "Saturn" : SATURN_FACT,
 #       "Venus" : VENUS_FACT,
 #       "Uranus" : URANUS_FACT,
 #       "Mercury" : MERCURY_FACT,
 #       "Pluto" : PLUTO_FACT
 #   }

    if planet_type == option[0]:
        image = Image.open('Earth.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_EARTH_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = EARTH_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()
    
    if planet_type == option[1]:
        image = Image.open('Jupiter.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_JUPITER_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = JUPITER_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()
    
    if planet_type == option[2]:
        image = Image.open('Neptune.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_NEPTUNE_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = NEPTUNE_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()
    
    if planet_type == option[3]:
        image = Image.open('Mars.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_MARS_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = MARS_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[4]:
        image = Image.open('Saturn.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_SATURN_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = SATURN_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[5]:
        image = Image.open('Venus.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_VENUS_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = VENUS_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[6]:
        image = Image.open('Uranus.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_URANUS_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = URANUS_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[7]:
        image = Image.open('Mercury.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_MERCURY_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = MERCURY_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[8]:
        image = Image.open('Pluto.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_PLUTO_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = PLUTO_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

    if planet_type == option[9]:

        image = Image.open('Math.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)

        def add_numbers():
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 + num2
            label_result.config(text=f"Result: {result}")

    # Create label widgets
    label1 = tk.Label(fact_frame, text="Enter first Number:", font=('Arial', 9), bg='#121212', fg='white')
    label1.grid(column=0, row=0, sticky='W')
    entry1 = tk.Entry(fact_frame, width=10)
    entry1.grid(column=1, row=0, padx=5, pady=5)

    label2 = tk.Label(fact_frame, text="Enter second Number:", bg='#121212', font=('Arial', 9), fg='white')
    label2.grid(column=0, row=1, sticky='W')
    entry2 = tk.Entry(fact_frame, width=10)
    entry2.grid(column=1, row=1, padx=5, pady=5)

    label_result = tk.Label(fact_frame, text="Result:", bg='#121212', font=('Arial', 9), fg='white')
    label_result.grid(column=0, row=2, sticky='W')

    # Create button widget
    button = tk.Button(fact_frame, text="Add", command=add_numbers)
    button.grid(column=1, row=3, sticky='E')
    item4.pack()

    if planet_type == option[10]: #Excel created!!!!
        #
        #
        #
        #
        #
        image = Image.open('Pluto.jpg')
        basewidth = 400
    #copy-pasted from stack overflow---
    #Assigns a new canvas to paste on top of the existing canvas, it creates an image and resizes it based on its size
    # and imports the photo
        canvas2 = tk.Canvas(root, height = 400, width = 400, bg = '#171717', bd = 0, highlightthickness= 0, relief= 'ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        item4= canvas2.create_image(225, 210, image= photo)
    #---------------------------
        canvas2.place(relx = 0.05, rely = 0.1, relheight = 0.6, relwidth = 0.5)
        #For the other frames we need to destroy the children

        #creating labels for the planet:
        planet_label = tk.Label(desc_frame, text = FULL_PLUTO_DESC, font = ('Arial', 9), bg = '#121212', fg = 'white')
        planet_label.pack()
        planet_fact = tk.Label(fact_frame, text = PLUTO_FACT, font = ('Times New Roman', 14), bg = '#121212', fg = 'white')
        planet_fact.pack(side = 'left')
        item4.pack()

#
#
#
#
# Excel Creation ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

desc_frame = tk.Frame(root, bg = "#121212")
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame = tk.Frame(root, bg = "#212121")
fact_frame.place(relx = 0.05, rely = 0.72, relheight = 0.2, relwidth = 0.9)

#Dropdown Menu -----
option = ['Earth', 'Jupiter', 'Neptune', 'Mars', 'Saturn', 'Venus', 'Uranus', 'Mercury', 'Pluto', 'Calculations', 'Excel']
clicked = StringVar()
clicked.set(option[0]) #Option set by default to earth, upon running the program, the earth wont automatically popup until clicked
drop = OptionMenu(root, clicked, *option)
drop.config(bg = '#121212', fg = GREEN)
drop.place(relx = 0.4, rely = 0.01, relheigh = 0.05, relwidth = 0.1)
#-------------------

#Button to select from Dropdownmenu ---
button = tk.Button(canvas, text = 'Get Info') #instance of button, put inside the canvas, button text says 'Get Info' 
button.config(bg = '#121212', fg = GREEN) #change the color of the button
button.bind('<Button-1>', planet) #allows us to run the function created, binding to button-1, which is the left-click of the mouse, when hit, runs planet function.
button.place(relx = 0.3, rely = 0.01, relheight = 0.05, relwidth = 0.1)

text = 'Welcome to the Planet App!\n\n\nChoose a planet to start...\n\n\nProject origin:\nAnthony Terrano (YouTube)\n\n inherited by Algonquin College:\n Space Apps Team'
text2 = 'Fun facts will show up in this box here!'

#Labels to put into the frames
#in tKinter, font is defined as --> font('fontName', size)
initial_label = tk.Label(desc_frame, text = text, font = ('Times New Roman', 18), bg = '#121212', fg = 'white')
initial_label.pack()
initial_label2 = tk.Label(fact_frame, text = text2, font = ('Arial', 18), bg = '#121212', fg = 'white')
initial_label2.pack(side = 'left')

root.mainloop()
