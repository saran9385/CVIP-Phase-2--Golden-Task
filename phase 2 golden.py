import time
class Mail:
    sender = 'saran@gmail.com'

    def __init__(self, name, recipient_email):
        self.name = name
        self.recipient_email = recipient_email
        self.body = ''

    def set_message(self,common_message):
        self.body = common_message

    def display_message(self):
        print(f"\n\nsender:{Mail.sender}\n----------\nSubject: Common annoucement\nTo: {self.recipient_email}\n          Body: {self.body}          \n----------")
        

    @classmethod
    def call(cls):
        recipents=[
            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),

            Mail('John', 'john@example.com'),
            Mail('Alice', 'alice@example.com'),
        ]
        
        common_message="""Dear Recipient,
We are pleased to announce we are in deadline. This is an exciting development. We appreciate your ongoing support and commitment to intership.

Thank you,
saran
"""
        count_recipents=16
        a=0
        while a<count_recipents:
            for i in recipents:
                time.sleep(0.5)
                i.set_message(common_message)
                i.display_message()
                a+=1
                if a>=count_recipents:
                    break

Mail.call()


