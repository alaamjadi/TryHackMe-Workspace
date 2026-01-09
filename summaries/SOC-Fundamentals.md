# SOC Fundamentals

This summary provides a concise breakdown of the core pillars, roles, processes, and technologies within a Security Operations Center (SOC).

### 1. Introduction to Security Operations Center (SOC)

A SOC is a dedicated, centralized facility where a specialized team continuously monitors an organization’s network and resources 24/7 to identify, detect, and respond to suspicious activity.

**Core Objectives:**

- **Detection**: Identifying vulnerabilities, unauthorized activities, policy violations, and network intrusions.
- **Response**: Minimizing the impact of incidents and performing root cause analysis to prevent future occurrences.
- **The Pillars**: A mature SOC environment relies on the synergy of **People, Process, and Technology**.

### 2. The People: Roles and Responsibilities

The "People" pillar consists of professional individuals who identify harmful activities that automated solutions might miss.

| Role               | Responsibility                                                                                                                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| SOC Analyst (L1)   | **First Responders**: Perform basic alert triage to determine if a detection is harmful and report them through proper channels. |
| SOC Analyst (L2)   | **Deep Investigators**: Perform deeper analysis by correlating data from multiple sources.                                       |
| SOC Analyst (L3)   | **Threat Hunters**: Proactively look for threat indicators and manage critical incidents (containment, eradication, recovery).   |
| Security Engineer  | **Architects**: Responsible for the deployment and configuration of security solutions.                                          |
| Detection Engineer | **Logic Builders**: Design the security rules and logic used by tools to identify harmful activities.                            |
| SOC Manager        | **Admin/Lead**: Manages the team's processes and communicates the security posture to the CISO.                                  |

### 3. The Process: Alert Triage and Reporting

Processes define how roles interact and ensure that security incidents are handled systematically.

**The 5 Ws of Alert Triage:**
The basis of the SOC team is answering these five questions to prioritize and analyze alerts:

1.  **What?**: The nature of the malicious activity (e.g., malware detected).
2.  **When?**: The exact timestamp of the detection.
3.  **Where?**: The specific host, directory, or network location involved.
4.  **Who?**: The specific user account associated with the activity.
5.  **Why?**: The root cause of the activity (e.g., user downloaded pirated software).

### 4. The Technology: Security Solutions

Technology automates detection and minimizes manual effort across the organization's network.

| Term      | Short Definition                                                                                                             | Primary Focus               |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| SIEM      | Security Information and Event Management collects logs from various sources and uses rules to identify suspicious activity. | Detection (Log Correlation) |
| EDR       | Endpoint Detection and Response provides real-time visibility and automated response capabilities directly on devices.       | Endpoint Security           |
| Firewall  | A barrier between internal and external networks that filters traffic based on security rules.                               | Network Perimeter           |
| Forensics | Analyzing system or network artifacts to determine the root cause of an incident.                                            | Root Cause Analysis         |

### 5. Detection vs. Response: Functional Comparison

A functional breakdown of how a SOC manages security events from discovery to mitigation.

| Category  | Component             | Description                                                                             |
| :-------- | :-------------------- | :-------------------------------------------------------------------------------------- |
| Detection | Vulnerabilities       | Discovering software weaknesses (e.g., unpatched systems) that attackers could exploit. |
| Detection | Unauthorized Activity | Spotting credential abuse or logins from unusual geographic locations.                  |
| Detection | Policy Violations     | Identifying breaches of internal rules, such as insecure file transfers.                |
| Response  | Incident Response     | Steps taken to minimize impact and perform root cause analysis.                         |
| Response  | Support               | Assisting specialized teams in carrying out containment and recovery steps.             |
