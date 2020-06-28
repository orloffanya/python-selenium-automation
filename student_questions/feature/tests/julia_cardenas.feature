# Created by juliacardenas at 6/9/20
Feature: Test Scenario to add and check items in the cart

  Scenario: User search for a product and put in shopping cart
    Given Open Amazon page
    When Input lego for boys age 8-12 into search field
    And Click on search icon
    And The number of items is equal to 72
    And User click on chosen item
    And User add item to shopping cart
    When Input lego for boys age 8-12 into search field
    And Click on search icon
    And User click on another chosen item
    And User add item to shopping cart
    Then User open shopping cart
    Then Verify that 2 items in shopping cart