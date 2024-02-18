


import os


# List of strings
file_names = [
"Advanced Query and Scan Operations",
"Atomic Counter",
"Attributes",
"Auto Scaling",
"Backup and Restore Strategies",
"Batch Operations",
"Capacity Modes",
"Conditional Expressions",
"Conditional Writes",
"Consistent Reads",
"DAX (DynamoDB Accelerator)",
"DynamoDB Accelerator (DAX)",
"DynamoDB Local",
"DynamoDB Streams",
"DynamoDB Transactions",
"Eventual Consistency Model",
"Expression Attribute Names and Values",
"Filter Expressions",
"Fine-Grained Access Control (FGAC)",
"Global Secondary Index (GSI)",
"Global Tables",
"Items",
"Local Secondary Index (LSI)",
"On-Demand Backup and Restore",
"On-Demand Capacity",
"Partition Key Selection Strategies",
"Point-in-Time Recovery (PITR)",
"Primary Key",
"Provisioned Throughput",
"Secondary Index",
"Tables",
"Time-to-Live (TTL)",
"Transactions",



]

# Directory to save Markdown files
output_directory = "/Users/chris/code/OSDSC/Learning/Data Engineering/DynamoDB"

# Ensure the output directory exists, create if not
os.makedirs(output_directory, exist_ok=True)

# Loop through the list and create empty Markdown files
for file_name in file_names:
    file_path = os.path.join(output_directory, f"{file_name}.md")
    with open(file_path, "w") as file:
        # Writing an empty file
        pass

print("Markdown files created successfully.")
