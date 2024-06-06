
import os
from simple_term_menu import TerminalMenu

class Ninja:
    def __init__(self):
        pass

    def troubleshoot(self):
        print("You selected Troubleshoot.")
        # Add Troubleshoot logic here
        input("Press Enter to continue...")

    def network_health_status(self):
        print("You selected Network Health Status.")
        # Add Network Health Status logic here
        input("Press Enter to continue...")

    def general_checkup(self):
        print("You selected General Checkup.")
        # Add General Checkup logic here
        input("Press Enter to continue...")

    def monitor(self):
        print("You selected Monitor.")
        # Add Monitor logic here
        input("Press Enter to continue...")

    def menu(self):
        options = [
            "Troubleshoot",
            "Network Health Status",
            "General Checkup",
            "Monitor",
            "Exit"
        ]

        menu_options = {
            "Troubleshoot": self.troubleshoot,
            "Network Health Status": self.network_health_status,
            "General Checkup": self.general_checkup,
            "Monitor": self.monitor,
            "Exit": exit
        }

        terminal_menu = TerminalMenu(options)

        while True:
            os.system('clear')  # Use 'cls' instead of 'clear' if on Windows
            menu_entry_index = terminal_menu.show()
            menu_entry = options[menu_entry_index]
            
            if menu_entry == "Exit":
                print("Exiting...")
                break
            else:
                menu_options[menu_entry]()

def main():
    ninja = Ninja()
    ninja.menu()

if __name__ == "__main__":
    main()


'''

Unreachable Hosts: 
Slow Internet Speeds: 
Open/Closed Ports: 
DNS Resolution Issues: 
Network Route Problems:
Network Interface Problems: 
Bandwidth Usage: 
Device Detection: .
Network Latency: 
Intermittent Connection Issues: 

'''