# Use-of-embedded-functions

Map:
The map () function takes one function object as the first parameter. (Functions can also be sent to another function as they are objects.) Taking the iteration data as a 2nd parameter, applying the sent function on each element and returning the results as a map object.

Reduce:
The reduce () function applies the function it takes as a value to the first 2 elements of the list, starting from the left, and then applies the resulting result to the 3rd element of the list, continuing in this way and returning one value when the list ends.

Filter:
The filter () function takes a function that always returns a logical value (True, False) as the first parameter and applies this function to each element of data types such as a list. The filter only returns one filter object, taking values that produce True results.

Zip:
The zip function creates one list by grouping the elements of the lists into bundles, respectively.

Enumerate:
Sometimes we enumerate each element with indexes and form bunch pairs. When writing a for loop, we may sometimes want to get both elements and indexes. In such a case, we can use the enumerate function that enumerates.

All and Any:
The all () function returns True if all values are True, and False if at least one value is False.
The any () function returns False if all values are False, and True if at least one value is True.
