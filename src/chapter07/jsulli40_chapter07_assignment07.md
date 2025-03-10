# Technical Design Document

## Name:

**Joseph D Sullivan**

## Date Created:

**March 09, 2025**

---

## **Program Description**

Collects user input for paragraph text, splits input into sentences using regular expressions, and displays sentences to
the user.

---

## **Constant(s)**

| Name             | Type                       | Description                                                                      |
|------------------|----------------------------|----------------------------------------------------------------------------------|
| `REGEX_SENTENCE` | Regular Expression Pattern | Regular expression pattern to match sentences. Modified from `book_code_7.4.py`. |

### **Allows:**

- Matches sentences that start with a number (0-9) or an uppercase letter (A-Z).
- Captures everything until a period (`.`), exclamation (`!`), or question mark (`?`).
- Ensures that the next character is either an uppercase letter, a number, or the end of the string.
- Uses `DOTALL` and `MULTILINE` flags to handle multiline input properly.

---

## **Function(s)**

### **1. `main`**

- **Description**:  
  Entry function for when code is invoked directly.  
  Retrieves a paragraph from user input, splits it into sentences, and displays results.

- **Parameters**:  
  *None*

- **Logic**:
    1. Retrieve paragraph from user input.
    2. Split input into sentences.
    3. Display results.

- **Returns**:  
  *None*

---

### **2. `get_sentences`**

- **Description**:  
  Extracts sentences from a paragraph using `REGEX_SENTENCE`.

- **Parameters**:

| Name        | Type  | Description                               |
|-------------|-------|-------------------------------------------|
| `paragraph` | `str` | The paragraph text to get sentences from. |

- **Logic**:  
  Uses a regular expression to find and extract sentences.

- **Returns**:

| Type        | Description                                 |
|-------------|---------------------------------------------|
| `List[str]` | A list of sentences found in the paragraph. |

---

### **3. `display_sentences`**

- **Description**:  
  Displays each sentence in the provided list and prints the total sentence count.

- **Parameters**:

| Name        | Type        | Description          |
|-------------|-------------|----------------------|
| `sentences` | `List[str]` | A list of sentences. |

- **Logic**:
    1. Print each sentence found in the input.
    2. Print the total number of sentences.

- **Returns**:  
  *None*

---

## **Logic Flow**

1. `main()`
2. `get_sentences()`
3. `display_sentences()`

---

## **Repository Link**

[GitHub Repository](https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter07/jsulli40_chapter07_assignment07.py)
