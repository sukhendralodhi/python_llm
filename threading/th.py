# What is threading in Python?
# Threading is a way to run multiple threads (smaller units of a process) concurrently within a single process. It allows you to perform multiple tasks at the same time, which can improve the performance of your program, especially when dealing with I/O-bound tasks.


# WHY OR WHEN TO USE THREADING IN PYTHON?
# 1. To perform multiple tasks concurrently, such as handling user input while performing background tasks.

# 2. To improve the performance of I/O-bound tasks, such as reading/writing files, making network requests, etc.
# 3. To create responsive applications, such as GUI applications, where you want to keep the user interface responsive while performing background tasks.
# 4. To take advantage of multi-core processors by running multiple threads in parallel (although Python's Global Interpreter Lock (GIL) can limit the performance benefits of threading for CPU-bound tasks).
# Example of threading in Python:
