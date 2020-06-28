# Created by Ooma at 6/22/2020
Feature: Colors of a product

  Scenario: The color name changes when clicking through item colors
    Given Open Amazon page
    When Input Dress into search field
    When Click on search
    When Click on the first item of Amazon search
    Then Verify that color names correspond with item color