import pyscreenshot
import random

def full_screen_shot():
    print("Please don't use numbers in the name.")
    while True:
        try:
            name_of_screenshot = input("Enter the name of the screenshot: ")
            if name_of_screenshot.isdigit():
                print(f"Please Don't Use Number : {name_of_screenshot}")
            else:
                break
        except Exception:
            print("Don't use strings?")

        screenshot_image = pyscreenshot.grab()
        screenshot_image.show()

        screenshot_number = random.randint(1, 10000)
        screenshot_image.save(f"{name_of_screenshot}_{screenshot_number}.png")
        print("Screenshot Saved successfully!")


def customize_screen_shot():
    while True:
        try:
            name_of_screenshot = input("Enter the name of the screenshot: ")
            if (name_of_screenshot.isdigit()):
                print(f"Please Don't Use Number : {name_of_screenshot}")
                break

            left_coordinates = int(input("Enter the Left coordinate: "))
            top_coordinates = int(input("Enter the Top coordinate: "))
            right_coordinates = int(input("Enter the Right coordinate: "))
            bottom_coordinates = int(input("Enter the Bottom coordinate: "))

            custom_screenshot = pyscreenshot.grab(bbox=(left_coordinates, top_coordinates, right_coordinates,   bottom_coordinates))

            screenshot_number = random.randint(1, 10000)
            custom_screenshot.save(f"{name_of_screenshot}_{screenshot_number}.png")
            custom_screenshot.show()
            print("Screenshot Saved successfully!")

        except Exception:
            print("Invalid input. Please enter only numbers for screen coordinates.")


def select_option():
    print("Select the option by number only.\n")
    print("""
    1. Take Full Screen Shot of Monitor
    2. Customize the Screenshot by Entering Coordinates (x1, x2, y1, y2)
    """)

    try:
        option = int(input("Enter Your Choice (1 or 2): "))

        if option == 1:
            full_screen_shot()
        elif option == 2:
            customize_screen_shot()
        else:
            print("Please Select Either 1 or 2 only.")

    except ValueError:
        print("Invalid input. Please enter a number Only.")


# Run the program
select_option()
