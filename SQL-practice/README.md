The following tasks must be completed using Python 3.

Create some database for this task.

### Task 1

Create a table "Hospital" with the following parameters:

- `Hospital_Id` with <a href="https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/">auto-increment type</a> and `Primary key`
- `Hospital_Name` with `Varchar` type, not `NULL`
- `Bed_Count` with <a href="https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/">auto-increment type</a>

##### After it, insert following sql:

```sql
INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count)
    VALUES
    ('1', 'Mayo Clinic', 200),
    ('2', 'Cleveland Clinic', 400),
    ('3', 'Johns Hopkins', 1000),
    ('4', 'UCLA Medical Center', 1500);
```

##### Your goal:

- Create a function that returns data based on 3 options with all columns that return:
  - `Hospital_Name` in ascending order
  - `Bed_Count` is greater than 600, sort from most to least
  - Average number of beds in all hospitals
- Create procedure to insert new hospital by `name` and `count`, update `count` if `hospital name` already exists
- Implement procedure to deleting data from table by `hospital name`

### Task 2

Create a table `Doctor` with the following parameters:

- `Doctor_Id` with <a href="https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/">auto-increment type</a> and `Primary key`
- `Doctor_Name` with `VARCHAR` type, not `NULL`
- `Hospital_Id` with <a href="https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/">auto-increment type</a> and not `NULL`
- `Joining_Date` with `date` type, not `NULL`
- `Speciality` with `VARCHAR`, not `NULL`
- `Salary` with `INTEGER` type not `NULL`
- `Experience` `SMALLINT` type

##### After it, insert following sql:

```sql
INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience)
    VALUES
    ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL),
    ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL),
    ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL),
    ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL),
    ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL),
    ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL),
    ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL),
    ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);
```

##### Your goal:

- Create a function that returns data based on 3 options:
  - Return all doctor names with their repective salaries that are greater than average salary, sorted from lowest to highest
  - Return all information about doctors who have joined since the beginning of 2012, sorted from oldest employee to newest.
  - Return how many doctors belong to specialties from a table. (Pediatric: 2, Oncologist: 1, Garnacologist: 3, etc.)
- Create a procedure to update rows based on the `doctor's name`.
- Create a procedure to insert data from csv or json file.

### Task 3

Previous 2 tables(`Hospital` and `Doctor`) should be ready to use!

##### Your goal:

- Create a function that returns data based on 3 options:
  - Join 2 tables where the columns will contain `doctor's name`, `hospital name`, `joined date` and `salary`.
  - Return the names of doctors with the name of the hospital they belong to, whose hospital has more than 800 beds and a salary greater than or equal to 32000
  - Sort by the names of hospitals that pay less than 60,000 in total
- When you delete a `hospital` from the `Hospital` table, delete all rows related to that `hospital` from `Doctor` table.
- Create a procedure to insert data from 2 joined tables into csv or json file with all information except `hospital id` and `bed count`.
