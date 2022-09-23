Feature: RegistrationPage

  Scenario Outline: Verify fill the form ang login
    Given I navigate to the way2automation site
    When Enter the Name as "<name>"
    When Enter the PhoneNum ad "<phone_number>"
    When Enter the Email as "<email>"
    When select the Country as "<country>"
    When Enter the City as "<city>"
    When Enter the Username "<username>"
    When Enter the Password as "<password>"
    Then I click on the submit the form

    Examples:
    |name    |phone_number|email            |country  |city     |username        |password  |
    |Testing1|089098761   |testing1@test.com|India    |Bangalore|  username1     |password1 |
    |Testing2|089098762   |testing2@test.com|Germany  |Delhi    |  username2     |password2 |