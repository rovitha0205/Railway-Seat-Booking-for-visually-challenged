import pyttsx3
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def call():
    print("Enter the valid")
    speak("Please enter a valid input")
print("Welcome To Railway Reservation")
speak("Welcome to Railway Reservation")
a = 0
d = 0
o = 0
s = 0
ca = 0
otp = 0
mm = 0
yy = 0
cvv = 0
while o != 28:
    speak("Enter the beginning station number")
    speak("28 is Chennai")
    o = int(input("Enter beginning station number: "))
    if o == 28:
        while a not in [101, 102, 103, 104, 105]:
            speak("101 = Namakkal")
            speak("102 = Salem")
            speak("103 = Aathur")
            speak("104 = Chinna Salem")
            speak("105 = Villupuram")
            print("101 = Namakkal")
            print("102 = Salem")
            print("103 = Aathur")
            print("104 = Chinna Salem")
            print("105 = Villupuram")
            speak("Enter the destination station number")
            a = int(input("Enter destination station number: "))
            if a == 101:
                speak("Enter the number of passengers")
                b = int(input("Enter the number of passengers: "))
                speak("Your destination is Chennai to Namakkal")
                print("Chennai to Namakkal")
                c = b * 400
            elif a == 102:
                speak("Enter the number of passengers")
                b = int(input("Enter the number of passengers: "))
                speak("Your destination is Chennai to Salem")
                print("Chennai to Salem")
                c = b * 350
            elif a == 103:
                speak("Enter the number of passengers")
                b = int(input("Enter the number of passengers: "))
                speak("Your destination is Chennai to Aathur")
                print("Chennai to Aathur")
                c = b * 300
            elif a == 104:
                speak("Enter the number of passengers")
                b = int(input("Enter the number of passengers: "))
                speak("Your destination is Chennai to Chinna Salem")
                print("Chennai to Chinna Salem")
                c = b * 250
            elif a == 105:
                speak("Enter the number of passengers")
                b = int(input("Enter the number of passengers: "))
                speak("Your destination is Chennai to Villupuram")
                print("Chennai to Villupuram")
                c = b * 200
            else:
                call()
        speak("Enter the class you prefer")
        speak("1=First AC")
        speak("2=Second AC")
        speak("3=Third AC")
        speak("4=Sleeper")
        print("1 = First AC")
        print("2 = Second AC")
        print("3 = Third AC")
        print("4 = Sleeper")
        while s not in [1, 2, 3, 4]:
            speak("Enter the class")
            s = int(input("Enter the class: "))
            
            if s == 1:
                print("First AC")
                speak("You preferred 1st AC")
                m = (b * 300) + c
            elif s == 2:
                print("Second AC")
                speak("You preferred 2nd AC")
                m = (b * 200) + c
            elif s == 3:
                print("Third AC")
                speak("You preferred 3rd AC")
                m = (b * 100) + c
            elif s == 4:
                print("Sleeper")
                speak("You preferred Sleeper")
                m = c
            else:
                call()
        speak(f"Your ticket price is {m}")
        print(f"Your ticket price is {m}")
        speak("Enter the mode of payment")
        speak("1=Debit card")
        speak("2=Credit card")
        speak("3=Net banking")
        speak("4=Paying at station")
        print("1 = Debit card")
        print("2 = Credit card")
        print("3 = Net banking")
        print("4 = Paying at station")
        while d not in [1, 2, 3, 4]:
            speak("Enter the mode of payment")
            d = int(input("Enter the mode of payment: "))
            if d == 1:
                print("Debit Card")
                while ca != -1:
                    speak("Enter the last 6 digits of your Debit card")
                    ca = int(input("Enter the last 6 digits of your Debit card: "))
                    if 99999 < ca <= 999999:
                        ca = -1
                        while mm != -1:
                            speak("Enter the Validity month")
                            mm = int(input("Enter the Validity month: "))
                            if 0 < mm < 13:
                                while yy != -1:
                                    mm = -1
                                    speak("Enter the Validity year")
                                    yy = int(input("Enter the Validity year: "))
                                    if 2023 < yy < 2041:
                                        while cvv != -1:
                                            yy = -1
                                            speak("Enter the CVV number")
                                            cvv = int(input("Enter the CVV number: "))
                                            if 99 < cvv < 1000:
                                                while otp != -1:
                                                    cvv = -1
                                                    speak("Enter the 4 digit OTP received by your Mobile number")
                                                    otp = int(input("Enter the 4 digit OTP received by your Mobile number: "))
                                                    if 999 < otp <= 9999:
                                                        otp = -1
                                                        print("Payment has been received")
                                                        speak("Payment has been received")
                                                    else:
                                                        call()
                                            else:
                                                call()
                                    else:
                                        call()
                            else:
                                call()
                    else:
                        call()
            elif d == 2:
                print("Credit Card")
                while ca != -1:
                    speak("Enter the last 6 digits of your Credit card")
                    ca = int(input("Enter the last 6 digits of your Credit card: "))
                    if 99999 < ca <= 999999:
                        ca = -1
                        while mm != -1:
                            speak("Enter the Validity month")
                            mm = int(input("Enter the Validity month: "))
                            if 0 < mm < 13:
                                while yy != -1:
                                    mm = -1
                                    speak("Enter the Validity year")
                                    yy = int(input("Enter the Validity year: "))
                                    if 2023 < yy < 2041:
                                        while cvv != -1:
                                            yy = -1
                                            speak("Enter the CVV number")
                                            cvv = int(input("Enter the CVV number: "))
                                            if 99 < cvv < 1000:
                                                while otp != -1:
                                                    cvv = -1
                                                    speak("Enter the 4 digit OTP received by your Mobile number")
                                                    otp = int(input("Enter the 4 digit OTP received by your Mobile number: "))
                                                    if 999 < otp <= 9999:
                                                        otp = -1
                                                        print("Payment has been received")
                                                        speak("Payment has been received")
                                                    else:
                                                        call()
                                            else:
                                                call()
                                    else:
                                        call()
                            else:
                                call()
                    else:
                        call()
            elif d == 3:
                print("Net Banking")
                speak("Currently Net Banking service is not available")
                print("Currently service is not available")
            elif d == 4:
                print("Pay at station")
                speak("Pay the amount at the station before three hours for your travel")
            else:
                call()
        speak("Your seats have been confirmed")
        print("Your seats have been confirmed")
        speak("Please share your feedback")
        speak("1=Poor")
        speak("2=Need improvement")
        speak("3=Good")
        speak("4=Very good")
        speak("5=Excellent")
        print("1 = Poor")
        print("2 = Need improvement")
        print("3 = Good")
        print("4 = Very good")
        print("5 = Excellent")
        while m not in [1, 2, 3, 4, 5]:
            speak("Enter your rating")
            m = int(input("Enter your Rating: "))
            if m in [1, 2]:
                print("Thank you for your feedback. We are enhancing our platform")
                speak("Thank you for your feedback. We are enhancing our platform")
            elif m in [3, 4, 5]:
                print("Thank you for your feedback")
                speak("Thank you for your feedback")
            else:
                call()
        print("Thank you for contacting us. Have a nice day")       
        speak("Thank you for contacting us. Have a nice day")
    else:
        call()
print("********HAPPY JOURNEY***********")
speak("********HAPPY JOURNEY***********")
