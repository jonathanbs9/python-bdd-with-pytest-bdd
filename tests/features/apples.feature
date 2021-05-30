@apple-basket
Feature: Apple Basket
    Como cosechador,
    quiero llevar las manzanas a la canasta
    así no las tiro

    # Agrego manzanas a la canasta
    @add
    Scenario Outline: Add apples to a basket
        Given the basket has "<initial>" apples
        When "<some>" apples are added to the basket
        Then the basket contains "<total>" apples

        Examples: Amounts
            | initial | some | total |
            | 2       | 4    | 6     |
            | 0       | 3    | 3     |
            | 14      | 1    | 15    |
            | 15      | 0    | 15    |
    
    # Quito manzanas de la canasta
    @remove
    Scenario Outline: Remove apples to a basket
        Given the basket has "8" apples
        When "3" apples are removed from the basket
        Then the basket contains "5" apples

        Examples: Amounts
            | initial | some | total |
            | 15      | 1    | 14    |
            | 9       | 3    | 6     |
            | 2       | 1    | 1     |
            | 1       | 1    | 0     |
