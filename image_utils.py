from PIL import Image
'''print sizes of all the images in a directory'''


#####
def get_sizes(img_dir):
    onlyfiles = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir,f))]
    for img_name in onlyfiles:
        img = np.array(Image.open(os.path.join(img_dir,img_name)))
        print(img_name, np.shape(img))

####ROTATING THE IMAGE
import cv2
from PIL import Image
from scipy import ndimage
imag = Image.open('/home/fractaluser/Downloads/DOTA_devkit-master/example/images/P0706.png')
print(np.shape(imag))
imag.show()

#rotation angle in degree
rotated = ndimage.rotate(imag, 45)
rot_img = Image.fromarray(rotated, 'RGB')
rot_img.save('my.png')
rot_img.show()
#########################

        def display_image_in_actual_size(img):

    dpi = 80
    #im_data = plt.imread(im_path)
    height, width, depth = img.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')
    # Display the image.
    ax.imshow(img, cmap='gray')

    plt.show()
    
    
