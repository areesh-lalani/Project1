Feature: A Lord should be able to approve/deny and leave messages on reimbursement requests
  Background: The Lord is logged in
    Given The Lord is on the Login Page
    When The Lord enters their username
    When The Lord enters their password
    When The Lord checks the lord button
    When The Lord clicks the login button
    Then The Lord should be on the Lord Dashboard Page

    Scenario: The Lord Approves a request
      When The Lord clicks a view request button
      Then The view request form should appear
      When The Lord clicks the approve button
      When The Lord clicks the submit button
      Then The edit form should close

    Scenario: The Lord Denies a request
      When The Lord clicks a view request button
      Then The view request form should appear
      When The Lord clicks the deny button
      When The Lord clicks the submit button
      Then The edit form should close

    Scenario: The Lord leaves a message
      When The Lord clicks a view request button
      Then The view request form should appear
      When The Lord clicks the deny button
      When The Lord leaves a message
      When The Lord clicks the submit button
      Then The edit form should close
