import json
import subprocess
import sys

class SemgrepParser:
    def __init__(self, target_directory):
        self.target_directory = target_directory

    def semgrep_scan(self):
        cmd = [
            'semgrep',
            'scan',
            '--config', 'p/ci',       # General Semgrep rules from the 'ci' pack
            '--config', 'p/security-audit', # Security audit rules
            '--config', 'p/r2c-security-audit', # Extensive Security audit rules
            '--metrics=off',
            '--json',
            f'--json-output={self.target_directory}/semgrep_output.json',
            self.target_directory          # Scan the specified target directory
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode not in [0, 1]:
                print("Error running semgrep:")
                print(result.stderr)
                sys.exit(1)
        except FileNotFoundError:
            print("Semgrep is not installed or not found in PATH.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while running semgrep: {e}")
            sys.exit(1)
        semgrep_json_path = f'{self.target_directory}/semgrep_output.json'
        #print(result.stdout)
    
        findings = []
        try:
            with open(semgrep_json_path, "r+") as f :
                semgrep_json_output = f.read()
            data = json.loads(semgrep_json_output)
            for result in data.get("results", []):
                finding = {
                    "check_id" : result.get("check_id", "Unknown Title"),  # Title
                    "severity" : result.get("extra", {}).get("metadata", {}).get("impact", "Unknown Severity."),  # Severity
                    "explanation" : result.get("extra", {}).get("message", "No explanation provided."),  # Explanation
                    "path" : result.get("path", "Unknown Path"),  # Code path
                    "lines" : result.get("extra", {}).get("lines", "No code snippet provided."),  # Code snippet
                    "fix" : result.get("extra", {}).get("metadata", {}).get("fix", "No recommendation provided.")  # Recommendation
                }
                
                #print("FINDING:\n")
                #print(finding)
                findings.append(finding)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
        return findings