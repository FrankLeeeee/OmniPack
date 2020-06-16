import powerpack
import os
import pytest


def test_get_memory_state():
    total, used, free = powerpack.get_memory_state()
    assert used < total and free < total

    rss = powerpack.get_memory_state(os.getpid())
    assert rss < used


def test_get_cpu_state():
    pcent = powerpack.get_cpu_state()
    assert pcent < 100
    pcent = powerpack.get_cpu_state(os.getpid())
    assert pcent < 100
