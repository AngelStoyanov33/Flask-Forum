import appsettings
<<<<<<< HEAD
import random
import string
=======
import string
import random
>>>>>>> 07cfc3220e74aee3ffe680d63b7c445a7151c0b3

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in appsettings.ALLOWED_EXTENSIONS

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))