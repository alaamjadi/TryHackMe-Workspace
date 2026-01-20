# CAPA: The Basics

**References:** [CAPA Website](https://mandiant.github.io/capa/), [CAPA Explorer Web](https://mandiant.github.io/capa/explorer/), [CAPA GitHub](https://github.com/mandiant/capa), [CAPA Rules GitHub](https://github.com/mandiant/capa-rules), [CAPA documentation](https://github.com/mandiant/capa/blob/master/doc/README.md), [MITRE ATT&CK](https://attack.mitre.org/), [MAEC Documentation](https://maecproject.github.io/documentation/maec5-docs/), [Malware Behavior Catalog Matrix](https://maecproject.github.io/ema/), [Malware Behavior Catalog (MBC)](https://github.com/MBCProject/mbc-markdown), [MBC Summary](https://github.com/MBCProject/mbc-markdown/blob/main/mbc_summary.md)

CAPA identifies high-level capabilities in executable code using static analysis and a ruleset that maps low-level features to behaviors and labels.

### Introduction

CAPA helps triage unknown software by reporting what a program can do (capabilities), rather than only listing low-level indicators.

### Tool Overview

CAPA extracts low-level features (imports, strings, API usage patterns, instruction sequences, etc.) from code and applies a ruleset that translates those features into higher-level (human-readable) behaviors (persistence, communication, obfuscation, injection).

#### Analysis

The table below contrasts static and dynamic analysis to clarify what CAPA can and cannot observe.

| Analysis approach | What it does                                 | Strengths                                                          | Limitations                                                                       |
| ----------------- | -------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Static analysis   | Inspects code and data without executing it. | Safe, fast triage, works on non-runnable samples.                  | Misses behaviors only visible at runtime; can be impacted by packing/obfuscation. |
| Dynamic analysis  | Observes behavior while the sample runs.     | Captures runtime-only activity (network, process, registry, etc.). | Riskier, needs a controlled environment; behavior may be gated or delayed.        |

#### Supported Artifacts

In CAPA, an artifact is the input being analyzed (for example, a binary, shellcode, or a process memory dump). The table lists common artifact types CAPA can accept.

| Artifact type | Description                                              |
| ------------- | -------------------------------------------------------- |
| Executable    | PE/ELF/Mach-O binaries.                                  |
| Process dump  | Memory snapshots of running processes.                   |
| Shellcode     | Raw code blobs.                                          |
| .NET module   | Managed assemblies (coverage depends on rules/features). |

#### Report Structure (Blocks)

CAPA reports results in blocks that support different analysis tasks:

| Section                        | What it contains                                          | Why it matters                                                   |
| ------------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------- |
| General information            | Hashes, target OS/format/arch, analysis type, input path. | Confirms what was analyzed; supports tracking and deduplication. |
| MITRE ATT&CK                   | Tactics/techniques/sub-techniques (e.g., `T1053.005`).    | Standard behavior labeling for reporting and communication.      |
| MAEC                           | High-level categorization (e.g., `launcher`).             | Classifies the sample’s role at a coarse level.                  |
| Malware Behavior Catalog (MBC) | Objectives and behaviors with IDs (e.g., `B0032.020`).    | Alternative behavior taxonomy for clustering and reporting.      |
| Capability                     | Human-readable capability statements.                     | Primary triage output. What behaviors does it implement?         |
| Namespaces                     | Rule grouping and hierarchy behind capabilities.          | Helps filter and pivot into related behaviors and rules.         |

### Running CAPA

Run the CLI against a target artifact and increase verbosity when you need evidence.

Common command patterns:

| Goal               | Command pattern                                  | Notes                                                   |
| ------------------ | ------------------------------------------------ | ------------------------------------------------------- |
| Help/usage         | `capa -h`                                        | Lists flags and input expectations                      |
| Basic analysis     | `capa <path-to-artifact>`                        | Human-readable results report.                          |
| More detail        | `capa -v <path-to-artifact>`                     | Adds additional context to matches.                     |
| Deep match detail  | `capa -vv <path-to-artifact>`                    | Includes extensive match evidence; output can be large. |
| JSON output        | `capa -j <path-to-artifact> > <output.json>`     | Machine-readable output for tooling.                    |
| JSON + deep detail | `capa -j -vv <path-to-artifact> > <output.json>` | Useful for Explorer-style review and match inspection.  |

Notes:

- Instead of using `-v` and `-vv` flags, the `--verbose` and `--vverbose` flags can be used respectively.
- On Windows, the binary may be `capa.exe`.
- Use output redirection (`>`) to save reports as json files.

### CAPA Results

CAPA output is grouped into blocks; interpret each block for its intended purpose.

#### Report Block: General Information

```
┌────────────────────────────────────────────────────┬──────────────────┐
│ md5,sha1,sha256, analysis, os, format, arch, path  │ respected values │
└────────────────────────────────────────────────────┴──────────────────┘
```

This block provides file identity and analysis context.

| Fields                  | Meaning                                                 |
| ----------------------- | ------------------------------------------------------- |
| `md5`, `sha1`, `sha256` | Cryptographic hashes of the analyzed artifact.          |
| `analysis`              | Analysis mode used to extract features and match rules. |
| `os`                    | Target operating system inferred/selected.              |
| `format`                | File format (e.g., PE/ELF)                              |
| `arch`                  | Architecture (e.g., x86/x64)                            |
| `path`                  | Input path CAPA analyzed                                |

#### Report Block: MITRE ATT&CK

MITRE ATT&CK is a knowledge base that maps how attackers operate across each phase of an intrusion (e.g., initial access, persistence, privilege escalation, defense evasion, and lateral movement). CAPA formats its findings to align with this structure. Some findings include technique/sub-technique identifiers while others don’t.

```
┌───────────────┬───────────────────────────────┐
│ ATT&CK Tactic │ ATT&CK Technique              │
├───────────────┼───────────────────────────────┤
│ Tactic Group  │ Technique::Sub-Technique [ID] │
└───────────────┴───────────────────────────────┘
```

This is the label format for ATT&CK table:

| ATT&CK Technique Format         | Example                                                                     |
| ------------------------------- | --------------------------------------------------------------------------- |
| `Technique [ID]`                | `Encode Data` or `Obfuscated Files or Information [T1027]`                  |
| `Technique::Sub-Technique [ID]` | `Obfuscated Files or Information::Indicator Removal from Tools [T1027.005]` |

#### Report Block: MAEC

MAEC (Malware Attribute Enumeration and Characterization) is a vocabulary for describing malware attributes and behaviors.

```
┌──────────────────┬─────────────────────┐
│ MAEC Category    │ MAEC Value          │
├──────────────────┼─────────────────────┤
│ malware-category │ launcher/downloader │
└──────────────────┴─────────────────────┘
```

CAPA commonly emits `malware-category` values like:

| MAEC Value Format | What it indicates                                                  |
| ----------------- | ------------------------------------------------------------------ |
| `launcher`        | The sample triggers or stages actions that enable other behaviors. |
| `downloader`      | The sample retrieves additional content and executes it.           |

Typical implications:

- `launcher`: acts as an initial stage that triggers execution flow (may stage/decode/decompress payloads, configure execution, enabling persistence mechanism, or contacting C2 servers).
- `downloader`: often pulls additional payloads/resources from external locations, pulling updates, running secondary stages, and retrieving configuration files.

#### Report Block: Malware Behavior Catalog (MBC)

The MBC is a standardized catalog used to label and report malware behaviors, compare samples, and support similarity analysis. It complements (but doesn’t duplicate) MITRE ATT&CK by mapping behaviors to attacker objectives and sometimes linking to ATT&CK techniques, though names don’t always match.

MBC organizes findings into:

- Level 1:
  - **Objective**: A high-level malware behavior goal, largely aligned with ATT&CK tactics (though not all tactics are included). MBC also includes objectives specifically for malware analysis such as Anti-Behavioral and Anti-Static Analysis (e.g., staying on the machine, stealing data, or avoiding analysis).
  - **Micro-Objective**: A smaller, analysis-focused goal tied to one or more micro-behaviors. These reflect actions that may be common in legitimate software but are frequently abused in malware, hence CAPA may flag them.
- Level 2:
  - **Behaviors**: The set of defined behaviors and micro-behaviors in MBC, describe what the malware does, sometimes listed with associated methods and identifiers (e.g., “create a process,” “encrypt data”).
  - **Micro-Behavior** (Low-level behavior): A very basic action (e.g., creating a TCP socket, checking a string condition) that isn’t inherently malicious on its own, but can be part of malicious activity depending on context.
  - **Enhanced Malware ATT&CK Techniques**: MITRE ATT&CK techniques (and sub-techniques) that have been augmented with malware-specific details to better support malware analysis and reporting.
- Level 3:
  - **Methods**: Specific techniques/implementations used to carry out a behavior. Methods are attached to behaviors, and you find the full list by looking at each behavior or micro-behavior’s details.

```
┌───────────────────────────┬──────────────────────────────┐
│ MBC Objective             │ MBC Behavior                 │
├───────────────────────────┼──────────────────────────────┤
│ Objective/Micro-Objective │ Behavior::Method [ID]        │
|                           | Micro-Behavior::Method [ID]  │
|                           | Enhanced-ATT&CK::Method [ID] |
└───────────────────────────┴──────────────────────────────┘
```

This is the label format for MBC table:

| MBC Behavior Format            | Example                                                                    |
| ------------------------------ | -------------------------------------------------------------------------- |
| `Behavior [ID]`                | `Virtual Machine Detection [B0009]`                                        |
| `Behavior::Method [ID]`        | `Executable Code Obfuscation::Stack Strings [B0032.017]`                   |
| `Micro-Behavior [ID]`          | `Check String [C0019]`                                                     |
| `Micro-Behavior::Method [ID]`  | `HTTP Communication::Read Header [C0002.014]`                              |
| `Enhanced-ATT&CK [ID]`         | `File and Directory Discovery [E1083]`                                     |
| `Enhanced-ATT&CK::Method [ID]` | `Obfuscated Files or Information::Encoding-Standard Algorithm [E1027.m02]` |

#### Report Block: Capability, Namespace, Rule

| Item           | Meaning                                      |
| -------------- | -------------------------------------------- |
| Capability     | Rule display name (what CAPA prints)         |
| Namespace      | Taxonomy location for the rule (grouping)    |
| Rule YAML file | Rule definition that produced the capability |

- **Capability and Rule**: CAPA reports the capability described by the rule, and the rule name is what you see as the capability label. So capability is not a separate object from a rule — it’s the result of a rule match. CAPA may show match counts (e.g., `(<n> matches)`) indicating the rule triggered multiple times.
- **Namespaces**: A namespace is a hierarchical label attached to a rule (in meta.namespace) used to group related capabilities (and to keep output organized). Namespaces look like paths: `communication/http/client`. The filesystem layout of the rule repo mirrors namespaces, and CAPA output is ordered/grouped by namespace.
  - **TLN**: The first component of the namespace path is the top-level namespace (TLN), followed by more specific categories. Typical structure is as `tln/category/subcategory/...`.

Rules are “bound” to namespaces via metadata:

- A rule has one `meta.namespace` (usually).
- When that rule matches, CAPA reports the capability (rule name) and shows its namespace next to it.

```
┌────────────────────────────────┬──────────────────┐
│ Capability                     │ Namespace        │
├────────────────────────────────┼──────────────────┤
│ Capability Name (# of matches) │ TLN/namespace(s) │
└────────────────────────────────┴──────────────────┘
```

| Namespace Format    | Example                              |
| ------------------- | ------------------------------------ |
| `TLN/namespace/...` | `anti-analysis/anti-vm/vm-detection` |

> Rule defines logic → if it matches → CAPA reports Capability (rule name) → grouped under Namespace (rule meta)

##### Concrete example (rule → capability → namespace)

A typical rule skeleton looks like:

```yaml
rule:
  meta:
    name: <capability name>
    namespace: <tln>/<subpath>
    scopes: # Where the rule applies
      static: <file|function|basic block|instruction|unsupported>
      dynamic: <file|process|thread|span of calls|call|unsupported>
    att&ck: # Optional
      - <Tactic::Technique [T#### or T####.###]>
  features: # Match logic over extracted features
    - <and/or/not/match/...>
```

Rules can also be building blocks for other rules.

- CAPA supports rules that match other rules using `match: ...`
- “Library rules” are marked with `meta.lib: True` and are not rendered as results (they exist to support other rules).

So you can have:

- lib rule matches (internally)
- which helps a non-lib technique rule match
- and only the non-lib one shows up as a reported capability

##### How to think about it (a quick diagram)

```python
          (rule set on disk)
     YAML rule files, each with:
     - meta.name       -> what you'll see as the "capability"
     - meta.namespace  -> how it's grouped/sorted (TLN is the root)
     - features        -> detection logic
                |
                v
  CAPA extracts features from the binary
                |
                v
  rule engine evaluates rules
                |
                v
  matched rules -> reported as "capabilities"
                |
                v
  output grouped by namespace
```

##### Practical tips to make this stick

- Treat Capability == rule name (most of the time).
- Treat Namespace == folder-like category label for that rule.
- Treat TLN == the namespace root folder (first segment).
- Remember some rules are helpers (`rule.meta.lib: True`) and won’t appear as capabilities. **lib rules** are reusable building blocks, meant to be matched by other rules, not shown as standalone results
- If you want to focus on a slice of the rules, CAPA supports filtering by metadata value.

Top-Level Namespaces (TLNs) commonly encountered:

| TLN                 | Focus                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| `anti-analysis`     | Anti-debug/anti-VM, packing/obfuscation indicators                     |
| `collection`        | Data discovery/collection behaviors                                    |
| `communication`     | Network protocols and C2-related behaviors                             |
| `compiler`          | Build environment/compiler signatures                                  |
| `data-manipulation` | Encoding/encryption/hashing and transformations                        |
| `executable`        | Executable-file attributes (sections, debug info, etc.)                |
| `exploitation`      | Exploit-like primitives and vulnerability-exploitation behavior        |
| `host-interaction`  | OS interaction (file system, processes, registry, services)            |
| `impact`            | Effects such as destruction, modification, or disruption               |
| `internal`          | Internal rules (not intended as end-user capabilities)                 |
| `lib`               | Building-block rules used by other rules                               |
| `linking`           | Linking/dynamic loading related behaviors                              |
| `load-code`         | Code loading/injection-style behaviors                                 |
| `malware-family`    | Family identification rules                                            |
| `nursery`           | Staging area for less-polished rules (may contain rules for many TLNs) |
| `persistence`       | Behaviors that maintain access over time                               |
| `runtime`           | Runtime/platform/language identification                               |
| `targeting`         | Target-specific behaviors (ruleset-dependent)                          |

### CAPA Explorer Web

Explorer Web is used to review verbose/JSON output interactively (capability tree, matched features, and filters).

Workflow:

| Step | Action                                                                                    |
| ---- | ----------------------------------------------------------------------------------------- |
| 1    | Generate verbose JSON: `capa -j -vv <path-to-artifact> > <output.json>`                   |
| 2    | Open [Explorer Web](https://mandiant.github.io/capa/explorer/) and upload `<output.json>` |
| 3    | Use the global search box and filters to narrow results                                   |
| 4    | Pivot from a capability to its matched features to understand why it triggered            |

Explorer Web surfaces rule logic and matched features. Strings shown in matches may be represented as patterns (rule-dependent).

**Global Search Box**: Use global search to jump to capabilities, namespaces, or rule names without manually expanding the full tree.

### Key Takeaways

| Topic              | Summary                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| Fast triage        | CAPA reports capabilities to quickly understand what a program can do    |
| Evidence           | Use `-v`/`-vv` when you need the match details behind a capability       |
| Standard labels    | ATT&CK, MAEC, and MBC mappings help standardize reporting and comparison |
| Rule taxonomy      | Namespaces help locate and group related behaviors in the ruleset        |
| Interactive review | Explorer Web speeds up inspection of verbose/JSON results                |
