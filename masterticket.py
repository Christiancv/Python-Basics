TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(number_of_tickets):

    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("Tickets remaining: {}".format(tickets_remaining))
    username = input("What is your name? ")
    ticket_amount = input("hey {}, how many tickets would you like? ".format(username))
    try:
        ticket_amount = int(ticket_amount)
        if ticket_amount > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as e:
        print("oh no! we ran into an issue. {}".format(e))
    else:
        total = calculate_price(ticket_amount)
        print("{}, your total is ${}".format(username, total))
        answer = input("would you like to continue? (Y/N) ")
        if answer.lower() == "y":
            print("Sold!!!")
            tickets_remaining -= ticket_amount
        else:
            print("Thank you anyways {}!".format(username))
print("Sorry, the tickets are sold out!")

