# Created by Ooma at 6/22/2020
Feature: Popups

  Scenario: Close popups on Youtube page
    Given Open Youtube page
    When Click on the first youtube video
    Then Check Youtube popup
