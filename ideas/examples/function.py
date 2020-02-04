"""This module enables someone to use ``function`` as a keyword
   equivalent to ``lambda``.

   It is slightly more complicated than ``function_simplest.py`` as it
   demonstrates how we can pass parameters when adding an import hook;
   these parameters will be passed back to our function
   ``transform_source``.
"""
import sys

from ideas import import_hook, token_utils


def print_info(kind, source):
    """prints information about the source - either original or transformed"""
    print(f"==========={kind}============")
    print(source)
    print("-----------------------------")


def transform_source(source, show_original=False, show_transformed=False, **kwargs):
    """This function is called by the import hook loader with the named keyword
       that we specified when we created the import hook.

       It gives us the option to compare the original source and the transformed
       one. This type of additional option can be useful when debugging
       a source transformer. Furthermore, if we wish to define a source
       transformation that combines the effect of multiple existing
       transformations, we can combine the existing "inner" functions to
       create our new transformation.
    """
    if show_original:
        print_info("Original", source)

    source = function_as_a_keyword(source)

    if show_transformed:
        print_info("Transformed", source)
    return source


def function_as_a_keyword(source):
    """A simple replacement of ``function`` by ``lambda``.

    Note that, while the string ``lambda`` is shorter than ``function``, we
    do not adjust the information (start_col, end_col) about the position
    of the token. ``untokenize`` uses that information together with the
    information about each original line, to properly keep track of the
    spacing between tokens.
    """
    new_tokens = []
    for token in token_utils.tokenize_source(source):
        if token == "function":  # equivalent to token.string == "function"
            token.string = "lambda"
        new_tokens.append(token)

    new_source = token_utils.untokenize(new_tokens)
    return new_source


def add_hook(show_original=False, show_transformed=False):
    """Creates and adds the import hook in sys.meta_path"""
    callback_params = {
        "show_original": show_original,
        "show_transformed": show_transformed,
    }
    hook = import_hook.create_hook(
        transform_source=transform_source,
        callback_params=callback_params,
        name=__name__,
    )
    sys.meta_path.insert(0, hook)
    return hook
