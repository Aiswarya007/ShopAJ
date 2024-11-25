// Define a custom command for performing a search
Cypress.Commands.add('performSearch', (term) => {
  cy.get('input[name="q"]').clear().type(term); // Clear the input and type the search term
  cy.get('button[type="submit"]').click(); // Click the search button
});