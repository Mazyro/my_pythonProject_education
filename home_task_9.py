from dataclasses import dataclass


@dataclass
class Date:

    year: int
    month: int
    day: int

    def as_tuple(self):
        return self.year, self.month, self.day

    def __gt__(self, other):
        assert isinstance(other, Date)
        return self.as_tuple() > other.as_tuple()


@dataclass
class DateRange:

    start_date: Date
    end_date: Date

    def __gt__(self, other):
        assert isinstance(other, DateRange)
        return self.start_date > other.start_date


def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
    arr = insurance_periods
    arr.sort()

    res = [
        DateRange(arr[el].end_date, arr[el+1].start_date)
        for el in range(0, len(arr)-1) if arr[el].end_date < arr[el+1].start_date
    ]

    return res


if __name__ == '__main__':

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 6, 25)),
        DateRange(Date(2020, 7, 1), Date(2020, 8, 31)),
        DateRange(Date(2020, 6, 29), Date(2020, 7, 31)),
        DateRange(Date(2020, 10, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == [
        DateRange(Date(2020, 6, 25), Date(2020, 6, 29)),
        DateRange(Date(2020, 8, 31), Date(2020, 10, 1)),
    ]

    assert get_ranges_wo_insurance([]) == []

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
        DateRange(Date(2020, 7, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == []
