This tool automates the creation of PostgreSQL database objects based on a YAML configuration. 
It uses Python and Jinja2 to generate standard table definitions and its related objects.
​How to Run
​To generate a SQL script, run the following command from your PowerShell terminal:
python genDDL.py --n Sample
• ​This will look for InputYaml-Sample.yml in the same directory.
• ​The generated SQL will be saved as OutputSql-Sample.sql.
• ​Replace 'Sample' with a meaningful business object name.