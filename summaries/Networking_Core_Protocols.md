# Networking Core Protocols Summary

| **Protocol** | **Transport Protocol** | **Default Port Number** |
| ------------ | ---------------------- | ----------------------- |
| TELNET       | TCP                    | 23                      |
| DNS          | UDP or TCP             | 53                      |
| HTTP         | TCP                    | 80                      |
| HTTPS        | TCP                    | 443                     |
| FTP          | TCP                    | 21                      |
| SMTP         | TCP                    | 25                      |
| POP3         | TCP                    | 110                     |
| IMAP         | TCP                    | 143                     |

## DNS Protocol

Reference: [RFC1035](https://www.ietf.org/rfc/rfc1035.txt)

Domain Name System (DNS) is responsible for properly mapping a domain name to an IP address.

> Application Layer 7 of OSI  
> Traffic on UDP prot 53  
> Fallback on TCP port 53

### DNS recods:

1. `A` record: (Address) maps a hostname to one or more IPv4 addresses. example.com -> 172.17.2.172
2. `AAAA` (quad-A) record: similar to A Record, but for IPv6.
3. `CNAME` (Canonical Name) record: maps a domain name to another domain name. www.example.com -> example.com or example.org.
4. `MX` (Mail Exchange) record: specifies the mail server responsible for handling emails for a domain.

### Example:

- Browsing example.com -> browser resloves domain name by querying the DNS server
- Sending email to test[at]example.com -> the mail server queries the DNS server to find MX record.

### CLI:

- `nslookup {Domain.TLD}`
- `dig {Domain.TLD}`

## WHOIS Protocol

Reference: [RFC1035](https://www.ietf.org/rfc/rfc3912.txt)

Provides information about the entity that registered a domain name, including name, phone number, email, and address. Record first creation and last updated date. Moreover, you can find the registrant’s name, address, phone, and email.

### CLI:

`whois {Domain.TLD}`

## HTTP/HTTPS Protocol

References: HTTP [RFC2616](https://www.ietf.org/rfc/rfc2616.txt), HTTPS [REFC2660](https://www.ietf.org/rfc/rfc2660.txt)

The Hypertext Transfer Protocol (Secure) relies on TCP and defines how your web browser communicates with the web servers.

> HTTP listens on TCP port 80 or 8080  
> HTTPS listens on TCP prot 443 or 8443

### Commands/Methods:

- `GET` retrieves data (HTML, Image,...) from a server
- `POST` allows us to submit new data (submitting a form, uploading a file) to the server.
- `PUT` is used to create a new resource on the server and to update and overwrite existing information.
- `DELETE` is used to delete a specified file or resource on the server.

### CLI:

- `telnet {Host} 80`
- `GET / HTTP/1.1` or `GET /{Path/File-Name} HTTP/1.1`
- `Host: {Host}` or `Host: anything`  
  Note: on some servers, specifying the host is not necessary.

## FTP Protocol

Reference: [RFC959](https://www.ietf.org/rfc/rfc959.txt)

File Transfer Protocol (FTP) is very efficient for file transfer, and when all conditions are equal, it can achieve higher speeds than HTTP.

> Server listens on TCP port 21  
> Data transfer is conducted via another connection from the client to the server.

### Commands:

- `USER` is used to input the username
- `PASS` is used to enter the password
- `RETR` (retrieve) is used to download a file from the FTP server to the client.
- `STOR` (store) is used to upload a file from the client to the FTP server.

### CLI:

- `ftp {Host}`
- `{Username}`  
   Note: anonymous can be used as username if not specified.
- `{Password}`  
   Note: press enter for anonymous user.
- `type ascii`  
   Note: switched to ASCII mode as the file was a text file.
- `get {File-Name}`
- `ls`, `cd`, `pwd`, and ...
- `close` or `bye`

## SMTP Protocol

Reference: [RFC5321](https://www.ietf.org/rfc/rfc5321.txt)

Simple Mail Transfer Protocol (SMTP) defines how a mail client talks with a mail server and a mail server talks with another mail server.

> Server listens on TCP port 25

### Commands:

- `HELO` or `EHLO` initiates an SMTP session
- `MAIL FROM` specifies the sender’s email address
- `RCPT TO` specifies the recipient’s email address
- `DATA` indicates that the client will begin sending the content of the email message
- `.` (dot) is sent on a line by itself to indicate the end of the email message

### CLI:

- `telnet {Host} 25`
- `HELO/EHLO {Host}`
- `MAIL FROM: <{Sender-Email}>`
- `RCPT TO: <{Receiver-Email}>`
- `DATA`
- ```
  From: {Sender-Email}
  To: {Receiver-Email}
  Subject: {Subject}

  {Message}
  ```

- `.`
- `QUIT`

## POP3 Protocl

Reference: [RFC1939](https://www.ietf.org/rfc/rfc1939.txt)

Post Office Protocol version 3 (POP3) is designed to retrieve email messages from a mail server to a local client.

> Server listens on TCP port 110

### Commands:

- `USER` identifies the user
- `PASS` provides the user’s password
- `STAT` requests the number of messages and total size
- `LIST` lists all messages and their sizes
- `RETR` retrieves the specified message
- `DELE` marks a message for deletion
- `QUIT` ends the POP3 session applying changes, such as deletions

### CLI:

- `telnet {IP-Address} 110`
- `AUTH`
- `USER {Username}`
- `PASS {Password}`
- `STAT`
- `LIST`
- `RETR {Message-Number}`
- `DELE {Message-Number}`

## IMAP Protocol

Reference: [RFC9051](https://www.ietf.org/rfc/rfc9051.txt)

Internet Message Access Protocol (IMAP) allows synchronizing read, moved, and deleted messages.

> Server listens on TCP port 143

### Commands:

- `LOGIN` <username> <password> authenticates the user
- `SELECT` <mailbox> selects the mailbox folder to work with
- `FETCH` <mail_number> <data_item_name> Example fetch 3 body[] to fetch message number 3, header and body.
- `MOVE` <sequence_set> <mailbox> moves the specified messages to another mailbox
- `COPY` <sequence_set> <data_item_name> copies the specified messages to another mailbox
- `LOGOUT` logs out

### CLI:

- `telnet {IP-Address} 143`
- `A LOGIN {User-Name} {Password}`
- `B SELECT {Folder-Name}`
- `C FETCH {Message-Number} body[]`
- `D LOGOUT`
