from enum import IntEnum
try:
    from enum import IntFlag
except ImportError:
    IntFlag = IntEnum


class SummaryType(IntFlag):
    """SummaryType indicates which types of summary should be calculated.

    Based on :class:`enum.IntEnum` in Python 3.5 or earlier. `SummaryType`'s can
    be or'ed together. Python 3.6 or higher returns a new `IntFlag`, while in
    previous versions it will be casted down to `int`.

    >>> SummaryType.MINIMUM | SummaryType.MAXIMUM  # Returns minimum and maximum
    <SummaryType.MAXIMUM|MINIMUM: 12>  # On Python 3.6+
    12  # On previous versions

    Detailed information is available at https://techsupport.osisoft.com/Documentation/PI-AF-SDK/html/T_OSIsoft_AF_Data_AFSummaryTypes.htm
    """

    #: No summary data
    NONE = 0
    #: A total over the time span
    TOTAL = 1
    #: Average value over the time span
    AVERAGE = 2
    #: The minimum value in the time span
    MINIMUM = 4
    #: The maximum value in the time span
    MAXIMUM = 8
    #: The range of the values (max-min) in the time span
    RANGE = 16
    #: The sample standard deviation of the values over the time span
    STD_DEV = 32
    #: The population standard deviation of the values over the time span
    POP_STD_DEV = 64
    #: The sum of the event count (when the calculation is event weighted). The sum of the event time duration (when the calculation is time weighted.)
    COUNT = 128
    #: The percentage of the data with a good value over the time range. Based on time for time weighted calculations, based on event count for event weigthed calculations.
    PERCENT_GOOD = 8192
    #: The total over the time span, with the unit of measurement that's associated with the input (or no units if not defined for the input).
    TOTAL_WITH_UOM = 16384
    #: A convenience to retrieve all summary types
    ALL = 24831
    #: A convenience to retrieve all summary types for non-numeric data
    ALL_FOR_NON_NUMERIC = 8320


class CalculationBasis(IntEnum):
    """CalculationBasis indicates how values should be weighted over a time range

    Detailed information is available at https://techsupport.osisoft.com/Documentation/PI-AF-SDK/html/T_OSIsoft_AF_Data_AFCalculationBasis.htm
    """

    #: Each event is weighted according to the time over which it applies.
    TIME_WEIGHTED = 0
    #: Each event is weighted equally
    EVENT_WEIGHTED = 1
    TIME_WEIGHTED_CONTINUOUS = 2
    TIME_WEIGHTED_DISCRETE = 3
    EVENT_WEIGHTED_EXCLUDE_MOST_RECENT = 4
    EVENT_WEIGHTED_EXCLUDE_EARLIEST = 5
    EVENT_WEIGHTED_INCLUDE_BOTH_ENDS = 6


class TimestampCalculation(IntEnum):
    AUTO = 0
    EARLIEST_TIME = 1
    MOST_RECENT_TIME = 2


class ExpressionSampleType(IntEnum):
    EXPRESSION_RECORDED_VALUES = 0
    INTERVAL = 1
