# # Object -> specific instance of a class
# # Class -> general definition

class iPhone:
    def __init__(self, name, model, color): #constructor -> called when creating a new instance
        self.name = name
        self.model = model
        self.color = color
        self.messages = []

    def receive_iMessage(self, message):
        print("Receiving iMessage...")
        self.messages.append(message)

    def send_iMessage(self, message, recipient):
        print("Sending iMessage...")
        recipient.receive_iMessage(message)

    def check_iMessage(self):
        print(self.messages)
    
    def set_name(self, new_name):
        self.name = new_name
    
    def __str__(self): #string representation of the object
        return f'iPhone {self.name}'
        

phone1 = iPhone(name = "phone1", model = 'iPhone 16 Pro', color = 'black')
phone2 = iPhone(name = "phone2", model = 'iPhone 11', color = 'white')

phone2.set_name("new_phone2")
phone1.send_iMessage("Hello, this is a message from phone1 to phone2.", phone2)
phone2.check_iMessage()