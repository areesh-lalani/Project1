Feature: Lords should be able to login and view their knight's reimbursement requests

  Scenario: Login to the Lord Dashboard
    Given The Lord is on the Login Page
    When The Lord enters their username
    When The Lord enters their password
    When The Lord checks the lord button
    When The Lord clicks the login button
    Then The Lord should be on the Lord Dashboard Page