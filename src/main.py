#! /usr/bin/env python3


class A:
    def run(self):
        print("I'm A")


class B(A):
    def run(self):
        print("I'm B")


class C(A):
    def run(self):
        print("I'm C")


class D(B, C):
    pass


if __name__ == "__main__":
    d = D()
    d.run()
