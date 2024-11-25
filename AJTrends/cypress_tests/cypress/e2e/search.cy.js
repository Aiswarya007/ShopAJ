// Test suite for search functionality
describe('Search Functionality on E-Commerce Platform', () => {
  const baseUrl = 'http://127.0.0.1:8000/';

  beforeEach(() => {
    cy.visit(baseUrl);
  });

  it('should display results for a valid product search', () => {
    cy.fixture('searchTerms').then((data) => {
      // Use the custom command for searching
      cy.performSearch(data.validTerm);

      // Check if results are displayed
      cy.get("img[alt='Classic Denim Jeans']").should('have.length.greaterThan', 0);
    });
  });

  it('should show "No products match your search query." for an invalid product search', () => {
    cy.fixture('searchTerms').then((data) => {
      // Use the custom command for searching
      cy.performSearch(data.invalidTerm);

      // Assert that the "No products match your search query" message is displayed
      cy.get('p').should('contain.text', 'No products match your search query.');
    });
  });

  it('should prompt user to enter a search term if search is empty', () => {
    // Leave the search bar empty and click the search button
    cy.get('button[type="submit"]').click();

    // Assert that an empty search message is displayed
    cy.get('p').should('contain.text', 'Please enter a search term');
  });
});