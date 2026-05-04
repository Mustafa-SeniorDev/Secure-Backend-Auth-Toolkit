import os
import hashlib
import re

# ThreatSpy-Analyzer: Static Malware Analysis Engine
# Author: Mustafa-SeniorDev (15+ Years Experience)

class MalwareAnalyzer:
    """Core engine for identifying malicious patterns in suspicious binaries."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.suspicious_indicators = [
            r"CreateRemoteThread", r"WriteProcessMemory", 
            r"HttpSendRequest", r"ShellExecute", r"InternetOpen"
        ]

    def calculate_hashes(self):
        """Calculates MD5 and SHA256 for threat intelligence cross-referencing."""
        with open(self.file_path, "rb") as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
        return md5, sha256

    def scan_strings(self):
        """Extracts and analyzes strings for suspicious API calls and domains."""
        found_threats = []
        with open(self.file_path, "rb") as f:
            content = f.read().decode(errors="ignore")
            for pattern in self.suspicious_indicators:
                if re.search(pattern, content):
                    found_threats.append(pattern)
        return found_threats

    def run_audit(self):
        print(f"[*] Analyzing file: {os.path.basename(self.file_path)}")
        md5, sha256 = self.calculate_hashes()
        threats = self.scan_strings()
        
        print(f"[+] MD5: {md5}")
        print(f"[+] SHA256: {sha256}")
        
        if threats:
            print(f"[!] WARNING: Found {len(threats)} suspicious API indicators:")
            for t in threats:
                print(f"    - {t}")
        else:
            print("[+] No immediate suspicious API calls found.")

if __name__ == "__main__":
    # Example usage on a dummy file
    # In a real scenario, this would scan suspect binaries
    print("--- ThreatSpy Static Analysis Engine ---")
    # analyzer = MalwareAnalyzer("suspect_file.bin")
    # analyzer.run_audit()
