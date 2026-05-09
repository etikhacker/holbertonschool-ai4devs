# Benchmark Tasks

## Task 1 - CRUD Endpoint

**Requirements**: Implement a `POST /users` endpoint with input validation.  
**Inputs**: JSON body `{ "name": string, "email": string }`  
**Outputs**: Stored user object with auto-generated ID  
**Acceptance Criteria**:
- Returns `201 Created` with the new user object on success
- Returns `400 Bad Request` if email format is invalid
- Returns `400 Bad Request` if `name` or `email` fields are missing
- User is persisted in an in-memory store or database

---

## Task 2 - Word Frequency Counter

**Requirements**: Write a Python script that reads a `.txt` file and prints the word count and the top 5 most common words.  
**Inputs**: A plain text file path passed as a command-line argument (e.g., `python counter.py sample.txt`)  
**Outputs**: Printed output showing:
- Total word count
- Top 5 most frequent words with their counts

**Acceptance Criteria**:
- Handles missing or invalid file path with a clear error message
- Word comparison is case-insensitive (e.g., "The" and "the" count as the same word)
- Punctuation is stripped before counting
- Output is formatted and easy to read

---

## Task 3 - Random Joke Web Page

**Requirements**: Build a simple static web page that displays a random joke loaded from a local `jokes.json` file.  
**Inputs**: A `jokes.json` file containing an array of at least 5 joke strings  
**Outputs**: A web page (`index.html`) that displays one random joke and a button to load another  
**Acceptance Criteria**:
- Page loads without errors when served via a local HTTP server
- Clicking the "New Joke" button displays a different joke each time
- Jokes are fetched from `jokes.json` using the Fetch API
- Page displays a fallback message if the JSON file fails to load

---

## Task 4 - Temperature Converter CLI

**Requirements**: Build a command-line tool that converts temperatures between Celsius, Fahrenheit, and Kelvin.  
**Inputs**: Two command-line arguments — the temperature value and the conversion type (e.g., `node convert.js 100 CtoF`)  
**Outputs**: Converted temperature value printed to the console  
**Acceptance Criteria**:
- Supports conversions: `CtoF`, `FtoC`, `CtoK`, `KtoC`, `FtoK`, `KtoF`
- Returns a clear error message for unsupported conversion types
- Handles non-numeric input gracefully
- Results are rounded to 2 decimal places
