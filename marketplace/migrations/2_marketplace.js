const Token = artifacts.require("Token");
var marketplace = artifacts.require("marketplace");

module.exports = function(deployer) {
    deployer.deploy(Token).then(function() {
        return deployer.deploy(marketplace, Token.address);
    });
}