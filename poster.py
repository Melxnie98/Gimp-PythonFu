#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def poster(file1, file2, file3, file4, text1, fontSize1, font1, textColour1, letterSpacing1, text2, fontSize2, font2, textColour2, letterSpacing2) :
              # Make a new image. Size 10x10 for now -- we'll resize later.
              imageW, imageH = 2480, 3508
              posterImage = gimp.Image(imageW, imageH, RGB)
              gimp.message("image poster created")
 
              # make teh colors for fore and backgound
              colorB = gimpcolor.RGB(255, 204, 204)
              colorF = gimpcolor.RGB(247, 223, 194)
              pdb.gimp_context_set_background(colorB)
              pdb.gimp_context_set_foreground(colorF)
              gimp.message("f and b colors created")
 
              # make the background
              background = gimp.Layer(posterImage, "background", imageW,
                                      imageH, RGB_IMAGE, 100, NORMAL_MODE)
              background.fill(BACKGROUND_FILL)
              posterImage.add_layer(background, 1)
              gimp.message("background created")
 
              # add an image layer for image1
              image1 = pdb.file_jpeg_load(file1, file1)
              pdb.gimp_image_scale(image1, imageW/1.5, imageH/1.6)
              pdb.gimp_edit_copy(image1.layers[0])
              imageLayer1 = gimp.Layer(posterImage, "image 1", imageW, imageH,
                                       RGBA_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(imageLayer1)
              floatingLayer1 = pdb.gimp_edit_paste(imageLayer1, TRUE)
              pdb.gimp_floating_sel_anchor(floatingLayer1)
              imageLayer1.translate(imageW/8, imageH/100)
              gimp.message("image 1 created")

              # add an image layer for image2
              image2 = pdb.file_jpeg_load(file2, file2)
              pdb.gimp_image_scale(image2, imageW/1.8, imageH/1.8)
              pdb.gimp_edit_copy(image2.layers[0])
              imageLayer2 = gimp.Layer(posterImage, "image 2", imageW/3, imageH,
                                       RGBA_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(imageLayer2)
              floatingLayer2 = pdb.gimp_edit_paste(imageLayer2, TRUE)
              pdb.gimp_floating_sel_anchor(floatingLayer2)
              imageLayer2.translate(imageW/8, imageH/60)
              gimp.message("image 2 created")

              # add an image layer for image3
              image3 = pdb.file_jpeg_load(file3, file3)
              pdb.gimp_image_scale(image3, imageW, imageH/2.6)
              pdb.gimp_edit_copy(image3.layers[0])
              imageLayer3 = gimp.Layer(posterImage, "image 3", imageW-200, imageH+350,
                                       RGBA_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(imageLayer3)
              floatingLayer3 = pdb.gimp_edit_paste(imageLayer3, TRUE)
              pdb.gimp_floating_sel_anchor(floatingLayer3)
              imageLayer3.translate(imageW/350, imageH/4)
              pdb.gimp_item_transform_shear( imageLayer3, ORIENTATION_VERTICAL , -800)
              gimp.message("image 3 created")

              # add an image layer for image4
              image4 = pdb.file_tiff_load(file4, file4)
              pdb.gimp_image_scale(image4, imageW*1.2, imageH)
              pdb.gimp_edit_copy(image4.layers[0])
              imageLayer4 = gimp.Layer(posterImage, "image 4", imageW, imageH, RGBA_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(imageLayer4)
              floatingLayer4 = pdb.gimp_edit_paste(imageLayer4, TRUE)
              pdb.gimp_floating_sel_anchor(floatingLayer4)
              imageLayer4.translate(imageW/imageW, imageH/imageH)
              gimp.message("image 4 created")

 
              # make a text layer
              textLayer = pdb.gimp_text_fontname(posterImage, None, imageW/7, imageH/19,
                                                 text1, 10, TRUE, fontSize1, PIXELS, font1)
              textLayer.translate(-textLayer.width/8, -textLayer.height/7)
              pdb.gimp_text_layer_set_color(textLayer, textColour1)
              pdb.gimp_text_layer_set_letter_spacing(textLayer, letterSpacing1)
              gimp.message("text layer 1 created")
              # make a text layer
              textLayer2 = pdb.gimp_text_fontname(posterImage, None, imageW/6, imageH/6,
                                                 text2, 10, TRUE, fontSize2, PIXELS, font2)
              textLayer2.translate(-textLayer2.width/10, -textLayer2.height/7)
              pdb.gimp_text_layer_set_letter_spacing(textLayer2, letterSpacing2)
              pdb.gimp_text_layer_set_color(textLayer2,textColour2)
              gimp.message("text layer 2 created")

             
              # Create a new image window
              gimp.Display(posterImage)
              # Show the new image window
              gimp.displays_flush()
    
register(
              "python_fu_poster",
              "Costal Ireland",
              "Some Images of WGB Building",
              "ML",
              "Copyright@ML",
              "2022",
              "The Irish Coast",
              "", # Create a new image, don't work on an existing one
              [
                (PF_FILE, "file1", "Choose Image 1", ""),
                (PF_FILE, "file2", "Choose Image 2", ""),
                (PF_FILE, "file3", "Choose Image 3", ""),
                (PF_FILE, "file4", "Choose Image 4", ""),
                (PF_STRING, "text1", "Copywrite Text", "The Irish Coast"),
                (PF_SLIDER, "fontSize1", "Font size", 280, (0,350,10)), 
                (PF_FONT, "font1", "Font", "Baskerville Bold Italic"),
                (PF_COLOR, "textColour1", "Text colour", (255,255,255)),
                (PF_SLIDER, "letterSpacing1", "Letter spacing", 10, (0,100,5)),
                (PF_STRING, "text2", "Text 2", "Take a walk on the wild side!"),
                (PF_SLIDER, "fontSize2", "Font size", 150,(0,200,10)), 
                (PF_FONT, "font2", "Font", "Baskerville Bold Italic"),
                (PF_COLOR, "textColour2", "Text colour",  (106,74,183)),
                (PF_SLIDER, "letterSpacing2", "Letter spacing",0, (0,100,5)),  
              ],
              [],
              poster, menu="<Image>/File/Create/The Irish Coast"
)
 
main()


