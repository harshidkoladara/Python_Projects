from Container_Recycling_Machine import Container_Recycling_Machine

# Object for Container Recycling Machine
machine = Container_Recycling_Machine()

# loop for run machine
while True:
    user_inp = input("\n(N)ext customer, or (Q)uit? ")
    if user_inp == 'N':
        machine.balance = 0.0
        machine.paper_c = 0
        machine.bottle_c = 0
        machine.box_c = 0
        machine.can_c = 0
        machine.item = None
        machine.n_item = 0
        machine.option = None

        # loop for take items from one user
        while True:
            machine.accept_product()
            if machine.option.lower() == 'stop':
                machine.print_receipt()
                break
            else:
                machine.select_product()
                machine.payout(machine.money)
                machine.item = None
                machine.n_item = 0
                machine.option = None
    elif user_inp == 'Q':
        break
