# Metasploit: Meterpreter

This summary covers the advanced capabilities of the Meterpreter payload, its stealth mechanisms, and essential post-exploitation commands.

### 1. Overview and Stealth Features

Meterpreter is an advanced, multi-faceted payload that operates as an agent within a command and control (C2) architecture.

- **In-Memory Execution**: It runs entirely in memory and does not write itself to the disk, significantly reducing the footprint and avoiding detection by signature-based antivirus scans.
- **Encrypted Communication**: Establishes a TLS-encrypted channel between the target and the attacker to bypass Network Intrusion Detection Systems (NIDS/IPS).
- **Process Ghosting**: It often hides under legitimate process names (e.g., `spoolsv.exe`) and avoids using easily identifiable strings in DLLs.

### 2. Payload Categories

Metasploit payloads are divided into two primary types:

- **Inline (Non-Staged)**: The entire exploit and payload are sent in one go.
- **Staged**: A small "stager" is sent first to establish a connection, which then pulls the larger "stage" (the actual Meterpreter payload) into memory.
  - _Note_: In MSF, staged payloads are denoted by a forward slash (e.g., `windows/meterpreter/reverse_tcp`), while non-staged use underscores (e.g., `windows/meterpreter_reverse_tcp`).

### 3. Essential Post-Exploitation Commands

Once a Meterpreter session is established, these commands are used to gather intelligence and escalate privileges. Use `sessions` to list all the available sessions and connect with `sessions -i <session_id>`.

#### System and User Discovery

- **`getuid`**: Displays the user account the payload is currently running under.
- **`getsystem`**: Attempts to automatically elevate privileges to the local SYSTEM account (requires `use priv` first).
- **`hashdump`**: Dumps the contents of the SAM database (Windows NTLM hashes) for offline cracking.

#### Process Management

- **`ps`**: Lists all running processes and their PIDs.
- **`migrate <pid>`**: Moves the Meterpreter session into another running process.
  - **Note**: Migrate to a stable process (like `explorer.exe`) to prevent the session from closing if the original exploited application crashes. If you migrate from a higher privileged (system) user to a process started by a lower privileged (webserver) user and may not be able to gain them back.

#### Data Gathering

- **`search -f <file_pattern>`**: Searches the filesystem for specific files (e.g., `search -f *.txt` or `search -f config*`).
- **`shell`**: Drops into a standard system command-line shell (CMD or Bash). Use `CTRL+Z` to return to Meterpreter.

#### Specialized Modules

- **`load kiwi` / `load Mimikatz`**: Used for advanced credential harvesting, including clear-text passwords from memory and "Golden Ticket" attacks.
- **`load python`**: Allows for the native execution of Python scripts on the target machine without requiring a local installation.

### 4. Post-Exploitation Goals

Meterpreter is the primary tool for achieving the following objectives:

1.  **Information Gathering**: Finding sensitive files and credentials.
2.  **Privilege Escalation**: Moving from a low-privileged user to Admin/SYSTEM.
3.  **Lateral Movement**: Using the compromised machine as a pivot to attack other systems on the internal network.
