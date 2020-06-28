# Created by Ooma at 6/22/2020
Feature: Verify number of elements in Amazon results

  Scenario: User is getting proper number of elements
    Given Open Amazon page
    When Input lego into search field
    And Click on search icon
    Then Number of elements is equal to 60