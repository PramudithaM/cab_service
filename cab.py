import datetime         #import date and time
class CabServic:        #creat Main cab service class
    def __init__(self,name,id_number,address,phone_number,datetime):
        self.name = name
        self.id_number = id_number
        self.address = address
        self.phone_number = phone_number
        self.datetime = datetime

class Car(CabServic):  #creat sub class in car
    def __init__(self, name, id_number, address, phone_number,datetime):  ##call Main calss Variable 
        super().__init__(name, id_number, address, phone_number,datetime)

        car_pass_3 = AdminCar.car_passengers_3  #call adminCar calss Variable 
        car_pass_4 = AdminCar.car_passengers_4

        print("3 Passengers Cars ", car_pass_3 , "4 Passengers Cars",car_pass_4)
        print("If You Want Creat Job Or Release The Job \n Creat Job Enter 'C' And Release The Job Enter 'R'")  #checking creat job or release job
        creat_release = input().lower()

        if creat_release == "c":   #checking creat job or release job
            print("Enter Maximum Number Of Passengers : ")
            carType =  int(input())

            if carType < 4 :  #checking maximum passengers 
                print("3 Passengers Cars ",car_pass_3)
                print("How Many Cars Do You Want :")
                try :         #Exception handling
                    creatCar = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                car_pass_3 = car_pass_3 - creatCar      #delete hair car 
                print("3 Passengers Cars:",car_pass_3, "\n","Welcome...!")

                AdminCar.car_passengers_3 = car_pass_3   #assign new value in admincar class 
            
            elif carType == 4:   #checking maximum passengers
                print("4 Passengers Cars ",car_pass_4)
                print("How Many Cars Do You Want :")
                try :            #Exception handling
                    creatCar = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                car_pass_4 = car_pass_4 - creatCar     #delete hair car 
                print("3 Passengers Cars:",car_pass_4, "\n","Welcome...!")

                AdminCar.car_passengers_4 = car_pass_4    #assign new value in admincar class 
            
            else:
                print("We Have Maximum 4 Passengers Cars Only... \n Please Try Van.... ")
        
        elif creat_release == "r":   #checking creat job or release job
            print("Enter Maximum Number Of Passengers : ")
            carType =  int(input())

            if carType < 4:  #checking maximum passengers 
                print("3 Passengers Cars ",car_pass_3)
                print("How Many Cars Do You Release :")
                try :        #Exception handling
                    creatCar = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                car_pass_3 = car_pass_3 + creatCar    #add release car
                print("3 Passengers Cars:",car_pass_3, "\n","Welcome...!")

                AdminCar.car_passengers_3 = car_pass_3  #assign new value in admincar class 
            
            elif carType == 4:  #checking maximum passengers 
                print("4 Passengers Cars ",car_pass_4)
                print("How Many Cars Do You Release :")
                try :          #Exception handling
                    releaseCar = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                car_pass_4 = car_pass_4 + releaseCar   #add release car
                print("3 Passengers Cars:",car_pass_4, "\n","Welcome...!")

                AdminCar.car_passengers_4 = car_pass_4  #assign new value in admincar class 
            
            else:
                print("Check Again.....")
        
            

