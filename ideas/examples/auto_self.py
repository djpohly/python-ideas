"""Description here
"""
from functools import partial
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

    source = automatic_self(source)

    if show_transformed:
        print_info("Transformed", source)
    return source


def automatic_self(source):
    """Description here.
    """
    new_tokens = []
    auto_self_block = False
    self_name = ""
    indentation = 0

    get_nb = partial(token_utils.get_number_nonspace_tokens, ignore_comments=True)
    get_index = token_utils.get_first_nonspace_token_index

    for tokens in token_utils.get_lines_of_tokens(source):
        if auto_self_block:
            if get_nb(tokens) == 1:
                variable = tokens[get_index(tokens)]
                new_string = f"{self_name}.{variable.string} = {variable.string}\n"
                line = " " * indentation + new_string
                tokens = [line]
            else:
                auto_self_block = False
        elif get_nb(tokens) == 4:
            index = get_index(tokens)
            if (
                tokens[index].is_identifier()
                and tokens[index + 1] == "."
                and tokens[index + 2] == "="
                and tokens[index + 1].end_col == tokens[index + 2].start_col
                and tokens[index + 3] == ":"
            ):
                self_name = tokens[index].string
                indentation = tokens[index].start_col
                auto_self_block = True
                continue
        new_tokens.extend(tokens)
    return token_utils.untokenize(new_tokens)


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
