const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('test the index page', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
        expect(response.request.method).to.equal('GET');
        expect(body).to.equal('Welcome to the payment system');
        done();
      }
    });
  });
  it('test with a correct endpoint', (done) => {
    request('http://localhost:7865/cart/10', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
        expect(response.request.method).to.equal('GET');
        expect(body).to.equal('Payment methods for cart 10');
        done();
      }
    });
  });
  it('test with a wrong endpoint', (done) => {
    request('http://localhost:7865/cart/wrong', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(404);
        done();
      }
    });
  });
});
