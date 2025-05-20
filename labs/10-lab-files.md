# 🧪 Lab 10: Logging Detector Signal Values

## 🎯 Objective

Create a Python program that simulates logging signal readings from a detector. The program will:

1. Ask the user to enter signal values.
2. Add a timestamp to each reading.
3. Save the results to a file.
4. (Extension) Read the data back and display the log.

---

## 📍Step 1: Gather Input with Timestamps

Prompt the user to enter signal strengths (as numbers). Each time they enter a value:

* Record the **current date and time** alongside it.
* Continue collecting values until the user types `'done'`.

**Hint:** Use a loop and store the readings in a list. Each item in the list should include both the signal value and the time it was entered.

---

## 📍Step 2: Write to a File

Once all values have been entered:

* Open a file in **write mode**.
* Write each reading (with its timestamp) to the file.
* Choose a format that separates the timestamp and the value clearly — e.g. using a pipe (`|`) or a comma.

**Hint:** Use the `with` statement when working with files.

---

## 📍Step 3 (Extension): Read and Display Logged Values

Write a second part to your program (or a separate script) that:

* Opens the file you just created.
* Reads each line of the file.
* Splits the line into a timestamp and signal value.
* Converts the timestamp **back into a `datetime` object**.

**Hint:** Look up `datetime.strptime()` for parsing strings into datetime objects.

---

## 🔍 Example Output

```
Enter signal values (type 'done' to finish):
> 3.4
> 3.5
> 2.9
> done

Data saved to signal_log.txt
```

When reading the file:

```
At 2025-05-20 14:23:45.123456, signal was 3.4
At 2025-05-20 14:24:10.456789, signal was 3.5
At 2025-05-20 14:25:02.789012, signal was 2.9
```

---

## 💡 Extension Ideas

* Ask the user for the **filename** instead of hardcoding it.
* Add a unit (e.g. MeV) to each reading.
* Include **input validation** to ensure signal values are floats.
* Calculate the **average** signal after reading the file back in.

