# Created by Ooma at 6/27/2020
Feature: Amazon main page popups

  Scenario: Sign in popup appears and then disappears
    Given Open Amazon page
    Then Verify Sing in popup is present and clickable
    When Sign in popup disappears
    Then Verify Sign in popup is not clickable