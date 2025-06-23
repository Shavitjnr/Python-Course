from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to, date):
        # date is expected to be a datetime object
        print(f"Ticket is booked in Train No: {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}.")

t = Train(12345)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")