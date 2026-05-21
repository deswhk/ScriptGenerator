# ScriptGenerator

A Python tool that generates PostgreSQL DDL scripts from a single YAML schema definition.

## Why I built this

Writing DDL by hand is repetitive and error-prone. ScriptGenerator solves that: define a schema once in YAML, get correct DDL out the other end — no copy-pasting from old scripts, no typos in column types.

This is the first iteration and is intentionally minimal: it generates `CREATE TABLE` statements only, with no diff/`ALTER` support yet. The next iteration will add schema-change detection so the tool can produce migration scripts when the YAML evolves. Watch this space.

## Tech used

- **Python 3.10+**
- **YAML** — for schema definition
- **Jinja2** — for templating the SQL output
- **Git + GitHub** — version control

## How to run

From a terminal, in the project folder:

​```
python genDDL.py --n InputYaml-Sample.yml
​```

- Looks for `InputYaml-Sample.yml` in the same directory.
- Writes output to `OutputSql-Sample.sql`.
- Replace `Sample` with any meaningful name (typically a business object).

