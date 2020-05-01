# FINAL PROJECT

"""Program 1: The Taco Image (15 points for code, 10 points for comments)
Search Unsplash for a taco image (for example https://unsplash.com/photos/JiRSy0GfqPA) and save the image on your computer.

The downloaded image is very large. Use pillow to resize the image to a smaller size, perhaps no more than 800px wide or tall (make sure you preserve the aspect ratio).
Write the text "Random Taco Cookbook" on the image.
Save the modified image to a new file. """

# Imported libraries
from PIL import Image, ImageDraw, ImageFont
import requests
import docx

# CODE PROGRAM 1
image = Image.open('Taco_spencer_davis_unsplash_Original.jpg')

width = image.width  # Width
height = image.height  # Height

width_sized = int(width / 3)
height_sized = int(height / 3.75)

sized_image = image.resize((width_sized, height_sized))

image_draw = ImageDraw.Draw(sized_image)
font = ImageFont.truetype('DejaVuSans.ttf', 50)
image_draw.text([100, 700], 'Random Taco Cookbook', fill='Fuchsia', font=font)

sized_image.save('Image_Tacos_last_modified.jpg')

"""Program 2: Make the Random Taco Recipe Book (40 points for code, 35 points for comments) Use requests to download 
three random tacos from the random taco API. Save the data for each of three tacos in your program. Notice that each 
recipe is divided into five sections for base_layer, seasoning, mixin, condiment, and shell. Use Python to create a 
Word document. On the first page, insert the header text "Random Taco Cookbook" On the first page, add the resized 
taco image that you created with part 1. (hint: adding images to Word documents is covered in the textbook) On the 
first page, write the name of the image author On the first page, write the text of the random taco API URL On the 
first page, write your own name. On the second page, start writing the first taco recipe. Write all five components 
of the recipe. Use a larger font or heading for the heading for each of the sections. Please see example document for 
suggested style. After the first recipe, add a page break. To add another page, hint: google "python-docx add page 
break" Repeat to write all of the next recipe and a page break. Repeat to write all the third recipe. Save your word 
document. """

# CODE PROGRAM 2

recipe1 = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
recipe2 = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
recipe3 = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()

recipes_book = docx.Document()
recipes_book.add_paragraph('Random Taco Cookbook', 'Title')
recipes_book.add_picture('Image_Tacos_last_modified.jpg', width=docx.shared.Inches(6),
                         height=docx.shared.Inches(6))
recipes_book.add_paragraph('Credits', 'Heading 1')
recipes_book.add_paragraph('Taco image: Photo by Spencer Davis on Unsplash', style='List Bullet')
recipes_book.add_paragraph('Tacos from: http://taco-randomizer.herokuapp.com/random/?full_taco=true', style='List '
                                                                                                            'Bullet')
recipes_book.add_paragraph('Code by: Paseng Moua', style='List Bullet')

recipes_book.add_page_break()
recipes_book.add_paragraph(f'{recipe1["base_layer"]["name"]} with {recipe1["seasoning"]["name"]}, {recipe1["condiment"]["name"]} and {recipe1["mixin"]["name"]} in {recipe1["shell"]["name"]}', 'Title')
recipes_book.add_paragraph(f'{recipe1["base_layer"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe1["base_layer"]["recipe"]}')
recipes_book.add_paragraph(f'Seasoning: {recipe1["seasoning"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe1["seasoning"]["recipe"]}')
recipes_book.add_paragraph(f'Condiment: {recipe1["condiment"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe1["condiment"]["recipe"]}')
recipes_book.add_paragraph(f'Mixin: {recipe1["mixin"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe1["mixin"]["recipe"]}')
recipes_book.add_paragraph(f'Wrap: {recipe1["shell"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe1["shell"]["recipe"]}')

recipes_book.add_page_break()
recipes_book.add_paragraph(f'{recipe2["base_layer"]["name"]} with {recipe2["seasoning"]["name"]}, {recipe2["condiment"]["name"]} and {recipe2["mixin"]["name"]} in {recipe2["shell"]["name"]}', 'Title')
recipes_book.add_paragraph(f'{recipe2["base_layer"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe2["base_layer"]["recipe"]}')
recipes_book.add_paragraph(f'Seasoning: {recipe2["seasoning"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe2["seasoning"]["recipe"]}')
recipes_book.add_paragraph(f'Condiment: {recipe2["condiment"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe2["condiment"]["recipe"]}')
recipes_book.add_paragraph(f'Mixin: {recipe2["mixin"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe2["mixin"]["recipe"]}')
recipes_book.add_paragraph(f'Wrap: {recipe2["shell"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe2["shell"]["recipe"]}')

recipes_book.add_page_break()
recipes_book.add_paragraph(f'{recipe3["base_layer"]["name"]} with {recipe3["seasoning"]["name"]}, {recipe3["condiment"]["name"]} and {recipe3["mixin"]["name"]} in {recipe3["shell"]["name"]}', 'Title')
recipes_book.add_paragraph(f'{recipe3["base_layer"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe3["base_layer"]["recipe"]}')
recipes_book.add_paragraph(f'Seasoning: {recipe3["seasoning"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe3["seasoning"]["recipe"]}')
recipes_book.add_paragraph(f'Condiment: {recipe3["condiment"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe3["condiment"]["recipe"]}')
recipes_book.add_paragraph(f'Mixin: {recipe3["mixin"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe3["mixin"]["recipe"]}')
recipes_book.add_paragraph(f'Wrap: {recipe3["shell"]["name"]}', 'Heading 1')
recipes_book.add_paragraph(f'{recipe3["shell"]["recipe"]}')
recipes_book.save('Random Recipes Book.docx')

#print(f'{recipe1["seasoning"]["recipe"]}')
"""
CODE TEST
for i in recipe1['mixin'][data]:
    recipes_book.add_paragraph(f'{data}', 'Heading 1')
recipes_book.save('Random Recipes Book.docx')
# for i in recipe1:
#   print(i, recipe1[i])"""


