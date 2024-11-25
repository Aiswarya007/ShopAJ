Feature: Search for products on the e-commerce platform

  Scenario: Search for an existing product
    Given the user is on the homepage
    When they enter a valid product name into the search bar
    And click the search button
    Then they should see a list of results matching the product name

  Scenario: Search for a non-existing product
    Given the user is on the homepage
    When they enter a product name that does not exist
    And click the search button
    Then they should see a "No products match your search query" message

  Scenario: Perform a search with an empty search bar
    Given the user is on the homepage
    When they leave the search bar empty
    And click the search button
    Then they should see a message prompting them to enter a search term
