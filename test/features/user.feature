Feature: Handle storing, retrieving and deleting customer details

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'michael01'
    Then I should get a '200' response
    And the following user details are returned:
    | name           |
    | Michael Pretus |

  Scenario: Register a customer
    Given user identified by 'darlene01' and named 'Darlene Alderson'
    When I send the customer details
    Then I should get a '200' response
    And the following user details are returned:
    | name             |
    | Darlene Alderson |