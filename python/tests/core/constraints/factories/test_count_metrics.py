from whylogs.core.constraints.factories import (
    count_below_number,
    null_percentage_below_number,
    null_values_below_number,
)


def test_count_below_number(builder, nan_builder):
    builder.add_constraint(count_below_number(column_name="weight", number=10))
    builder.add_constraint(count_below_number(column_name="weight", number=1))
    constraint = builder.build()
    assert not constraint.validate()
    # ReportResult(name, passed, failed, summary)
    assert constraint.generate_constraints_report() == [
        ("count of weight lower than 10", 1, 0, None),
        ("count of weight lower than 1", 0, 1, None),
    ]

    nan_builder.add_constraint(count_below_number(column_name="a", number=10))
    nan_builder.add_constraint(count_below_number(column_name="a", number=1))
    constraint = nan_builder.build()
    assert not constraint.validate()
    assert constraint.generate_constraints_report() == [
        ("count of a lower than 10", 1, 0, None),
        ("count of a lower than 1", 0, 1, None),
    ]
    for (x, y) in zip(constraint.report(), constraint.generate_constraints_report()):
        assert (x[0], x[1], x[2]) == (y[0], y[1], y[2])


def test_null_values_below_number(builder, nan_builder):
    builder.add_constraint(null_values_below_number(column_name="legs", number=1))
    builder.add_constraint(null_values_below_number(column_name="weight", number=1))
    constraint = builder.build()
    assert not constraint.validate()
    # ReportResult(name, passed, failed, summary)
    assert constraint.generate_constraints_report() == [
        ("null values of legs lower than 1", 1, 0, None),
        ("null values of weight lower than 1", 0, 1, None),
    ]
    for (x, y) in zip(constraint.report(), constraint.generate_constraints_report()):
        assert (x[0], x[1], x[2]) == (y[0], y[1], y[2])

    nan_builder.add_constraint(null_values_below_number(column_name="a", number=10))
    nan_builder.add_constraint(null_values_below_number(column_name="a", number=3))
    constraint = nan_builder.build()
    assert not constraint.validate()
    assert constraint.generate_constraints_report() == [
        ("null values of a lower than 10", 1, 0, None),
        ("null values of a lower than 3", 0, 1, None),
    ]
    for (x, y) in zip(constraint.report(), constraint.generate_constraints_report()):
        assert (x[0], x[1], x[2]) == (y[0], y[1], y[2])


def test_null_percentage_below_number(builder, nan_builder):
    builder.add_constraint(null_percentage_below_number(column_name="weight", number=1.0))
    builder.add_constraint(null_percentage_below_number(column_name="weight", number=0.1))
    constraint = builder.build()
    assert not constraint.validate()
    # ReportResult(name, passed, failed, summary)
    assert constraint.generate_constraints_report() == [
        ("null percentage of weight lower than 1.0", 1, 0, None),
        ("null percentage of weight lower than 0.1", 0, 1, None),
    ]
    for (x, y) in zip(constraint.report(), constraint.generate_constraints_report()):
        assert (x[0], x[1], x[2]) == (y[0], y[1], y[2])

    nan_builder.add_constraint(null_percentage_below_number(column_name="a", number=1.0))
    nan_builder.add_constraint(null_percentage_below_number(column_name="a", number=0.1))
    constraint = nan_builder.build()
    assert not constraint.validate()
    assert constraint.generate_constraints_report() == [
        ("null percentage of a lower than 1.0", 1, 0, None),
        ("null percentage of a lower than 0.1", 0, 1, None),
    ]
    for (x, y) in zip(constraint.report(), constraint.generate_constraints_report()):
        assert (x[0], x[1], x[2]) == (y[0], y[1], y[2])
