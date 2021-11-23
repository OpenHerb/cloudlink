"""
Telemetry Model
===============
Modified: 2021-10

Model for OpenHerb Telemetry

Dependancies
------------
```
import uuid
import json
import random
from enum import IntEnum
from datetime import datetime
from typing import Any, Dict, Tuple
from cloudlink.models.model import Model, _PKey
```

Copyright © 2021 OpenHerb.
"""
import uuid
import json
import random
from enum import IntEnum
from datetime import datetime
from typing import Any, Dict, Tuple
from cloudlink.models.model import Model, _PKey


class StatusCode(IntEnum):
    NOMINAL = 0
    GENERAL_ERROR = 1
    NO_DATA = 2


class Telemetry(Model):

    # Resolution of float values stored in this model
    STORAGE_RESOLUTION = 1
    # Operating temp
    OPERATING_TEMPERATURE: Tuple[float, float] = (0.0, 40.0)

    def __init__(self) -> None:
        super().__init__(str(uuid.uuid4()))

    def __repr__(self) -> str:
        return "Telemetry: {}".format("\n" + json.dumps(self.serialize(), indent=2))

    def serialize(self) -> Dict[str, Any]:
        """
        Iteratively get all object properties and values

        :return: object attributes and values
        :rtype: Dict[str, Any]
        """
        return {
            'id': self.id,
            'tp': self.tp,
            'rh': self.rh,
            'pa': self.pa,
            'lx': self.lx,
            'sm': self.sm,
            'sc': self.sc,
            'ts': self.ts
        }

    def deserialize(self, **payload) -> None:
        """
        Iteratively set object properties
        """
        for k, v in payload.items():
            # timestamp unsettable
            if k != 'ts':
                setattr(self, k, v)

    @property
    def tp(self) -> float:
        """
        Get ambient temperature (°C) @ storage resolution

        :return: ambient temperature measurement in °C
        :rtype: float
        """
        return self.__tp

    @tp.setter
    def tp(self, temperature: float) -> None:
        """
        Set ambient temperature (°C) @ storage resolution

        :param temperature: ambient temperature measurement in °C
        :type temperature: float
        """
        self.__tp = round(temperature, self.STORAGE_RESOLUTION)

    @property
    def pa(self) -> float:
        """
        Get ambient pressure (kPa) @ storage resolution

        :return: ambient pressure measurement in kPa
        :rtype: float
        """
        return self.__pa

    @pa.setter
    def pa(self, pressure: float) -> None:
        """
        Set ambient pressure (kPa) @ storage resolution

        :param pressure: ambient pressure measurement in kPa
        :type pressure: float
        """
        self.__pa = round(pressure, self.STORAGE_RESOLUTION)

    @property
    def rh(self) -> float:
        """
        Get relative humidity (%) @ storage resolution

        :return: relative humidity measurement in %
        :rtype: float
        """
        return self.__pa

    @rh.setter
    def rh(self, humidity: float) -> None:
        """
        Set relative humidity (%) @ storage resolution

        :param humidity: relative humidity measurement in %
        :type humidity: float
        """
        self.__pa = round(humidity, self.STORAGE_RESOLUTION)

    @property
    def lx(self) -> int:
        """
        Get ambient luminous flux (Lux) @ storage resolution

        :return: ambient luminous flux measurement in Lux
        :rtype: int
        """
        return self.__lx

    @lx.setter
    def lx(self, flux: int) -> None:
        """
        Set ambient luminous flux (Lux)

        :param flux: ambient luminous flux measurement in Lux
        :type flux: int
        """
        self.__lx = flux

    @property
    def sm(self) -> float:
        """
        Get soil moisture (%) @ storage resolution

        :return: soil moisture measurement as %
        :rtype: float
        """
        return self.__sm

    @sm.setter
    def sm(self, moisture: float) -> None:
        """
        Set soil moisture (%) @ storage resolution

        :param flux: soil moisture measurement as %
        :type flux: int
        """
        self.__sm = round(moisture, self.STORAGE_RESOLUTION)

    @property
    def ts(self) -> str:
        """
        Get sensorframe as UTC ISO timestamp

        :return: sensorframe as UTC ISO timestamp
        :rtype: str
        """
        return datetime.isoformat(datetime.utcnow())

    @property
    def sc(self) -> StatusCode:
        """
        Get telemetry status code

        :return: telemetry status code
        :rtype: StatusCode
        """
        return self.__sc

    @sc.setter
    def sc(self, code: StatusCode) -> None:
        """
        Set telemetry status code

        :param code: telemetry status code
        :type code: StatusCode
        """
        self.__sc = code

    def mock(self) -> None:
        """
        Mock telemetry object
        """
        code = random.randint(0, 2)
        if code == StatusCode.GENERAL_ERROR:
            self.sc = StatusCode.GENERAL_ERROR
        elif code == StatusCode.NO_DATA:
            self.sc = StatusCode.NO_DATA
        else:
            self.sc = StatusCode.NOMINAL
        self.sm = random.uniform(0.0, 100.0)
        self.rh = random.uniform(0.0, 100.0)
        self.lx = random.randint(0, 10000)
        self.pa = random.uniform(90, 110)
        self.tp = random.uniform(0.0, 40.0)
