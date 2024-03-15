# Created by colto at 2/26/2024
Feature: Target.com search tests
  # Enter feature description here

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for coffee
    Then Search results for coffee are shown

  Scenario: User can search for a mug on target
    Given Open target main page
    When Search for mug
    Then Search results for mug are shown

    # Enter steps here