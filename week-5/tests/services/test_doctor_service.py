from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock
from uuid import UUID

import pytest

from app.models.availability import Availability
from app.schemas.doctor import CreateAvailabilityRequest, DoctorAvailability
from app.services.doctor_service import DoctorService


@pytest.fixture
def mock_db_session():
    session = AsyncMock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    return session


@pytest.fixture
def doctor_service(mock_db_session):
    return DoctorService(mock_db_session)


@pytest.mark.asyncio
async def test_add_availability_success(doctor_service, mock_db_session):

    doctor_id = UUID("123e4567-e89b-12d3-a456-426614174000")
    slot = CreateAvailabilityRequest(
        date="03-01-2025", start_time="10:00", end_time="11:00"
    )

    mock_db_session.add = MagicMock()

    result = await doctor_service.add_availability(doctor_id, slot)

    assert isinstance(result, DoctorAvailability)
    assert result.date == "03-01-2025"
    assert result.start_time == "10:00"
    assert result.end_time == "11:00"

    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_awaited_once()
    mock_db_session.refresh.assert_awaited_once()


@pytest.mark.asyncio
async def test_add_availability_invalid_time_range(doctor_service):
    doctor_id = UUID("123e4567-e89b-12d3-a456-426614174000")
    slot = CreateAvailabilityRequest(
        date="03-01-2025", start_time="12:00", end_time="11:00"
    )
    # Should raise ValueError
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        await doctor_service.add_availability(doctor_id, slot)
