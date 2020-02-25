from ideas import import_hook
from ideas.examples import french, repeat

additional_vocab = {
    "répéter": "repeat",
    "sansfin": "forever",
    "jusquà": "until",
}

french.fr_to_py.update(additional_vocab)


def print_info(kind, source):
    """Prints the source code.

    ``kind`` is usually either ``"Original"`` or ``"Transformed"``
    """
    print(f"==========={kind}============")
    print(source)
    print("-----------------------------")


def transform_source(source, callback_params=None, **kwargs):
    """This function is called by the import hook loader and is used as a
    wrapper for the function where the real transformation is performed.
    """
    if callback_params is not None:
        if callback_params["show_original"]:
            print_info("Original", source)

    source = french.french_to_english(source)
    source = repeat.convert_repeat(source)

    if callback_params is not None:
        if callback_params["show_transformed"]:
            print_info("Transformed", source)

    return source


def add_hook(show_original=False, show_transformed=False, verbose_finder=False):
    """Creates and adds the import hook in sys.meta_path"""
    callback_params = {
        "show_original": show_original,
        "show_transformed": show_transformed,
    }
    hook = import_hook.create_hook(
        transform_source=transform_source,
        callback_params=callback_params,
        hook_name=__name__,
        extensions=[".pyfr"],
        verbose_finder=verbose_finder,
    )
    return hook
