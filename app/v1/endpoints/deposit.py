from datetime import datetime
from typing import Mapping

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, status

from app.v1.models import deposit, exceptions

router = APIRouter()


async def calculate(
        amount: int, date: str, periods: int, rate: float
) -> Mapping[str, float]:
    result = {}
    amount_with_monthly_interest: float = float(amount)
    start_date = datetime.strptime(date, "%d.%m.%Y")

    for idx in range(periods):
        amount_with_monthly_interest *= 1 + rate / 12 / 100
        current_date = start_date + relativedelta(months=idx)
        result[current_date.strftime("%d.%m.%Y")] = round(
            amount_with_monthly_interest, 2
        )
    return result


@router.post(
    "/calculate",
    summary="Endpoint for deposit calculation",
    response_model=Mapping[str, float],
    responses={
        status.HTTP_200_OK: {
            "description": "Returns the result of deposit calculation by month"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": exceptions.ExceptionModel,
            "description": "Validation error",
        }
    }
)
async def deposit_calculation(model: deposit.DepositModel):
    return await calculate(model.amount, model.date, model.periods, model.rate)
