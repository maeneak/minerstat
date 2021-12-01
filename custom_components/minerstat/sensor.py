"""Sensor platform for Minerstat."""
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import ATTRIBUTION, DEFAULT_NAME, MS_HARDWARE, NAME, VERSION
from .const import DOMAIN
from .const import ICON
from .const import SENSOR


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    devices = []
    for worker in list(coordinator.data.keys()):
        devices.append(MinerstatWorkerSensor(coordinator, entry, worker))
        for hardware in coordinator.data[worker][MS_HARDWARE]:
            devices.append(
                MinerstatHardwareSensor(coordinator, entry, worker, hardware["bus"])
            )

    async_add_devices(devices)


class MinerstatHardwareSensor(CoordinatorEntity):
    """minerstat Sensor class."""

    def __init__(self, coordinator, config_entry, worker, bus):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.ref = worker
        self.bus = bus

    def hardware_device(self):
        return next(
            (
                l
                for l in self.coordinator.data[self.ref][MS_HARDWARE]
                if l["bus"] == self.bus
            ),
            None,
        )

    def bus_id(self):
        return str(self.bus).removesuffix(":00:00")

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}_{self.ref}_{self.bus_id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.ref)},
            "name": self.ref,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""

        return {
            "attribution": ATTRIBUTION,
            "id": f"{self.ref}_hardware_bus{self.bus_id}",
            "integration": DOMAIN,
            **self.hardware_device(),
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self.hardware_device()['name']} ({self.bus})"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.hardware_device()["speed"]

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "minerstat__custom_device_class"


class MinerstatWorkerSensor(CoordinatorEntity):
    """minerstat Sensor class."""

    def __init__(self, coordinator, config_entry, worker):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.ref = worker

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}_{self.ref}_worker"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.ref)},
            "name": self.ref,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""

        return {
            "attribution": ATTRIBUTION,
            "id": f"{self.name}_worker",
            "integration": DOMAIN,
            **self.coordinator.data[self.ref]["info"],
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        _name = self.coordinator.data[self.ref]["info"]["name"]
        return f"{_name}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data[self.ref]["info"]["status"]

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "minerstat__custom_device_class"


class MinerstatSensor(CoordinatorEntity):
    """minerstat Sensor class."""

    def __init__(self, coordinator, config_entry, worker):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.ref = worker

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}_{self.ref}_worker"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.ref)},
            "name": self.ref,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""

        return {
            "attribution": ATTRIBUTION,
            "id": f"{self.name}_worker",
            "integration": DOMAIN,
            **self.coordinator.data[self.ref]["info"],
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        _name = self.coordinator.data[self.ref]["info"]["name"]
        return f"{_name}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data[self.ref]["info"]["status"]

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "minerstat__custom_device_class"
