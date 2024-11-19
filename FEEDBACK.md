<!-- code_chunk_output -->

- [LAB-9 Feedback](#lab-9-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test: Running the code](#blind-test-running-the-code)
    - [Open Test: Looking at the code](#open-test-looking-at-the-code)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

<!-- /code_chunk_output -->

# LAB-9 Feedback

### Test Cases

- No test cases

### Blind Test: Running the code

| Result     | Description                                                                              |
|------------|------------------------------------------------------------------------------------------|
| **YES-** | Asks the user for an input file name                                                    |
| **YES-** | Asks user to try again if input file name doesn't exist (try `bbb.txt`)                 |
| **YES-** | Works  with `yalew.txt`, `sibren.txt`, and `nweke.txt`. |
| **-NO** | The number of tables should be the length of file divided by 5 |
| **YES-** | Try all three files again. Each table should have 5 people at each table                |
| **YES-** | Output of assignments has `~~~~~` lines between each, or something similar              |
| **YES-** | For each person, it lists Table number, Seat number, Name                               |

### Open Test: Looking at the code

| Result     | Description                                                                              |
|------------|------------------------------------------------------------------------------------------|
| **YES-** | The algorithm matches the code                                           |
| **YES-** | Purpose of the program is clearly stated |  
| **YES-** | There is at least one for loop in the code                                              |
| **YES-** | All loops except for error checking on user input is a loop                             |
| **YES-** | Error checking on user input `filename` with  `while os.path.isfile(filename)` |
| **YES-** | There is a function for error checking file name that returns file name                 |
| **YES-** | There is a function for reading from the file that returns a list of names              |
| **YES-** | There is a function for determining and outputting table assignments                    |


### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**YES-** | Reflection 1   |
|**YES-** | Reflection 2   |
|**YES-** | Algorithm      |

### Comments on the grading
- ` for names in name_sign(file_name):` should have been `names = name_sign(file_name)` <br>` for name in names:`
- `name_sign` and `read_file` does the same thing
- 

### Grade: M

### Participation Grade: S
 - If participation grade is unsatisfactory check the `NO` in the documents sections
