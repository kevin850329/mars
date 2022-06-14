import functools

import dao


@functools.lru_cache()
def get_full_url(short_url: str):
    return dao.get_full_url(short_url)


def add_full_url(full_url):
    short_url = dao.get_or_gen_short_id(full_url)
    return short_url


def add_full_url_with_name(full_url, name):
    short_url = dao.get_or_gen_short_id_with_name(full_url, name)
    return short_url


def get_short_url(full_url):
    return dao.get_short_url(full_url)
