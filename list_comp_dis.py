"""Print dissasembly of list comprehensions to files."""
import dis
import os.path


def for_loop(n: int) -> list[int]:
    m_list = []
    for x in range(n):
        m_list.append(x)
    return m_list


def simple_list_comp(n: int) -> list[int]:
    return [x for x in range(n)]


if __name__ == "__main__":
    base = f"{os.getcwd()}/build"
    if not os.path.exists(base):
        os.makedirs(base)

    with open(f"{base}/for_loop", "w+") as f:
        dis.dis(for_loop, file=f)

    with open(f"{base}/simple_list_comp", "w+") as f:
        dis.dis(simple_list_comp, file=f)
