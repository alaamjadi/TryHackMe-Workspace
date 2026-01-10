# Firewall Fundamentals

This document explains the role of firewalls in securing systems and networks, the different types of firewalls, how firewall rules work, and hands-on firewall management in Windows and Linux environments.

### Purpose of a Firewall

A firewall acts as a security control point between a trusted system or network and untrusted traffic. It inspects incoming and outgoing traffic and decides whether to allow, deny, or forward it based on predefined rules.

Firewalls are designed to prevent unauthorized access, reduce attack surfaces, and enforce security policies at the network and host level.

### Types of Firewalls

Different firewall types operate at different OSI layers and provide varying levels of inspection and protection.

| Firewall type            | OSI layer  | Characteristics                                                                       |
| ------------------------ | ---------- | ------------------------------------------------------------------------------------- |
| Stateless firewall       | Layer 3, 4 | Filters packets based on rules only, no connection tracking, fast but limited context |
| Stateful firewall        | Layer 3, 4 | Tracks connection state, applies rules based on session history                       |
| Proxy firewall           | Layer 7    | Acts as an intermediary, inspects packet contents, supports content filtering         |
| Next-generation firewall | Layer 3–7  | Deep packet inspection, intrusion prevention, heuristic analysis, SSL/TLS inspection  |

#### Firewall Characteristics Comparison

| Firewall                 | Capabilities                                                  |
| ------------------------ | ------------------------------------------------------------- |
| Stateless firewall       | Basic filtering, no session awareness, high performance       |
| Stateful firewall        | Connection tracking, pattern recognition, improved security   |
| Proxy firewall           | Content inspection, application control, anonymity            |
| Next-generation firewall | Advanced threat prevention, IPS, encrypted traffic inspection |

### Firewall Rules

Firewall rules define how traffic is handled based on specific criteria.

| Rule component      | Description                   |
| ------------------- | ----------------------------- |
| Source address      | Originating IP address        |
| Destination address | Target IP address             |
| Port                | Network port used             |
| Protocol            | Communication protocol        |
| Action              | Allow, deny, or forward       |
| Direction           | Inbound, outbound, or forward |

#### Rule Actions

| Action  | Description                              |
| ------- | ---------------------------------------- |
| Allow   | Permits matching traffic                 |
| Deny    | Blocks matching traffic                  |
| Forward | Redirects traffic to another destination |

**Deny all** or implicit deny is the last firewall rule that block any network traffic not explicitly permitted in the previous rules. This will reduce the attack surface by preventing unintended or unknown access.

#### Rule Directionality

| Direction | Purpose                                 |
| --------- | --------------------------------------- |
| Inbound   | Controls incoming traffic               |
| Outbound  | Controls outgoing traffic               |
| Forward   | Routes traffic between network segments |

### Windows Defender Firewall

Windows Defender Firewall is a built-in firewall in Windows that allows users to manage network traffic through predefined and custom rules.

#### Network Profiles

| Profile | Usage                            |
| ------- | -------------------------------- |
| Private | Trusted networks such as home    |
| Public  | Untrusted networks such as cafés |

Each profile can have different firewall rules applied.

#### Custom Rules in Windows Firewall

Custom rules allow fine-grained control over traffic, such as blocking specific ports or protocols.

### Linux Firewall Fundamentals

Linux firewalls are built on the Netfilter framework, which provides packet filtering, NAT, and connection tracking.

#### Linux Firewall Utilities

| Utility   | Description                                      |
| --------- | ------------------------------------------------ |
| iptables  | Traditional firewall utility using Netfilter     |
| nftables  | Successor to iptables with improved capabilities |
| firewalld | Zone-based firewall management                   |
| ufw       | Simplified firewall interface                    |

#### Common ufw (uncomplicated firewall) Commands

| Command                  | Purpose                 |
| ------------------------ | ----------------------- |
| ufw status               | Check firewall status   |
| ufw enable               | Enable firewall         |
| ufw disable              | Disable firewall        |
| ufw deny 22/tcp          | Block incoming SSH      |
| ufw status numbered      | List rules with numbers |
| ufw delete <rule_number> | Delete a rule           |

The `ufw default deny outgoing` is an example of blocking all outgoing traffic.
