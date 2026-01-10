# Hacking

Things to keep in mind while working on the code....

## Callouts

When you need to make a callout, ensure that you have a space between the opening (`{`) and closing bracket (`}`):

````
::: { #tip-06-name-error .callout-tip title="Stop & Think" collapse="false" }
Look at the following code:

```python
try:
    print(gene)
except NameError as error:
    print(f"{error=}")
```

What do you think will happen and why?
:::
````

This is important for the scripts that parse the markdown content!! (E.g., for chunking the markdown files.)
