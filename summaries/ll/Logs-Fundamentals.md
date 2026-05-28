# Logs Fundamentals

Understanding, analyzing, and investigating logs during security operations.

### What Are Logs?

Logs are **digital footprints** left behind by every activity occurring in a system, application, or network.  
These activities can be benign or malicious.

Logs help security teams:

- Reconstruct attack timelines
- Identify attacker behavior
- Perform incident investigations
- Support compliance and auditing

Logs are to digital systems what physical traces are to crime scenes.

### Why Logs Matter (Use Cases)

| Use case                             | Description                                                  |
| :----------------------------------- | :----------------------------------------------------------- |
| Security events monitoring           | Detect anomalous or malicious behavior in real time          |
| Incident investigation and forensics | Reconstruct events and identify root cause                   |
| Troubleshooting                      | Diagnose system and application errors                       |
| Performance monitoring               | Gain insight into application and system performance         |
| Auditing and compliance              | Maintain traceability of actions for regulatory requirements |

### Types of Logs

Logs are categorized to reduce noise and make investigations efficient.

| Log type         | Primary usage                           | Examples                                          |
| :--------------- | :-------------------------------------- | :------------------------------------------------ |
| System logs      | Operating system activity and stability | Startup/shutdown, driver loading, hardware errors |
| Security logs    | Security-relevant events                | Authentication, authorization, account changes    |
| Application logs | Application-specific activity           | User actions, updates, crashes                    |
| Audit logs       | Change tracking and compliance          | Data access, policy enforcement                   |
| Network logs     | Network traffic visibility              | Firewall logs, incoming/outgoing traffic          |
| Access logs      | Resource access tracking                | Web server access, database access, API calls     |

Note: Log availability depends on operating system, applications, and services.

### Log Analysis Overview

Log analysis is the process of extracting **valuable information** from large volumes of logs by identifying:

- Abnormal behavior
- Suspicious patterns
- Indicators of compromise

Manual analysis with raw logs is inefficient at scale, so both **manual and automated techniques** are used.

### Windows Event Logs

Windows logs system activity into structured event logs accessible through **Event Viewer**.

| Log name    | Purpose                                           |
| :---------- | ------------------------------------------------- |
| Application | Application-related errors and events             |
| System      | OS-level operations, drivers, services            |
| Security    | Authentication, authorization, and policy changes |

Event Viewer provides:

- Graphical interface
- Filtering and searching
- Event ID-based investigations

### Key Windows Event Log Fields

| Field       | Description                          |
| ----------- | ------------------------------------ |
| Description | Detailed explanation of the activity |
| Log name    | Category of the log                  |
| Logged      | Timestamp of the event               |
| Event ID    | Unique identifier for the activity   |

Event IDs allow investigators to quickly search for specific actions.

### Important Windows Event IDs (Security)

| Event ID | Description            |
| -------- | ---------------------- |
| 4624     | Successful login       |
| 4625     | Failed login           |
| 4634     | Successful logoff      |
| 4720     | User account created   |
| 4724     | Password reset attempt |
| 4722     | User account enabled   |
| 4725     | User account disabled  |
| 4726     | User account deleted   |

Remembering common Event IDs significantly speeds up investigations.

### Event Viewer Filtering

Event Viewer supports filtering logs by:

- Event ID
- Time range
- Severity

Filtering allows analysts to isolate relevant events instead of scanning entire log sets.

### Web Server Access Logs

Web servers log every request made to hosted applications.

Typical Apache access log location: `/var/log/apache2/access.log`

These logs record:

- Who made the request
- When it was made
- What was requested
- How the server responded

### Common Web Access Log Fields

| Field       | Description                        |
| ----------- | ---------------------------------- |
| IP address  | Source of the request              |
| Timestamp   | Time of the request                |
| HTTP method | Action requested (GET, POST, etc.) |
| URL         | Requested resource                 |
| Status code | Server response result             |
| User-Agent  | Client OS and browser information  |

### Manual Log Analysis (Linux)

Several command-line tools help with manual log analysis.

| Command      | Purpose                                     |
| ------------ | ------------------------------------------- |
| cat          | Display contents of a log file              |
| grep         | Search for specific strings or patterns     |
| less         | View logs page-by-page                      |
| b / spacebar | Navigate between search pages within less   |
| /pattern     | Search within less                          |
| n / N        | Navigate between search results within less |

Logs are often **rotated**, and multiple files may need to be combined during investigations.

### Investigation Scenarios

Logs are essential when:

- Identifying compromised users
- Tracing attacker actions
- Investigating data exfiltration
- Correlating events across systems

Windows Event Logs and Web Access Logs together provide:

- User activity visibility
- Network interaction evidence
- Timeline reconstruction

### Key Takeaways

| Concept                         | Summary                                |
| :------------------------------ | :------------------------------------- |
| Logs are evidence               | Every action leaves a trace            |
| Categorization matters          | Correct log type speeds investigations |
| Event IDs are powerful          | Enable precise filtering               |
| Manual analysis is foundational | Automation builds on these basics      |
| Logs support IR                 | Core input for incident response       |
