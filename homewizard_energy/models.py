"""Models for HomeWizard Energy."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any


@dataclass
class Device:
    """Represent Device config."""

    product_name: str | None
    product_type: str | None
    serial: str | None
    api_version: str | None
    firmware_version: str | None

    @staticmethod
    def from_dict(data: dict[str, str]) -> Device:
        """Return Device object from API response.

        Args:
            data: The data from the HomeWizard Energy `api` API.

        Returns:
            A Device object.
        """
        return Device(
            product_name=data.get("product_name"),
            product_type=data.get("product_type"),
            serial=data.get("serial"),
            api_version=data.get("api_version"),
            firmware_version=data.get("firmware_version"),
        )


@dataclass
class Data:
    """Represent Device config."""

    wifi_ssid: str | None
    wifi_strength: int | None

    smr_version: int | None
    meter_model: str | None
    unique_meter_id: str | None

    active_tariff: int | None

    total_power_import_kwh: float | None
    total_power_import_t1_kwh: float | None
    total_power_import_t2_kwh: float | None
    total_power_import_t3_kwh: float | None
    total_power_import_t4_kwh: float | None
    total_power_export_kwh: float | None
    total_power_export_t1_kwh: float | None
    total_power_export_t2_kwh: float | None
    total_power_export_t3_kwh: float | None
    total_power_export_t4_kwh: float | None

    active_power_w: float | None
    active_power_l1_w: float | None
    active_power_l2_w: float | None
    active_power_l3_w: float | None

    active_voltage_l1_v: float | None
    active_voltage_l2_v: float | None
    active_voltage_l3_v: float | None

    active_current_l1_a: float | None
    active_current_l2_a: float | None
    active_current_l3_a: float | None

    active_frequency_hz: float | None

    voltage_sag_l1_count: int | None
    voltage_sag_l2_count: int | None
    voltage_sag_l3_count: int | None

    voltage_swell_l1_count: int | None
    voltage_swell_l2_count: int | None
    voltage_swell_l3_count: int | None

    any_power_fail_count: int | None
    long_power_fail_count: int | None

    active_power_average_w: float | None
    montly_power_peak_w: float | None
    montly_power_peak_timestamp: datetime | None

    total_gas_m3: float | None
    gas_timestamp: datetime | None
    gas_unique_id: str | None

    active_liter_lpm: float | None
    total_liter_m3: float | None

    external_devices: list[ExternalDevice]

    @staticmethod
    def convert_timestamp_to_datetime(timestamp: str | None) -> datetime | None:
        """Convert SRM gas-timestamp to datetime object.

        Args:
            timestamp: Timestamp string, formatted as yymmddhhmmss

        Returns:
            A datetime object.
        """
        if timestamp is None:
            return None

        return datetime.strptime(str(timestamp), "%y%m%d%H%M%S")

    @staticmethod
    def get_external_devices(external_devices) -> list[ExternalDevice] | None:
        """Convert external device object to ExternalDevice Object List."""

        if external_devices is None:
            return None

        devices: list[ExternalDevice] = []

        for external in external_devices:
            devices.append(ExternalDevice.from_dict(external))

        return devices

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Data:
        """Return State object from API response.

        Args:
            data: The data from the HomeWizard Energy `api/v1/data` API.

        Returns:
            A State object.
        """

        return Data(
            wifi_ssid=data.get("wifi_ssid"),
            wifi_strength=data.get("wifi_strength"),
            smr_version=data.get("smr_version"),
            meter_model=data.get("meter_model"),
            unique_meter_id=data.get("unique_id"),
            active_tariff=data.get("active_tariff"),
            total_power_import_kwh=data.get("total_power_import_kwh"),
            total_power_import_t1_kwh=data.get("total_power_import_t1_kwh"),
            total_power_import_t2_kwh=data.get("total_power_import_t2_kwh"),
            total_power_import_t3_kwh=data.get("total_power_import_t3_kwh"),
            total_power_import_t4_kwh=data.get("total_power_import_t4_kwh"),
            total_power_export_kwh=data.get("total_power_export_kwh"),
            total_power_export_t1_kwh=data.get("total_power_export_t1_kwh"),
            total_power_export_t2_kwh=data.get("total_power_export_t2_kwh"),
            total_power_export_t3_kwh=data.get("total_power_export_t3_kwh"),
            total_power_export_t4_kwh=data.get("total_power_export_t4_kwh"),
            active_power_w=data.get("active_power_w"),
            active_power_l1_w=data.get("active_power_l1_w"),
            active_power_l2_w=data.get("active_power_l2_w"),
            active_power_l3_w=data.get("active_power_l3_w"),
            active_voltage_l1_v=data.get("active_voltage_l1_v"),
            active_voltage_l2_v=data.get("active_voltage_l2_v"),
            active_voltage_l3_v=data.get("active_voltage_l3_v"),
            active_current_l1_a=data.get("active_current_l1_a"),
            active_current_l2_a=data.get("active_current_l2_a"),
            active_current_l3_a=data.get("active_current_l3_a"),
            active_frequency_hz=data.get("active_frequency_hz"),
            voltage_sag_l1_count=data.get("voltage_sag_l1_count"),
            voltage_sag_l2_count=data.get("voltage_sag_l2_count"),
            voltage_sag_l3_count=data.get("voltage_sag_l3_count"),
            voltage_swell_l1_count=data.get("voltage_swell_l1_count"),
            voltage_swell_l2_count=data.get("voltage_swell_l2_count"),
            voltage_swell_l3_count=data.get("voltage_swell_l3_count"),
            any_power_fail_count=data.get("any_power_fail_count"),
            long_power_fail_count=data.get("long_power_fail_count"),
            active_power_average_w=data.get("active_power_average_w"),
            montly_power_peak_w=data.get("montly_power_peak_w"),
            montly_power_peak_timestamp=Data.convert_timestamp_to_datetime(
                data.get("montly_power_peak_timestamp")
            ),
            total_gas_m3=data.get("total_gas_m3"),
            gas_timestamp=Data.convert_timestamp_to_datetime(data.get("gas_timestamp")),
            gas_unique_id=data.get("gas_unique_id"),
            active_liter_lpm=data.get("active_liter_lpm"),
            total_liter_m3=data.get("total_liter_m3"),
            external_devices=Data.get_external_devices(data.get("external")),
        )


@dataclass
class ExternalDevice:
    """Represents externally connected device."""

    class DeviceType(Enum):
        """Device type allocations.

        Based on:
          https://oms-group.org/fileadmin/files/download4all/omsSpezifikationen/generation4/spezifikation/vol2/OMS-Spec_Vol2_Primary_v442.pdf
          Page 18, Chapter 2.3, Table 2
        """

        UNKNOWN = -1
        GAS_METER = 3
        HEAT_METER = 4
        WARM_WATER_METER = 6
        WATER_METER = 7
        INLET_HEAT_METER = 12

        @classmethod
        def _missing_(cls, _):
            return cls.UNKNOWN

        @staticmethod
        def from_string(value: str) -> ExternalDevice.DeviceType:
            """Convert string to enum."""
            try:
                return {
                    "gas_meter": ExternalDevice.DeviceType.GAS_METER,
                    "heat_meter": ExternalDevice.DeviceType.HEAT_METER,
                    "warm_water_meter": ExternalDevice.DeviceType.WARM_WATER_METER,
                    "water_meter": ExternalDevice.DeviceType.WATER_METER,
                    "inlet_heat_meter": ExternalDevice.DeviceType.INLET_HEAT_METER,
                }[value]
            except (KeyError):
                return ExternalDevice.DeviceType.UNKNOWN

    unique_id: str
    meter_type: DeviceType
    value: float
    unit: str
    timestamp: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> dict:
        """Return State object from API response.

        Args:
            data: The data from a external device in the HomeWizard Energy `api/v1/state` API.
        Returns:
            An ExternalDevice Device object.
        """
        return ExternalDevice(
            unique_id=data.get("unique_id"),
            meter_type=ExternalDevice.DeviceType.from_string(data.get("type")),
            value=data.get("value"),
            unit=data.get("unit"),
            timestamp=Data.convert_timestamp_to_datetime(data.get("timestamp")),
        )


@dataclass
class State:
    """Represent current state."""

    power_on: bool | None
    switch_lock: bool | None
    brightness: int | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> dict:
        """Return State object from API response.

        Args:
            data: The data from the HomeWizard Energy `api/v1/state` API.

        Returns:
            A State object.
        """
        return State(
            power_on=data.get("power_on"),
            switch_lock=data.get("switch_lock"),
            brightness=data.get("brightness"),
        )


@dataclass
class System:
    """Represent current state."""

    cloud_enabled: bool | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> dict:
        """Return System object from API response.

        Args:
            data: The data from the HomeWizard Energy `api/v1/system` API.

        Returns:
            A System object.
        """
        return System(
            cloud_enabled=data.get("cloud_enabled"),
        )


@dataclass
class Decryption:
    """Represent decryption API."""

    key_set: bool | None
    aad_set: bool | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> dict:
        """Return Decryption object from API response.

        Args:
            data: The data from the HomeWizard Energy `api/v1/decryption` API.

        Returns:
            A Decryption object.
        """
        return Decryption(
            key_set=data.get("key"),
            aad_set=data.get("aad"),
        )
