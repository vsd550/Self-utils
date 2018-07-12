##Given images and the boxes
draw = ImageDraw.Draw(img)
for box in boxes:
    draw.rectangle(list(box), outline='red')
img.show()


##MatplotLib utils
#1. create fig and axes`
fig = plt.figure(frameon=False)
fig.set_size_inches(im.shape[1] / dpi, im.shape[0] / dpi)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.axis('off')
fig.add_axes(ax)
ax.imshow(im)
##2. for multiple figures
im2 = np.zeros((im.shape[0], im.shape[1], 3)).astype(np.uint8)
fig2 = plt.figure(frameon=False)
fig2.set_size_inches(im.shape[1] / dpi, im.shape[0] / dpi)
ax2 = plt.Axes(fig2, [0., 0., 1., 1.])
ax2.axis('off')
fig2.add_axes(ax2)
ax2.imshow(im2)

ax.add_patch(
                plt.Rectangle((bbox[0], bbox[1]),   ##this is x,y,w,h
                              bbox[2] - bbox[0],
                              bbox[3] - bbox[1],
                              fill=False, edgecolor='g',
                              linewidth=0.5, alpha=box_alpha))

ax.text(
                    bbox[0], bbox[1] - 2,
                    get_class_string(classes[i], score, dataset),
                    fontsize=3,
                    family='serif',
                    bbox=dict(
                        facecolor='g', alpha=0.4, pad=0, edgecolor='none'),
                    color='white')


ax.add_patch(polygon)

ax.plot(
                            kps[0, i2], kps[1, i2], '.', color=colors[l],
                            markersize=3.0, alpha=0.7)

##finally save all the figs
output_name = os.path.basename(im_name) + '.' + ext
fig.savefig(os.path.join(output_dir, '{}'.format(output_name)), dpi=dpi)
#vij : added here
output_name_mod = os.path.basename(im_name) + '.' + 'jpg'
fig2.savefig(os.path.join(output_dir, '{}'.format(output_name_mod)), dpi=dpi)

plt.close('all')

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

###OPERATIONS on polygons and arrays
poly = np.array(seg).reshape((int(len(seg)/2), 2))   ##CHECK??
polygons.append(Polygon(poly))


c = (np.random.random((1, 3))*0.6+0.4).tolist()[0]

if _isArrayLike(ids): ###checking ---- Nice programming skills
    return [self.imgs[id] for id in ids]
elif type(ids) == int:
    return [self.imgs[ids]]

s  [785.0, 2382.5, 777.5, 2372.0, 780.0, 2369.5, 825.0, 2335.5, 833.5, 2344.0, 785.0, 2382.5]
# for s in seg:
#     print(s)
s = seg[0]
print('s ',s)
poly1 = np.array(s)
print('poly ',poly1)
poly2 = poly1.reshape((int(len(s)/2), 2))   
print('poly ',poly2)


pylab.rcParams['figure.figsize'] = (30.0, 30.0)  ##imp for notebook

def poly2origpoly(poly, x, y, rate):
    '''Adds the x y coordinate to get coordinate with respect to original image
        x,y comes from image name'''
    origpoly = []
    for i in range(int(len(poly)/2)):
        tmp_x = float(poly[i * 2] + x) / float(rate)
        tmp_y = float(poly[i * 2 + 1] + y) / float(rate)
        origpoly.append(tmp_x)
        origpoly.append(tmp_y)
    return origpoly
###CNN formula
W_2 = (W_1 - F + 2P)/S + 1


##takes the mean over the flattened array
logger.info(precision   = -np.ones((T,R,K))
precision.shape
ap_default = np.mean(precision[precision > -1])

            #imp array operations -- np array
 a_ = [[1, 2, 3], [4, 5], [6, 7, 8, 9,10]]
a_
np.array(a_)
b_ = np.zeros([len(a_),len(max(a_,key = lambda x: len(x)))])

for i,j in enumerate(a_):
#     print(len(j))
    print(j[-1])
#     print(j[-2:])
    b_[i][0:len(j[:-1])] = j[:-1]
    b_[i][len(j[:-1]):-1 ] = 
    
    b_[i][-1] = j[-1]
b_

##another one
            a = np.empty(((622, 3)))
a.shape
b = np.empty((263, 3))
b.shape

aa=np.array(a)
bb =np.array(b)

np.concatenate((aa, bb))

ll = []

ll.append(a)
ll.append(b)
ll
