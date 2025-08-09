Feature: Order

  Scenario: Complete an order successfully
    Given I am logged in
    When I add a product to the cart and checkout
    Then I should see order confirmation
