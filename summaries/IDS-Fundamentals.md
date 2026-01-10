# IDS Fundamentals

This document explains the role of Intrusion Detection Systems, their types and detection methods, and provides a practical overview of Snort as a widely used IDS solution.

### What Is an IDS

An Intrusion Detection System (IDS) is a security solution deployed inside a network to monitor traffic and detect malicious activities that bypass perimeter defenses such as firewalls. IDS generates alerts when suspicious behavior is detected but does not actively block the traffic.

IDS acts as a monitoring and alerting mechanism, providing visibility into malicious or abnormal activities occurring within a network or host.

### Types of IDS

IDS solutions are categorized based on deployment location and detection techniques.

#### Deployment Modes

| IDS type                           | Description                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Host Intrusion Detection System    | Installed on individual hosts, monitors host-specific activities, provides detailed visibility but is resource-intensive |
| Network Intrusion Detection System | Monitors traffic across the entire network, provides centralized detection for all connected hosts                       |

#### Detection Modes

| Detection type      | Description                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| Signature-based IDS | Detects known attacks using predefined signatures, cannot detect zero-day attacks                             |
| Anomaly-based IDS   | Detects deviations from normal behavior, capable of identifying zero-day attacks but prone to false positives |
| Hybrid IDS          | Combines signature-based and anomaly-based detection to leverage strengths of both approaches                 |

### IDS Example: Snort

Snort is a widely used open-source IDS that supports both signature-based and anomaly-based detection. It relies on rule files to identify malicious traffic patterns and generate alerts.

Snort allows:

- Use of built-in rule sets
- Creation of custom detection rules
- Disabling unnecessary rules based on environment needs

#### Snort Modes of Operation

| Mode                | Description                                       | Use case                                     |
| ------------------- | ------------------------------------------------- | -------------------------------------------- |
| Packet sniffer mode | Displays network packets without analysis         | Network monitoring and troubleshooting       |
| Packet logging mode | Logs network traffic into PCAP files              | Forensic investigations and traffic analysis |
| Network IDS mode    | Analyzes traffic using rules and generates alerts | Real-time intrusion detection                |

The Network IDS mode is the primary mode used for intrusion detection.

### Snort Usage and Configuration

Snort requires configuration of network interfaces and monitored ranges. To capture traffic beyond the local host, promiscuous mode must be enabled on the network interface.

#### Snort Directory Structure

Snort files are stored in the following directory:

| Path       | Purpose                                                |
| ---------- | ------------------------------------------------------ |
| /etc/snort | Main directory containing configuration and rule files |

Important components include configuration files and rule directories used to control detection behavior.

#### Snort Rule Structure

Snort rules define the conditions under which alerts are generated.

<img src="./media/snort-rule-format.png" alt= "Snort Rule Format" width="800">

##### Rule Components

| Component        | Description                        |
| ---------------- | ---------------------------------- |
| Action           | Action taken when the rule matches |
| Protocol         | Protocol to match                  |
| Source IP        | Origin of the traffic              |
| Source port      | Port originating the traffic       |
| Destination IP   | Target address                     |
| Destination port | Target port                        |
| Metadata         | Message, signature ID, revision    |

##### Rule Metadata Fields

| Field | Purpose                     |
| ----- | --------------------------- |
| msg   | Alert message displayed     |
| sid   | Unique signature identifier |
| rev   | Rule revision number        |

##### Custom Rule Creation and Testing

Custom rules are stored in a local rule file and can be tested by running Snort in IDS mode.

| File        | Description                         |
| ----------- | ----------------------------------- |
| local.rules | Stores custom Snort detection rules |

Rules can be validated by generating traffic that matches the defined conditions and observing the generated alerts.

##### An Example Rule

```shell
alert icmp any any -> $HOME_NET any (msg:"Ping Detected"; sid:10001; rev:1;)
```

#### Analyzing PCAP Files with Snort

Snort can analyze historical traffic stored in PCAP files for forensic investigations.

| Capability       | Description                                    |
| ---------------- | ---------------------------------------------- |
| PCAP analysis    | Detects malicious activity in captured traffic |
| Forensic support | Enables root cause analysis after incidents    |

This allows investigators to detect intrusions even after the attack has occurred.

#### Snort Commands

| Purpose                                   | Command                                                                            |
| ----------------------------------------- | ---------------------------------------------------------------------------------- |
| List Snort configuration and rule files   | `ls /etc/snort`                                                                    |
| Edit custom Snort rules                   | `sudo nano /etc/snort/rules/local.rules`                                           |
| Run Snort in IDS mode with console alerts | `sudo snort -q -l /var/log/snort -i lo -A console -c /etc/snort/snort.conf`        |
| Generate ICMP traffic to test rules       | `ping 127.0.0.1`                                                                   |
| Analyze a PCAP file with Snort            | `sudo snort -q -l /var/log/snort -r Task.pcap -A console -c /etc/snort/snort.conf` |

### Key Takeaways

| Concept           | Summary                                                   |
| ----------------- | --------------------------------------------------------- |
| IDS purpose       | Detects and alerts on malicious activity                  |
| Detection methods | Signature, anomaly, and hybrid approaches                 |
| Snort flexibility | Supports live traffic and PCAP analysis                   |
| Rules             | Core mechanism for detection                              |
| Visibility        | IDS complements firewalls by monitoring internal activity |