class Van(CabServic):   #creat sub class in van
    def __init__(self, name, id_number, address, phone_number,datetime): #call main calss Variable in init function 
        super().__init__(name, id_number, address, phone_number,datetime)

        van_pass_6 = AdminVan.van_passengers_6     #call adminvan calss Variable 
        van_pass_8 = AdminVan.van_passengers_8

        print("6 Passengers Vans ", van_pass_6 , "8 Passengers Vans",van_pass_8)
        print("If You Want Creat Job Or Release The Job \n Creat Job Enter 'C' And Release The Job Enter 'R'")  #checking creat job or release job
        creat_release = input().lower()

        if creat_release == "c":   #checking creat job or release job
            print("Enter Maximum Number Of Passengers : ")
            vanType =  int(input())

            if vanType < 7 : #checking maximum passengers 
                print("6 Passengers Vans ",van_pass_6)
                print("How Many Vans Do You Want :")
                try :        #Exception handling
                    creatVan = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                van_pass_6 = van_pass_6 - creatVan  #delete hair van 
                print("6 Passengers Vans:",van_pass_6, "\n","Welcome...!")

                AdminVan.van_passengers_6 = van_pass_6  #assign new value in adminvan class 
            
            elif vanType > 6 and vanType < 9:   #checking maximum passengers 
                print("8 Passengers Vans ",van_pass_8)
                print("How Many Vans Do You Want :")
                try :                           #Exception handling
                    creatVan = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                van_pass_8 = van_pass_8 - creatVan
                print("8 Passengers Cars:",van_pass_8, "\n","Welcome...!")

                AdminVan.van_passengers_8 = van_pass_8
            
            else:
                print("We Have Maximum 8 Passengers Van... Sorry....  ")
        
        elif creat_release == "r":  #checking creat job or release job
            print("Enter Maximum Number Of Passengers : ")
            vanType =  int(input())

            if vanType < 7:   #checking maximum Passengers 
                print("6 Passengers Vans ",van_pass_6)
                print("How Many Vans Do You Release :")
                try :         #Exception handling
                    releaseVan = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                van_pass_6 = van_pass_6 + releaseVan   #delete hair van 
                print("6 Passengers Vans:",van_pass_6, "\n","Welcome...!")

                AdminVan.van_passengers_6 = van_pass_6 #assign new value in adminvan class 
            
            elif vanType > 6 and vanType < 9:  #checking maximum passengers 
                print("12 Passengers Vans ",van_pass_8)
                print("How Many Vans Do You Release :")
                try :                          #Exception handling
                    releaseVan = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                van_pass_8 = van_pass_8 + releaseVan   #delete hair van 
                print("8 Passengers Vans:",van_pass_8, "\n","Welcome...!")

                AdminVan.van_passengers_8 = van_pass_8  #assign new value in adminvan class
            
            else:
                print("Check Again.....")


class Three_Wheeler(CabServic):     #creat sub class in three wheeler
    def __init__(self, name, id_number, address, phone_number,datetime):   #call main calss Variable in init function
        super().__init__(name, id_number, address, phone_number,datetime)

        threee_wheel = AdminThree_wheeler.three_wheeler     #call admin three wheeler calss Variable 

        print("Three Wheeler ", threee_wheel )
        print("If You Want Creat Job Or Release The Job \n Creat Job Enter 'C' And Release The Job Enter 'R'")   #checking creat job or release job
        creat_release = input().lower()

        if creat_release == "c":     #checking creat job or release job
            print("Enter Maximum Number Of Passengers : ") 
            passengers = int(input())
            if passengers < 4 :   #checking maximum passengers 
                print("Three Wheelers :  ",threee_wheel)
                print("How Many Three Wheeler Do You Want :")
                try :            #Exception handling
                    creatThreeWheel = int(input())
                except Exception:
                    print("Enter Number Please... ")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                threee_wheel = threee_wheel - creatThreeWheel   #delete hair three Wheeler
                print("Three Wheelers:",threee_wheel, "\n","Welcome...!")

                AdminThree_wheeler.three_wheeler = threee_wheel   #assign new value in adminthreeWheeler class 

            else :    
                print("Maxium Passenges Of Three Wheelers is 3.. \n","Please Try Car......")
        
        elif creat_release == "r":    #checking creat job or release job
            print("You Release Three Wheelers ") 
            print("Three Wheelers :  ",threee_wheel)
            print("How Many Three Wheeler Do You Release :")
            try :                     #Exception handling
                releaseThreeWheel = int(input())
            except Exception :
                print("Enter Number Please...")

            print(name)
            print(id_number)
            print(address)
            print(phone_number)
            print(datetime)

            threee_wheel = threee_wheel + releaseThreeWheel  #add release three wheeler
            print("Three Wheelers:",threee_wheel, "\n","Welcome...!")

            AdminThree_wheeler.three_wheeler = threee_wheel  #assign new value in admithree wheeler
        
        else:
            print("Check Again..... ")

                

