# Created by maxyu at 10/10/2021


Feature: Helix Alarm Control

  Scenario: Arm Stay
    Given Open Login page
    When Login max.luna/123456
    And Click Arm Stay
    Then Panel is Armed Stay

  Scenario: Disarm Stay
    Given Open Login page
    When Login max.luna/123456
    And Click Disarm
    Then Panel is Disarmed

#  Scenario: Arm Away
#
#  Scenario:  Disarm Away
#
#  Scenario:  Arm Night
#
#  Scenario: Disarm Night
#  Scenario: Silent Arm Enable
#  Scenario: Silent Arm Disable
#  Scenario: No Entry Delay Enable
#  Scenario: No Entry Delay Disable
#  Scenario: Global Chime Enable
#  Scenario: Global Chime Disable