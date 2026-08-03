import json
import os
import socket
import ssl 


print("\n********************The Client Has Started******************** \n")


server_address = ("127.0.0.1", 52499)

Csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(Csock,
                           ca_certs="mycert.pem",
                           cert_reqs=ssl.CERT_REQUIRED)

Csock = ssl_sock
Csock.connect(server_address)
my_name = input("Enter client name: ")
Csock.send(my_name.encode('ascii'))
arr_icao = input("\nEnter the airport code:").upper()
Csock.send(arr_icao.encode('ascii'))

while True:
    print("\nSelect an Option:\n"
          "1. Display all arrived flights details.\n"
          "2. Display all delayed flights details.\n"
          "3. Display all flights coming from a specific city\n"
          "4. Display all details of particular flight\n"
          "5. Quit.\n")

    number = input("Sending number: ")
    Csock.sendall(number.encode('ascii'))
    if int(number) == 1:
        print("All arrived flights : ")
        Directory = r'{}\client_{}'.format(os.getcwd(), my_name)
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        
        with open(file_path, 'wb') as file:
            recvfile = Csock.recv(10485760)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Arrival Time : {}, "
                      "Terminal : {}, Gate : {}".format(flight['flight']['iata'],
                                                        flight['departure']['airport'],
                                                        flight['arrival']['actual'],
                                                        flight['arrival']['terminal'],
                                                        flight['arrival']['gate']))

    elif int(number) == 2:
        print("All delayed flights : ")
        Directory = r'{}\client_{}'.format(os.getcwd(), my_name)
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:
            recvfile = Csock.recv(1048576)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, "
                      "Departure Time : {}, Estimated Arrival Time : {}, "
                      "Terminal : {}, Gate : {}".format(flight['flight']['iata'],
                                                        flight['departure']['airport'],
                                                        flight['departure']['actual'],
                                                        flight['arrival']['estimated'],
                                                        flight['arrival']['terminal'],
                                                        flight['arrival']['gate']))

    elif int(number) == 3:
        cityName = input("Enter city code: ").upper()
        Csock.sendall(cityName.encode('ascii'))
        print("All flights coming from {}: ".format(cityName))
        Directory = r'{}\client_{}\city_{}'.format(os.getcwd(), cityName, cityName)
        if not os.path.exists(Directory):
            os.mkdir(Directory)
        file_path = Directory + '/G2.json'

        with open(file_path, 'wb') as file:
            recvfile = Csock.recv(1048576)
            file.write(recvfile)

        with open(file_path) as file:
            flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data["data"]:
                print("\nFlight code (IATA) : {}\nDeparture Airport : {}, Departure Time : {}, "
                      "Estimated Arrival Time : {}, Terminal : {}, "
                      "Gate : {}".format(flight['flight']['iata'],
                                         flight['departure']['airport'],
                                         flight['departure']['actual'],
                                         flight['arrival']['estimated'],
                                         flight['arrival']['terminal'],
                                         flight['arrival']['gate']))

    elif int(number) == 4:
        flightNum = input("Enter flight number: ")
        Csock.sendall(flightNum.encode('ascii'))

        print("DETAILS OF FLIGHT {}".format(flightNum))
        Directory = r'{}\client_{}\flight_{}'.format(os.getcwd(), my_name, flightNum)

        if not os.path.exists(Directory):
            os.mkdir(Directory)
            file_path = Directory + '/G2.json'

            with open(file_path, 'wb') as file:
                recvfile = Csock.recv(1035)
                file.write(recvfile)

                with open(file_path) as file:
                    flight_Data = json.load(file)  # Convert the JSON data into python objects
            for flight in flight_Data['data']:
                print("\nFlight code (IATA) : {},    Date : {},\nDeparture Airport : {}, "
                      "Departure Gate : {}, Departure Terminal : {}, \nArrival Airport : {}, "
                      "Arrival Gate : {}, Arrival Terminal : {}, Status : {}, Scheduled Departure Time"
                      " : {}, Scheduled Arrival Time : {}, Estimated Arrival Time : {}, delay : {}"
                      .format(flight['flight']['iata'], flight['flight_date'],
                              flight['departure']['airport'], flight['departure']['gate'],
                              flight['departure']['terminal'], flight['arrival']['airport'],
                              flight['arrival']['gate'], flight['arrival']['terminal'],
                              flight['flight_status'], flight['departure']['scheduled'],
                              flight['arrival']['scheduled'], flight['arrival']['estimated'],
                              flight['arrival']['delay']))

    elif int(number) == 5:
        print(Csock.recv(1024).decode('ascii'))  # Client receives goodbye
        print("\nClient closed\n" + 25 * "=")
        break

    else:
        print(Csock.recv(1024).decode('ascii'))  # When client enters a wrong number

Csock.close()
option = input("Sending number: ")
Csock.send(option.encode('ascii'))
