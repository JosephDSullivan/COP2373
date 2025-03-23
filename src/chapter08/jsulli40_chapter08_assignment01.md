# Technical Design Document

## Name:

**Joseph D Sullivan**

## Date Created:

**March 21, 2025**

---

## Program Description

This program allows an instructor to store and retrieve student score data.

---

## Constant(s)

| Name             | Type    | Description                                        | Value        |
|------------------|---------|----------------------------------------------------|--------------|
| `DEFAULT_SCORE`  | `float` | Default exam score if no score is provide.         | 0.0          |
| `MIN_SCORE`      | `float` | Minimum valid exam score.                          | 0.0          |
| `MAX_SCORE`      | `float` | Maximum valid exam score.                          | 120.0        |
| `DATA_FILE_NAME` | `str`   | CSV file name used to store student grade records. | `grades.csv` |

---

## Class(es)

### `StudentScore`

- #### Description
  Data class representing a single student's exam scores.

- #### Attribute(s)

  | Name         | Type    | Description               | 
  |--------------|---------|---------------------------|
  | `first_name` | `str`   | The student's first name. |
  | `last_name`  | `str`   | The student's last name.  |
  | `exam01`     | `float` | Score for exam 1.         |
  | `exam02`     | `float` | Score for exam 2.         |
  | `exam03`     | `float` | Score for exam 3.         |

- #### Method(s)

  1. ##### `__post_init__`

      ###### Description
      Validate the student score data.

      ###### Parameter(s)
        | Name   | Type | Description |
        |--------|------|-------------|
        | `self` |      |             |

      ###### Logic
      1. Verify first name and last name are not empty.
      1. Verify all scores are between MIN_SCORE and MAX_SCORE, inclusive.

      ###### Return(s)
      | Type | Description |
      |------|-------------|
      | None |             |

---

### `StudentScores`

- #### Description
  List of StudentScore, representing all students' scores.

- #### Attribute(s)

  | Name       | Type                 | Description             | 
  |------------|----------------------|-------------------------|
  | `students` | `List[StudentScore]` | A list of StudentScore. |

- #### Method(s)

  1. ##### `add_student`

      ###### Description
      Adds a StudentScore to the students list and the CSV data file.

      ###### Parameter(s)
      | Name      | Type           | Description              |
      |-----------|----------------|--------------------------|
      | `self`    |                |                          |
      | `student` | `StudentScore` | The StudentScore to add. |

      ###### Logic
      1. Validate data.
      1. Add student to students list.
      1. Add student to csv data file.

      ###### Return(s)
      | Type | Description |
      |------|-------------|
      | None |             |

  1. ##### `display_students`

      ###### Description
      Displays all students' scores in a tabular format.

      ###### Parameter(s)
      | Name   | Type | Description |
      |--------|------|-------------|
      | `self` |      |             |

      ###### Logic
      1. Display all students in tabular format.

      ###### Return(s)
     | Type | Description |
     |------|-------------|
     | None |             |

  1. ##### `load_students`

      ###### Description
      Loads student records from the CSV file into the student list. Warns user if file does not exist.

      ###### Parameter(s)
      | Name   | Type | Description |
      |--------|------|-------------|
      | `self` |      |             |

      ###### Logic
      1. Clear current list before importing.
      1. Open csv data file and import all rows into self.students. If file not found, warn user.

      ###### Return(s)
     | Type | Description |
     |------|-------------|
     | None |             |

---

## Function(s)

### main

#### Description
Entry function for when code is invoked directly.

Load student scores list, display table, retrieve new student scores,
redisplay table, repeat until the user exits, and redisplay table one
final time.

#### Parameter(s)
| Name | Type | Description |
|------|------|-------------|
|      |      |             |

#### Logic
1. Load student scores list.
1. Display initial data to user.
1. Retrieve number of students to add from user.
1. Loop for each new student: create new student and append it to students.
1. Display new students list to user.
1. Display results one final time and exit program if 0 entered.

