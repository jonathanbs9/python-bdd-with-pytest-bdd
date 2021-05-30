@service @duckduckgo 
Feature: DuckDuckGo Instant Answer API
    As an app developer,
    I want to get instant answers for search terms via REST-API,
    So that my app can get answers anywhere

    Scenario Outline: Basic DuckDuckGo API Query
        Given the DuckDuckGo API is queried with "<phrase>"
        Then the response status code is "200"
        And the response contains results for "<phrase>"

        Examples: Equipos
            | phrase | 
            | Barcelona  | 
            | Independiente  |
            | Boca |
            | Estudiantes |
        
        Examples: Frutas
            | phrase | 
            | banana  | 
            | manzana  | 
            | kiwi |
            | pera |
            | durazno |
            
            
            