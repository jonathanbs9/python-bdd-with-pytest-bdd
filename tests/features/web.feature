Feature: DuckDuckGo Web Browsing
    As a web surfer, 
    I want to find information online,
    So I can learn new things and get tasks done.

    Background: 
      Given the DuckDuckGo home page is displayed
    
    Scenario: Basic DuckDuckGo Search
      When the user searches for "Jonathan Brull Schroeder"
      Then results are shown for "Jonathan Brull Schroeder"

    Scenario: Lengthy DuckDuckGo Search
      When the user searches for the phrase:
          """El mas grande sigue siendo River Plate"""
      Then one of the results contains "Ignacio Copani"