# Created by maxyu at 10/10/2021


Feature: Helix Alarm Control

  Scenario: Arm Stay
    Given Open Login page
    When Login maxhelixus/123123
    And Click Arm Stay
    Then Panel is Armed Stay
