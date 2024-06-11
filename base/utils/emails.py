from django.core.mail import send_mail


class EmailHandler:
    """ Dealing with sending text and token via email """
    def __init__(self):
        ...
    
    def send_otp(self, email, token):
        """ send otp to use without any special text """
        print("################################")
        print(f"Your token is: {token}")
        print("################################")