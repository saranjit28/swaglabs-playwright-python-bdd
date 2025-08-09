Feature: SwagLabs Order Purchase Flow
  Scenario: Complete an order successfully
    Given I am on the login page
    When I login with valid credentials
    And I add "Sauce Labs Backpack" to the cart
    And I proceed to checkout with "John" "Doe" "12345"
    Then I should see order confirmation