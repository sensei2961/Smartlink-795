# Created by maxyu at 8/26/2021
Feature: Login

  Scenario: Login using valid credentials
    Given Open Login page
    When Enter username maxiotega
    And Enter password 123123
    And Click Login button
    Then Verify User can Log in

  Scenario: Login using invalid username
    Given Open Login page
    When Enter invalid username fakeusernameinvalid
    And Enter password 123123
    And Click Login button
    Then User receives bad credentials error

  Scenario: Login using invalid password
    Given Open Login page
    When Enter username maxiotega
    And Enter password fake_password_invalid
    And Click Login button
    Then User receives bad credentials error

#  In development...
#  Scenario: Forgot password
#    Given Open Login page
#    When Click Forgot Password
#    And Enter forgot username max.luna
#    And Enter Phone Number 2536530821
#    And Enter Email Address max.yurkaev@securenettech.com
#    And Click Next
#    Then Verify Email has been sent
##    When Click Back
#    When Open Gmail max.yurkaev@securenettech.com