class Truck(CabServic):    #creat sub class in truck
    def __init__(self, name, id_number, address, phone_number,datetime):  #call main calss Variable in init function
        super().__init__(name, id_number, address, phone_number,datetime)

        truck_7ft = AdminTruck.size_7ft      #call admintruck calss Variable
        truck_12ft = AdminTruck.size_12ft

        print("Size 7ft Trucks ", truck_7ft , "Size 12ft Trucks",truck_12ft)
        print("If You Want Creat Job Or Release The Job \n Creat Job Enter 'C' And Release The Job Enter 'R'")   #checking creat job or release job
        creat_release = input().lower()

        if creat_release == "c":   #checking creat job or release job
            print("Enter Truck Size ft :'")
            truckSize =  float(input())

            if truckSize < 8 :   #checking maximum size 
                print("Size 7ft Trucks ",truck_7ft)
                print("How Many Truck Do You Want :")
                try :           #Exception handling
                    creatTruck = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                truck_7ft = truck_7ft - creatTruck   #delete hair Truck
                print("Size 7ft Trucks :",truck_7ft, "\n","Welcome...!")

                AdminTruck.size_7ft = truck_7ft   #assign new value in admitruck class 

            elif truckSize > 7 and truck_12ft < 13:   #checking maximum size 
                print("Size 12ft Trucks ",truck_12ft)
                print("How Many Trucks Do You Want :")
                try :                                 #Exception handling
                    creatTruck = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                truck_12ft = truck_12ft - creatTruck    #delete hair truck 
                print("Size 12ft Trucks :",truck_12ft, "\n","Welcome...!")

                AdminTruck.size_12ft =truck_12ft   #assign new value in admintruck class 
            
            else:
                print("We Have Maximum Size is 12ft....\n", "Please Try To Lorry...")
        
        elif creat_release == "r":    #checking creat job or release job
            print("Enter You Hair Truck Size :'")
            truckSize =  int(input())

            if truckSize < 8 :   #checking maximum size 
                print("Size 7ft Trucks ",truck_7ft)
                print("How Many Truck Do You Releae :")
                try :            #Exception handling
                    releaseTruck = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                truck_7ft = truck_7ft + releaseTruck   #addd hair truck 
                print("Size 7ft Trucks :",truck_7ft, "\n","Welcome...!")

                AdminTruck.size_7ft = truck_7ft   #assign new value in admintruck class 
            
            elif truckSize > 7 and truck_12ft < 13:   #checking maximum size 
                print("Size 12ft Trucks ",truck_12ft)
                print("How Many Trucks Do You Want :")
                try :                                 #Exception handling
                    releaseTruck = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                truck_12ft = truck_12ft + releaseTruck  #add release truck
                print("Size 12ft Trucks :",truck_12ft, "\n","Welcome...!")

                AdminTruck.size_12ft =truck_12ft   #assign new value in admintruck class 
            
            else:
                print("Check Again.....")



class Lorry(CabServic):       #creat sub class in lorry
    def __init__(self, name, id_number, address, phone_number,datetime):   #call main calss Variable in init function
        super().__init__(name, id_number, address, phone_number,datetime)

        lorry_2500 = AdminLorry.load_2500     #call adminlorry calss Variable 
        lorry_3500 = AdminLorry.load_3500

        print("Load 2500Kg Lorrys ", lorry_2500 , "Load 3500Kg Lorrys",lorry_3500)
        print("If You Want Creat Job Or Release The Job \n Creat Job Enter 'C' And Release The Job Enter 'R'")   #checking creat job or release job
        creat_release = input().lower()

        if creat_release == "c":    #checking creat job or release job
            print("Enter Your Load Size In kg :'")
            lorryLoad =  float(input())

            if lorryLoad <= 2500  :    #checking maximum Load size 
                print("Load 2500Kg Lorrys ",lorry_2500)
                print("How Many Lorrys Do You Want :")
                try :                  #Exception handling
                    creatLorry = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                lorry_2500 = lorry_2500 - creatLorry    #delete hair Lorry 
                print("Load 2500Kg Lorrys :",lorry_2500, "\n","Welcome...!")

                AdminLorry.load_2500 = lorry_2500    #assign new value in adminLorry class 
            
            elif lorryLoad > 2500 and lorryLoad < 3500:   #checking maximum Load size 
                print("Load 3500Kg Lorrys ",lorry_3500)
                print("How Many Lorrys Do You Want :")
                try :                                     #Exception handling
                    creatLorry = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                lorry_3500 = lorry_3500 - creatLorry    #delete hair Lorry 
                print("Load 3500Kg Lorrys :",lorry_3500, "\n","Welcome...!")

                AdminLorry.load_3500 =lorry_3500   #assign new value in adminLorry class 
            
            else:
                print("We Have Maximum Load is 3500Kg....\n", "Sorry...")
        
        elif creat_release == "r":   #checking creat job or release job
            print("Enter You Hair Lorry Load Size :'")
            lorrySize =  int(input())

            if lorrySize < 2500 :   #checking maximum Load size 
                print("Load 2500Kg Lorrys ",lorry_2500)
                print("How Many Lorrys Do You Releae :")
                try :               #Exception handling
                    releaseLorry = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                lorry_2500 = lorry_2500 + releaseLorry    #add release lorry
                print("Load 2500Kg Lorrys :",lorry_2500, "\n","Welcome...!")

                AdminLorry.load_2500 = lorry_2500    #assign new value in adminLorry class 
            
            elif lorrySize > 2500 and lorrySize < 3500:   #checking maximum Load size 
                print("Load 3500Kg Lorrys ",lorrySize)
                print("How Many Lorrys Do You Releas :")
                try :                                      #Exception handling
                    releaselorry = int(input())
                except Exception :
                    print("Enter Number Please...")

                print(name)
                print(id_number)
                print(address)
                print(phone_number)
                print(datetime)

                lorry_3500 = lorry_3500 + releaselorry      #add release lorry
                print("Load 3500Kg Lorrys :",lorry_3500, "\n","Welcome...!")

                AdminLorry.load_3500 = lorry_3500    #assign new value in adminLorry class 
            
            else:
                print("Check Again.....")

        



