from PIL import Image

##----- please check file name & path before running
frames = [
    'bowl_images/original_bowl_frame.jpg',
    'bowl_images/masked_Bowl_result_white.jpg',
    'bowl_images/inpainted_result.png'
]


base_image = Image.open(frames[0]).convert("RGBA")
base_size = base_image.size

images = [base_image]
for path in frames[1:]:
    img = Image.open(path).convert("RGBA").resize(base_size)
    images.append(img)


images[0].save('output_using_pillow_bowl.gif',
               save_all=True,
               append_images=images[1:],
               duration=1000,  
               loop=0,
               disposal=2)     
