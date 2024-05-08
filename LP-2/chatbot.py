import random

class restro():

    def __init__(self):

        self.menu = {
            "Pohe" : 20,
            "Upama": 20,
            "Vada Pav": 15,
            "Pav Bhaji": 40,
            "Misal Pav":50
        }

        self.bill = 0
        self.reservation = []

    def welcome_message(self):
        l=["Welcome to Mohit Restrorant, How can I help you", "Namaste from Mohit, How can I assist you?","Mohit's Fine Dining madhe aaple swagat aahe, Me kase aapli madat karu sakto?"]
        return random.choice(l)
    
    def Menu(self):
        print("\tMenu")
        print("Item\t\tPrice")
        for i,j in self.menu.items():
            print(i+'\t\t'+str(j))

    def res(self,name,no_of_people, date_time):
        self.reservation.append((name,no_of_people,date_time))
        print("Added Successfully")

    def get_feedback(self, feedback):
        feedback_responses = ["Thank you for your feedback!", "We appreciate your input. Thank you!", "Your feedback helps us improve. Thank you!"]
        return random.choice(feedback_responses)
    
    def calculate_bill(self):
        n='Start'
        while (n != "stop"):
            self.Menu()
            i = input("Enter dish name: ").lower()

            if i == 'pohe':
                self.bill+= 20
            elif i == "upama":
                self.bill+= 20

            n = input("Do you want to order anything else? If yes enter y, to calculate bill enter stop").lower()

        print("Thank You Order Placed!!!"+ f"Your total bill is {self.bill}")


chatbot = restro()

chatbot.calculate_bill()