class AdminCar():   #creat class in car
    
    car_passengers_3 = 5   #creat class Variable 
    car_passengers_4 = 5

    

    def carAdd(self):  # creat carAdd function 

        print("If You Add 3 Passengers Car Or 4 Passengers Cars \n","3 Passengers Cars Enter '3' and 4 Passengers Cars Enter '4'")
        carType =  int(input())
        if carType == 3:   # cheak car type 
            print("Passengers 3 Cras : ", self.car_passengers_3)
            print("How Many Cars Add : ")

            try :                #Exception handling
                add_car = int(input())
            except Exception:
                print("Enter Number Please...")

            self.car_passengers_3 = self.car_passengers_3 + add_car    #add car 
            print("Passenger 3 Cars : ", self.car_passengers_3)
        
        elif carType == 4:    # cheak car type 
            print("Passengers 4 Cras : ", self.car_passengers_4)
            print("How Many Cars Add : ")
            try:               #Exception handling
                add_car = int(input())
            except Exception :
                print("Enter Number Please...")

            self.car_passengers_4 = self.car_passengers_4 + add_car  #add car 
            print("Passenger 4 Cars : ", self.car_passengers_4)
        
        else :
            print("Enter Carrect Type...!")

    def carDel(self):   #creat carDel function 
        print("If You Delet 3 Passengers Car Or 4 Passengers Cars \n","3 Passengers Cars Enter '3' and 4 Passengers Cars Enter '4'")
        carType =  int(input())
        if carType == 3:    # cheak car type 
            print("Passengers 3 Cras : ", self.car_passengers_3)
            print("How Many Cars Delet : ")
            try :            #Exception handling
                del_car = int(input())
            except Exception :
                print("Enter Number Please...")
            
            self.car_passengers_3 = self.car_passengers_3 - del_car  #delete car
            print("Passenger 3 Cars : ", self.car_passengers_3)
        
        elif carType == 4:  # cheak car type 
            print("Passengers 4 Cras : ", self.car_passengers_4)
            print("How Many Cars Delet : ")
            try:           #Exception handling
                del_car = int(input())
            except Exception:
                print("Enter Number Please....")

            self.car_passengers_4 = self.car_passengers_4 - del_car    #delete car
            print("Passenger 4 Cars : ", self.car_passengers_4)
        
        else :
            print("Enter Carrect Type...!")
      

