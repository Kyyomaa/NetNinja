import subprocess
import os
from simple_term_menu import TerminalMenu

class Ninja:
    def __init__(self):
        # Initialize color codes for terminal output
        self.red = '\033[1;31m'
        self.green = '\033[32m'
        self.reset = '\033[0m'
        self.yellow = '\033[33m'

    def troubleshoot(self):
        # Starting the troubleshooting process
        print("You selected Troubleshoot.")
        print("\n-----------------------------------")
        print("Troubleshooting first layer ISO/OSI"
              "\n(Your Network interfaces)\n")
        try:
            # Run the command to get network interfaces information
            result = subprocess.run(["ip", "-br", "a"], text=True, capture_output=True)
            lines = result.stdout.strip().split('\n')
            interfaces = []

            # Process each line of the command output
            for line in lines:
                parts = line.split()
                interface = {
                    'name': parts[0],
                    'status': parts[1],
                    'address': parts[2:],
                    'overall_status': 'UNKNOWN',  # Initialize as UNKNOWN
                    'ip_status': 'UNKNOWN'        # Initialize as UNKNOWN
                }
                interfaces.append(interface)
                addresses = ', '.join(interface['address'])

                # Check if the interface is down
                if interface['status'] == 'DOWN':
                    interface['overall_status'] = 'DOWN'
                    print(f"{self.red}UH-OH, This interface is not up {self.reset}\n")
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.red}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")

                # Check if the interface is up
                elif interface["status"] == 'UP':
                    interface['overall_status'] = 'UP'
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.green}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")
                    print(f"{self.green}UP AND RUNNING {self.reset}\n")

                    # Check if the interface has no IP address assigned
                    if not interface["address"]:
                        interface['ip_status'] = 'NO IP'
                    else:
                        interface['ip_status'] = 'HAS IP'

                # Handle unknown status
                else:
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.yellow}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")
                    print(f"{self.yellow}UNKNOWN STATUS{self.reset}\n")
            
            # Final evaluation of the network interfaces
            print("------------------------------------")
            print("FINAL EVALUATION")
            for interface in interfaces:
                if interface['overall_status'] == 'UP':
                    print(f"This interface is {self.green}UP{self.reset}: {interface['name']}")
                    if interface['ip_status'] == 'NO IP':
                        print(f"{self.red}NO IP ADDRESS{self.reset}\n Interface is up but it does not have an IP")
                    else:
                        print(f"Interface has an IP assigned")
                        print("IP:")
                        for addr in interface['address']:
                            print(f"\t{addr}")                        
                elif interface['overall_status'] == 'DOWN':
                    print(f"Interface {interface['name']} is {self.red}DOWN{self.reset}")
                else:
                    print(f"Interface {interface['name']} has {self.yellow}UNKNOWN{self.reset} STATUS, probably a loopback interface?")
        except Exception as e:
            print(f"ERR: {e} ")
        
        print("------------------------------------")
        
        input("Press Enter to continue...")

    def network_health_status(self):
        # Placeholder for Network Health Status logic
        print("You selected Network Health Status.")
        input("Press Enter to continue...")

    def general_checkup(self):
        # Placeholder for General Checkup logic
        print("You selected General Checkup.")
        input("Press Enter to continue...")

    def monitor(self):
        # Placeholder for Monitor logic
        print("You selected Monitor.")
        input("Press Enter to continue...")

    def menu(self):
        # Define the menu options
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

        # Show the menu and handle user selections
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
    # Create an instance of the Ninja class and display the menu
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
Device Detection: 
Network Latency: 
Intermittent Connection Issues: 
'''
