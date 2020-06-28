# Created by lena at 6/9/2020
Feature: Scenarios for Cart functionality

  Scenario: User can add to cart and check
    Given Open Amazon page
    When Search item Alexa
    And Click search Button
    And Click image of the first item
    And Click add to the cart
    And Close popup
    Then Number of items in the cart more than zero