import json


class JsonParser:

    def __init__(self, value):
        self._value = value

    def __enter__(self):
        return json.loads(self._value)

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'{tuple((self._x, self._y))}'

    def as_tuple(self):
        return tuple((self._x, self._y))


class Rectangle:

    def __init__(self, sp, ep):
        self._sp = sp  # test (1, 0)
        self._ep = ep  # test (7, 3)

    def __str__(self):
        return f'rect{tuple((self._sp.as_tuple(), self._ep.as_tuple()))}'

    def contains(self, point=(0, 0)):

        x = self._sp.as_tuple()[0]  # (1, 0)[0]
        y = self._sp.as_tuple()[1]  # (1, 0)[1]
        w = self._ep.as_tuple()[0]  # (7, 3)[0]
        h = self._ep.as_tuple()[1]  # (7, 3)[1]
        p_x = point.as_tuple()[0]  # (1, 0)[0]
        p_y = point.as_tuple()[1]  # (1, 0)[1]

        if not ((x <= p_x <= w) and (y <= p_y <= h)):
            return False
        return True


if __name__ == '__main__':

    with JsonParser('"hello"') as res:
        # print(res)
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        # print(res)
        assert res == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    # print(str(start_point))
    end_point = Point(7, 3)
    # print(str(end_point))
    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    # print(str(rect))
