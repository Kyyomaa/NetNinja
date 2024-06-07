import subprocess
import os
from simple_term_menu import TerminalMenu

class Ninja:
    def __init__(self):
        self.red = '\033[1;31m'
        self.green = '\033[32m'
        self.reset = '\033[0m'

    def troubleshoot(self):
        print("You selected Troubleshoot.")
        print("\n-----------------------------------")
        print("Troubleshooting first layer ISO/OSI"
            "\n(Your Network interfaces)\n")
        try:
            result = subprocess.run(["ip", "-br", "a"], text = True, capture_output= True)
            lines = result.stdout.strip().split('\n')
            interfaces = []
            for line in lines:
                parts = line.split()
                interface = {
                    'name': parts[0],
                    'status': parts[1],
                    'address': parts[2:]
           }        
                interfaces.append(interface)
                addresses = ', '.join(interface['address'])
                if interface['status'] == 'DOWN':
                    print(f"{self.red}UH-OH, This interface is not up {self.reset}\n")
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.red}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")

                elif interface["status"] == 'UP':
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.green}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")
                    print(f"{self.green}UP AND RUNNING {self.reset}\n")

                else:
                    print(f"[+] NAME: {interface['name']}, \n[+] STATUS: {self.green}{interface['status']}{self.reset}, \n[+] ADDRESSES: {addresses}\n")
                    print(f"UNKNOWN STATUS\n")

        except Exception as e:
            print(f"ERR:,{e} ")
        
        print("------------------------------------")
        
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