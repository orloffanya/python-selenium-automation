# Created by Ooma at 6/15/2020
Feature: Browse Products results


  Scenario: Check how many results are on Browse Products page
#    student's code
      Scenario: Validate the quantity of the products shown on "Browse products"
    Given Open Whole Foods page
    When Click on Browse Products
    And Choose the store
#    Then Number of products per page is 60
#        student's code
#    Given Open Wholefoods page
#    When Click on Browse Products link
#    When Chose a store at 95054 zip
#    Then Count products on a page
  Then Number of products per group is 4
