'''
Author: Jay Dempsey
Name: bike_app.py
Purpose: Kopis_Exercise
'''


# Def the main function used to start the application
def main():
    #Define setting variables used to customize the application. These variables were put here for reset purposes
    criteria_setting = 0
    t_setting = 1
    h_setting = 1
    o_setting = 1
    w_setting = 1
    feedback_setting = 0

    #Call the menu function
    menu(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# All of the functions in this comment block are used for error handling user inputs and setting high/low values
#######################################################################################################################
def check_menu_option():
    # Take user input to control the startup functionality of the app
    option = input("Hello! Welcome to the bike app! Would you like to check today's conditions, \n"
                   "use our forecast option, or choose whats important for your bike riding experience?\n"
                   " (T=today, F=forecast, C=custom) \n")

    # This while loop is used to ensure only acceptable input is entered
    while True:
        if option in ("F", "f", "T", "t", "C", "c"):
            return option
            break
        else:
            print("Invalid input")
            option = input("Hello! Welcome to the bike app! Would you like to check today's conditions, \n"
                   "use our forecast option, or choose whats important for your bike riding experience?\n"
                   " (T=today, F=forecast, C=custom) \n")
def check_temp():
    # This while loop ensures that a integer is entered
    while True:
        try:
            temp = int(input("Enter temperature during time of ride: \n"))
            return temp
            break
        except ValueError:
            print("Invalid input")
def check_hum():
    # This while loop ensures that a integer is entered
    while True:
        try:
            humidity = int(input("Enter humidity at time of ride: \n"))
            return humidity
            break
        except ValueError:
            print("Invalid input")
def check_over():
    # Take overcast input
    over = input("Enter expected overcast at time of ride (S=Sunny, C=Cloudy, R=Rain, T=Thunderstorm: \n")

    # This while loop is used to ensure only acceptable input is entered
    while True:
        if over in ("S", "s", "R", "r", "T", "t", "C", "c"):
            return over
            break
        else:
            print("Invalid input")
            over = input("Enter expected overcast at time of ride (S=Sunny, C=Cloudy, R=Rain, T=Thunderstorm: \n")
def check_wind():
    # This while loop ensures that a integer is entered
    while True:
        try:
            wind = int(input("Enter expected wind speeds (mph) at time of ride: \n"))
            return wind
            break
        except ValueError:
            print("Invalid input")
def check_forecast_option():
    # Takes response from user
    f_option = input("Would you like to check the 7 day forecast using these same preferences? (Y=Yes, N=No)\n")

    # This while loop is used to ensure only acceptable input is entered
    while True:
        if f_option in ("Y", "y", "Yes", "yes"):
            f = 1
            return f
            break
        elif f_option in ("N", "n", "No", "no"):
            f = 0
            return f
            break
        else:
            print("Invalid input")
            f_option = input("Would you like to check the 7 day forecast using these same preferences? (Y=Yes, N=No)\n")
def check_temp_criteria():
    # Takes input from the user when asked if temperature is relevant to their riding conditions
    c_temp = input("Temperature at ride time? ")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if c_temp in ("Y", "y", "Yes", "yes"):
            t = 1
            return t
            break
        elif c_temp in ("N", "n", "No", "no"):
            t = 0
            return t
            break
        else:
            print("Invalid input")
            c_temp = input("Temperature at ride time? ")
def check_hum_criteria():
    # Takes input from the user when asked if humidity is relevant to their riding conditions
    c_hum = input("Humidity at ride time? ")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if c_hum in ("Y", "y", "Yes", "yes"):
            h = 1
            return h
            break
        elif c_hum in ("N", "n", "No", "no"):
            h = 0
            return h
            break
        else:
            print("Invalid input")
            c_hum = input("Humidity at ride time? ")
def check_over_criteria():
    # Takes input from the user when asked if overcast is relevant to their riding conditions
    c_over = input("Overcast at ride time? ")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if c_over in ("Y", "y", "Yes", "yes"):
            o = 1
            return o
            break
        elif c_over in ("N", "n", "No", "no"):
            o = 0
            return o
            break
        else:
            print("Invalid input")
            c_over = input("Overcast at ride time? ")
def check_wind_criteria():
    # Takes input from the user when asked if wind is relevant to their riding conditions
    c_wind = input("Wind at ride time? ")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if c_wind in ("Y", "y", "Yes", "yes"):
            w = 1
            return w
            break
        elif c_wind in ("N", "n", "No", "no"):
            w = 0
            return w
            break
        else:
            print("Invalid input")
            c_wind = input("Wind at ride time? ")
def check_custom_menu():
    # This c_option variable is used to determine if the user wants to check just today's conditions
    # or use the 7 day forecast option
    c_option = input("Now that your preferences have been modified would you like to check today's riding conditions "
                     "or the seven day forecast? (T=Today, F=Forecast)\n")

    # This while loop is used to ensure only acceptable input is entered
    while True:
        if c_option in ("T", "t", "F", "f"):
            return c_option
            break
        else:
            print("Invalid input")
            c_option = input("Now that your preferences have been modified would you like to check today's riding "
                             "conditions or the seven day forecast? (T=Today, F=Forecast)\n")
def check_feedback():
    # This input is used to determine if calculations should be modified to better fit the users opinions
    feedback = input("Would you agree with our assessment of today's biking conditions? (Y/N)")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if feedback in ("Y", "y", "Yes", "yes"):
            f = 1
            return f
            break
        elif feedback in ("N", "n", "No", "no"):
            f = 0
            return f
            break
        else:
            print("Invalid input")
            feedback = input("Would you agree with our assessment of today's biking conditions? (Y/N)")
def check_better_worse(criteria_setting):
    # Ask the user if what they would change
    print("If any of the following criteria stood out please select if you think it made the conditions better or worse.\n"
          " If it was not significant enough to change please select 'Accurate' (B=Better, W=Worse, A=Accurate) ")

    # If a criteria setting that has temp low is selected set temp to "A"
    if (criteria_setting >= 1 and criteria_setting <= 7):
        temp = "A"
    else:
        # Take inputs for each value and ensure a valid input
        temp = input("Temperature?")
        while True:
            if temp not in ("B", "b", "W", "w", "A", "a"):
                print("Invalid input")
                temp = input("Temperature?")
            else:
                break

    # If a criteria setting that has humidity low is selected set hum to "A"
    if ((criteria_setting >= 1 and criteria_setting <= 3) or (criteria_setting >= 8 and criteria_setting <= 11)):
        hum = "A"
    else:
        hum = input("Humidity?")
        while True:
            if hum not in ("B", "b", "W", "w", "A", "a"):
                print("Invalid input")
                hum = input("Humidity?")
            else:
                break

    # If a criteria setting that has overcast low is selected set over to "A"
    if (criteria_setting == 1 or criteria_setting == 4 or criteria_setting == 5 or criteria_setting == 8
            or criteria_setting == 9 or criteria_setting == 12 or criteria_setting == 13):
        over = "A"
    else:
        over = input("Overcast?")
        while True:
            if over not in ("B", "b", "W", "w", "A", "a"):
                print("Invalid input")
                over = input("Overcast?")
            else:
                break

    # If a criteria setting that has wind low is selected set wind to "A"
    if (criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 6 or criteria_setting == 8
            or criteria_setting == 10 or criteria_setting == 12 or criteria_setting == 14):
        wind = "A"
    else:
        wind = input("Wind?")
        while True:
            if wind not in ("B", "b", "W", "w", "A", "a"):
                print("Invalid input")
                wind = input("Wind?")
            else:
                break

    # Return all of the values
    return [temp, hum, over, wind]
def check_redo():
    # Checks to see if the user would like to re-run the app with updated conditions
    redo = input("Would you like to re-run our app with updated conditions?")

    # This while loop is used to ensure only acceptable input is entered and sets the return value high/low
    while True:
        if redo in ("Y", "y", "Yes", "yes"):
            r = 1
            return r
            break
        elif redo in ("N", "n", "No", "no"):
            r = 0
            return r
            break
        else:
            print("Invalid input")
            redo = input("Would you like to re-run our app with updated conditions?")
def check_feedback_setting(t_setting, h_setting, o_setting, w_setting):
    # Checks to see if any feedback has been given based on changed calculation variables
    if (t_setting != 1 or h_setting != 1 or o_setting != 1 or w_setting != 1):
        setting = 1
        return setting
    else:
        setting = 0
        return setting
def check_reset():
    # Checks to see if the user would like reset the custom settings or keep them
    reset = input("Would you like to reset your custom settings and feedback? (Y/N)\n")

    # Ensures valid input and returns a high/low value
    while True:
        if reset in ("Y", "y", "Yes", "yes"):
            r = 1
            return r
            break
        elif reset in ("N", "n", "No", "no"):
            r = 0
            return r
            break
        else:
            print("Invalid input")
            reset = input("Would you like to reset your custom settings and feedback? (Y/N)\n")
#######################################################################################################################


# This functions takes in the input values for the criteria and the necessary
# corresponding setting to perform the correct calculations
def custom_calculations(t, h, o, w, criteria_setting, t_setting, h_setting, o_setting, w_setting):

    # All of the following if statements include the point allocating systems that correspond to the criteria setting
    # a table that shows what values are high for each criteria setting is included in the supporting documentation

    # Point values are based off of a 25 point max.
    # The setting variables used for calculations below are changed based on user feedback

    # If a criteria setting that has temp low is selected set temp_calc to 0
    if (criteria_setting >= 1 and criteria_setting <= 7):
        temp_calc = 0
    # Checks the quality of temperature
    else:
        if (t >= 90):
            temp_calc = 16.66 * t_setting
        elif (t >= 60 and t <= 89):
            temp_calc = 25 * t_setting
        elif (t >= 40 and t <= 59):
            temp_calc = 8.33 * t_setting
        elif (t <= 39):
            temp_calc = 4.33 * t_setting

    # If a criteria setting that has humidity low is selected set hum_calc to 0
    if ((criteria_setting >= 1 and criteria_setting <= 3) or (criteria_setting >= 8 and criteria_setting <= 11)):
        hum_calc = 0
    else:
        # Checks the quality of humidity
        if (h >= 50):
            hum_calc = 4.33 * h_setting
        elif (h >= 30 and h <= 49):
            hum_calc = 25 * h_setting
        elif (h >= 21 and h <= 29):
            hum_calc = 16.66 * h_setting
        elif (h <= 20):
            hum_calc = 8.33 * h_setting

    # If a criteria setting that has overcast low is selected set over_calc to 0
    if (criteria_setting == 1 or criteria_setting == 4 or criteria_setting == 5 or criteria_setting == 8
            or criteria_setting == 9 or criteria_setting == 12 or criteria_setting == 13):
        over_calc = 0
    else:
        # Checks the overcast
        if (o == "S" or o == "s"):
            over_calc = 25 * o_setting
        elif (o == "C" or o <= "c"):
            over_calc = 16.66 * o_setting
        elif (o == "R" or o == "r"):
            over_calc = 8.33 * o_setting
        elif (o == "T" or o == "t"):
            over_calc = 4.33 * o_setting

    # If a criteria setting that has wind low is selected set wind_calc to 0
    if (criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 6 or criteria_setting == 8
            or criteria_setting == 10 or criteria_setting == 12 or criteria_setting == 14):
        wind_calc = 0
    else:
        # Checks the quality of the wind
        if (w >= 30):
            wind_calc = 4.33 * w_setting
        elif (w >= 16 and w <= 29):
            wind_calc = 8.33 * w_setting
        elif (w >= 6 and w <= 15):
            wind_calc = 16.66 * w_setting
        elif (w <= 5):
            wind_calc = 25 * w_setting

    # Take the sum of the calculations
    total = temp_calc + hum_calc + over_calc + wind_calc

    #print(total)

    # Return the total to be used for condition readings.
    return total


# This function is used to determining the riding conditions of a custom day (today)
# based on the users preferred criteria
def todays_custom_conditions(total, temp, humidity, overcast, wind, criteria_setting, t_setting, h_setting, o_setting,
                             w_setting, feedback_setting):

    # This scale is based on all criteria being active
    if (criteria_setting == 0):

        # The totals are based on a 100 point scale. Since there are 5 different riding conditions, the totals are
        # divided into 5 different point ranges.

        # If the total is >= 80 then the riding conditions are "excellent"
        if (total >= 80):
            print("Today's biking conditions are excellent!")
            
            # On excellent riding days the conditions will be recorded to a text file for the user to look back on
            file = open("todays_conditions.txt", "w")
            intro_text = "The details of your ideal day have been recorded here:"
            text_space = "\n"
            temp_text = "The temperature at time of ride was: {}\n".format(temp)
            hum_text = "The humidity at time of ride was: {}\n".format(humidity)
            over_text = "The overcast at time of ride was: {}\n".format(overcast)
            wind_text = "The wind at time of ride was: {}\n".format(wind)
            file.write(intro_text)
            file.write(text_space)
            file.write(temp_text)
            file.write(hum_text)
            file.write(over_text)
            file.write(wind_text)
            file.close()
        # If the total is between 60-80 then the conditions are "good" since these aren't the "best" days their details
        # are not recorded
        elif (total >= 60 and total < 80):
            print("Today's biking conditions are good.")
        # If the total is between 40-60 then the conditions are "average"
        elif (total >= 40 and total < 60):
            print("Today's biking conditions are average.")
        # If the total is between 20-40 then the conditions are "bad"
        elif (total >= 20 and total < 40):
            print("Today's biking conditions are bad.")
        # If the total is less than 20 then the conditions are "terrible"
        elif (total < 20):
            print("Today's biking conditions are terrible.")
    # This scale is based on only 3 criteria being used
    elif (criteria_setting == 7 or criteria_setting == 11 or criteria_setting == 13 or criteria_setting == 14):

        # The totals are based on a 75 (3/4 of original point scale) point scale. Since there are 5 different riding
        # conditions, the totals are divided into 5 different point ranges.

        # If the total is >= 60 then the riding conditions are "excellent"
        if (total >= 60):
            print("Today's biking conditions are excellent!")

            # On excellent riding days the conditions will be recorded to a text file for the user to look back on
            file = open("todays_conditions.txt", "w")
            intro_text = "The details of your ideal day have been recorded here:"
            text_space = "\n"
            temp_text = "The temperature at time of ride was: {}\n".format(temp)
            hum_text = "The humidity at time of ride was: {}\n".format(humidity)
            over_text = "The overcast at time of ride was: {}\n".format(overcast)
            wind_text = "The wind at time of ride was: {}\n".format(wind)
            file.write(intro_text)
            file.write(text_space)
            file.write(temp_text)
            file.write(hum_text)
            file.write(over_text)
            file.write(wind_text)
            file.close()
        # If the total is between 45-60 then the riding conditions are "good"
        elif (total >= 45 and total < 60):
            print("Today's biking conditions are good.")
        # If the total is between 30-45 then the riding conditions are "average"
        elif (total >= 30 and total < 45):
            print("Today's biking conditions are average.")
        # If the total is between 15-30 the conditions are "bad"
        elif (total >= 15 and total < 30):
            print("Today's biking conditions are bad.")
        # If the total is < 15 the conditions are "terrible"
        elif (total < 15):
            print("Today's biking conditions are terrible.")
    # This scale is based on only 2 criteria being used
    elif (criteria_setting == 3 or criteria_setting == 5 or criteria_setting == 6 or criteria_setting == 9
            or criteria_setting == 10 or criteria_setting == 12):

        # The totals are based on a 50 (1/2 of original point scale) point scale. Since there are 5 different riding
        # conditions, the totals are divided into 5 different point ranges.

        # If the total is >= 40 the riding conditions are "excellent"
        if (total >= 40):
            print("Today's biking conditions are excellent!")

            # On excellent riding days the conditions will be recorded to a text file for the user to look back on
            file = open("todays_conditions.txt", "w")
            intro_text = "The details of your ideal day have been recorded here:"
            text_space = "\n"
            temp_text = "The temperature at time of ride was: {}\n".format(temp)
            hum_text = "The humidity at time of ride was: {}\n".format(humidity)
            over_text = "The overcast at time of ride was: {}\n".format(overcast)
            wind_text = "The wind at time of ride was: {}\n".format(wind)
            file.write(intro_text)
            file.write(text_space)
            file.write(temp_text)
            file.write(hum_text)
            file.write(over_text)
            file.write(wind_text)
            file.close()
        # If the total is between 30-40 the riding conditions are "good"
        elif (total >= 30 and total < 40):
            print("Today's biking conditions are good.")
        # If the total is between 20-30 the riding conditions are "average"
        elif (total >= 20 and total < 30):
            print("Today's biking conditions are average.")
        # If the total is between 10-20 the riding conditions are "bad"
        elif (total >= 10 and total < 20):
            print("Today's biking conditions are bad.")
        # If the total is < 10 the riding conditions are "terrible"
        elif (total < 10):
            print("Today's biking conditions are terrible.")
    # This scale is based on only 1 criteria being used
    elif (criteria_setting == 1 or criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 8):

        # When only 1 criteria is being used a 25 (1/4 of original point scale) point scale is used. Note that in order
        # to get a "terrible" condition when only using 1 criteria, the user must submit feedback saying the conditions
        # were "worse" than expected.

        # If total is >= 25 the riding conditions are "Excellent"
        if (total >= 25):
            print("Today's biking conditions are excellent!")

            # On excellent riding days the conditions will be recorded to a text file for the user to look back on
            file = open("todays_conditions.txt", "w")
            intro_text = "The details of your ideal day have been recorded here:"
            text_space = "\n"
            temp_text = "The temperature at time of ride was: {}\n".format(temp)
            hum_text = "The humidity at time of ride was: {}\n".format(humidity)
            over_text = "The overcast at time of ride was: {}\n".format(overcast)
            wind_text = "The wind at time of ride was: {}\n".format(wind)
            file.write(intro_text)
            file.write(text_space)
            file.write(temp_text)
            file.write(hum_text)
            file.write(over_text)
            file.write(wind_text)
            file.close()
        # If the total is between 16.66-25 then the riding conditions are "good"
        elif (total >= 16.66 and total < 25):
            print("Today's biking conditions are good.")
        # If the total is between 8.33-16.66 then the riding conditions are "average"
        elif (total >= 8.33 and total < 16.66):
            print("Today's biking conditions are average.")
        # If the total is between 4.33-8.33 then the riding conditions are "bad"
        elif (total >= 4.33 and total < 8.33):
            print("Today's biking conditions are bad.")
        # If the total is <= 3.25 the riding conditions are "terrible"
        elif (total <= 3.25):
            print("Today's biking conditions are terrible")

    # Ask the user if they agree with the apps conclusion of the riding conditions
    feedback = check_feedback()

    # If the agree with the apps conclusion
    if (feedback == 1):

        # After checking the conditions of today the user has the option to use the same criteria
        # and check the seven day forecast
        c_forecast = check_forecast_option()

        # If the choose to check the 7 day forecast call the forecast_mode function
        if (c_forecast == 1):
            forecast_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)
        # If they choose no then they will be sent back to the menu.
        elif (c_forecast == 0):
            app_end(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)

    # If the user does not agree with the apps conclusion of the riding conditions
    elif (feedback == 0):
        # Check to see if the user thought the day's conditions were better/worse
        bw_temp, bw_hum, bw_over, bw_wind = check_better_worse(criteria_setting)

        # If the user thought the day's temperature conditions were better than the app concluded
        if bw_temp in ("B" "b"):
            # Ensure max setting isn't reached already
            if (t_setting >= 2):
                print("Temperature setting is at the max setting")
            # Update calculation setting variable
            else:
                t_setting = t_setting + 0.25
        # If the user thought the day's temperature conditions were worse than the app concluded
        elif bw_temp in ("W", "w"):
            # Ensure min setting isn't reached already
            if (t_setting <=0):
                print("Temperature setting is at the min setting")
            # Update calculation setting variable
            else:
                t_setting = t_setting - 0.25

        # If the user thought the day's humidity conditions were better than the app concluded
        if bw_hum in ("B", "b"):
            # Ensure max setting isn't reached already
            if (h_setting >= 2):
                print("Humidity setting is at the max setting")
            # Update calculation setting variable
            else:
                h_setting = h_setting + 0.25
        # If the user thought the day's humidity conditions were worse than the app concluded
        elif bw_hum in ("W", "w"):
            # Ensure min setting isn't reached already
            if (h_setting <=0):
                print("Temperature setting is at the min setting")
            # Update calculation setting variable
            else:
                h_setting = h_setting - 0.25

        # If the user thought the day's overcast conditions were better than the app concluded
        if bw_over in ("B", "b"):
            # Ensure max setting isn't reached already
            if (o_setting >= 2):
                print("Overcast setting is at the max setting")
            # Update calculation setting variable
            else:
                o_setting = o_setting + 0.25
        # If the user thought the day's overcast conditions were worse than the app concluded
        elif bw_over in ("W", "w"):
            # Ensure the min setting isn't reached already
            if (o_setting <=0):
                print("Overcast setting is at the min setting")
            # Update the calculation setting variable
            else:
                o_setting = o_setting - 0.25

        # If the user thought the day's wind conditions were better than the app concluded
        if bw_wind in ("B", "b"):
            # Ensure max setting isn't reached already
            if (w_setting >= 2):
                print("Wind setting is at the max setting")
            # Update calculation setting variable
            else:
                w_setting = w_setting + 0.25
        # If the user thought the day's wind conditions were worse than the app concluded
        elif bw_wind in ("W", "w"):
            # Ensure min setting ins't already reached
            if (w_setting <= 0):
                print("Wind setting is at the min setting")
            # Update calculation setting variable
            else:
                w_setting = w_setting - 0.25

        # Update feedback setting variables
        feedback_setting = check_feedback_setting(t_setting, h_setting, o_setting, w_setting)

        # After calculation setting variables have been modified ask the user if they would like to re-run the
        # application with the new settings
        redo_today = check_redo()

        # If the user chooses to re-run, call necessary functions
        if (redo_today == 1):
            updated_calc = custom_calculations(temp, humidity, overcast, wind, criteria_setting, t_setting,
                                               h_setting, o_setting, w_setting)
            todays_custom_conditions(updated_calc, temp, humidity, overcast, wind, criteria_setting, t_setting,
                                     h_setting, o_setting, w_setting, feedback_setting)
        # Otherwise return to main menu
        else:
            print("Thanks for using the bike app!")
            app_end(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# This function is used to gather input about the 7 day forecast and calculate
# the biking conditions for each day. It takes a "criteria_setting" variable which is
# used to tell the program what criteria is important to the user
def forecast_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):
    # Declare the array that the calculated totals are stored in
    d_total = []
    # Day is used as a counter here
    day = 1

    # This while loop uses the day variable to iterate through 7 times and get the conditions for the next seven days
    while (day < 8):
        text_day = "Please enter day {} conditions".format(day)
        print(text_day)
        # If a criteria setting is selected with temperature low, set d_temp = 0
        if (criteria_setting >= 1 and criteria_setting <= 7):
            d_temp = 0
        else:
            d_temp = check_temp()
        # If a criteria setting is selected with humidity low, set d_hum = 0
        if ((criteria_setting >= 1 and criteria_setting <= 3) or (criteria_setting >= 8 and criteria_setting <= 11)):
            d_hum = 0
        else:
            d_hum = check_hum()
        # If a criteria setting is selected with overcast low, set d_over = 0
        if (criteria_setting == 1 or criteria_setting == 4 or criteria_setting == 5 or criteria_setting == 8
                or criteria_setting == 9 or criteria_setting == 12 or criteria_setting == 13):
            d_over = 0
        else:
            d_over = check_over()
        # If a criteria setting is selected with wind low, set d_wind = 0
        if (criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 6 or criteria_setting == 8
                or criteria_setting == 10 or criteria_setting == 12 or criteria_setting == 14):
            d_wind = 0
        else:
            d_wind = check_wind()

        # Append the total from the custom_calculations function to the d_total list
        d_total.append(custom_calculations(d_temp, d_hum, d_over, d_wind, criteria_setting, t_setting, h_setting,
                                           o_setting, w_setting))
        day = day + 1

    # Call the forecast conditions function to get the quality of each day
    forecast_conditions(d_total, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# Checks to see the biking conditions for each day
def forecast_conditions(d_total, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):

    # This is a list used to track the best days
    best_days = []

    # In order to save the most recent forecast data, the application writes the forecast
    # to a txt file that the user can go back and read at any time.
    file = open("forecast.txt", "w")

    # For setting 0, the condition measurement system in on a 100 point scale since
    # all criteria are being used.
    if (criteria_setting == 0):
        # enumerates through the loop to get the value and position of each value in the array
        for pos, val in enumerate(d_total):
            # If the total value is greather than or equal to 80 then it is excellent
            # biking conditions
            if (val >= 80):
                # The day variable is used to keep track of which day it is. Since the array
                # (or list in this case) starts at position 0, 1 must be added to the position
                day = pos + 1
                text_excellent = "Day {} would be excellent for biking\n".format(day)
                file.write(text_excellent)
                best_days.append(1)
            # If the total value is between or equal to 60-79 then it is good
            # biking conditions
            elif (val >= 60 and val < 80):
                day = pos + 1
                text_good = "Day {} would be good for biking\n".format(day)
                file.write(text_good)
            # If the total value is between or equal to 40-59 then it is average
            # biking conditions
            elif (val >= 40 and val < 60):
                day = pos + 1
                text_avg = "Day {} would be average for biking\n".format(day)
                file.write(text_avg)
            # If the total value is between or equal to 20-39 then it is bad
            # biking conditions
            elif (val >= 20 and val < 40):
                day = pos + 1
                text_bad = "Day {} would be bad for biking\n".format(day)
                file.write(text_bad)
            # If the total value is less than or eqal to 19 then it is terrible
            # biking conditions
            elif (val < 20):
                day = pos + 1
                text_terrible = "Day {} would be terrible for biking\n".format(day)
                file.write(text_terrible)

        text_space = "\n"
        file.write(text_space)

        for pos, val in enumerate(best_days):
            if (val == 1):
                e_day = pos + 1
                text_excellent_days = "Day {} would be one of the best for biking\n".format(e_day)
                file.write(text_excellent_days)
    # For these settings the condition measurement system in on a 75 point scale since 3/4 of the criteria
    # are being used.
    elif (criteria_setting == 7 or criteria_setting == 11 or criteria_setting == 13 or criteria_setting == 14):
        # enumerates through the loop to get the value and position of each value in the array
        for pos, val in enumerate(d_total):
            if (val >= 60):
                day = pos + 1
                text_excellent = "Day {} would be excellent for biking\n".format(day)
                file.write(text_excellent)
                best_days.append(1)
            elif (val >= 45 and val < 60):
                day = pos + 1
                text_good = "Day {} would be good for biking\n".format(day)
                file.write(text_good)
            elif (val >= 30 and val < 45):
                day = pos + 1
                text_avg = "Day {} would be average for biking\n".format(day)
                file.write(text_avg)
            elif (val >= 15 and val < 30):
                day = pos + 1
                text_bad = "Day {} would be bad for biking\n".format(day)
                file.write(text_bad)
            elif (val < 15):
                day = pos + 1
                text_terrible = "Day {} would be terrible for biking\n".format(day)
                file.write(text_terrible)

        text_space = "\n"
        file.write(text_space)

        for pos, val in enumerate(best_days):
            if (val == 1):
                e_day = pos + 1
                text_excellent_days = "Day {} would be one of the best for biking\n".format(e_day)
                file.write(text_excellent_days)
    # For these settings the condition measurement system in on a 50 point scale since 1/2 of the criteria
    # are being used.
    elif (criteria_setting == 3 or criteria_setting == 5 or criteria_setting == 6 or criteria_setting == 9
          or criteria_setting == 10 or criteria_setting == 12):
        # enumerates through the loop to get the value and position of each value in the array
        for pos, val in enumerate(d_total):
            if (val >= 40):
                day = pos + 1
                text_excellent = "Day {} would be excellent for biking\n".format(day)
                file.write(text_excellent)
                best_days.append(1)
            elif (val >= 30 and val < 40):
                day = pos + 1
                text_good = "Day {} would be good for biking\n".format(day)
                file.write(text_good)
            elif (val >= 20 and val < 30):
                day = pos + 1
                text_avg = "Day {} would be average for biking\n".format(day)
                file.write(text_avg)
            elif (val >= 10 and val < 20):
                day = pos + 1
                text_bad = "Day {} would be bad for biking\n".format(day)
                file.write(text_bad)
            elif (val < 10):
                day = pos + 1
                text_terrible = "Day {} would be terrible for biking\n".format(day)
                file.write(text_terrible)

        text_space = "\n"
        file.write(text_space)

        for pos, val in enumerate(best_days):
            if (val == 1):
                e_day = pos + 1
                text_excellent_days = "Day {} would be one of the best for biking\n".format(e_day)
                file.write(text_excellent_days)
    # For these settings the condition measurement system in on a 25 point scale since only 1 criteria
    # is being used.
    elif (criteria_setting == 1 or criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 8):
        for pos, val in enumerate(d_total):
            if (val >= 25):
                day = pos + 1
                text_excellent = "Day {} would be excellent for biking\n".format(day)
                file.write(text_excellent)
                best_days.append(1)
            elif (val >= 16.66 and val < 25):
                day = pos + 1
                text_good = "Day {} would be good for biking\n".format(day)
                file.write(text_good)
            elif (val >= 8.33 and val < 16.66):
                day = pos + 1
                text_avg = "Day {} would be average for biking\n".format(day)
                file.write(text_avg)
            elif (val >= 4.33 and val < 8.33):
                day = pos + 1
                text_bad = "Day {} would be bad for biking\n".format(day)
                file.write(text_bad)
            elif (val <= 3.25):
                day = pos + 1
                text_terrible = "Day {} would be terrible for biking\n".format(day)
                file.write(text_terrible)

        text_space = "\n"
        file.write(text_space)

        for pos, val in enumerate(best_days):
            if (val == 1):
                e_day = pos + 1
                text_excellent_days = "Day {} would be one of the best for biking\n".format(e_day)
                file.write(text_excellent_days)

    # Be sure to close the file that is being wrote to.
    file.close()

    # Let the user know their data has been written to the txt file.
    print("Your most recent forecast predictions have been saved to a text file for you!")
    # Go to app_end function
    app_end(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# This function is used to determine what criteria is important to the user.
def custom_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):
    # Ask the user what criteria is important to them
    print("Please select yes or no if these conditions are important to your bike ride.")
    t = check_temp_criteria()
    h = check_hum_criteria()
    o = check_over_criteria()
    w = check_wind_criteria()

    # Get the total of the high variables
    total = t + h + o + w

    # If all or none of the criteria were selected the application returns to the main menu
    if (total == 4):
        print("It seems no changes were made from the default settings. Returning to the menu.")
        menu(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)
    elif (total == 0):
        print("It seems that no custom conditions were deemed important. Returning to menu.")
        menu(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)
    # Otherwise go to the custom_menu function
    else:
        print("Custom settings recorded")
        custom_menu(t, h, o, w, total, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# This functions provides the custom menu for the user if the want to check today's
# riding conditions with their custom criteria
def custom_menu(temp, hum, over, wind, total, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):

    c_option = check_custom_menu()

    # If the user selects the today option the app checks to see which criteria is relevant and gets
    # the necessary input from the user. It also assigns the corresponding setting number
    if (c_option == "T" or c_option == "t"):
        if (total == 3):
            if (temp == 0):
                print("Based on your custom settings, temperature questions have been removed.")
                ct_temp = 0
                ct_hum = check_hum()
                ct_over = check_over()
                ct_wind = check_wind()
                criteria_setting = 7
            elif (hum == 0):
                print("Based on your custom settings, humidity questions have been removed.")
                ct_temp = check_temp()
                ct_hum = 0
                ct_over = check_over()
                ct_wind = check_wind()
                criteria_setting = 11
            elif (over == 0):
                print("Based on your custom settings, overcast questions have been removed.")
                ct_temp = check_temp()
                ct_hum = check_hum()
                ct_over = 0
                ct_wind = check_wind()
                criteria_setting = 13
            elif (wind == 0):
                print("Based on your custom settings, wind questions have been removed.")
                ct_temp = check_temp()
                ct_hum = check_hum()
                ct_over = check_over()
                ct_wind = 0
                criteria_setting = 14
        elif (total == 2):
            if (temp == 0 and hum == 0):
                print("Based on your custom settings, temperature and humidity questions have been removed")
                ct_temp = 0
                ct_hum = 0
                ct_over = check_over()
                ct_wind = check_wind()
                criteria_setting = 3
            elif (over == 0 and hum == 0):
                print("Based on your custom settings, overcast and humidity questions have been removed")
                ct_temp = check_temp()
                ct_hum = 0
                ct_over = 0
                ct_wind = check_wind()
                criteria_setting = 9
            elif (over == 0 and wind == 0):
                print("Based on your custom settings, overcast and wind questions have been removed")
                ct_temp = check_temp()
                ct_hum = check_hum()
                ct_over = 0
                ct_wind = 0
                criteria_setting = 12
            elif (over == 0 and temp == 0):
                print("Based on your custom settings, overcast and temperature questions have been removed")
                ct_temp = 0
                ct_hum = check_hum()
                ct_over = 0
                ct_wind = check_wind()
                criteria_setting = 5
            elif (hum == 0 and wind == 0):
                print("Based on your custom settings, wind and humidity questions have been removed")
                ct_temp = check_temp()
                ct_hum = 0
                ct_over = check_over()
                ct_wind = 0
                criteria_setting = 10
            elif (temp == 0 and wind == 0):
                print("Based on your custom settings, temperature and wind questions have been removed")
                ct_temp = 0
                ct_hum = check_hum()
                ct_over = check_over()
                ct_wind = 0
                criteria_setting = 6
        elif (total == 1):
            if (temp == 1):
                print("Based on your custom settings, temperature is the only relelvant question.")
                ct_temp = check_temp()
                ct_hum = 0
                ct_over = 0
                ct_wind = 0
                criteria_setting = 8
            elif (hum == 1):
                print("Based on your custom settings, humidity is the only relelvant question.")
                ct_temp = 0
                ct_hum = check_hum()
                ct_over = 0
                ct_wind = 0
                criteria_setting = 4
            elif (over == 1):
                print("Based on your custom settings, overcast is the only relelvant question.")
                ct_temp = 0
                ct_hum = 0
                ct_over = check_over()
                ct_wind = 0
                criteria_setting = 2
            elif (wind == 1):
                print("Based on your custom settings, wind is then only relevant question.")
                ct_temp = 0
                ct_hum = 0
                ct_over = 0
                ct_wind = check_wind()
                criteria_setting = 1

        # After the input is gathered from the user, send the data to the custom_calculations function
        todays_custom_calc = custom_calculations(ct_temp, ct_hum, ct_over, ct_wind, criteria_setting, t_setting, h_setting, o_setting, w_setting)

        # The total returned from those calculations is then sent to the custom_conditions function
        # to check the quality of today's riding conditions
        todays_custom_conditions(todays_custom_calc, ct_temp, ct_hum, ct_over, ct_wind, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)

    # If the forecast option is chosen the app prints to the screen which questions have been removed from
    # consideration, assigns then corresponding setting number and sends that setting number to the
    # forecast_mode function
    elif (c_option == "F" or c_option == "f"):
        if (total == 3):
            if (temp == 0):
                print("Based on your custom settings, temperature questions have been removed.")
                criteria_setting = 7
            elif (hum == 0):
                print("Based on your custom settings, humidity questions have been removed.")
                criteria_setting = 11
            elif (over == 0):
                print("Based on your custom settings, overcast questions have been removed.")
                criteria_setting = 13
            elif (wind == 0):
                print("Based on your custom settings, wind questions have been removed.")
                criteria_setting = 14
        if (total == 2):
            if (temp == 0 and hum == 0):
                print("Based on your custom settings, temperature and humidity questions have been removed")
                criteria_setting = 3
            elif (over == 0 and hum == 0):
                print("Based on your custom settings, overcast and humidity questions have been removed")
                criteria_setting = 9
            elif (over == 0 and wind == 0):
                print("Based on your custom settings, overcast and wind questions have been removed")
                criteria_setting = 12
            elif (over == 0 and temp == 0):
                print("Based on your custom settings, overcast and temperature questions have been removed")
                criteria_setting = 5
            elif (hum == 0 and wind == 0):
                print("Based on your custom settings, humidity and wind questions have been removed")
                criteria_setting = 10
            elif (temp == 0 and wind == 0):
                print("Based on your custom settings, temperature and wind questions have been removed")
                criteria_setting = 6
        elif (total == 1):
            if (temp == 1):
                print("Based on your custom settings, temperature is the only relelvant question.")
                criteria_setting = 8
            elif (hum == 1):
                print("Based on your custom settings, humidity is the only relelvant question.")
                criteria_setting = 4
            elif (over == 1):
                print("Based on your custom settings, overcast is the only relelvant question.")
                criteria_setting = 2
            elif (wind == 1):
                print("Based on your custom settings, wind is then only relevant question.")
                criteria_setting = 1
        forecast_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# This is just a conclusion print statement to signify the end of the application.
def app_end(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):
    print("Thanks for using the bike app!")
    # Return to main menu
    menu(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


# This function is used for the startup menu which gathers user input
def menu(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting):

    # If any changes have been made from the standard settings, let the user know their changes are still active
    if (feedback_setting != 0 or criteria_setting != 0):
        print("Your most recent feedback is still saved!")

        # Ask the user if they would like to reset changes
        reset = check_reset()

        # If so call the main() to reset setting variables and start the app fresh.
        if (reset == 1):
            print("Resetting preferences to default\n")
            main()

    # Ask the user which mode they would like to run the app in first.
    option = check_menu_option()

    # If the user selects the "today" option the app asks for today's weather conditions
    if (option == "T" or option == "t"):
        # If a criteria setting that has temperature low is selected, set temp = 0
        if (criteria_setting >= 1 and criteria_setting <= 7):
            temp = 0
        else:
            temp = check_temp()
        # If a criteria setting that has humidity low is selected, set humidity = 0
        if ((criteria_setting >= 1 and criteria_setting <= 3) or (criteria_setting >= 8 and criteria_setting <= 11)):
            humidity = 0
        else:
            humidity = check_hum()
        # If a criteria setting that has overcast low is selected, set overcast = 0
        if (criteria_setting == 1 or criteria_setting == 4 or criteria_setting == 5 or criteria_setting == 8
                or criteria_setting == 9 or criteria_setting == 12 or criteria_setting == 13):
            overcast = 0
        else:
            overcast = check_over
        # If a criteria setting that has wind low is selected, set wind = 0
        if (criteria_setting == 2 or criteria_setting == 4 or criteria_setting == 6 or criteria_setting == 8
                or criteria_setting == 10 or criteria_setting == 12 or criteria_setting == 14):
            wind = 0
        else:
            wind = check_wind()

        # Function call to process necessary calculations for riding conditions
        todays_calc = custom_calculations(temp, humidity, overcast, wind, criteria_setting, t_setting, h_setting, o_setting, w_setting)
        todays_custom_conditions(todays_calc, temp, humidity, overcast, wind, criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting,)

    # If the user selects the "forecast" option the app goes to the forecast_mode function
    elif (option == "F" or option == "f"):
        forecast_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)

    # If the user selects the "custom" option the app goes to the custom_mode function
    elif (option == "C" or option == "c"):
        custom_mode(criteria_setting, t_setting, h_setting, o_setting, w_setting, feedback_setting)


main()
