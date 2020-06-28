# Created by Ooma at 6/22/2020
Feature: Test Scenarios for Amazon search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Dress into search field
    And Click on search icon
    Then Product results for Dress are shown
    #And First result contains skirt