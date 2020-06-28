# Created by Ooma at 6/22/2020
Feature: Validate Best Sellers Header

  Scenario: Validate the quantity of the links in the header
      Given Open Amazon Best Sellers page
      Then Check that 5 links are present