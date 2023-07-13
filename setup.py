# Check that everything was installed correctly by enrolling with Ockam Orchestrator.
#
# This will create a Space and Project for you in Ockam Orchestrator and provision an
# End-to-End Encrypted Cloud Relay service in your `default` project at `/project/default`.
ockam enroll

# -- APPLICATION SERVICE --

# Start an application service, listening on a local IP and port, that clients would access
# through the cloud encrypted relay. We'll use a simple HTTP server for this first example
# but this could be any other application service.
python3 -m http.server --bind 127.0.0.1 6000

# In a new terminal window, setup a tcp-outlet that makes a TCP service available at the given
# address `6000`. We can use this to send raw TCP traffic to the HTTP server on port `6000`.
# Finally create a relay in your default Orchestrator project. Relays make it possible to
# establish end-to-end protocols with services operating in a remote private networks, without
# requiring a remote service to expose listening ports to an outside hostile network like the
# Internet.
ockam tcp-outlet create --to 6000
ockam relay create

# -- APPLICATION CLIENT --

# Setup a a local tcp-inlet to allow raw TCP traffic to be received on port `7000` before
# it is forwarded. A TCP inlet is a way of defining where a node should be listening for
# connections, and where it should forward that traffic to.
ockam tcp-inlet create --from 7000

# Access the application service, that may be in a remote private network though
# the end-to-end encrypted secure channel, via your private and encrypted cloud relay.
curl --head 127.0.0.1:7000
