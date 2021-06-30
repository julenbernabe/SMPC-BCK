# eventeum-skeleton

## Steps

0. First you need to have a network where you have deployed a Smart Contract with some events. Thus you know:
- The URL of the network.
- The address of the Smart Contract.
- The name of, at least, one event of the Smart Contract.
1. Go to the docker-compose file and change the item `ETHEREUM_NODE_URL` by writing your network URL.
2. Open the terminal and run the command `docker-compose up -d`. This command will deploy four repositories,. which you should see when running `docker ps`:
```
eventeum
kafka
zookeeper
mongodb
```
3. Run in terminal the command `docker logs eventeum` and assure that no errors ocurred in deployments of the previous step. If everything is right, go ahead. If not, the network URL where you have deployed the Smart Contract is likely to be wrong.
4. To communicate with Eventeum, run `initial_subscription.py`:
- If you want to add a new event for Eventeum to listen to, run the function `post()` inside it.
- If you want to delete an event that is being listened, run the function `delete()` inside it.

Step 4 is not trivial at all, so you must study the code in `initial_subscription.py` before executing it. There are some items that should be changed inside that file, customize it to fit in your Smart Contract.


## Intallation Requirements

The following python libraries are required:
- requests
- kafka-python
