from Container import Paper, Bottle, Can, Box

# Container_Recycling_Machine class for creating machine
class Container_Recycling_Machine():

    # Default cunstructor for initialize object
    def __init__(self):
        self.paper = 0
        self.bottle = 0
        self.can = 0
        self.box = 0
        self.paper_c = 0
        self.bottle_c = 0
        self.can_c = 0
        self.box_c = 0
        self.balance = 0.0
        self.money = 0.0
        self.option = None
        self.item = None
        self.n_item = 0

    # accept_product method to: accept item from user
    def accept_product(self):
        print("\nBalance: ${}. Please select a product: (Paper, Bottle, Can, Box, Stop):".format(
            self.balance), end=" ")
        self.option = input("")

    # select_product method to: select items which user has selcted and take number of items
    def select_product(self):
        # cheeck user selected paper
        if self.option.lower() == 'paper':
            self.item = Paper()
            self.n_item = int(
                input("How Many {}s do you have ? : ".format(self.item.name)))
            # Check number of paper is not exceeded 50    
            if (self.paper + self.n_item) <= 50:
                print("Please Place {} {}(s) into Machine.".format(
                    self.n_item, self.item.name))
                self.paper += self.n_item
                self.paper_c += self.n_item
                self.money = self.item.price * self.n_item
            else:
                print("You can not add {} {}s in Machine".format(
                    self.n_item, self.item.name))
                self.n_item = 0    

        # cheeck user selected bottle
        elif self.option.lower() == 'bottle':
            self.item = Bottle()
            self.n_item = int(
                input("How Many {}s do you have ? : ".format(self.item.name)))
            # Check number of bottle is not exceeded 50
            if (self.bottle + self.n_item) <= 50:
                print("Please Place {} {}(s) into Machine.".format(
                    self.n_item, self.item.name))
                self.bottle += self.n_item
                self.bottle_c += self.n_item
                self.money = self.item.price * self.n_item
            else:
                print("You can not add {} {}s in Machine".format(
                    self.n_item, self.item.name))
                self.n_item = 0    

        # cheeck user selected can
        elif self.option.lower() == 'can':
            self.item = Can()
            self.n_item = int(
                input("How Many {}s do you have ? : ".format(self.item.name)))
            # Check number of can is not exceeded 50    
            if(self.can + self.n_item) <= 50:
                print("Please Place {} {}(s) into Machine.".format(
                    self.n_item, self.item.name))
                self.can += self.n_item
                self.can_c += self.n_item
                self.money = self.item.price * self.n_item
            else:
                print("You can not add {} {}s in Machine".format(
                    self.n_item, self.item.name))
                self.n_item = 0    

        # cheeck user selected box
        elif self.option.lower() == 'box':
            self.item = Box()
            self.n_item = int(
                input("How Many {}s do you have ? : ".format(self.item.name)))
            # Check number of box is not exceeded 50    
            if(self.box + self.n_item) <= 50:
                print("Please Place {} {}(s) into Machine.".format(
                    self.n_item, self.option))
                self.box += self.n_item
                self.box_c += self.n_item
                self.money = self.item.price * self.n_item
            else:
                print("You can not add {} {}s in Machine".format(
                    self.n_item, self.item.name))
                self.n_item = 0    

        # It accepts items from user
        if self.n_item != 0 :
            for i in range(self.n_item):
                print("{} accepted".format(self.item.name))

    #payout to: give number of item selected and show total balance till
    def payout(self, anAmount):
        self.balance += anAmount
        print("You added {} {}(s) for ${} each. You have ${}.".format(self.n_item, self.item.name, self.item.price,self.balance))

    # print_receipt to: printing the receipt
    def print_receipt(self):
        print("\n-----Reciept-----\n")
        if self.paper_c != 0:
            o = Paper()
            print("{} {}(s)              ${}".format(self.paper_c, o.name, o.price*self.paper_c))
        if self.bottle_c != 0:
            o = Bottle()
            print("{} {}(s)             ${}".format(self.bottle_c, o.name, o.price*self.bottle_c))
        if self.can_c != 0:
            o = Can()
            print("{} {}(s)                ${}".format(self.can_c, o.name, o.price*self.can_c))
        if self.box_c != 0:
            o = Box()
            print("{} {}(s)                ${}".format(self.box_c, o.name, o.price*self.box_c))

        print("\nNumber of containers	 {}".format(self.box_c+self.can_c+self.bottle_c+self.paper_c))
        print("Amount paid:		 ${}\n".format(self.balance))
        print("Thank you for recycling at FedUni!")

        

