import subprocess
import os
from simple_term_menu import TerminalMenu
import time
class Ninja:
    def __init__(self):
        # Initialize color codes for terminal output
        self.red = '\033[1;31m'
        self.green = '\033[32m'
        self.reset = '\033[0m'
        self.yellow = '\033[33m'
        self.first_layer_status = None
    
    def first_layer(self):
        print("\n#################################")
        print("TROUBLESHOOTING FIRST LAYER ISO/OSI"
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
                        self.first_layer_status = "up but no ip" 
                        print(f"{self.red}NO IP ADDRESS{self.reset}\n Interface is up but it does not have an IP")
                    else:
                        self.first_layer_status = "OK"
                        print(f"Interface has an IP assigned")
                        print("IP:")
                        for addr in interface['address']:
                            print(f"\t{addr}")                        
                elif interface['overall_status'] == 'DOWN':
                    self.first_layer_status = "DOWN"
                    print(f"Interface {interface['name']} is {self.red}DOWN{self.reset}")
                else:
                    print(f"Interface {interface['name']} has {self.yellow}UNKNOWN{self.reset} STATUS, probably a loopback interface?")
        except Exception as e:
            print(f"ERR: {e} ")
        
        print("\n#################################")
        #input("Press Enter to continue...")
        
    def second_layer(self):
        print("\n#################################")
        print("TROUBLESHOOTING SECOND LAYER ISO/OSI"
              " (MAC ADDRESS ETC)\n")
        print("not really a priority RN, will work on it later")

    def third_layer(self):
        print("\n#################################")
        print("TROUBLESHOOTING THIRD LAYER ISO/OSI"
              " (IP/DNS/DHCP/NTP)\n")
        print("List of third layer protocols supported:")
        print(f"1. {self.green}IP{self.reset}")
        print(f"2. {self.green}DNS{self.reset}")
        print(f"3. {self.red}DHCP{self.reset}")
        print("4. WILL ADD MORE IN THE FUTURE")
        
        if self.first_layer_status == 'OK':
            print(f"\nInterfaces are up and you have an ip.")
            print(f"Lets start pinging\n")
            time.sleep(1)
        flag = 'y' #default
        while flag ==  'y':
            result = subprocess.run(['ping', '8.8.8.8', '-c' , '3'] , text= True, capture_output=True)
            print(result)
            print(" \nwant to ping again? it may be a temporary error") 
            flag = input("[y/n]")
            #solve the result thing
            #parse and alanlyze output 
            #use the loop only if the results are negatives
        
    def troubleshoot(self):
        # Starting the troubleshooting process
        print("You selected Troubleshoot.")
        self.first_layer()
        input("Press Enter to continue...")
        os.system('clear')
        self.second_layer()
        input("Press Enter to continue...")
        os.system('clear')
        self.third_layer()
        input("Press Enter to continue...")
        os.system('clear')

        
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
