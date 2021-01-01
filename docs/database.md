# Database Structure

## Telemetry
The sensor values will be collected and sent in a payload to the cloud in a json document:
```json
{
    "T": 30.0,
    "H": 45.0,
    "L": 78.0,
    "I": "2021-01-01T19:20:21+00:00"
}
```
At this point in time we do not have alot of data to be publishing. `T` is the temperature in celsuis, `H` is the soil humidity in %, `L` is the luminous flux or ambient sunlight in lux and `I` is the timestamp of the last completed water injection.

## Cloud Services
Here are 2 conventional approaches to IoT architectures:
![img](img/cloud.png)

This solution emphasizes more computational load to the IoT device since it has to be an MQTT and HTTP client making 2 requests on every publish

![img](img/cloud2.png)

This solution emphasizes more computational load to the backend since on every delta it has to publish to the api to store in the database.

Both of these solutions are great since they can be scaled to any size system. This can be very complicated to implement for prototyping however.

### Firebase Real-time Database

Firebase has a backend which combines HTTP and MQTT processes into a single cloud platform. When data is pushed to a firebase RTD the data is automatically timestamped and the remaining subscribed devices are updated automatically while the data is being stored into the database. This makes it very easy to prototype IoT solutions without the need for a complicated backend solution.