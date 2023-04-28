# student-csv-maker
A simple python script for creating a mock student csv file

## Usage

`python make_csv.py`

### Will ask the user:
- How many records do you want to generate?*
- What is the lowest grade in your range?*
- What is the highest grade in your range?*

\* All three questions only support integer entries.

## Output:

- CSV file with the following fields:

`last name,first name,student ID,email,grade level`

- Student IDs are generated as `S####`. The first student gets S0000, second is S0001, and so on.
- email addresses are generated as `<first name>.<last name>@anytownschools.org`
