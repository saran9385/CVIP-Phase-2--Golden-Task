
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
        while True:
            common_message=input('enter a common mail for all recipients :')
        
            for i in recipents:
                i.set_message(common_message)
                i.display_message()

Mail.call()


