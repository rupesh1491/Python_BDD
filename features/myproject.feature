Feature: Open login page
  Scenario: Login  with username and pass
    Given open dshboard page
    When Enter username "varniktech@gmail.com" and password "varnik20@123"
    Then click on login button
    And close browser