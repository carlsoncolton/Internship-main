# Created by colto at 2/21/2024
Feature: Target.com Sign In
  # Enter feature description here

  Scenario: Verify Logged Out User Can Access Sign In
    Given Open target main page
    When Click on sign in
    Then From right side navigation menu, click sign in
    Then Verify sign in form opened


