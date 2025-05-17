describe('Teste E2E da API de Estoque', () => {
  const baseUrl = 'http://localhost:8000/produtos';

  it('GET /produtos deve retornar lista inicial vazia ou existente', () => {
    cy.request('GET', baseUrl).then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.be.an('array');
    });
  });

  it('POST /produtos deve adicionar um novo produto', () => {
    const novoProduto = {
      nome: 'Banana',
      quantidade: 10,
      preco: 2.5,
      categoria: 'Frutas'
    };

    cy.request('POST', baseUrl, novoProduto).then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('nome', 'Banana');
    });
  });

  it('PUT /produtos/{index} deve atualizar o produto', () => {
    const produtoAtualizado = {
      nome: 'Banana Prata',
      quantidade: 15,
      preco: 3.0,
      categoria: 'Frutas Tropicais'
    };

    cy.request('PUT', `${baseUrl}/0`, produtoAtualizado).then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('nome', 'Banana Prata');
    });
  });

  it('DELETE /produtos/{index} deve remover o produto', () => {
    cy.request('DELETE', `${baseUrl}/0`).then(response => {
      expect(response.status).to.eq(200);
    });
  });

  it('GET /produtos após remoção deve refletir a lista atualizada', () => {
    cy.request('GET', baseUrl).then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.be.an('array');
    });
  });
});
