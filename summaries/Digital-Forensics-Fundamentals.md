# Digital Forensics Fundamentals

Digital Forensics is the application of investigation methods to solve cyber crimes by finding and analyzing evidence on digital devices for legal proceedings.

### 1. NIST Digital Forensics Methodology

The National Institute of Standards and Technology (NIST) defines a four-phase process for conducting digital investigations:

| Phase       | Short Definition                                                                                     |
| :---------- | :--------------------------------------------------------------------------------------------------- |
| Collection  | Gathering data from devices (PC, USB, etc.) while ensuring original data is not tampered with.       |
| Examination | Filtering the collected volume to extract specific data of interest (e.g., specific dates or users). |
| Analysis    | Correlating evidence to draw conclusions and extract a chronology of events.                         |
| Reporting   | Preparing a detailed report of findings and methodology for law enforcement and management.          |

### 2. Types of Digital Forensics

Different categories of forensics focus on specific data sources and environments:

- **Computer Forensics**: Investigating personal systems like laptops and desktops.
- **Mobile Forensics**: Extracting call records, SMS, and GPS data from mobile devices.
- **Network Forensics**: Analyzing network traffic logs to investigate activity beyond individual devices.
- **Database Forensics**: Investigating unauthorized data modification or exfiltration within databases.
- **Cloud Forensics**: Investigating data stored on cloud infrastructure.
- **Email Forensics**: Analyzing emails to determine if they are part of phishing or fraudulent campaigns.

### 3. Evidence Acquisition & Integrity

Acquiring evidence securely is critical to ensure it remains admissible in court.

- **Proper Authorization**: Investigators must obtain legal approval before collecting private or sensitive data.
- **Chain of Custody**: A formal document tracking evidence details (who, when, where) to prove integrity and reliability. Some of the key details are:
  - Description of the evidence (name, type).
  - Name of individuals who collected the evidence.
  - Date and time of evidence collection.
  - Storage location of each piece of evidence.
  - Access times and the individual record who accessed the evidence.
  - [NIST chain of custory sample form](https://www.nist.gov/document/sample-chain-custody-formdocx)
- **Write Blockers**: Devices used to prevent any data alteration on original evidence during the collection process.
- **Disk Image**: A bit-by-bit, non-volatile copy of storage (HDD/SSD) that survives a system restart.
- **Memory Image**: A volatile copy of RAM; must be captured before shutdown to preserve running processes and network connections.

### 4. Essential Forensics Tools

These tools are commonly used for the acquisition and analysis of Windows-based evidence:

| Tool                                                                    | Primary Use                                                                                              |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| FTK Imager                                                              | Creating bit-by-bit disk images and analyzing their contents.                                            |
| [Autopsy](https://www.autopsy.com/)                                     | An open-source platform for extensive disk image analysis, including keyword searches and file recovery. |
| [DumpIt](https://www.toolwar.com/2014/01/dumpit-memory-dump-tools.html) | A command-line utility used specifically for taking Windows memory (RAM) images.                         |
| [Volatility](https://volatilityfoundation.org/)                         | A powerful tool for analyzing memory images across Windows, Linux, and macOS.                            |
| ExifTool                                                                | A tool used to read and write metadata (EXIF) in files, such as GPS coordinates in images.               |

### 5. Metadata Analysis

Digital artifacts often contain hidden information that can provide critical leads:

- **Document Metadata**: Advanced editors like MS Word store creation dates, authors, and software versions. `pdfinfo <file.pdf>` displays various metadata.
- **Photo EXIF Data**: Digital images can contain camera models, capture times, and highly probable GPS coordinates (latitude/longitude). `exiftool <file.jpg>` can read and write metadata.
