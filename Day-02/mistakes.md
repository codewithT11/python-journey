# Things to Remember
- Strings support indexing and slicing.
- Slicing syntax: `start:end:step`
- End index is excluded.
- Negative indexing starts from the end.
- `[::-1]` reverses a string or list.
- `append()` adds one item.
- `extend()` adds multiple items from another iterable.
- Lists are mutable.
- Tuples are immutable.
- Sets store only unique values and are unordered.
- Dictionaries store data as key-value pairs.
- Dictionary keys must be immutable.
- Dictionary values can be of any data type, including lists.

# Mistakes
- Forgot that list slicing returns a new list.
- Didn't know that `[::-2]` means reverse while skipping every second character.
- Thought assigning one list to another (`a = numbers`) creates a copy—it only creates another reference.
- Thought a list could be a dictionary key. Dictionary keys must be immutable.
- Explained dictionaries as "key-value pairs" instead of explaining the problem they solve.
- Avoid writing repetitive code; use loops when the same task repeats.
- Always check if an item exists before removing it from a list.