class AdminVan():  #creat class in van

    van_passengers_6 = 6   #creat class Variable 
    van_passengers_8 = 8

    

    def vanAdd(self):   # creat vanAdd function 

        print("If You Add 6 Passengers Van Or 8 Passengers Van \n","6 Passengers Vans Enter '6' and 8 Passengers Vans Enter '8'")
        vanType =  int(input())
        if vanType == 6:    # cheak van type 
            print("Passengers 6 Vans : ", self.van_passengers_6)
            print("How Many Vans Add : ")
            try :           #Exception handling
                add_van = int(input())
            except Exception:
                print("Enter Number Please")

            self.van_passengers_6 = self.van_passengers_6 + add_van   #add van 
            print("Passenger 6 Vans : ", self.van_passengers_6)
        
        elif vanType == 8:     # cheak van type 
            print("Passengers 8 Vans : ", self.van_passengers_8)
            print("How Many Vans Add : ")
            try :             #Exception handling
                add_van = int(input())
            except Exception:
                print("Enter Number Please...")

            self.van_passengers_8 = self.van_passengers_8 + add_van    #add van
            print("Passenger 8 Vans : ", self.van_passengers_8)
        
        else :
            print("Enter Carrect Type...!")  

    def vanDel(self): #creat vanDel function 
        print("If You Delete 6 Passengers Van Or 8 Passengers Van \n","6 Passengers Vans Enter '6' and 8 Passengers Vans Enter '8'")
        vanType =  int(input())
        if vanType == 6: # cheak van type 
            print("Passengers 6 Vans : ", self.van_passengers_6)
            print("How Many Vans Delete : ")
            try :        #Exception handling
                del_van = int(input())
            except Exception : 
                print("Enter Number Pelase...")

            self.van_passengers_6 = self.van_passengers_6 - del_van  #delete vqn
            print("Passenger 6 Vans : ", self.van_passengers_6)
        
        elif vanType == 8:   # cheak van type 
            print("Passengers 8 Vans : ", self.van_passengers_8)
            print("How Many Vans Delete : ")
            try :            #Exception handling
                del_van = int(input())
            except Exception :
                print("Enter Number Please...")

            self.van_passengers_8 = self.van_passengers_8 - del_van   #delete van
            print("Passenger 8 Vans : ", self.van_passengers_8)
        
        else :
            print("Enter Carrect Type...!")

class AdminThree_wheeler:  #creat class in three Wheeler

    three_wheeler = 10  #creat  class Variable 

    def three_wheelerAdd(self): # creat three wheeler add function 
        print("Three Wheelers : ", self.three_wheeler)
        print("How Many Three Wheelers Add : ")
        try :                   #Exception handling
            add_three_wheeler = int(input())
        except Exception :
            print("Enter Number Please...")

        self.three_wheeler = self.three_wheeler + add_three_wheeler  #add three wheeler
        print("Three Wheelers : ", self.three_wheeler)

    def three_wheelerDel(self): #creat three wheeler Del function 
        print("Three Wheelers : ", self.three_wheeler)
        print("How Many Three Wheelers Delete : ")
        try :                   #Exception handling
            del_three_wheeler = int(input())
        except Exception :
            print("Enter Number Please...")

        self.three_wheeler = self.three_wheeler - del_three_wheeler  #delete three wheeler
        print("Three Wheelers : ", self.three_wheeler)

class AdminTruck:    #creat class in truck

    size_7ft = 3   #creat class Variable
    size_12ft = 4

    def truckAdd(self):   # creat truckAdd function 

        print("If You Add Size 7ft Truck Or Size 12ft Truck \n","Size 7ft Truck Enter '7' and Size 12ft Truck Enter '12'")
        truckType =  int(input())
        if truckType == 7:    # cheak truck type 
            print("Size 7ft Truck : ", self.size_7ft)
            print("How Many Truck Add : ")
            try :             #Exception handling
                add_truck = int(input())
            except Exception :
                print("Enter Number Please...")

            self.size_7ft = self.size_7ft + add_truck  #add truck
            print("Size 7ft Trucks : ", self.size_7ft)
        
        elif truckType == 12: # cheak truck type 
            print("Size 12ft Truck : ", self.size_12ft)
            print("How Many Truck Add : ")
            try :             #Exception handling
                add_truck = int(input())
            except Exception:
                print("Enter Number Please...")

            self.size_12ft = self.size_12ft + add_truck  #add truck 
            print("Size 12ft Trucks : ", self.size_12ft)
        
        else :
            print("Enter Carrect Type...!") 
        
    def truckDel(self):  #creat truckDel function 
        print("If You Delete Size 7ft Truck Or Size 12ft Truck \n","Size 7ft Truck Enter '7' and Size 12ft Truck Enter '12'")
        truckType =  int(input())
        if truckType == 7:  # cheak truck type
            print("Size 7ft Truck : ", self.size_7ft)
            print("How Many Truck Delete : ")
            try :           #Exception handling
                del_truck = int(input())
            except Exception :
                print("Enter Number Please...")

            self.size_7ft = self.size_7ft - del_truck   #delete truck
            print("Size 7ft Trucks : ", self.size_7ft)
        
        elif truckType == 12:  # cheak truck type 
            print("Size 12ft Truck : ", self.size_12ft)
            print("How Many Truck Delete : ")
            try :              #Exception handling
                del_truck = int(input())
            except Exception :
                print("Enter Number Please...")

            self.size_12ft = self.size_12ft - del_truck   #delete truck
            print("Size 12ft Trucks : ", self.size_12ft)
        
        else :
            print("Enter Carrect Type...!") 



class AdminLorry:     #creat class in lorry

    load_2500 = 2   #creat class Variable 
    load_3500 = 3
    
    def lorryAdd(self):  # creat lorryAdd function 
        print("If You Add Load 2500Kg Lorry Or Load 3500Kg \n","Load 2500Kg Lorry Enter '2500' and Load 3500Kg Lorry Enter '3500'")
        lorryType =  int(input())
        if lorryType == 2500:   # cheak lorry type =
            print("Load 2500Kg Lorry : ", self.load_2500)
            print("How Many Lorry Add : ")
            try :               #Exception handling
                add_lorry = int(input())
            except Exception :
                print("Enter Number Please...")

            self.load_2500 = self.load_2500 + add_lorry   #add lorru
            print("Load 2500Kg Lorry : ", self.load_2500)
        
        elif lorryType == 3500:  # cheak lorry type
            print("Load 3500Kg Lorry : ", self.load_3500)
            print("How Many Lorry Add : ")
            try :               #Exception handling
                add_lorry = int(input())
            except Exception:
                print("Enter Number Please...")

            self.load_3500 = self.load_3500 + add_lorry    #add lorry
            print("Load 3500Kg Lorry : ", self.load_3500)
        
        else :
            print("Enter Carrect Type...!") 

    def lorryDel(self): #creat lorryDel function 
        print("If You Delete Load 2500Kg Lorry Or Load 3500Kg \n","Load 2500Kg Lorry Enter '2500' and Load 3500Kg Lorry Enter '3500'")
        lorryType =  int(input())
        if lorryType == 2500:   # cheak lorry type 
            print("Load 2500Kg Lorry : ", self.load_2500)
            print("How Many Lorry Delete : ")
            try :               #Exception handling
                del_lorry = int(input())
            except Exception :
                print("Enter Number Please...")

            self.load_2500 = self.load_2500 - del_lorry   #delete lorry
            print("Load 2500Kg Lorry : ", self.load_2500)
         
        elif lorryType == 3500:   # cheak lorry type 
            print("Load 3500Kg Lorry : ", self.load_3500)
            print("How Many Lorry Delete : ")
            try :                 #Exception handling
                del_lorry = int(input())
            except Exception :
                print("Enter Number Please...")

            self.load_3500 = self.load_3500 - del_lorry   #delete loory
            print("Load 3500Kg Lorry : ", self.load_3500)
        
        else :
            print("Enter Carrect Type...!")
