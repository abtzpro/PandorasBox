# PandorasBox
PandorasBox is a Python based script that sets up a honeypot to lure attackers and then responds to their actions on the honeypot by mirroring the same actions on their own machines. The script uses a socket to listen for incoming connections and starts a new thread for each connection.

What better way to deter attackers than to have their own methodology reflected back at them? 

You know the old legend attributed to PandorasBox - Don't open it. Not even once. Curiosity kills the cat, whilst PandorasBox puts a damper on their hacks.

### Requirements

- Python 3.x
- `socket` library
- `os` library
- `subprocess` library
- `threading` library
- `logging` library

### Installation

1. Clone the repository:

   
2. Navigate to the project directory:

   ```
   cd PandorasBox
   ```

### Usage

1. Run the script:

   ```
   python PandorasBox.py
   ```

2. The script will start listening for incoming connections on port `8080`.

3. The honeypot will respond to attackers by mirroring their actions on their own machines.

4. Information about the attackers is saved to a log file (`honeypot.log`) and a database (`attacker_info.txt`).

5. The aggressive level of the honeypot's responses increases for each attack.

### PandorasBox Attacks that take place

Level 1: The honeypot sends the message "You have been hacked!" to the attacker's machine.

Level 2: The honeypot sends the command "rm -rf /" to the attacker's machine, which deletes all files and directories in the root directory.

Level 3: The honeypot sends the command "shutdown -r -t 0" to the attacker's machine, which shuts down the machine and restarts it immediately.

Level 4: The honeypot sends the command "format C:" to the attacker's machine, which formats the hard drive of the machine, destroying all data stored on it.



### License

This project is licensed under the MIT License. See the LICENSE file for more information.

### Developed by

PandorasBox is developed by Adam Rivers and Hello Security LLC

### Warnings

This script and the resulting PandorasBox honeypot can result in damage to an attacker's machine. Please be wary of applicable laws and ethics when using PandorasBox.
