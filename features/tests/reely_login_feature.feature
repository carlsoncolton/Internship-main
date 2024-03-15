# Created by colto at 3/14/2024
Feature: Reely.io login feature
  # Enter feature description here

  Scenario: User can open product detail and see three options of visualization
    Given Open reely main page
    When Login to the page
    Then Click on “off plan” at the left side menu
    Then Click on the first product
    Then Verify the three options of visualization are 'architecture', 'interior', 'lobby'
    Then Verify the visualization options are clickable
    # Enter steps here