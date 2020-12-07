""" My Sweet Integration Project"""
__author__ = "Mackenzie Wolf"
# This project consists of a text-based two player Mad Lib simulator.
# Part One:The two users will input their information and interests.
# I will input the information into a magical generator in Part Two.
# I hope this game can be used by kids on road trips to kill time!
# TIP FOR PARENTS: Have kids explain why their word choice.  (Kills more time)


print("Players, welcome to Mad Lib: Travel Edition!")
# Have players input names.  Input() function does this.
print("Are you bored of watching cars pass and pointing at boring signs?")
response_1 = input("Type yes or no")

# Or is Boolean Operator & will print a statement if the response is Yes.
# == is a Conditional Operator meaning are both sides equal?
# The source is Boolean Operator information: Pogil 5: Boolean Expressions.
if response_1 == "yes" or response_1 == "Yes":
    """ Function's purpose is to introduce the player to typing choices."""
    print("Then let's get on with it!")

# If-Elif-Else shortens processing.  Source is from Pogil 6.
elif response_1 == "no" or response_1 == "No":
    print("Too bad!")
    """ Function's purpose is to continue a sassy user/computer dialogue."""

# Pogil 6: Else refers any other possible input.  If true, statement's printed.
else:
    print("Oh really? Sassy pants.")
    """ Function's purpose is to encompass all other possible responses."""

name_1 = input("Player One, type your name!")
# + :string operator, This 1 includes an assigned name in the printed text.
print("Hello " + name_1 + "!")
anima1_1 = input("Type an animal you've seen off the road")
name_2 = input("Player Two, it's your turn. Type your name...")
snack = input(name_2 + " enter your favorite roadside snack")
# Code to add "saurus" + "animal" for each name.  This is for part 2.
print("Greetings " + name_1 + " and " + name_2 + "!")
print("Before we start, your magical program requires more information!")

print("Stage One: Nouns, Verbs, Adverbs, and Adjectives")
print(name_2 + " Type in an adjective ending in -y-")
sassy_adjective = input("Input Adjective")
park_color = input(name_1 + " Please input a " + sassy_adjective + " color.")
# The sassy color will be a replacement for "Yellow" in "YellowStone Park"
body_part = input(name_2 + ", please type in a limb.")
country_name = input(name_2 + ", enter the name of a country.")
store_name = input(name_1 + ", think of the worst fast food place & type it.")
gas_worker = input(name_1 + ", input a gas station attendant's name.")
pet_name = input(name_2 + ", input a cliche pet name.")
holiday = input(name_1 + ", please type your favorite holiday.")
adv_funny = input(name_2 + ", input an ADJ that answers the question: how?")
verb_1 = input(name_1 + " input a verb.")
distance = input(name_2 + " describe a distance in 1 word. ex: close")
halloween_costume = input(name_2 + " type the name of a halloween costume.")
crime_committed = input(name_1 + " please type a crime ending in -ing-.")
seasoning = input(name_2 + " type which do you prefer, spicy, salty, or sweet")
movie_type = (name_1 + " what is the clichest type of movie?")
print("We are done with Stage One: part 1. Let us move onto shnazzy numbers!")

print("Stage One: Digits")
# Players input different numbers.  Int() means an integer is being inputted
print("For this section, only input numbers. Ex: 5, not five.")
# Source of try/except format: Professor Vanselow Loops Page


def asking_time():
    """ Function's purpose is to collect a user input for the MadLib and to
    verify and check that the input is an integer to prevent errors in the
     mathematical calculations. """
    try:
        inputted_time = int(input("# of times can one ask -are we there yet?"))
        return int(inputted_time)
    finally:
        print("Invalid input. Input a whole number. Try again!")
        inputted_time = int(input("Enter your new answer: "))
        return inputted_time


asking_time()


def favorited_input():
    """ Function's purpose is to collect a user input for the MadLib and to
    verify and check that the input is an integer to prevent errors in the
     mathematical calculations. """
    try:
        most_favorite = int(input("Player 1 input your favorite whole number"))
        return most_favorite
    finally:
        print("Invalid input. Input a whole number. Try again!")
        most_favorite = int(input("Player 1 input your favorite whole number"))
        return most_favorite


# Range() is "used to determine how many times the loop is executed."
# Standard iterative structures: Range function is from Pogil #9 For Loops.
x = 1
for x in range(0, 3):
    """The function's purpose is to assign num a value based on an input."""
    num = x


def funny_input():
    """ Function's purpose is to collect a user input for the MadLib and to
    verify and check that the input is an integer to prevent errors in the
     mathematical calculations. """
    try:
        number_fun = int(input("what 2 digit whole # is funnier > 24?"))
        return int(number_fun)
    finally:
        print("Invalid input. Input a whole 2 digit number. Try again!")
        number_fun = int(input("Enter your new answer: "))
        return number_fun


variable_funny = funny_input()