#### Return(s)
| Type | Description |
|------|-------------|
| None |             |

---

### get_student

#### Description
Retrieves student data from user and create a StudentScore with that data.

#### Parameter(s)
| Name | Type | Description |
|------|------|-------------|
|      |      |             |

#### Logic
1. Regular expression Pattern to verify string is not blank.
1. Prompt user to enter student score data.
1. Return student score data as StudentScore.

#### Return(s)
| Type         | Description                                         |
|--------------|-----------------------------------------------------|
| StudentScore | A dataclass instance containing the student's data. |

---

### get_int

#### Description
Prompt the user to enter an integer, validate input, and return it.

#### Parameter(s)
| Name               | Type         | Description                                                                                            |
|--------------------|--------------|--------------------------------------------------------------------------------------------------------|
| prompt             | str  \| None | The message displayed to the user when asking for input. Defaults to None, which represents no prompt. |
| lbound             | int \| None  | The lower bound (inclusive) for valid input. Defaults to None, which represents no lower bound.        |
| ubound             | int \| None  | The upper bound (inclusive) for valid input. Defaults to None, which represents no upper bound.        |
| repeat_until_valid | bool \| None | Whether to keep prompting until valid input is received. Defaults to True.                             |

#### Logic
1. Loop until exit.
1. Retrieve input from user.
1. Validate input.
1. Validate bounds. If out of bounds, warn user and reloop.
1. Return validated input.

#### Return(s)
| Type        | Description                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------|
| int \| None | The validated integer input from the user, or None if repeat_until_valid is False and input is invalid. |

---

### get_Float

#### Description
Prompt the user to enter an float, validate input, and return it.

#### Parameter(s)
| Name               | Type         | Description                                                                                            |
|--------------------|--------------|--------------------------------------------------------------------------------------------------------|
| prompt             | str  \| None | The message displayed to the user when asking for input. Defaults to None, which represents no prompt. |
| lbound             | float \| None  | The lower bound (inclusive) for valid input. Defaults to None, which represents no lower bound.        |
| ubound             | float \| None  | The upper bound (inclusive) for valid input. Defaults to None, which represents no upper bound.        |
| repeat_until_valid | bool \| None | Whether to keep prompting until valid input is received. Defaults to True.                             |

#### Logic
1. Loop until exit.
1. Retrieve input from user.
1. Validate input.
1. Validate bounds. If out of bounds, warn user and reloop.
1. Return validated input.

#### Return(s)
| Type          | Description                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------|
| float \| None | The validated float input from the user, or None if repeat_until_valid is False and input is invalid. |

---

### get_str

#### Description
Prompt the user to enter an float, validate input, and return it.

#### Parameter(s)
| Name               | Type                | Description                                                                                                                          |
|--------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| prompt             | str  \| None        | The message displayed to the user when asking for input. Defaults to None, which represents no prompt.                               |
| pattern            | Union[str, Pattern] | The regular expression - as a string or a compiled re.Pattern - to validate input. Defaults to None, which represents no validation. |
| repeat_until_valid | bool \| None        | Whether to keep prompting until valid input is received. Defaults to True.                                                           |

#### Logic
1. Loop until exit.
1. Retrieve input from user.
1. Validate input.
1. Validate bounds. If out of bounds, warn user and reloop.
1. Return validated input.

#### Return(s)
| Type        | Description                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------|
| str \| None | The validated string input from the user, or None if repeat_until_valid is False and input is invalid. |

---

## **Logic Flow**

1. `main()`
1. `StudentScores()`
1. `StudentScores().load_students()`
1. `StudentScores().display_students()`
1. `get_int()`
1. `StudentScores().display_students()`
1. `get_student()`
1. `get_str()`
1. `get_float()`
1. `StudentScores().add_student()`
1. `StudentScores().display_students()`

---

## **Repository Link**

[GitHub Repository](https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter08/jsulli40_chapter08_assignment01.py)
