var Bandwidth = require("node-bandwidth");

var client = new Bandwidth({
    userId    : "u-cbnapluxzd4wndtezeitasq", // <-- note, this is not the same as the username you used to login to the portal
    apiToken  : "t-dkfhqbmlimll7sfwxtl2ijy",
    apiSecret : "vagoxd24knrdrxvuify6ks2eq2fv4wpba6c2dcy"
});


 
client.Message.send({
    from : "+19102414176", // This must be a Catapult number on your account
    to   : "+18432604372",
    text : "Hello world."
})
.then(function(message) {
    console.log("Message sent with ID " + message.id);
})
.catch(function(err) {
    console.log(err.message);
});

