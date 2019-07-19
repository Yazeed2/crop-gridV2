import cv2

#editing the input to mach everything!
photo = input("drag and drop the image here")
photo = photo.lower()
photo = photo.replace('"', '')
photo = photo.replace('.tiff', '.png')
photo = photo.replace('.jpeg', '.png')
photo = photo.replace('.jpg', '.png')

# read image
img = cv2.imread(photo, cv2.IMREAD_UNCHANGED)

# get dimensions of image
dimensions = img.shape

# height, width
height = img.shape[0]
width = img.shape[1]


#functions

def onebyone(paddingx, paddingy):
    #chosing the option
    print('wich one would you like? ')

    print("""
1-
[][]
[][]
    """)
    print(""""
2- 
[][][]
[][][]
[][][]
    
    """)

    option = input(':')
    # 2 by 2
    if option == '1':
        y = paddingy
        x = paddingx
        crop_size = (width - (2*x))/2
        crop_size = round(crop_size)

        h = crop_size
        w = crop_size

        #croping the image and saving the parts of the image in order
        part = photo.replace(".png", "1.png")
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "2.png")
        crop_img = img[y:y + h, x + w:width - x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "3.png")
        crop_img = img[y + h:height - y, x:x + w]
        cv2.imwrite(part, crop_img)


        part = photo.replace(".png", "4.png")
        crop_img = img[y + h:height - y, x + w: width-x]
        cv2.imwrite(part, crop_img)

        print('done')

    elif option == '2':
       #3 by 3

       #take the measures
        x = paddingx
        y = paddingy
        crop_size = (width - (2*x))  / 3
        crop_size = round(crop_size)
        crop2 = crop_size * 2


        #croping the image and saving the parts of the image in order
        #layer 1
        part = photo.replace(".png", "1.png")
        crop_img = img[y:crop_size+y, x:crop_size+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "2.png")
        crop_img = img[y:crop_size+y, crop_size+x:crop2+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "3.png")
        crop_img = img[y:crop_size+y, crop2+x:width-x ]
        cv2.imwrite(part, crop_img)

        #layer 2

        part = photo.replace(".png", "4.png")
        crop_img = img[crop_size+y:crop2+y, x:crop_size+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "5.png")
        crop_img = img[crop_size+y:crop2+y, crop_size+x:crop2+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "6.png")
        crop_img = img[crop_size+y:crop2+y, crop2+x:width-x]
        cv2.imwrite(part, crop_img)

        #layer 3
        part = photo.replace(".png", "7.png")
        crop_img = img[crop2+y:height - y, x:crop_size+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "8.png")
        crop_img = img[crop2+y:height-y, crop_size+x:crop2+x]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "9.png")
        crop_img = img[crop2+y:height-y, crop2+x:width-x]
        cv2.imwrite(part, crop_img)

        print('done')


########################################################################################################################

def threebytwo(paddingx):

    #3 by 3

    #take the measures
    x = paddingx
    y = 0
    crop_size = (width - (2*x))  / 3
    crop_size = round(crop_size)
    crop2 = crop_size * 2

    # croping the image and saving the parts of the image in order
    # layer 1
    part = photo.replace(".png", "1.png")
    crop_img = img[y:crop_size + y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "2.png")
    crop_img = img[y:crop_size + y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "3.png")
    crop_img = img[y:crop_size + y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    # layer 2

    part = photo.replace(".png", "4.png")
    crop_img = img[crop_size + y:height - y, x:crop_size + x]

    cv2.imwrite(part, crop_img)
    part = photo.replace(".png", "5.png")
    crop_img = img[crop_size + y:height - y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "6.png")
    crop_img = img[crop_size + y:height - y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    print("done")

######################################################################################################################
def twobyone(paddingx):

    #take the measures
    x = paddingx
    y = 0
    crop_size = (width - (2*x))  / 2

    # croping the image and saving the parts of the image in order

    part = photo.replace(".png", "1.png")
    crop_img = img[y:height- y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "2.png")
    crop_img = img[y:height - y, crop_size + x:width - x]
    cv2.imwrite(part, crop_img)

    print("done")

def threebyone(paddingx):


    x = paddingx
    y = 0
    crop_size = (width - (2 * x)) / 3
    crop_size = round(crop_size)
    crop2 = crop_size * 2

    # layer 1
    part = photo.replace(".png", "1.png")
    crop_img = img[y:height-y, x:crop_size+x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "2.png")
    crop_img = img[y:height-y, crop_size+x:crop2+x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "3.png")
    crop_img = img[y:height-y, crop2+x:width-x]
    cv2.imwrite(part, crop_img)
    print('done')
##################################################################################################################

def threebyfour(paddingy) :

    # take the measures
    x = 0
    y = paddingy
    crop_size = (height - (2 * y)) / 4
    crop_size = round(crop_size)
    crop2 = crop_size * 2
    crop3 = crop_size * 3


    # croping the image and saving the parts of the image in order
    # layer 1
    part = photo.replace(".png", "1.png")
    crop_img = img[y:crop_size + y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "2.png")
    crop_img = img[y:crop_size + y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "3.png")
    crop_img = img[y:crop_size + y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    # layer 2

    part = photo.replace(".png", "4.png")
    crop_img = img[crop_size + y:crop2 + y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "5.png")
    crop_img = img[crop_size + y:crop2 + y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "6.png")
    crop_img = img[crop_size + y:crop2 + y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    # layer 3
    part = photo.replace(".png", "7.png")
    crop_img = img[crop2 + y:crop3 + y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "8.png")
    crop_img = img[crop2 + y:crop3 + y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "9.png")
    crop_img = img[crop2 + y:crop3 + y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    # layer 4
    part = photo.replace(".png", "10.png")
    crop_img = img[crop3 + y:height - y, x:crop_size + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "11.png")
    crop_img = img[crop3 + y:height - y, crop_size + x:crop2 + x]
    cv2.imwrite(part, crop_img)

    part = photo.replace(".png", "12.png")
    crop_img = img[crop3 + y:height - y, crop2 + x:width - x]
    cv2.imwrite(part, crop_img)

    print('done')









#check the ratio
ratio = height/width
if ratio != 1 :
    print('okay proceeding to auto croping...')
    if ratio < 1 :
        r = width / height
        if r >= 3:
            # we cut it as a three by one
            paddings = (width / 3) - height
            paddings = paddings / 2
            paddings = round(paddings)
            threebyone(paddings)

        elif r >= 2:
            # we cut as a two by one
            paddings = (width / 2) - height
            paddings = paddings / 2
            paddings = round(paddings)
            twobyone(paddings)
        elif r >= 1.5:
            # we cut it as three by two
            paddings = (width/3) - (height/2)
            paddings = paddings/2
            paddings = round(paddings)
            threebytwo(paddings)

        elif r < 1.5:
            # we cut it as a square
            paddings = width - height
            paddings = paddings/2
            paddings = round(paddings)
            onebyone(paddings, 0)
    else:
        # we cut it as a four by three

        if ratio <= 1.3 :

            #we can cut it as a square
            paddings = height - width
            paddings = paddings / 2
            paddings = round(paddings)
            onebyone(0, paddings)
        elif ratio > 1.3 :
            # we can cut it as a four by three
            paddings = (height / 4) - (width / 3)
            paddings = paddings / 2
            paddings = round(paddings)
            threebyfour(paddings)

# then it is a 1:1 ratio
else:
   onebyone(0, 0)

