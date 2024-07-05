
print()
print("****" * 30)

print("""     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777 """)

print("****" * 30)
print()

print("Welcome to the 007 Adventure Game ! Try or Die !")
print()
print("Read the below given instructions and save the world !")
print("1. Remember the choices you make matter")
print("2. Type out the choice you wish to carry out to determine your fate !")
print("3. You only got 1 life 1 chance 1 shot")
print()

run = True

name = input("Input Player Name : ")
age = int(input("Input Player Age : "))

def game_func():
    global run
    global name
    global age

    # print(f"Greetings {name}, you are just in time to stop Dr.Shonal from destroying the world !")
    while run:
        if age < 18:
            print("Woah there Pardner ! You're too young to save the world don't you think ?!")
            run = False
            exit()
        elif age >= 18:
            print(f"Greetings {name}, you are just in time to stop Dr.Shonal from destroying the world ! I will now teleport you to his hidden lair in the deep forest of Amazon")

        print()
        print(f"**You have been successfully teleported Agent {name}**")
        print()

        choice1 = input("How do you choose to enter inside ? Ring The Lair Entrance Bell ? Sneak Left ? Sneak Right ? ")

        choice1 = choice1.lower()
        print()

        if choice1 == "ring the lair entrance bell":
            print("You Fool ! Did you really think that would work ? Shonal just blasted you into a bazillion pieces after opening the entrance !")
            print()
            print("WOMP WOMP ! Game Over !")
            run = False
        elif choice1 == "sneak left":
            print("Tough Luck ! While sneaking you stepped on a 3ft venomous snake and got bit :( You have been poisoned to Death !")
            print()
            print("WOMP WOMP ! Game Over !")
            run = False
        elif choice1 == "sneak right":
            choice2 = input("You see an underground entrance and a open window to the base, how do you proceed ? Underground Entrance ? Open Window ? ")
            print()
            choice2 = choice2.lower()
            if choice2 == "open window":
                print("What's that stink ? Did you really just jump into a guard toilet ? Ewww ! Your foot is in the toilet bowl xD and yes you died from exessive shit foot !")
                print("WOMP WOMP ! Game Over !")
                run = False
            elif choice2 == "underground entrance":
                choice3 = input("You walk for miles and miles and finally come out of an opening and see Shonal working on his laptop with his back turned to you.\nCharge him with your Katana or Shoot him with your supressed M9 pistol.\nKatana ? M9 ? ")
                choice3 = choice3.lower()

                if choice3 == "katana":
                    print(f"An honorable death for a low life scum ? You truly are the greatest I've seen ! You charge shonal with your katana, one swift swing his head comes clean off ! You saved the World Agent {name}!")
                    print("Honorable Victory ! Fatality !")
                    print("***"*10)
                    print()
                    print(f"Thanks for playing 007 ! {name}, I hope you had a fun time killing me and saving the world !")
                    print( "Ah yes ! What a twist ! This game was created by me Shonal ;) So who actually won in the end huh ? BWAHAHAHAHAAHA")
                    print("To be continued.....")
                    print("Copyright © Shonal 2024")
                    run = False
                elif choice3 == "m9":
                    print(f"Quick and Easy eh ? That's what that low life scum deserves ! You whip out the M9 and take 2 shots, 1 to his groin 1 to his head.\nShonal dies instantly ! What a funny way to kill a villain !\nYou saved the World Agent {name}!")
                    print("Swift Stealthy Victory ! Fatality !")
                    print("***"*10)
                    print()
                    print(f"Thanks for playing 007 ! {name}, I hope you had a fun time killing me and saving the world !")
                    print( "Ah yes ! What a twist ! This game was created by me Shonal ;) So who actually won in the end huh ? BWAHAHAHAHAAHA")
                    print("To be continued.....")
                    print("Copyright © Shonal 2024")
                    run = False


game_func()