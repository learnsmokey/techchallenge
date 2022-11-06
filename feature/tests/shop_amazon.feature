# Created by Vallikannu at 10/19/2022
Feature: Shop products at Amazon
  # Enter feature description here

  Scenario: Open Amazon webpage
    Given Open amazon page
    When Search for books
    Then Click on search button
    Then Verify Correct product is searched
    Then Search for peppa pig

  Scenario: Multiple2 Amazon Search
    Given Open amazon page
    When Search for1 watch
    Then Click on search button
    When Search for1 iphone
    Then Click on search button

  Scenario: Multiple Amazon Search
    Given Open amazon page
    When Search for dress
    Then Click on search button

  Scenario: Multiple Amazon Search
    Given Open amazon page
    When Search for ball
    Then Click on search button

  Scenario: Multiple1 Amazon Search
    Given Open amazon page
    When Search item Kettle
    When Search item Pen
    When Search item Toy
    Then Click on search button

   Scenario Outline: Multiple1 Amazon search
     Given Open amazon page
     When Search item <search item>
     Then Click on search button
     Examples:
        | search item |
        | kettle      |
        | pen         |
        | toy         |