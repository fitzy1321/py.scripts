from dataclasses import dataclass, field


class Reusable:
    def test(self) -> None:
        print(f"Using object {type(self).__name__}: {id(self)=}")


@dataclass
class ReusablePool:
    size: int
    free: list = field(default_factory=list)
    in_use: list = field(default_factory=list)

    def __post_init__(self) -> None:
        for _ in range(self.size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception("No more objects available")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable) -> None:
        self.in_use.remove(r)
        self.free.append(r)


@dataclass
class PoolManager:
    pool: ReusablePool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self):
        self.pool.release(self.obj)


def main() -> int:
    pool = ReusablePool(2)
    with PoolManager(pool) as r:
        r.test()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
