Feature: Knight should be able to submit a reimbursement request
  Background: The Knight is logged in
    Given The Knight is on the Login Page
    When The Knight enters their username
    When The Knight enters their password
    When The Knight clicks the login button
    Then The Knight should be on the Knight Dashboard Page

  Scenario: Submit a reimbursement request
    When The Knight clicks the new request button
    Then The request form should appear
    When The Knight enters their requested amount
    When The Knight enters the reason for their request
    When The Knight clicks the submit button
    Then The form should close

  Scenario: Exit out of submit form
    When The Knight clicks the new request button
    Then The request form should appear
    When The Knight clicks the close button
    Then The form should close


