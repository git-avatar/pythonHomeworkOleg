def questions():
    global day
    global month
    global year
    global current_day
    global current_month
    global current_year
    global total_months
    global total_days

    day = int(input("Enter the day you were born in: "))
    month = int(input("Enter the month you were born in: "))
    year = int(input("Enter the year you were born in: "))
    current_day = int(input("Enter the current day: "))
    current_month = int(input("Enter the current month: "))
    current_year = int(input("Enter the current year: "))
    total_months = 12
    total_days = 30

def user_birthday():
    birthday = [day, month, year]

    d = birthday[0]
    m = birthday[1]
    y = birthday[2]

    date_str = f"{d}.{m}.{y}"

    return date_str

def user_age():
    age = 2023 - year
    return age

def time_till_birthday():
    days_till_b = (total_days + day) - current_day
    months_till_b = (total_months + month) -  current_month
    total_till_b_in_days = (months_till_b * 30) + days_till_b

    total_till_b = (
        f"Months till your next birthday: {months_till_b}",
        f"Days till your next birthday: {days_till_b}",
        f"Total in days: {total_till_b_in_days}"
    )

    return total_till_b

def current_lifespan():
    x = True
    healthy_lifespan = 85
    lifespan = healthy_lifespan

    while True:

        smoking = str(input("Do you smoke or have you smoked (yes/no)? ")).lower()

        if smoking != "yes" and smoking != "no":
            print("You can only answer this question with yes/no")
            x = False
            break

        if smoking == "yes":
            question = int(input("How many years have you/do you smoke/d for?: "))
            question0 = str(input("Do you still smoke? (yes/no)?")).lower()

            if question0 != "yes" and question0 != "no":
                print("You can only answer this question with yes/no")
                x = False
                break

            question1 = int(input("How many packages have you/do you smoke/d per day? "))

            if question0 == "no":
                question01 = int(input("How many years are u nicotine free for? "))

                if question01 > 15:
                    lifespan += 12

            if question1 > 4:
                lifespan -= question1 * 1.5
            if 1 < question <= 4:
                lifespan -= 2
            if 4 < question <= 7:
                lifespan -= 4
            if 7 < question <= 11:
                lifespan -= 6
            if 11 < question <= 15:
                lifespan -= 10
            if 15 < question <= 20:
                lifespan -= 13
            if question > 20:
                lifespan -= 20

        training = str(input("Do you train(yes/no)? ")).lower()

        if training != "yes" and training != "no":
            print("You can only answer this question with yes/no")
            x = False
            break

        if training == "yes":
            question2 = int(input("How many years do you train for? "))
            if 3 <= question2 <= 7:
                lifespan += 4
            if 7 < question2 <= 12:
                lifespan += 6
            if 12 < question2 <= 20:
                lifespan += 10
            if question2 > 20:
                lifespan += 15

        terminal_illness = str(input("Do you have a terminal illness(yes/no) ")).lower()

        if terminal_illness != "yes" and terminal_illness != "no":
            print("You can only answer this question with yes/no")
            x = False
            break

        if terminal_illness == "yes":
            question3 = str(input("Is your illness life threatening in any way (yes/no) ")).lower()
            if question3 != "yes" and question3 != "no":
                print("You can only answer this question with yes/no")
                x = False
                break

            if question3 == "yes":
                question4 = str(input("Is the threat minor or major ")).lower()


                if question4 != "major" and question4 != "minor":
                    print("You can only use the words -minor- and -major- to answer this question! ")
                    x = False
                    break
                if question4 == "minor":
                    lifespan -= 4
                if question4 == "major":
                    lifespan -= 10

        food = str(input("Mostly, do you eat healthy or unhealthy food?(healthy/unhealthy) ")).lower()


        if food != "healthy" and food != "unhealthy":
            print("You can only answer this question with -healthy- or -unhealthy-")
            x = False
            break

        if food == "healthy":
            lifespan += 5
        if food == "unhealthy":
            lifespan -= 10

        stress = str(input("Do you have a lot of stress(yes/no)? ")).lower()

        if stress != "no" and stress != "yes":
            print("You can only answer this question with yes/no")
            x = False
            break

        if stress != "yes" and stress != "no":
            print("You can only answer this question with yes/no")
        if stress == "yes":
            lifespan -= 5

        drinking = str(input("Do you drink alcohol(yes/no)? ")).lower()
        if drinking != "yes" and drinking != "no":
            print("You can only answer this question with yes/no")
            x = False
            break

        if drinking == "yes":
            question5 = str(input("Are you an alcoholic?(yes/no)"))
            if question5 != "yes" and question5 != "no":
                print("You can only answer this question with yes/no")
                x = False
                break

            if question5 == "yes":
                question6 = int(input("How many years do you actively drink alcohol for?"))

                if question6 > 5 and question6 < 8:
                    lifespan -= 5
                if question6 > 8 and question6 < 15:
                    lifespan -= 7
                if question6 > 15 and question6 < 20:
                    lifespan -= 10
                if question6 > 20:
                    lifespan -= 15

        gender = str(input("Are you a male or a female(answer only with male/female) ")).lower()

        if gender != "male" and gender != "female":
            print("You can only answer this question with male/female!")
            x = False
            break

        if gender == "male" and lifespan >= 78:
            print("Your health is in a good condition, your lifespan is above average!")

        if gender == "male" and lifespan < 78:
            print("Your health isn't in a good condition, your lifespan is below average!")
            print("Here are some tips for you:"
                  '\n'f"Train more!"
                  '\n'f"Don't smoke/do drugs!"
                  '\n'f"Stop eating unhealthy food!"
                  '\n'f"Try having less stress and talk to a therapist about your problems!")

        if gender == "female" and lifespan > 83:
            print("Your health is in a good condition, your lifespan is above average!")

        if gender == "female" and lifespan < 83:
            print("Your health isn't in a good condition, your lifespan is below average!")
            print("Here are some tips for you:"
                  '\n'f"Train more!"
                  '\n'f"Don't smoke/do drugs!"
                  '\n'f"Stop eating unhealthy food!"
                  '\n'f"Try having less stress and talk to a therapist about your problems!")
        break
    if x == False:
        lifespan = "Sorry u didn't provide enough information"

    return lifespan

def lean_body_mass():
    lean_body_mass_value = None
    weight = int(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))

    while True:
        gender = input("Are you a male or a female (only answer with male/female): ").lower()
        if gender == "male" or gender == "female":
            break
        else:
            print("You can only answer this question with male/female!")

    if gender == "male":
        lean_body_mass_value = (0.32810 * weight) + (0.33929 * height) - 29.5336
    elif gender == "female":
        lean_body_mass_value = (0.29569 * weight) + (0.41813 * height) - 43.2933

    while True:
        question = input("Do you want your lean body mass output to be in kg/pounds (answer with kg/pounds only): ").lower()
        if question == "kg" or question == "pounds":
            break
        else:
            print("You can only answer this question with kg/pounds!")

    if question == "pounds":
        lean_body_mass_value *= 2.2

    result = f"{lean_body_mass_value}" f"{question}"
    return result




def body_fat_percentage():
    weight = int(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    age = int(input("Enter your age: "))
    bmi = weight/(height*height)
    body_fat_percentage = (1.20 * bmi) + (0.23 * age) - 16.2

    return float(body_fat_percentage)

