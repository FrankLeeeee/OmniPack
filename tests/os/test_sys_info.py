import omnipack
import os
import pytest


def test_get_memory_state():
    total, used, free = omnipack.get_memory_state()
    assert used < total and free < total

    rss = omnipack.get_memory_state(os.getpid())
    assert rss < used


def test_get_cpu_state():
    pcent = omnipack.get_cpu_state()
    assert pcent < 100
    pcent = omnipack.get_cpu_state(os.getpid())
    assert pcent < 100
