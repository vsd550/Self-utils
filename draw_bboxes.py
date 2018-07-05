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

