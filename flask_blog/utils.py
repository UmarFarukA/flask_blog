ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def save_file(file):
#     random_hex = secrets.token_hex(8)
#     if allowed_file(file):
#         f_name, f_ext = os.path.splitext(file)
#         picture_name = random_hex + f_ext
#         picture_path = os.path.join(
#             app.root_path, 'static/images', picture_name)

#         output_size = (100, 100)
#         i = Image.open(file)
#         i.thumbnail(output_size)
#         i.save(picture_path)
#     return picture_name
