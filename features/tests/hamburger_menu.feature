# Created by Ooma at 6/22/2020
Feature: Scenarios for Amazon hamburger menu

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present