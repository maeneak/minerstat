"""MinerstatEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION, MS_HARDWARE, MS_INFO
from .const import DOMAIN
from .const import NAME
from .const import VERSION


class MinerstatEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry, worker, bus):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.ref = worker
        self.bus = bus

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        bus = str(self.bus).removesuffix(":00:00")
        return f"{self.config_entry.entry_id}_{self.ref}_{bus}"

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
            "id": self.ref + str(self.bus).removesuffix(":00:00"),
            "integration": DOMAIN,
            **self.hardware_device(),
        }

    def hardware_device(self):
        return next(
            (
                l
                for l in self.coordinator.data[self.ref][MS_HARDWARE]
                if l["bus"] == self.bus
            ),
            None,
        )
