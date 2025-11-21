Feature: Order transaction related validations

  Scenario Outline: Place an order and verify order success message shown in order details page
    Given Order is placed with <username> and <password>
    And the user is on the landing page
    When the user logs in to the application with <username> and <password>
    And the user navigated to the orders page
    And selects the order id
    Then the order message is successfully displayed
    Examples:
        | username                  | password                   |
        | sudhirsu17@gmail.com      | 13579@RahulShettyAcademy   |
