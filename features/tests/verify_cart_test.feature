# Created by colto at 2/8/2024
Feature: Target.com cart test
  # Enter feature description here

  Scenario: Verify cart is empty when searched
    Given Open target main page
    When Click on cart icon
    Then Verify cart empty icon is shown
