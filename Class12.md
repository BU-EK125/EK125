# Week 7A Preread: Dictionaries

A Python dictionary is a built-in data structure that stores data as key–value pairs, allowing fast lookup, insertion, and deletion by key. It is enclosed in curly braces `{}` and uses a colon `:` to separate each key from its value.

## Dictionaries

Dictionaries are a Python data structure, but they are a mapping type, not a sequence.  This is because indexing into a dictionary is accomplished using **keys**, not integers. The type of a dictionary is `dict`.

Dictionaries are created by putting key-value pairs in curly braces (`{}`). Keys are names specified as strings. The pair is specified as a key followed by a colon, followed by the value for that key, as in `'key':value`.  The following is an example of a dictionary that stores information about a particular hurricane.

```python
>>> bigone = {'name':'Bertha', 'year': 1952, 'category': 4}
```

Values can be retrieved from a dictionary by giving the name of the dictionary variable and then the name of the key in square brackets.

```python
>>> bigone['year']
1952
```

An error will result if the key does not exist in the dictionary.

```python
>>> bigone['size']
```
```
KeyError: 'size'
```

An error will also occur if you try to index using an integer; values are only referenced using keys.

Dictionaries are a mutable type. Values can be modified using assignment statements.

```python
>>> bigone['category'] = 5
>>> bigone
{'name': 'Bertha', 'year': 1952, 'category': 5}
```

More key-value pairs can be added to a dictionary in the same way.

```python
>>> bigone['eyewidth'] = 400
>>> bigone
{'name': 'Bertha', 'year': 1952, 'category': 5, 'eyewidth': 400}
```

Key-value pairs can be deleted from a dictionary using the `del` command.

```python
>>> del bigone['eyewidth']
>>> bigone
{'name': 'Bertha', 'year': 1952, 'category': 5}
```

The `len` function returns the number of key-value pairs in the dictionary.

```python
>>> len(bigone)
3
```

The `in` and `not in` operators can be used to find whether a key is in a dictionary or not.

```python
>>> 'year' in bigone
True
```

```python
>>> 'sqarea' not in bigone
True
```

The `list` function will return a list of all of the key names from a dictionary.

```python
>>> list(bigone)
['name', 'year', 'category']
```

There are a number of methods that work with dictionaries.

The `get` method retrieves a value from a dictionary; it returns `None` by default if the key is not in the dictionary.

```python
>>> bigone.get('year')
1952
```

If the key is not in the dictionary, the value `None` that is returned is not automatically shown, but can be printed, or tested in a selection statement.

```python
>>> print(bigone.get('size'))
None
```

A value other than `None` can also be specified to be used if the key is not in the dictionary, e.g. a flag value of -999.

```python
>>> bigone.get('size', -999)
-999
```

Note that this does not add a key-value pair to the dictionary.

The `get` method is therefore safer to use than just putting a key name in square brackets, since get will return a value if the key is not found, whereas using square brackets will result in an error if the key is not found.

The `pop` method deletes an item from a dictionary and returns its value. A default value to return can be specified in case the key is not in the dictionary; if the default is not specified and the key is not found in the dictionary, an error results.

```python
>>> delcat = bigone.pop('category')
>>> delcat
5
```

```python
>>> bigone
{'name': 'Bertha', 'year': 1952}
```

```python
>>> bigone.pop('size')
KeyError: 'size'
```

```python
>>> bigone.pop('size', -999)
-999
```

The `popitem` method deletes the last key-value pair in a dictionary, and returns this as a tuple.

```python
>>> k,v = bigone.popitem()
>>> print(k,v)
year 1952
```

The `clear` method deletes all of the key-value pairs from a dictionary.

```python
>>> bigone.clear()
>>> bigone
{}
```

There are also methods that can be used to iterate: `keys()`, `values()`, and `items()`, for the dictionary's keys, values, and key-value pairs, respectively.

For example, the following call to the keys method returns the names of the keys. Technically, it returns a `view` object, `dict_keys`.

```python
>>> bigone = {'name':'Bertha', 'year': 1952, 'category': 4}
>>> bigone.keys()
dict_keys(['name', 'year', 'category'])
```

Normally, the `view` object would not be accessed or displayed, however. Instead, it would be typical to iterate over the result.

```python
for kname in bigone.keys():
    print('The key is', kname)
The key is name
The key is year
The key is category
```

To loop over the key-value pairs, the `items` method is used, and two iterator variables are created to store the keys and values individually.

```python
for k, v in bigone.items():
    print('The value of',repr(k),'is',v)
The value of 'name' is Bertha
The value of 'year' is 1952
The value of 'category' is 4
```

We have stored information about one hurricane in a dictionary.  In order to store information on more than one hurricane, we could create a list of dictionaries.

```python
>>> hurr0 = {'name': 'Bertha', 'year': 1952, 'category': 4}
>>> hurr1 = {'name': 'Bob', 'year': 1990, 'category': 2}
>>> hurr2 = {'name': 'Camilla', 'year': 1960, 'category': 5}
>>> hurricanes = [hurr0, hurr1, hurr2]
>>> hurricanes[2]  # show example
{'name': 'Camilla', 'year': 1960, 'category': 5}
```

Once we have a list of dictionaries, we could iterate through the list, for example to print information on the more powerful hurricanes.

```python
print('The largest hurricanes were:')
for hurr in hurricanes:
    if hurr['category'] >= 4:
        print(repr(hurr['name']))
The largest hurricanes were:
'Bertha'
'Camilla'
```

It is also possible for values in a dictionary to be data structures themselves. This has already been done, since strings are a sequence data type. Another possibility would be to have a list as a value.  Note also in this example that each key-value pair is entered on a separate line, which makes it easier to read.

```python
icdessert = {
    'flavor': 'malted',
    'cone': True,
    'nscoops': 2,
    'addins': ['pecans', 'chocolate chips']
}
icdessert['addins']
['pecans', 'chocolate chips']
```

Since the key `addins` is a list, it can be indexed.

```python
>>> icdessert['addins'][0]
'pecans'
```

We could use a `for` loop to print the elements from the list individually.

```python
print('Your ice cream add-ins are:')
for yummy in icdessert['addins']:
    print(yummy.title(),'!!!')
Your ice cream add-ins are:
Pecans !!!
Chocolate Chips !!!
```

For a dictionary comprehension, key-value pairs must be created.

```python
>>> cubedict = {i: i**3 for i in range(5)}
>>> cubedict
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
```
