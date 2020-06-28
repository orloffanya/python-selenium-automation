# Created by Ooma at 6/22/2020
Feature: Test Scenarios for Amazon Help search functionality

  Scenario: User can search for a solution
    Given Open Amazon Help page
    When Input Cancel order into solutions search field
    And Click on Go
    Then Solution results are shown for Cancel order