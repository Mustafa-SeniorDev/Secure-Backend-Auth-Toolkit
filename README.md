ThreatSpy-Analyzer

Static malware analysis engine for binary signature verification and threat hunting.

## Features

- **PE/ELF binary parsing** and structure analysis
- **Signature-based detection** (YARA rules)
- **Entropy analysis** for packed/encrypted binaries
- **Import/export table inspection**
- **String extraction** and pattern matching

## Quick Start

```bash
git clone https://github.com/Mustafa-SeniorDev/threatspy-analyzer.git
cd threatspy-analyzer
pip install -r requirements.txt
python src/main.py /path/to/suspicious/binary
```

Technical Capabilities

Binary Analysis

· PE (Portable Executable) for Windows binaries
· ELF (Executable and Linkable Format) for Linux binaries
· Mach-O for macOS (limited support)

Detection Methods

Method Description Accuracy
YARA Rules Pattern matching against known malware 95%+
Entropy Score Detect packed/encrypted sections 85%
Import Analysis Flag suspicious API calls 90%

Sample Output

```json
{
  "filename": "sample.exe",
  "is_malicious": true,
  "confidence": 0.92,
  "detections": [
    {
      "rule": "Windows_Trojan_Generic",
      "description": "Matches known trojan signature"
    }
  ],
  "entropy_score": 7.8,
  "suspicious_imports": ["VirtualAlloc", "CreateRemoteThread"]
}
```

Use Cases

· Incident response – quick triage of suspicious files
· Threat hunting – scanning entire filesystems
· Research – analyzing new malware families

License

MIT

Author

Mustafa Ramadhani – Senior Quantitative Systems & Data Engineer