# // isolate's the tens place.  Takes a quotient and excludes decimal values.
b = variable_funny // 10
# % is modulo-takes the initial number,keeps the 1's place.
c = variable_funny % 10
# Spongebob is c divided by b(/).  The entire operation is squared (**).
funnier_input = (c / b) ** 2
# Multiply * candy bar price by 1000.
# + adds two inputted integers.
funnier_input = (funnier_input * 1000 + c)

response_1 = input("Shall we move on? Print -yes- or -no-")
if (response_1 == "yes") or (response_1 == "Yes"):
    """ Function's purpose is to amusingly connect Stage 1.1 & 1.2."""
    print("Aww yeah!")

# Python Activity 6: In IF-ELSE Statements, else refers to any other possible
# input.  The following print statement is given.
else:
    print("Sassy pants, we're moving on")
    """ Function's purpose is to encompass all other possible responses and"""
    """ to continue user/computer dialogue."""

print("Stage One: Emotions")
print("Okay " + name_1 + " and " + name_2 + "! Bet you two aren't ready "
                                            "to input your feelings!")
silly_word = input(name_2 + ", please input a silly verb ending in -ed-")
exclamation = input(name_1 + ", enter a saucy exclamation!")
# Whatever exclamation is given will be repeated twice for comedic effect.
exclamation = (exclamation * 2)
meaningful_stare = input(name_2 + " input a quote from a meme.")

print("Beepedy Boop Boop Beep, running calculations in...")


# http://greenteapress.com/thinkpython2/html cited for next part!
# Import time idea is from Openstax.com.
# While Loop is from Python Activity 08.
# While Loop is a repeating If-Statement.  Repeats till condition is satisfied.
# != is relational operator- Pogil 5- Identifies is 2 values are equal.
# "and" is a Boolean Operator from Pogil 5-requires two statements 2 be true.


def countdown(count):
    """ Function's purpose is to add a fun countdown to keep user interest."""
    while count != 0 and count > 0:
        print(count)
        count = (count - 1)

    else:
        print("let's go!")


countdown(3)

print("Stage Two: Game")
print("An introduction will lead into a 2 player script. " + name_1 +
      " will read from P1 and " + name_2 + " from P2.")
print("Introduction: Mom and son are adventuring through " + park_color +
      " State Park.")
print("They are on a " + sassy_adjective + ", in search for the mysterious-")
print("P2: Yea, but you have a " + snack + ". That's more important than "
      + body_part + "!")

print("P1: Ugh mommmm!")
print("P2: Listen " + sassy_adjective + ", I didn't spend my entire life "
                                        "savings of 25 dollars on an ")
print("underwater camera for you not to " + adv_funny + "oodle")
print("P1: Uhh... mom...? What is it?")
print("P2: " + sassy_adjective + " I just saw a Sea " + anima1_1
      + "! Go over and sit next to it, I want a picture of")
print("you petting it!")
print("P1: Mom! That's the " + holiday + " time " + adv_funny + "ly "
      + name_2 + "! It preys on children!")
print("P2: Oh, don't be such a " + pet_name + "! We did not just travel from "
      + park_color + " sunny " + store_name)
print("for this very moment. Just " + verb_1 + " and be still for me "
      + sassy_adjective + ".")
print("P1: *Give P2 the " + meaningful_stare + " look.*")
print("P2: *Stare back with equal " + adv_funny + ".*")
print("P1: Mom, the ranger said to stay a " + distance
      + " distance away from all " + holiday + " time ")
print(adv_funny + "ly " + name_2 + "!")
print("P2: My darling " + pet_name + "y " + pet_name + "-")
print("P1: No! I am not your " + pet_name + "y " + pet_name + "!")
print("P2: And I'm not your mom! For I am a " + halloween_costume
      + " and you're under arrest for " + crime_committed)
print(" my feelings")
print("P1: Well, Mrs. " + halloween_costume + " you're not my " + seasoning
      + " " + body_part + "!")
print("P2: All I wanted was one picture of you with a " + holiday + " time "
      + adv_funny + "ly " + name_2 + "! I don't")
print("ask for much from you. I give you " + snack + "s!")
print("P1: Relationships aren't all about " + snack + "s you "
      + halloween_costume + "! We're not in a ")
print("P2: I will take you out of this sufferingly wacky scene and "
      "feed you to the " + holiday + " time ")
print(adv_funny + "ly " + name_2 + "! Prepare to meet your end in...")


def countdown2(count2):
    """ Function's purpose is to add a fun countdown to keep user interest."""
    while count2 != 0 and count2 > 0:
        print(count2)
        count2 = (count2 - 1)


countdown(3)

print(exclamation)
print(name_1 + " " + name_2
      + ", please give feedback 2 this excellent integration project.")
print("Happy to have you on this travelling journey. Have a safe drive!")

print("Goodbye ~ Computer")
