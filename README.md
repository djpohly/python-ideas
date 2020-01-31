# ideas

**Easy creation of custom import hooks to try out new ideas for Python.**

![ideas logo](ideas.png)


## Documentation

[Look here](https://aroberge.github.io/ideas/docs/html/).  Note that
this is work in progress.

## Installation

```
pip install ideas
```

## Usage

Suppose that you want to use `function` as a keyword in Python, to mean
the same thing as `lambda`, enabling you to write

```python
# my_script.py

import some_other_module

square = function x: x**2
print(f"{square(4)} is the square of 4.")
```

You could do this by creating the following program

```python
# Lets's call this 'loader.py'

from ideas.examples import function
function.add_hook()

import my_script
```

and then run

```
python loader.py
```

So, `my_script.py` , `some_other_module.py`, and any other module
loaded by it would recognize that `function` is a valid alternative to `lambda`.

Many more examples can be found in the [documentation](https://aroberge.github.io/ideas/docs/html/).

## Infrequently asked questions ... and comments

The following list has been created before anyone else knew about
this project.

> _Why?_

Because it is fun. If this is not enough of a justification for you, have a look at
[motivation](https://aroberge.github.io/ideas/docs/html/motivation.html)
which contains a longer, and more serious answer.

> _Is it safe to use in production code?_

No.

> _But your example works perfectly well in my code; can I use it in my
> project?_

I don't think you should if your project is to be used by anyone else
but yourself.

> _I found a bug._

Please, by all means, file an issue so that I can perhaps fix it. Note however
that some examples, which are known to fail in some contexts, would
be too complex ensure that they always work in all contexts.

> _I found a cool use of import hooks in another project, different from
> all of your examples._

Please, give me the details and I will see if I can **easily** include
a similar example and if I think it is worthwhile to do so.

> _Can I contribute code for a new example?_

Yes, please, by all means. But I suggest that you first create an issue that gives
an overview of what you wish to accomplish.

> _I think that the explanation you have written for X could be improved upon._

Please tell me more by filing an issue first and possibly creating a pull-request afterwards.

> _I have an idea for a new example, but do not know how to write the code for it._

File an issue ... but please don't be offended if I don't write code for it
and end up closing the issue: I already have too many ideas of my own
for this project, too many other projects, and not
enough time to do all that I want.

> _In file X.py, you do not respect convention Y from PEP-8. This is unacceptable
> in a Python project._

**Seriously?**  This project is all about looking at introducing changes
to Python's syntax, some of which are downright crazy, and you complain
about a PEP-8 violation? ...  Ok, perhaps you can tell me and it might
make sense to change what I wrote.

> _People from the Python-ideas mailing lists mentioned that I should look
> at this project for my idea, but I don't know where to start._

Please, have a look at the [documentation](https://aroberge.github.io/ideas/docs/html/).

> _Why this silly name for a project? The word "ideas" has nothing to do with
> import hooks in Python._

For this project, I was thinking of using `importhook` (singular) or
`importhooks` (plural). However, there is already a project named
`importhook` on Pypi and I thought that using the plural form would
likely be just too confusing.

I settled on `ideas` as I am guessing that the main application would be
for people to try out suggestions from or for python-ideas.


## Tools

This project uses black for formatting, pytest for running tests,
and flake8 for linting.

## Contact:

You can either file an issue or email me at <Andre.Roberge@gmail.com>.


## License

MIT - see the file listed above.
