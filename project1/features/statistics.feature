Feature: The Lord should be able to view the statistics page
  Background: The Lord is logged in
    Given The Lord is on the Login Page
    When The Lord enters their username
    When The Lord enters their password
    When The Lord checks the lord button
    When The Lord clicks the login button
    Then The Lord should be on the Lord Dashboard Page

    Scenario: Lord views the statistics page
      When The Lord clicks the statistics button
      Then The Lord should be on the statistics page