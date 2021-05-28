import pytest
from pytest_bdd import parsers, scenarios, given, then, when
from functools import partial

from pytest_bdd.scenario import scenario
from apples import AppleBasket

EXTRA_TYPES ={ 
    'Number': int,
}

CONVERTERS = {
    'initial': int, 
    'some': int, 
    'total': int,
}

# Si usamos parametrize, va a correr sobre 1 solo escenario. De la forma actual, 
# corre sobre todos los escenarios. Y los ejemplo se especifican sobre el feature file
#@pytest.mark.parametrize(
#    ['initial', 'some', 'total'],
#    [(0,3,3),
#     (2,3,5),
#     (3,3,6),
#     (4,4,8),
#     (5,5,10)])
#@scenario('../features/apples.feature', 'Add apples to a basket')
#def test_add(initial, some, total):
#    pass

scenarios('../features/apples.feature', example_converters=CONVERTERS)

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

@given(parse_num('the basket has "{initial:Number}" apples'), target_fixture='basket')
@given('the basket has "<initial>" apples')
def basket(initial):
    return AppleBasket(initial_count=initial)

# Add    
@when(parse_num('"{some:Number}" apples are added to the basket'))
@when('"<some>" apples are added to the basket')
def add_apples(basket, some):
    basket.add(some)

# Remove
@when(parse_num('"{some:Number}" apples are removed from the basket'))
@when('"<some>" apples are removed from the basket')
def remove_apples(basket, some):
    basket.remove(some)

@then(parse_num('the basket contains "{total:Number}" apples'))
@then('the basket contains "<total>" apples')
def basket_has_total(basket, total):
    assert basket.count == total

