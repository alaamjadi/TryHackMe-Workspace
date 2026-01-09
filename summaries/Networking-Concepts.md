# Networking: Concepts

## Learning Objectives

- Understand the ISO OSI network model.
- Learn about IP addresses, subnets, and routing.
- Identify TCP, UDP, and port numbers.
- Connect to an open TCP port via the command line.

## OSI Model

The Open Systems Interconnection (OSI) model is a seven-layer conceptual framework developed by ISO to describe computer network communications. The OSI model is composed of **seven layers**:

**Mnemonic**: "Please Do Not Throw Spinach Pizza Away" (Physical to Application).

<img src="./media/OSI_Model.svg" alt= "Image of the OSI Model 7 layers" width="300">

### Layer 1: Physical Layer

- **Function**: Manages physical connections between devices.
- **Mediums**: Includes wire, fiber, and wireless.
- **Data**: Defines binary digits 0 and 1.

### Layer 2: Data Link Layer

- **Function**: Enables data transfer between nodes on a shared network segment.
- **Examples**: Ethernet (802.3) and WiFi (802.11).
- **MAC Address**: A six-byte hexadecimal address; the first three bytes identify the vendor.

### Layer 3: Network Layer

- **Function**: Handles logical addressing and routing packets between different networks.
- **Examples**: IP, ICMP, and VPN protocols (IPSec, SSL/TLS).

### Layer 4: Transport Layer

- **Function**: Supports end-to-end communication between applications.
- **Features**: Includes flow control, segmentation, and error correction.
- **Examples**: TCP and UDP.

### Layer 5: Session Layer

- **Function**: Establishes, maintains, and synchronizes communication between hosts.
- **Key Tasks**: Session establishment (negotiating parameters) and data synchronization (order and recovery).
- **Examples**: Network File System (NFS) and Remote Procedure Call (RPC).

### Layer 6: Presentation Layer

- **Function**: Acts as a translator ensuring data is in a format the application layer understands.
- **Tasks**: Handles data encoding, compression, and encryption/decryption.
- **Encoding Examples**: ASCII and Unicode.
- **Standards**:
  - Images: JPEG, GIF, PNG.
  - Email: Uses MIME to encode binary files into 7-bit ASCII.

### Layer 7: Application Layer

The application layer provides network services directly to end-user applications. It is the top layer where users interact with network protocols.

- **Function**: Provides interface for applications to access network services.
- **Examples**: HTTP (web browsing), FTP (file transfer), DNS (domain resolution), POP3/SMTP/IMAP (email).

### Summary Table of OSI Layers

| Layer Number | Layer Name   | Main Function                            | Example Protocols/Standards |
| :----------- | :----------- | :--------------------------------------- | :-------------------------- |
| Layer 7      | Application  | Services and interfaces for applications | HTTP, FTP, DNS, SMTP        |
| Layer 6      | Presentation | Data encoding, encryption, compression   | Unicode, MIME, JPEG, PNG    |
| Layer 5      | Session      | Managing and synchronizing sessions      | NFS, RPC                    |
| Layer 4      | Transport    | End-to-end communication/segmentation    | TCP, UDP                    |
| Layer 3      | Network      | Logical addressing and routing           | IP, ICMP, IPSec             |
| Layer 2      | Data Link    | Reliable transfer between adjacent nodes | Ethernet, WiFi              |
| Layer 1      | Physical     | Physical data transmission media         | Electrical/Optical signals  |

### TCP/IP Model

Developed by the DoD, this implemented model is designed to function even if parts of the network are out of service. It typically consists of four layers that map to the OSI model:

1.  **Application Layer**: Combines OSI layers 5, 6, and 7.
2.  **Transport Layer**: Maps to OSI layer 4.
3.  **Internet Layer**: Maps to OSI layer 3.
4.  **Link Layer**: Maps to OSI layer 2.

| Layer Number | ISO OSI Model      | TCP/IP Model (RFC 1122) | Protocols                                       |
| ------------ | ------------------ | ----------------------- | ----------------------------------------------- |
| 7            | Application Layer  | Application Layer       | HTTP, HTTPS, FTP, POP3, SMTP, IMAP, Telnet, SSH |
| 6            | Presentation Layer | $\uparrow$              | $\uparrow$                                      |
| 5            | Session Layer      | $\uparrow$              | $\uparrow$                                      |
| 4            | Transport Layer    | Transport Layer         | TCP, UDP                                        |
| 3            | Network Layer      | Internet Layer          | IP, ICMP, IPSec                                 |
| 2            | Data Link Layer    | Link Layer              | Ethernet 802.3, WiFi 802.11                     |
| 1            | Physical Layer     | -                       | -                                               |

### IP Address and Subnets

Every host requires a unique IP address to communicate without ambiguity.

- **IPv4 Structure**: Composed of four octets (32 bits), ranging from 0 to 255.
- **Reserved Addresses**: `.0` is usually the network address; `.255` is the broadcast address for targeting all hosts.
- **Subnet Mask**: Identifies which part of the IP is the network. For example, `/24` (255.255.255.0) means the first three octets are fixed for that subnet.
- **Private Addresses (RFC 1918)**: Ranges that cannot be reached directly from the internet:
  - 10.0.0.0 - 10.255.255.255
  - 172.16.0.0 - 172.31.255.255
  - 192.168.0.0 - 192.168.255.255
- **Routing**: Routers function at Layer 3 to forward packets to the correct network based on IP addresses.

### UDP and TCP

Transport protocols (Layer 4) use **port numbers** (1-65535) to identify specific processes.

- **UDP (User Datagram Protocol)**: Connectionless and "unreliable" (no delivery guarantee), offering better speed for real-time traffic.
- **TCP (Transmission Control Protocol)**: Connection-oriented and reliable. It uses a **three-way handshake** (SYN -> SYN-ACK -> ACK) to establish a connection.

### Encapsulation

Encapsulation is the process where each layer adds a header (and sometimes a trailer) to the data before passing it down.

1.  **Application Data**: User input.
2.  **Transport Segment/Datagram**: Adds TCP/UDP header.
3.  **Network Packet**: Adds IP header.
4.  **Data Link Frame**: Adds Ethernet/WiFi header and trailer.

<img src="./media/Encapsulation.svg" alt= "Encapsulation" width="700">

### Telnet

Telnet is a tool used to connect to and communicate with remote systems via text commands on a specific TCP port.

- **Echo Server (Port 7)**: Returns sent text.
- **Daytime Server (Port 13)**: Returns current date/time.
- **Web Server (Port 80)**: Can be used to manually request web pages (e.g., `GET / HTTP/1.1`).

### Conclusion

This room compared the OSI and TCP/IP models, detailed IP addressing, subnets, routing, and the differences between TCP and UDP, ending with practical telnet demonstrations.
