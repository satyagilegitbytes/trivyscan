import os
import json
import pandas as pd

def json_to_excel(input_dir, output_file):
    all_data = []
    
    for file in os.listdir(input_dir):
        if file.endswith('.json'):
            with open(os.path.join(input_dir, file), 'r') as f:
                data = json.load(f)
                for vuln in data.get("Results", []):
                    for finding in vuln.get("Vulnerabilities", []):
                        all_data.append({
                            "Target": data["ArtifactName"],
                            "Package": finding.get("PkgName"),
                            "Installed Version": finding.get("InstalledVersion"),
                            "Fixed Version": finding.get("FixedVersion"),
                            "Severity": finding.get("Severity"),
                            "Description": finding.get("Description"),
                        })
    
    # Create a DataFrame and save it to Excel
    df = pd.DataFrame(all_data)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_directory = "trivy-reports"
    output_excel = "report.xlsx"
    json_to_excel(input_directory, output_excel)
