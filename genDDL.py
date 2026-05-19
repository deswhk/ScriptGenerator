# DDL Script Generator
import os
import yaml
import argparse
from jinja2 import Environment, FileSystemLoader

TEMPLATES = [
    "1-table.sql.j2",
    "2-constraint.sql.j2",
    "3-index.sql.j2",
    "4-view.sql.j2",
    "5-function.sql.j2",
    "6-trigger.sql.j2",
    "7-ownership.sql.j2",
    "8-grant.sql.j2"
]

# --- Argument parsing ---
parser = argparse.ArgumentParser(description="SQL Generator from YAML")
parser.add_argument(
    "-n", "--name",
    required=True,
    help="Suffix name used after dash (e.g. Order, Customer, Invoice)"
)
args = parser.parse_args()

# --- Base folder ---
# Dynamically sets the path to the folder where this script is saved
base_folder = os.path.dirname(os.path.abspath(__file__))

# --- Build file names ---
yaml_filename = f"InputYaml-{args.name}.yml"
sql_filename = f"OutputSql-{args.name}.sql"

yaml_file = os.path.join(base_folder, yaml_filename)
output_file = os.path.join(base_folder, sql_filename)

# --- Load YAML ---
with open(yaml_file, "r", encoding="utf-8") as f:
    model = yaml.safe_load(f)

# --- Setup Jinja2 environment ---
env = Environment(
    loader=FileSystemLoader(os.path.join(base_folder, "template")),
    trim_blocks=True,
    lstrip_blocks=True
)

# --- Generate SQL ---
sql = []

# Loop over each table in YAML
for t in model.get("tables", []):
    # Each table may have its own schema
    ctx = { **t } # table-specific context includes schema, table, id, columns, joins, audit, triggers, etc.

    for tpl in TEMPLATES:
        sql.append(env.get_template(tpl).render(**ctx))

# Write the default setting at the very beginning
with open(output_file, "w", encoding="utf-8") as f:
    f.write("SET app.userid='00000000-0000-0000-0000-000000000000';\n")
    f.write("SET app.role='SRVC';\n") # Added newline for cleaner formatting
    
    # --- Write SQL to file ---
    f.write("\n".join(sql))

print(f"SQL generated successfully at {output_file}")