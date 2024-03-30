import tensorflow as tf
def normalize_and_resize(img_loc):
    # With Google Colab
    # my_img = tf.io.read_file(img_loc)

    # Read in image
    my_img = tf.io.read_file(img_loc)

    # Turn file into a tensor
    my_img = tf.image.decode_image(my_img)

    # Resize image
    my_img = tf.image.resize(my_img, size=[224, 224])

    # Normalize data
    my_img = my_img/ 255

    return my_img
class_names = ['Inorganic','Organic','Metal']
image_path=  "/Users/maniksinghsarmaal/Downloads/burger.jpeg"
custom_image = normalize_and_resize(image_path)
print(type(custom_image))
