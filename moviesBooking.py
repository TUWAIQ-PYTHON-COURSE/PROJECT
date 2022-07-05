from availableMovies import *
from moviesShowtime import *
class Booking():
    def __init__(self):
        self = self
        
    def allMovies(self) -> str :
        '''This method returns all movies currently available'''
        print('****** The available movies ******')
        print(all_movies_str)
        self.city()

    def city(self) -> str :
        '''This method returns all available cities'''
        print('\n\n****** The available cities ******')
        print(available_cities_str)
        self.theater()

    def theater(self) -> str :
        '''this method returns all available theaters based on the chosen city'''
        try:
            user_city : int = int(input('\nChoose your city : '))
            if user_city == 1:
                print('\n****** Riyadh Theaters ******')
                print(riyadh_theaters_str)
                self.riyadhMovies()

            if user_city == 2:
                print('\n****** Jeddah Theaters ******')
                print(jeddah_theaters_str)
                self.jeddahMovies()

            if user_city == 3:
                print('\n****** There is only one theater ******')
                self.dammamMovies()

            if user_city == 4:
                print('\n***** There is only one theater *****')
                self.jubailMovies()
            
            if user_city == 5:
                print('\n***** There is only one theater *****')
                self.tabukMovies()
            
            if user_city == 6:
                print('\n***** There is only one theater *****')
                self.hailMovies()

            if user_city > 6 or user_city <= 0:
                print('The city is not Found, Please enter your city again')
                self.theater()

        except:
            print('Invalit input, please enter an integer number')
            self.theater()

    def riyadhMovies(self) -> str:
        '''this method returns all available movies based on the chosen theater'''
        try:
            user_theater : int = int(input('\nChoose your theater : '))
            if user_theater == 1:
                print('\n****** The Roof Movies ******')
                print(theRoof_movies_str)
                self.showtimes()

            if user_theater == 2:
                print('\n****** The Esplanade Movies ******')
                print(theEsplanade_movies_str)
                self.showtimes()

            if user_theater == 3:
                print('\n****** Kingdom Center Movies ******')
                print(kingdomCenter_movies_str)
                self.showtimes()

            if user_theater == 4:
                print('\n****** Riyadh Front Movies *******')
                print(riyadhFront_movies_str)
                self.showtimes()

            if user_theater == 5:
                print('\n****** Riyadh Park Movies ******')
                print(riyadhPark_movies_str)
                self.showtimes()

            if user_theater > 5 or user_theater <= 0:
                print('The theater is not Found, Please enter your theater again')
                self.riyadhMovies()

        except:
            print('Invalit input, please enter an integer number')
            self.riyadhMovies()

    def jeddahMovies(self) -> str:
        '''this method returns all available movies based on the chosen theater'''
        try:
            user_theater : int = int(input('\nChoose your theater : '))
            if user_theater == 1:
                print('\n****** The Red Sea Movies ******')
                print(redSea_movies_str)
                self.showtimes()

            if user_theater == 2:
                print('\n****** Town Square Movies ******')
                print(townSquare_movies_str)
                self.showtimes()

            if user_theater > 2 or user_theater <= 0:
                print('The theater is not Found, Please enter your theater again')
                self.jeddahMovies()

        except:
            print('Invalit input, please enter an integer number')
            self.jeddahMovies()

    def dammamMovies(self) -> str :
        '''this method returns all available movies in Dammam'''
        print('****** The West Avenue Mall Movies ******')
        print(theWestAvenueMall_movies_str)
        self.showtimes()

    def jubailMovies(self) -> str :
        '''this method returns all available movies in Jubail'''
        print('****** Jubail Galleria Mall Movies ******')
        print(jubailGalleriaMall_movies_str)
        self.showtimes()
    
    def tabukMovies (self) -> str :
        '''this method returns all available movies in Tabuk'''
        print('****** Tabuk Park Movies ******')
        print(tabukPark_movies_str)
        self.showtimes()
    
    def hailMovies (self) -> str :
        '''this method returns all available movies in Hail'''
        print('****** Hail Square Movies ******')
        print(hailSquare_movies_str)
        self.showtimes()

    def showtimes(self) -> str :
        '''This method displays movie showtimes based on the entered movie code'''
        try:
            movie_code : int = int(input("\nPlease enter the movie code to display tha available showtimes : "))
            if movie_code == 893:
                print('\nElvis showtimes')
                print(elvis_sunday_string)
                print(elvis_monday_string)
                print(elvis_tuesday_string)
                print(elvis_wednesday_string)
                print(elvis_thursday_string)
                print(elvis_friday_string)
                print(elvis_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 763:
                print('\nThe gray man showtimes')
                print(theGrayMan_sunday_string)
                print(theGrayMan_monday_string)
                print(theGrayMan_tuesday_string)
                print(theGrayMan_wednesday_string)
                print(theGrayMan_thursday_string)
                print(theGrayMan_friday_string)
                print(theGrayMan_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 871:
                print('\nCrimes of the future showtimes')
                print(crimeOfTheFuture_sunday_string)
                print(crimeOfTheFuture_monday_string)
                print(crimeOfTheFuture_tuesday_string)
                print(crimeOfTheFuture_wednesday_string)
                print(crimeOfTheFuture_thursday_string)             
                print(crimeOfTheFuture_friday_string)
                print(crimeOfTheFuture_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 128:
                print('\nLast seen alive showtimes')
                print(lastSeenAlive_sunday_string)
                print(lastSeenAlive_monday_string)
                print(lastSeenAlive_tuesday_string)
                print(lastSeenAlive_wednesday_string)
                print(lastSeenAlive_thursday_string)
                print(lastSeenAlive_friday_string)
                print(lastSeenAlive_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 342:
                print('\nTop gun showtimes')
                print(topGun_sunday_string)
                print(topGun_monday_string)
                print(topGun_tuesday_string)
                print(topGun_wednesday_string)
                print(topGun_thursday_string)
                print(topGun_friday_string)
                print(topGun_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 428:
                print('\nMINIONS showtimes')
                print(MINIONS_sunday_string)
                print(MINIONS_monday_string)
                print(MINIONS_tuesday_string)
                print(MINIONS_wednesday_string)
                print(MINIONS_thursday_string)
                print(MINIONS_friday_string)
                print(MINIONS_saturday_string)
                self.chooseShowtime(movie_code)
            if movie_code == 905:
                print('\nThe black phone showtimes')
                print(theBlackPhone_sunday_string)
                print(theBlackPhone_monday_string)
                print(theBlackPhone_tuesday_string)
                print(theBlackPhone_wednesday_string)
                print(theBlackPhone_thursday_string)
                print(theBlackPhone_friday_string)
                print(theBlackPhone_saturday_string)
                self.chooseShowtime(movie_code)

            if movie_code == 562 :
                print('\nBERGEN showtimes')
                print(BERGEN_sunday_string)
                print(BERGEN_monday_string)
                print(BERGEN_tuesday_string)
                print(BERGEN_wednesday_string)
                print(BERGEN_thursday_string)
                print(BERGEN_friday_string)
                print(BERGEN_saturday_string)
                self.chooseShowtime(movie_code)

            if movie_code != 893 and movie_code != 763 and movie_code != 871 and movie_code != 128 and movie_code != 342 and movie_code != 428 and movie_code != 905 and movie_code != 562:
                print('The movie is not Found, Please enter your movie code again')
                self.showtimes()
        except:
            print('Invalit input, please enter an integer number')
            self.showtimes()

    def chooseShowtime(self, movie_code : int ) -> str :
        '''This method validates the chosen showtime'''
        self.movie_code = movie_code
        try:
            showtime = float(input('\nPlease enter your movie showtime : For example 2.3 .. '))
            if 1.1 <= showtime <= 1.3 or 2.1 <= showtime <= 2.4 or 3.1 <= showtime <= 3.5 or 4.1 <= showtime <= 4.4 or 5.1 <= showtime <= 5.5 or 6.1 <= showtime <= 6.5 or 7.1 <= showtime <= 7.3:
                self.screen_and_numberOfTickets(movie_code)
            else:
                print('The showtime is not Found, Please enter your movie showtime again')
                self.chooseShowtime(movie_code)

        except:
            print('Invalid input, please enter an float number')
            self.chooseShowtime(movie_code)

    def screen_and_numberOfTickets(self, movie_code : int ) -> str :
        '''This method asks the user about the type of theater screen and the number of tickets, then validates user entries'''
        self.movie_code = movie_code
        print('\n*** Theater Screen ***')
        print('Max, Gold, Standard')
        try:
            screen : str = input('\nPlease choose the screen you want : ')
            if screen == 'gold' or screen == 'Gold':
                number_of_ticket : int = int(input('Please enter the number of tickets : '))
                if 0 < number_of_ticket <= 32:
                    self.checkAge(movie_code)
                else:
                    print('The number of tickets must be at least 1 and at most 32')
                    self.screen_and_numberOfTickets(movie_code)
            if screen == 'max' or screen == 'Max':
                number_of_ticket : int = int(input('Please enter the number of tickets : '))
                if 0 < number_of_ticket <= 275:
                    self.checkAge(movie_code)
                else:
                    print('The number of tickets must be at least 1 and at most 275')
                    self.screen_and_numberOfTickets(movie_code)
            if screen == 'standard' or screen == 'Standard':
                number_of_ticket : int = int(input('Please enter the number of tickets : '))
                if 0 < number_of_ticket <= 135:
                    self.checkAge(movie_code)
                else:
                    print('The number of tickets must be at least 1 and at most 135')
                    self.screen_and_numberOfTickets(movie_code)
            if screen != 'gold' and screen != 'Gold' and screen != 'max' and screen != 'Max' and screen != 'standard' and screen != 'Standard':
                print('The screen is not Found, Please enter your theater screen again :')
                self.screen_and_numberOfTickets(movie_code)

        except:
            print('Invalid input')
            self.screen_and_numberOfTickets(movie_code)

    def checkAge(self, movie_code : int) -> str:
        '''This method checks whether the user's age is suitable for the movie or not'''
        self.movie_code = movie_code
        try:
            age = int(input('Enter your age : '))
            if movie_code == 893 or movie_code == 763 or movie_code == 871 or movie_code == 905:
                if age < 18:
                    print('This movie is +18, please choose another movie :')
                    self.showtimes()
                else:
                   print('\n****** Booked successfully ******')
            if movie_code == 128 or movie_code == 562:
                if age < 15:
                    print('This movie is +15, please choose another movie :')
                    self.showtimes()
                else:
                    print('\n****** Booked successfully ******')
            if movie_code == 342:
                if age < 12:
                    print('This movie is +12, please choose another movie :')
                    self.showtimes()
                else:
                   print('\n****** Booked successfully ******')
            if movie_code == 428:
                print('\n****** Booked successfully ******')
        except:
            print('Invalid input, please enter an integer number')
            self.checkAge(movie_code)