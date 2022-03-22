def display_greeting():
    """ Display Greeting to the user """
    print("***************************************************************************************")
    print("Welcome to this python car sales page. Here, you can select ")
    print("your dream car, and we will tell you how much it costs.")
    print("***************************************************************************************")

def display_prompt():
    """ Display prompts to the user """
    print("What would you like to do? ")
    print("a - Buy a car")
    print("b - Exit")


def get_user_option():
    """ Get the users vehicle type """
    display_prompt()
    user_option = input("> ")

    while user_option == "":
        print("You have to choose from the options listed.")
        display_prompt()
        user_option = input("> ")

    return user_option

def get_car(user_option):
    """ Get the users vehicle make """
    available_cars = dict()

    available_cars[1] = "Honda Civic"
    available_cars[2] = "Toyota Camry"
    available_cars[3] = "Ford Escape"
    available_cars[4] = "Nissan Altima"
    available_cars[5] = "Chevrolet Silverado"

    if user_option == 'b':
        print("Goodbye!")
        quit()
        
    elif user_option == 'a':
        print("")
        print("Choose from this list the car of your choice: ")
        for i in range(len(available_cars)):
            print(f"{i+1}. {available_cars[i+1]}")          
        user_car_option = int(input("> "))

    while user_car_option == "":
        print("")
        print("Choose from this list the car of your choice: ")
        for i in range(len(available_cars)):
            print(f"{i+1}. {available_cars[i+1]}")          
        user_car_option = int(input("> "))
    return available_cars[user_car_option]

def get_car_price(car_type):
    """ Get the users vehicle year """
    car_price = 0
    print("")
    print(f"{car_type} is a great car. Now choose the year of the car to get a price tag.")
    print("The available year for this car is 2008 to 2022. Type a year within this range.")
    user_car_year = int(input("> "))

    while (2008 >= user_car_year <= 2022):
        print("")
        print("The available year for this car is 2008 to 2022. Type a year within this range.")
        user_car_year = int(input("> "))
    
    if user_car_year >= 2008 and user_car_year <= 2010:
        car_price = 8000
    elif user_car_year >= 2011 and user_car_year <= 2013:
        car_price = 10000
    elif user_car_year >= 2014 and user_car_year <= 2016:
        car_price = 12000
    elif user_car_year >= 2017 and user_car_year <= 2019:
        car_price = 14800
    elif user_car_year >= 2020 and user_car_year <= 2022:
        car_price = 20000
    
    return car_price

def get_confirmation(price, car_type, user_option):
    """ This function asks the user to confirm their purchase of the car """
    print("")
    print(f"Awesome. Please confirm your purchase of this vehicle:")
    print(f"\tCar make & model: {car_type}")
    print(f"\tCar price       : ${price}")
    print("")
    print("Do you want to proceed with this purchase? (Y/N)")
    response = input("> ")
    response.lower()

    while response != 'y' and response != 'n':
        print("Please type 'y' for yes or 'n' for no")
        response = input("> ")
        response.lower()

    if response == 'y':
        print("Congratulations to the newest car owner in town! Hope you enjoy your new car.")
    elif response == 'n':
        print("Okay. We will return you to the car list menu.")
        print("")
        return get_car(user_option)


def main():
    display_greeting()

if __name__ == '__main__':
    main()
    user_option = get_user_option()
    car_type = get_car(user_option)
    price = get_car_price(car_type)
    get_confirmation(price, car_type, user_option)