Feature: Knights should be able to login and view their dashboard and submit requests
  Scenario: Login to the Knight Dashboard
    Given The Knight is on the Login Page
    When The Knight enters their username
    When The Knight enters their password
    When The Knight clicks the login button
    Then The Knight should be on the Knight Dashboard Page