while True:
    print("Enter User Type:")     
    userType = input().lower()
 
    if userType == "admin":             #checking user type
        print("Enter Vehicle Type : ")
        vehicle_type = input().lower()  

        if vehicle_type == "car":       #checking vehicle add or delete
            print("If You Want Add Or Delete Car \ n", "If You Add Car Enter 'A' and Delete Car Enter 'D'")
            add_delete = input().lower()
     
            if add_delete == 'a':      #checking vehicle add
                admin = AdminCar()     #call the admincar class
                AdminCar.carAdd(admin) #call admincar class and call caradd function

            elif add_delete == 'd':     #checking vehicle delete
                admin = AdminCar()      #call the admincar class
                AdminCar.carDel(admin)  #call admincar class and call cardel function

        elif vehicle_type == 'van':
            print("If You Want Add Or Delete Car \ n", "If You Add Van Enter 'A' and Delete Van Enter 'D'")
            add_delete = input().lower()

            if add_delete == 'a':      #checking vehicle add
                admin = AdminVan()     #call the adminvan class
                AdminVan.vanAdd(admin) #call adminvan class and call vanadd function

            elif add_delete == 'd':      #checking vehicle add
                admin = AdminVan()       #call the adminVan class
                AdminVan.vanDel(admin)   #call adminvan class and call vandel function


        elif vehicle_type == 'three wheeler':
            print("If You Want Add Or Delete Three Wheeler \ n", "If You Add Three Wheeler Enter 'A' and Delete Three Wheeler Enter 'D'")
            add_delete = input().lower()

            if add_delete == 'a':                            #checking vehicle add
                admin = AdminThree_wheeler()                 #call the adminthree wheeler class
                AdminThree_wheeler.three_wheelerAdd(admin)   #call adminthree Wheeler class and call three wheeleradd function
        
            elif add_delete == 'd':                         #checking vehicle add
                admin = AdminThree_wheeler()                #call the adminthree wheeler class
                AdminThree_wheeler.three_wheelerDel(admin)  #call adminthree wheeler class and call three wheelerdel function

    
        elif vehicle_type == 'truck':
            print("If You Want Add Or Delete Truck \ n", "If You Add Truck Enter 'A' and Delete Truck Enter 'D'")
            add_delete = input().lower()

            if add_delete == 'a':          #checking vehicle add
                admin = AdminTruck()       #call the admintruck class
                AdminTruck.truckAdd(admin) #call admintruck class and call truckadd function
        
            elif add_delete == 'd':          #checking vehicle add
                admin = AdminTruck()         #call the admintruck class
                AdminTruck.truckDel(admin)   #call admintruck class and call truckdel function


        elif vehicle_type == 'lorry':
            print("If You Want Add Or Delete Lorry \ n", "If You Add Lorry Enter 'A' and Delete Lorry Enter 'D'")
            add_delete = input().lower()

            if add_delete == 'a':               #checking vehicle add
                admin = AdminLorry()            #call the adminlorry class
                AdminLorry.lorryAdd(admin)      #call adminlorry class and call lorryadd function
        
            elif add_delete == 'd':            #checking vehicle add
                admin = AdminLorry()           #call the adminlorry class
                AdminLorry.lorryDel(admin)     #call adminlorry class and call lorrydel function

    elif userType == 'customer':
        print("Enter Customer Name :")     # get Customer data input
        Customer_Name = input()
        print("Enter ID Crad Number :")
        try:                               #Exception handling
            Customer_Id = int(input())
        except Exception:
            print("Enter Number Please...")
            break

        print("Enter Custormer Address :")
        Customer_Address = input()
        print("Enter Customer Phone Number :")
        try:                                #Exception handling 
            Customer_Phone = input()
        except Exception:
            print("Enter number Please..")
            break

        print("We have 5 type of Vehicle \n", "Vehicle Types are Cars,Vans,Three Wheelers,Trucks,Lorrys.....")
        print("Enter Type Of Vehicle :")
        Vehicle_Type = input().lower()

        now = datetime.datetime.now()  #assign date and time in now variable 
        date_time1 = now.strftime("%d-%m-%y %H:%M")  #creat Date time object
    
        if Vehicle_Type == 'car':         # checking Vehicle type and call car class
            customer = Car(Customer_Name,Customer_Id,Customer_Address,Customer_Phone,date_time1)
    
        elif Vehicle_Type == 'van':  # checking Vehicle type and call van class
            customer = Van(Customer_Name,Customer_Id,Customer_Address,Customer_Phone)

        elif Vehicle_Type == 'three wheeler':   # checking Vehicle type and call three wheeler class
            customer = Three_Wheeler(Customer_Name,Customer_Id,Customer_Address,Customer_Phone)

        elif Vehicle_Type == 'truck':    # checking Vehicle type and call truck class
            customer = Truck(Customer_Name,Customer_Id,Customer_Address,Customer_Phone)

        elif Vehicle_Type == 'lorry':    # checking Vehicle type and call lorry class
            customer = Lorry(Customer_Name,Customer_Id,Customer_Address,Customer_Phone)
        else:
            print("Enter Valid Vehicle Type...!")