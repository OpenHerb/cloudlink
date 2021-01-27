# OpenHerb Cloud-Link

![img](/docs/img/icon.png)

MQTT cloud interface and telemeter controller

## Quickstart
Start the publisher:
```
./bin/cloudlink
```

To run the publisher mocking serial sensorframe, set the `CL_DEBUG` flag in the `.env` file to `"true"`:
bash
```
export CL_DEBUG="true"
```

## License
[GNU General Public License v3.0](/LICENSE)