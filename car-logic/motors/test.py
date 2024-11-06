import time
from movements import MovementController

def display_menu():
    print("\nMovement Controller Menu:")
    print("1. Move Forward")
    print("2. Move Backward")
    print("3. Turn Right")
    print("4. Turn Left")
    print("5. Spin Right")
    print("6. Spin Left")
    print("7. Stop")
    print("8. Exit")

def main():
    controller = MovementController(p=True)  # Create an instance of the MovementController class with printing enabled

    try:
        while True:
            display_menu()
            choice = input("Select an option (1-8): ")

            if choice == '1':
                controller.foward()
            elif choice == '2':
                controller.backwards()
            elif choice == '3':
                controller.right()
            elif choice == '4':
                controller.left()
            elif choice == '5':
                controller.spinRight()
            elif choice == '6':
                controller.spinLeft()
            elif choice == '7':
                controller.stop()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 8.")
            # Pause briefly to allow user to see action output
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgram interrupted with KeyboardInterrupt. Exiting...")
    finally:
        controller.stop()  # Ensure the controller is stopped
        del controller 

if __name__ == "__main__":
    main()
