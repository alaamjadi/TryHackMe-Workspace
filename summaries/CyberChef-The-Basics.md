# CyberChef : The Basics

This document explains what CyberChef is, how to access and navigate the interface, common operation categories, and a practical mindset for using CyberChef effectively during investigations.

### What Is CyberChef

CyberChef is a web-based data analysis and transformation tool designed to perform a wide range of cyber-related operations directly in the browser. It functions as a modular toolbox that allows users to apply multiple operations in sequence, known as recipes, to process and analyze data.

CyberChef is commonly used for decoding, encoding, encryption, decryption, extraction, and data format transformations.

### Accessing CyberChef

CyberChef can be accessed in multiple ways depending on operational needs.

#### Online Access

| Method                                                   | Description                                                             |
| -------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Web-based](https://gchq.github.io/CyberChef)            | Access CyberChef directly through a browser with an internet connection |
| [Local copy](https://github.com/gchq/CyberChef/releases) | Download and run CyberChef locally on Windows or Linux systems          |

Using a local copy is recommended when handling sensitive data.

### Navigating the Interface

CyberChef is divided into four main areas, each serving a specific function.

| Area       | Purpose                                     |
| ---------- | ------------------------------------------- |
| Operations | Repository of all available operations      |
| Recipe     | Workspace to chain and configure operations |
| Input      | Area to provide text or files               |
| Output     | Displays processed results                  |

### Operations Area

The operations area contains categorized operations that can be searched and previewed.

#### Common Operations

| Operation       | Description                                      |
| --------------- | ------------------------------------------------ |
| From Morse Code | Converts Morse code to alphanumeric text         |
| URL Encode      | Encodes special characters into percent-encoding |
| To Base64       | Encodes data into Base64                         |
| To Hex          | Converts data to hexadecimal representation      |
| To Decimal      | Converts data to decimal values                  |
| ROT13           | Applies a Caesar cipher rotation                 |

### Recipe Area

The recipe area is where operations are assembled and configured.

#### Recipe Features

| Feature      | Function                              |
| ------------ | ------------------------------------- |
| Save recipe  | Store configured operation sequences  |
| Load recipe  | Reuse saved recipes                   |
| Clear recipe | Reset the recipe workspace            |
| Bake         | Execute the recipe                    |
| Auto Bake    | Automatically process input on change |

### Input Area

The input area allows users to provide data for processing.

#### Input Features

| Feature            | Description                      |
| ------------------ | -------------------------------- |
| Text input         | Paste or type raw data           |
| File input         | Upload a file as input           |
| Folder input       | Upload a directory of files      |
| Multiple tabs      | Work with multiple inputs        |
| Clear input/output | Reset data                       |
| Reset layout       | Restore default interface layout |

### Output Area

The output area displays the results of applied operations.

#### Output Features

| Feature       | Description                  |
| ------------- | ---------------------------- |
| Save output   | Export results to a file     |
| Copy output   | Copy raw output to clipboard |
| Replace input | Overwrite input with output  |
| Maximize pane | Expand output view           |

### CyberChef Thought Process

Using CyberChef effectively requires a structured approach.

| Step              | Description                            |
| ----------------- | -------------------------------------- |
| Define objective  | Clarify what you want to achieve       |
| Provide input     | Insert the data to analyze             |
| Select operations | Choose relevant transformations        |
| Validate output   | Confirm the result meets the objective |

### Common Operation Categories

#### Extractors

| Operation               | Purpose                         |
| ----------------------- | ------------------------------- |
| Extract IP addresses    | Extract IPv4 and IPv6 addresses |
| Extract URLs            | Extract URLs with protocol      |
| Extract email addresses | Extract email address patterns  |

#### Date and Time

| Operation           | Purpose                                 |
| ------------------- | --------------------------------------- |
| From UNIX Timestamp | Convert UNIX timestamp to readable date |
| To UNIX Timestamp   | Convert date to UNIX timestamp          |

#### Data Format

| Operation   | Purpose                     |
| ----------- | --------------------------- |
| From Base64 | Decode Base64 data          |
| URL Decode  | Decode percent-encoded URLs |
| From Base85 | Decode Base85-encoded data  |
| From Base58 | Decode Base58-encoded data  |
| To Base62   | Encode data into Base62     |

### Practical Usage Notes

| Use case              | Description                                |
| --------------------- | ------------------------------------------ |
| Data decoding         | Reveal hidden or encoded content           |
| Data extraction       | Identify indicators such as IPs and emails |
| Investigation support | Assist DFIR and SOC workflows              |
